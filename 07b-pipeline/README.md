# Modulo 07b – La pipeline dall'inizio alla fine

> ⚠️ **Solo simulazioni.** Tutte le agenzie sono **inventate**, con domini `@….example.com`. Nessuna e-mail inviata. Importi in USD (valuta dell'account di prova).

## Obiettivo
Gestire la pipeline delle trattative come un commerciale: capire in che fase va ogni trattativa, leggere i numeri giusti e vedere come gli spostamenti si possono automatizzare.

## Strumenti
HubSpot CRM Free · n8n (sul PC) · connettore Claude–HubSpot. Costo: 0 €.

## Lezioni

| # | Lezione | Cosa ho imparato |
|---|---|---|
| 1 | Trattative finte e vista a bacheca | Bacheca con importo totale e ponderato; fase giusta per ogni fatto; task completati (✓) e non eliminati; trattative senza prossima attività = dimenticate |
| 2 | Permessi, spostamento automatico e dashboard | Permessi `deals.read/write` sulla Service key; copia del workflow n8n per le prove; trattativa spostata dopo una risposta "interessata"; dashboard, imbuto e tasso di vincita |

## Quale fase per quale fatto

| Fatto | Fase |
|---|---|
| Agenzia in lista, nessun contatto | Nuovo Lead (10%) |
| E-mail partita (anche senza risposta) | Contatto Iniziale (20%) |
| Interessata, chiede prezzo o incontro | Presentazione Servizi (40%) |
| Offerta scritta inviata | Negoziazione (70%) |
| Contratto firmato (non il pagamento) | Chiuso Vinto (100%) |
| "No grazie" | Chiuso Perso (0%) |

## Pipeline finale della simulazione (26/11/2026)

| Fase | Trattative | Importo totale | Ponderato |
|---|---|---|---|
| Nuovo Lead | 2 | 2200 | 220 |
| Contatto Iniziale | 4 | 4700 | 940 |
| Presentazione Servizi | 2 | 3000 | 1200 |
| Negoziazione | 1 | 2000 | 1400 |
| Chiuso Vinto | 2 | 3000 | – |
| Chiuso Perso | 1 | 1200 | – |

**Tasso di vincita** = vinte ÷ (vinte + perse) = 2 ÷ 3 ≈ 67% (le trattative aperte non si contano).

## Cose da ricordare
- Si guarda il ponderato, non il totale: tanti contatti non vogliono dire tanti soldi.
- La dashboard **conta** le trattative (l'imbuto); la bacheca dice **quanto valgono**.
- Ogni trattativa aperta deve avere un prossimo task con una data.
- Le attività "Senza assegnazione" non hanno un responsabile: rischiano di non essere fatte.
- Le prove in n8n si fanno su una **copia** del workflow, per non creare doppioni.
- Lo spostamento automatico segue la catena: risposta → classificazione → ricerca della trattativa → cambio di fase.

## Competenze principali
- Leggere bacheca e dashboard della pipeline in HubSpot
- Assegnare la fase giusta a ogni trattativa
- Calcolare importo ponderato e tasso di vincita
- Gestire i task collegati alle trattative
- Dare a una chiave solo i permessi necessari
