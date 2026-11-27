# Modulo 07 – Dal canale al CRM con n8n

> ⚠️ **Solo simulazioni.** Le risposte sono inventate e le agenzie (Casa Prova, Collefinto) sono finte, con e-mail `@….example.com`. Nessuna e-mail inviata o ricevuta davvero. **La chiave di HubSpot non è in questo repository e non deve mai esserci.**

## Obiettivo
Quando un'agenzia risponde, n8n legge la risposta, capisce di che tipo è (interessata, non ora, no grazie) e aggiorna HubSpot da solo: azienda, contatto e prossimo task.

## Strumenti
n8n (installato sul PC, gratis) · HubSpot CRM Free con **Service key** · Claude. Costo: 0 €.

## Lezioni

| # | Lezione | Cosa ho imparato |
|---|---|---|
| 1 | Risposta finta → classificazione (solo n8n) | Trigger manuale → Edit Fields (risposta finta in JSON) → Code (parole chiave); ordine dei controlli NO → NON ORA → SÌ; rete di sicurezza "da leggere a mano" |
| 2 | n8n → HubSpot | Service key al posto delle app private; credenziale "Service Key" in n8n; nodi Create company → Create or update contact → Create engagement (task tra 3 mesi); `$json` e `$('Nome nodo')`; fuso orario Europe/Rome |

## Il workflow
```
When clicking 'Execute workflow' → Edit Fields → Code in JavaScript
  → Create a company → Create or update a contact → Create an engagement (task)
```

## File
- [`nodi-n8n.md`](nodi-n8n.md) – logica della classificazione ed espressioni di ogni nodo HubSpot
- [`risposte-finte.json`](risposte-finte.json) – le risposte inventate usate nelle prove

## Cose da ricordare
- Le regole a parole chiave sono gratis ma rigide: cercano parole esatte, non capiscono il significato. Per i casi difficili serve una persona oppure un nodo AI.
- "Create or update" usa l'e-mail come chiave (niente doppioni); "Create" crea un record nuovo a ogni esecuzione.
- Alla Service key si danno solo i permessi che servono, e non si incolla mai in chat, nei file o su GitHub.
- Senza `setZone('Europe/Rome')` n8n usava il fuso di New York.

## Competenze principali
- Costruire un workflow n8n con dati di prova e codice JavaScript
- Collegare n8n a HubSpot con una Service key
- Creare azienda, contatto e task collegati tra loro
- Passare dati tra nodi con le espressioni
- Evitare i doppioni durante le prove
