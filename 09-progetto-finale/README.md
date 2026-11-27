# Modulo 09 – Lezione 1: progetto finale con Claude Code

> ⚠️ **SIMULAZIONE.** Tutte le agenzie, i comuni, i siti e le e-mail (`@….example.com`) sono inventati. Nessun dato reale, nessun messaggio inviato.

## Cosa fa il flusso
Un solo prompt a **Claude Code** (app Claude → Code, cartella locale `09-Progetto-finale`) crea ed esegue lo script `flusso.py`, che fa tutta la catena in un colpo solo:

```
dati grezzi in formato Apify  →  pulizia  →  unione con i segnali  →  punteggio di priorità  →  foglio Google Sheets + mappa
```

| File | Ruolo |
|---|---|
| `dataset_apify_finto.json` | 13 righe che imitano l'output dell'Actor Google Maps di Apify (con 3 trappole: un doppione, un'agenzia chiusa, un franchising) |
| `segnali_finti.csv` | segnali di acquisto per dominio (annunci nuovi, offerta di lavoro, nuova sede/servizio, recensione negativa) |
| `prompt-claude-code.md` | il prompt unico dato a Claude Code |
| `flusso.py` | lo script scritto ed eseguito da Claude Code |
| `scartate.csv` | righe tolte con il motivo |
| `agenzie_priorita.csv` | lista finale per Google Sheets (separatore `;`, decimali con la virgola) |
| `mappa.html` | mappa SVG offline con punti colorati per priorità + tabella |

## Regola di punteggio
annunci nuovi ≥ 3: +2 · offerta di lavoro: +2 · nuova sede/servizio: +2 · voto ≥ 4,5: +1 · recensioni ≥ 20: +1.
**Alta** ≥ 5, **Media** 3–4, **Bassa** 0–2. La recensione negativa non toglie punti e non è mai un gancio.

## Risultato (controllato a mano)
- 13 righe → 3 scartate → **10 agenzie**
- **4 Alta**, 2 Media, 4 Bassa
- Prime 3: Ponte Vecchio Finto (8, nuova sede/servizio), Pratoverde (8, nuova sede/servizio), Valle Serena (6, offerta di lavoro)
- Lista importata in Google Sheets: *File → Importa → Carica*, separatore "Rileva automaticamente", conversione dei numeri attiva → foglio "GTM M9 – Agenzie finte priorità (SIMULAZIONE)"

## Cosa ho imparato
- Usare Claude Code come "regista": un prompt preciso con passi numerati sostituisce più strumenti usati a mano
- Preparare dati di prova con trappole per verificare che la pulizia funzioni
- Controllare i numeri prodotti dall'AI prima di usarli
- Importare un CSV in Google Sheets in formato italiano
- I segnali negativi servono a me, non si citano nel messaggio

Costo: 0 € (nessun credito Apify, nessuna modifica in HubSpot).
