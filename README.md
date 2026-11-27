# GTM Engineering – Outbound per agenzie immobiliari (simulazione)

Ho costruito **dall'inizio alla fine** un sistema di outbound B2B: trova le aziende giuste, le pulisce, sceglie a chi scrivere prima, prepara il messaggio con l'AI, registra tutto nel CRM e misura quanto costa ogni incontro ottenuto.

Caso di studio: una persona che aiuta le piccole agenzie immobiliari in Abruzzo a organizzare i contatti dei clienti con un CRM e qualche automazione semplice.

> ⚠️ **SIMULAZIONE.** Dal modulo 05 in poi tutte le agenzie, le persone, i fatti e le e-mail (`@….example.com`) sono **inventati**. Nessun messaggio è stato inviato e nessuna persona reale è stata contattata. I moduli 01–04, fatti su dati aziendali pubblici, qui sono solo riassunti.

## Il flusso

```
ICP → lista aziende → pulizia → arricchimento → segnali e priorità
    → messaggio scritto da Claude → invio (teoria) → risposta → CRM
    → pipeline → misure (costo per meeting, tasso di risposta)
```

## Cosa so fare

- **Definire il cliente ideale (ICP)** e scartare chi non c'entra (franchising, doppioni, aziende chiuse)
- **Costruire e arricchire liste** con Clay e Apify, tenendo sotto controllo crediti e costi
- **Dare una priorità** alle aziende con i segnali di acquisto (lead scoring)
- **Far scrivere a Claude e-mail a freddo** in italiano naturale, senza "impronte AI", e controllarle
- **Preparare l'invio** senza finire nello spam: dominio gemello, SPF/DKIM/DMARC, warm-up
- **Automatizzare il passaggio al CRM** con n8n: risposta → classificazione → azienda, contatto e task in HubSpot
- **Gestire la pipeline**: fase giusta per ogni fatto, importo ponderato, tasso di vincita
- **Misurare**: tasso di risposta e costo per meeting, con dashboard creata da Claude Code
- **Usare Claude Code come regista**: un prompt con passi numerati che fa tutta la catena, e io che controllo i numeri

## Strumenti

Claude e Claude Code · HubSpot CRM · Clay · Apify · n8n · Make · Google Sheets · MXToolbox — tutti su piani gratuiti (costo totale del corso: meno di 1 $ di crediti Apify).

## Moduli

| # | Modulo | Strumenti | Risultato principale |
|---|---|---|---|
| 01–04 | [Le basi: CRM, lista, arricchimento, segnali](01-04-basi-riassunto/) (riassunto) | HubSpot, Clay, Apify, n8n, Make | CRM configurato, 14 aziende complete importate, priorità con i segnali |
| 05 | [Messaggi scritti con Claude](05-messaggi-claude/) | Claude | Ricetta di prompt riutilizzabile + bozze approvate |
| 06 | [Invio e deliverability](06-invio-deliverability/) | MXToolbox, HubSpot | Regole anti-spam + simulazione completa in HubSpot |
| 07 | [Dal canale al CRM con n8n](07-n8n-risposte/) | n8n, HubSpot | Risposta classificata e salvata in HubSpot in automatico |
| 07b | [La pipeline dall'inizio alla fine](07b-pipeline/) | HubSpot, n8n | 12 trattative gestite, tasso di vincita 67% |
| 08 | [Misurare i risultati](08-misurare/) | Foglio di calcolo, Claude Code | Costo per meeting per campagna + dashboard |
| 09 | [Progetto finale con Claude Code](09-progetto-finale/) | Claude Code, Google Sheets | 13 righe grezze → 10 agenzie con priorità + mappa, con un solo prompt |

## Da dove partire

1. **[09 – Progetto finale](09-progetto-finale/)**: tutto il flusso in un colpo solo (prompt, script Python, risultato).
2. **[05 – Ricetta del prompt](05-messaggi-claude/ricetta-prompt.md)**: come faccio scrivere a Claude un'e-mail che non sembra scritta dall'AI.
3. **[08 – Misurare](08-misurare/)**: i due numeri che dicono se l'outbound funziona.

> Le pagine `.html` (dashboard e mappa) GitHub le mostra come codice: per vederle basta scaricarle (pulsante "Download raw file") e aprirle con doppio clic. Funzionano senza internet.

## Come ho lavorato

Corso pratico personalizzato con Claude come docente (novembre 2026). Regola fissa: **l'AI prepara, io controllo.** Ogni numero prodotto dall'AI è stato verificato a mano prima di essere usato.

---
*Autore: Ronald Pasquale Marcozzi — ex mediatore creditizio, oggi in formazione come GTM Engineer.*
