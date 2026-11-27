# Modulo 06 – Invio e deliverability

> ⚠️ **Solo simulazioni.** Nessuna e-mail è stata inviata. L'agenzia "Casa Prova Immobiliare" (`casaprova.example.com`) e tutte le persone sono **inventate**. I domini `.example.com` sono riservati agli esempi e non arrivano a nessuno.

## Obiettivo
Capire come si mandano e-mail a freddo senza finire nello spam (dominio, autenticazione, warm-up) e come si registra in HubSpot tutto quello che succede dopo l'invio.

## Strumenti
MXToolbox SuperTool (gratis, senza account) · HubSpot CRM Free · Claude. Costo: 0 €.

## Lezioni

| # | Lezione | Cosa ho imparato |
|---|---|---|
| 1 | Dominio e warm-up (teoria + MXToolbox) | Dominio "gemello" per le e-mail a freddo; SPF, DKIM e DMARC; warm-up di 2–3 settimane e partenza da ~10 e-mail al giorno per casella; Smartlead solo in teoria |
| 2 | Simulazione su HubSpot con un'agenzia finta | Azienda, contatto e trattativa collegati; e-mail inviata e risposta **registrate** (mai spedite); spostamento in pipeline quando succede un fatto; importo totale e ponderato; task con scadenza prima dell'evento |
| 3 | HeyReach (LinkedIn) | Saltata per scelta |

## Lezione 1 – Le regole della deliverability
- **Dominio gemello:** il dominio principale resta per i clienti; per le e-mail a freddo si usa un dominio simile (es. `ronaldcrm-agenzie.example.com`) con 2–3 caselle.
- **SPF** = quali server possono spedire; **DKIM** = firma sulla busta; **DMARC** = cosa fare se i controlli falliscono. Servono tutti e tre prima di partire; DMARC può iniziare in modalità "osserva" (`p=none`).
- **Prova pratica:** MXToolbox con `spf:gmail.com` e `dmarc:gmail.com` (dominio pubblico).
- **Warm-up:** 2–3 settimane, poi ~10 e-mail al giorno per casella, fino a ~30 in un mese. Fretta = spam.

## Lezione 2 – Simulazione "Casa Prova Immobiliare"
1. **Base nel CRM:** azienda (dominio per primo), contatto creato dalla scheda azienda (si collega da solo), base legale GDPR "Interesse legittimo - prospect/lead", trattativa creata dalla scheda del contatto.
2. **E-mail finta:** bozza scritta con la ricetta del Modulo 05, registrata con **Attività → E-mail → "Registra un'e-mail"** (non "Crea un'e-mail", che spedisce davvero), con l'etichetta `[SIMULAZIONE]`.
3. **Pipeline:** Nuovo Lead → Contatto Iniziale (e-mail partita).
4. **Risposta finta** (interessata, chiede il prezzo, propone un incontro) → **Presentazione Servizi**. Chiedere il prezzo non è ancora Negoziazione.
5. **Importo e task:** importo 1500; task "mandare una fascia di prezzo" con scadenza **prima** dell'incontro e collegato a trattativa, contatto e azienda.

**Regola:** si sposta la trattativa quando succede un fatto, non quando lo speri.

## Competenze principali
- Scegliere e preparare un dominio per le e-mail a freddo
- Leggere SPF e DMARC con MXToolbox
- Pianificare un warm-up e una partenza graduale
- Registrare e-mail e risposte in HubSpot senza spedire niente
- Leggere importo totale e ponderato di una trattativa
