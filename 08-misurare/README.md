# Modulo 08 – Misurare i risultati

> ⚠️ **Solo simulazioni.** Campagne, agenzie e trattative sono **inventate**. Nessuna e-mail inviata. Costi delle campagne in euro, importi delle trattative in USD (valuta dell'account HubSpot di prova).

## Obiettivo
Capire se l'outbound funziona e quanto costa, con due numeri chiave (**tasso di risposta** e **costo per meeting**), e mettere tutto in una dashboard costruita con **Claude Code**.

## Strumenti
Claude Sheets (foglio "GTM M8 – Metriche campagne finte") · HubSpot CRM Free (connettore in sola lettura) · Claude Code (app Claude → scheda Code). Costo: 0 €.

## Lezioni

| # | Lezione | Cosa ho imparato |
|---|---|---|
| 1 | Costo per meeting e tasso di risposta | Formule; confronto tra campagne sul costo per meeting (non sui meeting totali); diagnosi di una campagna a 0 meeting; formula `=IF(E2=0,"nessun meeting",F2/E2)` contro `#DIV/0!` |
| 2 | Dashboard con Claude Code | Dati in CSV → prompt a Claude Code → `dashboard.html` che si apre senza internet; controllo dei numeri; correzione con un secondo prompt |

## File

| File | Contenuto |
|---|---|
| [`campagne_finte.csv`](campagne_finte.csv) | 3 campagne finte (A Teramo, B Pescara, C L'Aquila) |
| [`trattative_finte.csv`](trattative_finte.csv) | 10 trattative finte della pipeline HubSpot |
| [`dashboard.html`](dashboard.html) | Dashboard creata da Claude Code (scaricarla e aprirla con doppio clic) |
| [`prompt-claude-code.md`](prompt-claude-code.md) | I due prompt usati: creazione e correzione |

## Formule

| Metrica | Formula |
|---|---|
| Tasso di risposta | risposte ÷ inviate |
| Tasso positivo | risposte positive ÷ inviate |
| Costo per meeting | **tutti** i costi (dominio, caselle, invio, arricchimento) ÷ meeting |
| Importo ponderato | importo × probabilità della fase |
| Tasso di vincita | vinte ÷ (vinte + perse) |

## Risultati della simulazione

**Campagne**

| Campagna | Inviate | Risposte | Tasso risposta | Meeting | Costi | Costo per meeting |
|---|---|---|---|---|---|---|
| A Teramo | 200 | 12 | 6,0% | 2 | 80 € | **40 €** |
| B Pescara | 500 | 20 | 4,0% | 4 | 200 € | 50 € |
| C L'Aquila | 150 | 3 | 2,0% | 0 | 60 € | nessun meeting |
| **Totale** | 850 | 35 | 4,1% | 6 | 340 € | 56,67 € |

**Pipeline**: aperte $ 9.700, ponderato delle aperte **$ 3.420**, chiuse $ 4.200, tasso di vincita 66,7% (2 vinte, 1 persa).

## Lezioni chiave
- Si confrontano le campagne sul **costo per meeting**: B fa più meeting, ma A è più conveniente.
- **0 meeting → pausa e diagnosi:** 0% di risposte = invio/oggetto; risposte tutte "no" = lista o offerta; risposte positive senza meeting = proposta dell'incontro.
- **Il ponderato si guarda solo sulle trattative aperte:** le chiuse sono già 100% o 0% e non entrano nella previsione.
- Claude Code costruisce la dashboard in pochi minuti; il GTM Engineer **controlla i numeri** e fa correggere con un prompt preciso ("Non cambiare nient'altro").
- In Claude Code la cartella di lavoro va aperta come cartella **principale** ("Apri cartella…"), non solo aggiunta.
