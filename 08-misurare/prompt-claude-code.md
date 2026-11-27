# Prompt usati con Claude Code (Modulo 08 – Lezione 2)

Claude Code (app Claude → scheda **Code**) aperto sulla cartella `08-Misurare` come **cartella principale** (non come "Include anche"), con i due CSV dentro.

## 1. Creare la dashboard

```
Lavori nella cartella 08-Misurare. È un esercizio di un corso: tutti i dati sono finti (simulazione), nessuna agenzia è reale.

Ci sono due file:
- campagne_finte.csv: campagne e-mail finte (Inviate, Risposte, Positive, Meeting, Costi_EUR)
- trattative_finte.csv: trattative finte di HubSpot (Fase, Probabilita, Importo_USD)

Crea un solo file dashboard.html che si apre con doppio clic nel browser, anche senza internet: niente librerie esterne, grafici fatti con HTML, CSS o SVG. Copia i dati dei CSV dentro la pagina. Non modificare i CSV e non installare niente.

Tutto in italiano, numeri in formato italiano (virgola per i decimali). Euro per i costi delle campagne, dollari per gli importi delle trattative. In alto una scritta ben visibile: "SIMULAZIONE – dati finti del corso GTM".

Sezione 1 – Campagne:
- riquadri in alto con i totali: e-mail inviate, risposte, tasso di risposta, meeting, costi totali, costo per meeting
- una tabella per campagna con: tasso di risposta (risposte ÷ inviate), tasso positivo (positive ÷ inviate), costo per meeting (costi ÷ meeting). Se i meeting sono 0 scrivi "nessun meeting", mai un errore
- un grafico a barre del costo per meeting di ogni campagna; evidenzia in verde la campagna più conveniente

Sezione 2 – Pipeline:
- un grafico a barre con il numero di trattative per fase, nell'ordine: Nuovo Lead, Contatto Iniziale, Presentazione Servizi, Negoziazione, Chiuso Vinto, Chiuso Perso
- una tabella per fase con importo totale e importo ponderato (importo × probabilità)
- riquadri con: valore delle trattative aperte, valore ponderato delle aperte, tasso di vincita (vinte ÷ (vinte + perse))

Stile semplice e pulito, leggibile anche sullo schermo di un portatile.

Alla fine scrivimi in chat, in italiano semplice, i numeri principali che hai calcolato, così li controllo.
```

## 2. Correzione dopo il controllo

Il totale ponderato della tabella ($ 6.420) includeva anche le trattative chiuse: si confondeva con il ponderato delle aperte ($ 3.420).

```
Nella tabella "Importi per fase" il "Totale" ponderato di $ 6.420 confonde, perché include anche le trattative già chiuse.
Sostituisci la riga Totale con due righe:
- "Totale aperte" (Nuovo Lead, Contatto Iniziale, Presentazione Servizi, Negoziazione): importo e ponderato
- "Totale chiuse" (Chiuso Vinto e Chiuso Perso): solo l'importo; nella colonna ponderato scrivi "–"
Evidenzia in grassetto il ponderato delle aperte. Non cambiare nient'altro.
Poi dimmi i due totali.
```
