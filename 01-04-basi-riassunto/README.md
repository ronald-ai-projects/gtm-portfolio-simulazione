# Moduli 01–04 – Le basi: CRM, lista, arricchimento e segnali (riassunto)

> ℹ️ In questi primi moduli ho lavorato anche su agenzie vere, usando solo dati aziendali pubblici. Per questo, in questo repository pubblico, i moduli 01–04 sono **solo riassunti**: niente file CSV, niente screenshot, nessun nome di agenzia o di persona. Il materiale completo resta in un repository privato.

## 01 – CRM con HubSpot (piano Free)
- Pipeline di vendita personalizzata: `Nuovo Lead → Contatto Iniziale → Presentazione Servizi → Negoziazione → Chiuso Vinto / Chiuso Perso`
- Importazione da CSV di aziende e contatti collegati tra loro, con proprietà personalizzate (annunci attivi, voto e recensioni Google, e-mail aziendale)
- Regole contro i doppioni: dominio per le aziende, e-mail per i contatti; 0 errori in importazione
- Concetto di **importo ponderato** = importo × probabilità della fase

## 02 – Lista e arricchimento con Clay
- Lista di 10 agenzie arricchita con sito, telefono, servizi e decisore: **3 lead pronti per il CRM**
- Waterfall per trovare il dominio; formula che scarta i portali immobiliari
- **Claygent** (agente AI di Clay) con prompt strutturato e risposta in JSON divisa in colonne
- Controllo qualità: colonna "Stato lead" e vista "Pronti per HubSpot"
- Costi: 3,35 crediti per agenzia, **11,17 crediti per lead pronto** (costo per riga ÷ tasso di conversione)
- Lista su scala: 81 agenzie in Abruzzo, filtri per escludere i franchising

## 03 – Apify: Google Maps e contatti
- Actor `compass/crawler-google-places` (Google Maps) e `vdrmota/contact-info-scraper` (e-mail dai siti)
- 3 zone, 25 attività trovate → 9 escluse dal controllo ICP → **14 aziende complete in HubSpot**
- Costo totale: circa **0,30 $** sui 5 $ gratuiti al mese, con tetto di spesa impostato su ogni Run
- Waterfall e-mail a mano: sito (piè di pagina, Contatti, Privacy) → Facebook → AI solo come ultima risorsa
- Regole ICP: fuori i franchising nazionali, dentro le piccole realtà locali con titolare sul territorio; solo e-mail aziendali o di ruolo

## 04 – Segnali di acquisto
- Segnali **strutturali** (chi è l'azienda) e **comportamentali** (cosa fa adesso: valgono solo se recenti)
- Colonne formula in Clay: "Volume clienti", "Segnale assunzioni" e **"Priorità"** (lead scoring Alta / Media / Bassa)
- Il segnale si cerca dove lo lascia l'ICP: per le piccole agenzie sito, Facebook e post, non i grandi portali di lavoro
- Workflow **n8n** "Segnale → arricchimento sito → riga Clay via webhook" (5 nodi, 0 crediti)
- Connettore **Claude + Clay**: ricerche e arricchimenti fatti da Claude, con i crediti controllati prima e dopo ogni passo
- Teoria con prezzi: Atoka, Crunchbase, Goji Berry

## Lezione di integrazione
- Apify → Clay e scenario **Make** "Apify → HubSpot" che aggiorna il voto Google delle aziende nel CRM

## Competenze
CRM e pipeline · importazioni senza doppioni · arricchimento a waterfall · prompt per agenti AI · scraping con Apify e controllo dei costi · lead scoring con i segnali · primi workflow n8n e Make · GDPR (solo dati aziendali pubblici)
