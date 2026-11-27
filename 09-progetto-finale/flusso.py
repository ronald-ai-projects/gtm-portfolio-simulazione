"""
flusso.py - SIMULAZIONE (agenzie inventate, nessun dato reale)

Catena completa in un colpo solo:
  1. PULIZIA   -> toglie chiuse, franchising/reti, doppioni (scrive scartate.csv)
  2. UNIONE    -> collega ogni agenzia ai segnali tramite il dominio del sito
  3. PUNTEGGIO -> punteggio, priorita (Alta/Media/Bassa) e gancio
  4. FOGLIO    -> agenzie_priorita.csv (formato italiano per Google Sheets)
  5. MAPPA     -> mappa.html (SVG, funziona offline, senza librerie)

I due file di partenza vengono solo letti, mai modificati.
Uso:  python flusso.py
"""
import csv
import html
import json
import math
import re
from pathlib import Path

CARTELLA = Path(__file__).resolve().parent
FILE_DATASET = CARTELLA / "dataset_apify_finto.json"
FILE_SEGNALI = CARTELLA / "segnali_finti.csv"
FILE_SCARTATE = CARTELLA / "scartate.csv"
FILE_FOGLIO = CARTELLA / "agenzie_priorita.csv"
FILE_MAPPA = CARTELLA / "mappa.html"

COLORI = {"Alta": "#2e9e4f", "Media": "#f08c00", "Bassa": "#9aa0a6"}


# ---------------------------------------------------------------- utilità
def dominio(url):
    """https://www.esempio.it/pagina -> esempio.it"""
    d = (url or "").strip().lower()
    d = re.sub(r"^[a-z]+://", "", d)
    d = re.sub(r"^www\.", "", d)
    return d.split("/")[0].split("?")[0].split("#")[0]


def si(valore):
    return str(valore).strip().lower() in ("sì", "si", "yes", "true", "1")


def numero_it(x, decimali=1):
    """4.7 -> '4,7' (decimali con la virgola)"""
    if x is None or x == "":
        return ""
    return f"{float(x):.{decimali}f}".replace(".", ",")


def scrivi_csv(percorso, colonne, righe):
    # utf-8-sig: accenti corretti anche aprendo il file con Excel
    with open(percorso, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(colonne)
        w.writerows(righe)


# ---------------------------------------------------------------- 1. PULIZIA
def pulizia(agenzie):
    tenute, scartate, visti = [], [], set()
    franchising = re.compile(r"\b(franchising|rete)\b", re.IGNORECASE)
    for a in agenzie:
        dom = dominio(a.get("website"))
        if a.get("permanentlyClosed") is True:
            motivo = "Chiusa definitivamente"
        elif franchising.search(a.get("title", "")):
            motivo = "Franchising / rete"
        elif dom and dom in visti:
            motivo = f"Doppione (stesso dominio {dom})"
        else:
            motivo = None
        if motivo:
            scartate.append((a, dom, motivo))
        else:
            a["_dominio"] = dom
            tenute.append(a)
        if dom:
            visti.add(dom)
    return tenute, scartate


# ---------------------------------------------------------------- 2. UNIONE
def carica_segnali():
    with open(FILE_SEGNALI, encoding="utf-8-sig", newline="") as f:
        return {dominio(r["dominio"]): r for r in csv.DictReader(f)}


# ---------------------------------------------------------------- 3. PUNTEGGIO
def calcola(a, s):
    annunci = int(s.get("annunci_nuovi_30gg") or 0) if s else 0
    lavoro = si(s.get("offerta_lavoro_aperta")) if s else False
    sede = si(s.get("nuova_sede_o_servizio")) if s else False
    voto = float(a.get("totalScore") or 0)
    recensioni = int(a.get("reviewsCount") or 0)

    punti = 0
    punti += 2 if annunci >= 3 else 0
    punti += 2 if lavoro else 0
    punti += 2 if sede else 0
    punti += 1 if voto >= 4.5 else 0
    punti += 1 if recensioni >= 20 else 0
    # recensione_negativa_recente: nessun effetto sul punteggio, mai un gancio

    priorita = "Alta" if punti >= 5 else "Media" if punti >= 3 else "Bassa"

    if sede:
        gancio = "Nuova sede o nuovo servizio"
    elif lavoro:
        gancio = "Offerta di lavoro aperta"
    elif annunci >= 3:
        gancio = f"{annunci} annunci nuovi negli ultimi 30 giorni"
    else:
        gancio = "Nessun segnale forte"
    return punti, priorita, gancio


# ---------------------------------------------------------------- 5. MAPPA
def crea_mappa(righe):
    L, H, M = 900, 560, 60  # larghezza, altezza, margine
    lats = [r["lat"] for r in righe]
    lngs = [r["lng"] for r in righe]
    lat0, lat1, lng0, lng1 = min(lats), max(lats), min(lngs), max(lngs)
    k = math.cos(math.radians((lat0 + lat1) / 2))  # correzione longitudine
    span_x = max((lng1 - lng0) * k, 1e-6)
    span_y = max(lat1 - lat0, 1e-6)
    scala = min((L - 2 * M) / span_x, (H - 2 * M) / span_y)
    ox = (L - span_x * scala) / 2
    oy = (H - span_y * scala) / 2

    def xy(lat, lng):
        return ox + (lng - lng0) * k * scala, H - (oy + (lat - lat0) * scala)

    # griglia leggera con le coordinate
    griglia = []
    passo = 0.1
    g = math.floor(lng0 / passo) * passo
    while g <= lng1 + passo:
        x, _ = xy(lat0, g)
        if 0 <= x <= L:
            griglia.append(f'<line x1="{x:.1f}" y1="0" x2="{x:.1f}" y2="{H}" class="g"/>'
                           f'<text x="{x + 3:.1f}" y="{H - 6}" class="gt">{g:.1f}°E</text>')
        g += passo
    g = math.floor(lat0 / passo) * passo
    while g <= lat1 + passo:
        _, y = xy(g, lng0)
        if 0 <= y <= H:
            griglia.append(f'<line x1="0" y1="{y:.1f}" x2="{L}" y2="{y:.1f}" class="g"/>'
                           f'<text x="4" y="{y - 3:.1f}" class="gt">{g:.1f}°N</text>')
        g += passo

    punti = []
    # disegna prima le Basse, così le Alte restano sopra
    ordine = {"Bassa": 0, "Media": 1, "Alta": 2}
    for r in sorted(righe, key=lambda r: ordine[r["priorita"]]):
        x, y = xy(r["lat"], r["lng"])
        info = (f'{r["agenzia"]} – {r["comune"]} ({r["provincia"]}) · '
                f'{r["punteggio"]} punti · priorità {r["priorita"]}')
        punti.append(
            f'<g class="p" data-info="{html.escape(info)}">'
            f'<title>{html.escape(info)}</title>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="11" fill="{COLORI[r["priorita"]]}"/>'
            f'<text x="{x:.1f}" y="{y + 4:.1f}" class="n">{r["punteggio"]}</text></g>')

    legenda = "".join(
        f'<span class="voce"><span class="pallino" style="background:{c}"></span>'
        f'{p} {"(5+ punti)" if p == "Alta" else "(3-4 punti)" if p == "Media" else "(0-2 punti)"}'
        f' — {sum(1 for r in righe if r["priorita"] == p)}</span>'
        for p, c in COLORI.items())

    tabella = "".join(
        f'<tr><td>{i}</td><td>{html.escape(r["agenzia"])}</td><td>{html.escape(r["comune"])}</td>'
        f'<td>{html.escape(r["provincia"])}</td><td>{html.escape(r["email"])}</td>'
        f'<td class="num">{numero_it(r["voto"])}</td><td class="num">{r["recensioni"]}</td>'
        f'<td class="num"><b>{r["punteggio"]}</b></td>'
        f'<td><span class="tag" style="background:{COLORI[r["priorita"]]}">{r["priorita"]}</span></td>'
        f'<td>{html.escape(r["gancio"])}</td></tr>'
        for i, r in enumerate(righe, 1))

    pagina = f"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mappa priorità agenzie – SIMULAZIONE</title>
<style>
  body {{ font-family: system-ui, "Segoe UI", Arial, sans-serif; margin: 0; padding: 24px;
         background: #f6f7f9; color: #1f2328; }}
  .wrap {{ max-width: 960px; margin: 0 auto; }}
  h1 {{ font-size: clamp(24px, 6vw, 44px); margin: 0 0 4px; color: #c62828; letter-spacing: .5px; }}
  .sotto {{ color: #57606a; margin: 0 0 18px; }}
  .carta {{ background: #fff; border: 1px solid #d0d7de; border-radius: 10px; padding: 16px;
           margin-bottom: 20px; position: relative; }}
  svg {{ width: 100%; height: auto; display: block; background: #eef4f8; border-radius: 6px; }}
  .g {{ stroke: #d3dee6; stroke-width: 1; }}
  .gt {{ fill: #8a99a6; font-size: 11px; }}
  .p circle {{ stroke: #fff; stroke-width: 2; cursor: pointer; }}
  .p:hover circle {{ stroke: #1f2328; stroke-width: 3; }}
  .n {{ fill: #fff; font-size: 11px; font-weight: 700; text-anchor: middle; pointer-events: none; }}
  .legenda {{ display: flex; gap: 22px; flex-wrap: wrap; margin-top: 12px; font-size: 14px; }}
  .pallino {{ display: inline-block; width: 14px; height: 14px; border-radius: 50%;
             margin-right: 6px; vertical-align: -2px; }}
  #tip {{ position: absolute; pointer-events: none; background: #1f2328; color: #fff;
         padding: 6px 10px; border-radius: 6px; font-size: 13px; display: none; white-space: nowrap; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
  th, td {{ padding: 8px 6px; border-bottom: 1px solid #e5e8eb; text-align: left; }}
  th {{ background: #f0f2f4; }}
  .num {{ text-align: right; font-variant-numeric: tabular-nums; }}
  .tag {{ color: #fff; padding: 2px 8px; border-radius: 10px; font-size: 12px; font-weight: 600; }}
  .nota {{ font-size: 12px; color: #6e7781; }}
</style>
</head>
<body>
<div class="wrap">
  <h1>SIMULAZIONE – agenzie inventate</h1>
  <p class="sotto">Priorità di contatto delle agenzie immobiliari (dati di prova, nessun dato reale).
     Passa sopra a un punto per vedere il nome; il numero nel punto è il punteggio.</p>

  <div class="carta">
    <svg viewBox="0 0 {L} {H}" role="img" aria-label="Mappa delle agenzie per priorità">
      {''.join(griglia)}
      {''.join(punti)}
    </svg>
    <div id="tip"></div>
    <div class="legenda"><b>Legenda:</b>{legenda}</div>
    <p class="nota">Posizioni calcolate da latitudine e longitudine (proiezione semplice, senza sfondo cartografico).</p>
  </div>

  <div class="carta">
    <h2 style="margin-top:0">Agenzie ordinate per punteggio</h2>
    <div style="overflow-x:auto"><table>
      <thead><tr><th>#</th><th>Agenzia</th><th>Comune</th><th>Prov.</th><th>Email</th>
        <th class="num">Voto</th><th class="num">Recensioni</th><th class="num">Punteggio</th>
        <th>Priorità</th><th>Gancio</th></tr></thead>
      <tbody>{tabella}</tbody>
    </table></div>
  </div>
</div>
<script>
  var tip = document.getElementById('tip'), carta = tip.parentNode;
  document.querySelectorAll('.p').forEach(function (p) {{
    p.addEventListener('mousemove', function (e) {{
      var r = carta.getBoundingClientRect();
      tip.textContent = p.getAttribute('data-info');
      tip.style.display = 'block';
      tip.style.left = (e.clientX - r.left + 14) + 'px';
      tip.style.top = (e.clientY - r.top + 14) + 'px';
    }});
    p.addEventListener('mouseleave', function () {{ tip.style.display = 'none'; }});
  }});
</script>
</body>
</html>
"""
    FILE_MAPPA.write_text(pagina, encoding="utf-8")


# ---------------------------------------------------------------- main
def main():
    agenzie = json.loads(FILE_DATASET.read_text(encoding="utf-8"))
    totale = len(agenzie)

    # 1. PULIZIA
    tenute, scartate = pulizia(agenzie)
    scrivi_csv(FILE_SCARTATE,
               ["motivo", "agenzia", "comune", "provincia", "dominio", "placeId"],
               [[m, a.get("title", ""), a.get("city", ""), a.get("state", ""), d, a.get("placeId", "")]
                for a, d, m in scartate])

    # 2. UNIONE + 3. PUNTEGGIO
    segnali = carica_segnali()
    righe, senza_segnali = [], []
    for a in tenute:
        s = segnali.get(a["_dominio"])
        if s is None:
            senza_segnali.append(a.get("title"))
        punti, priorita, gancio = calcola(a, s)
        righe.append({
            "agenzia": a.get("title", ""), "comune": a.get("city", ""),
            "provincia": a.get("state", ""), "email": a.get("email", ""),
            "voto": a.get("totalScore"), "recensioni": int(a.get("reviewsCount") or 0),
            "punteggio": punti, "priorita": priorita, "gancio": gancio,
            "lat": a["location"]["lat"], "lng": a["location"]["lng"],
        })
    # ordinato per punteggio (a parità: voto, poi recensioni)
    righe.sort(key=lambda r: (-r["punteggio"], -(r["voto"] or 0), -r["recensioni"]))

    # 4. FOGLIO
    scrivi_csv(FILE_FOGLIO,
               ["agenzia", "comune", "provincia", "email", "voto", "recensioni",
                "punteggio", "priorita", "gancio"],
               [[r["agenzia"], r["comune"], r["provincia"], r["email"], numero_it(r["voto"]),
                 r["recensioni"], r["punteggio"], r["priorita"], r["gancio"]] for r in righe])

    # 5. MAPPA
    crea_mappa(righe)

    # riepilogo
    print(f"Righe nel dataset: {totale}")
    print(f"Scartate: {len(scartate)}")
    for a, d, m in scartate:
        print(f"  - {a.get('title')}: {m}")
    if senza_segnali:
        print(f"ATTENZIONE, senza segnali: {', '.join(senza_segnali)}")
    print(f"Agenzie tenute: {len(righe)}")
    for p in ("Alta", "Media", "Bassa"):
        print(f"  {p}: {sum(1 for r in righe if r['priorita'] == p)}")
    print("Classifica:")
    for r in righe:
        print(f"  {r['punteggio']} pt | {r['priorita']:5} | {r['agenzia']} | {r['gancio']}")
    print(f"File scritti: {FILE_SCARTATE.name}, {FILE_FOGLIO.name}, {FILE_MAPPA.name}")


if __name__ == "__main__":
    main()
