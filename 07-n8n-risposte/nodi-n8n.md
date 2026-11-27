# Nodi del workflow "M7 L1 – Risposta finta → classificazione → HubSpot"

## Code in JavaScript – logica della classificazione
Il nodo controlla il testo della risposta con tre liste di parole chiave, **in quest'ordine**:

1. **NO** (es. "non ci interessa") – va per prima perché "non ci interessa" contiene anche "interessa"
2. **NON ORA** (tra le altre: "sentiamoci", "pieni di lavoro", aggiunte durante la lezione)
3. **SÌ** (es. "interessa")

Se nessuna parola corrisponde → **"da leggere a mano"** (rete di sicurezza).

Il nodo aggiunge 3 campi: `categoria`, `fase_hubspot`, `task`.

| Categoria | Fase HubSpot | Task |
|---|---|---|
| no grazie | Chiuso Perso | Nessun task: segnare di non ricontattare |
| non ora | Contatto Iniziale | Ricontattare `<nome>` tra 3 mesi |
| interessata | Presentazione Servizi | Mandare a `<nome>` una fascia di prezzo prima dell'incontro |
| da leggere a mano | Contatto Iniziale | Leggere la risposta di `<nome>` e decidere cosa fare |

Prova istruttiva: "Interessante, però adesso siamo pieni di lavoro. Sentiamoci a gennaio." → prima "da leggere a mano"; dopo aver aggiunto "sentiamoci" e "pieni di lavoro" alla lista NON ORA → "non ora".

## Create a company
- **Name:** `{{ $json.agenzia }}`
- **Company Domain Name:** `{{ $json.email.split('@')[1] }}`

## Create or update a contact
- **Email:** `{{ $('Code in JavaScript').item.json.email }}`
- **Associated Company Name or ID** (Expression): `{{ $json.companyId }}`
- **First Name:** `{{ $('Code in JavaScript').item.json.contatto.split(' ')[0] }}`
- **Last Name:** `{{ $('Code in JavaScript').item.json.contatto.split(' ').slice(1).join(' ') }}`

## Create an engagement
- **Type:** Task
- **Due Date** (Expression): `{{ $now.setZone('Europe/Rome').plus({ months: 3 }).set({ hour: 9, minute: 0, second: 0, millisecond: 0 }).toISO() }}`
- **Metadata → Subject:** `{{ $('Code in JavaScript').item.json.task }}`
- **Metadata → Body:** `[SIMULAZIONE] Categoria: … Risposta di …: "…"`
- **Associations → Contact IDs:** `{{ $json.vid }}`
- **Associations → Company IDs:** `{{ $('Create a company').item.json.companyId }}`

## Service key HubSpot
Percorso: **Altro → Sviluppo → Chiavi → Chiavi di servizio → Crea chiave di servizio**.
Permessi: `crm.objects.companies.read/write`, `crm.objects.contacts.read/write` (dal Modulo 07b anche `crm.objects.deals.read/write`). Rotazione automatica: Off. In n8n: credenziale di tipo **Service Key**.
