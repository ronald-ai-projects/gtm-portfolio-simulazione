# Prompt dato a Claude Code (M9 L1)

```
Sei il mio assistente GTM. Nella cartella ci sono due file di una SIMULAZIONE (agenzie immobiliari inventate, nessun dato reale):
- dataset_apify_finto.json = risultato di una ricerca Google Maps fatta con Apify
- segnali_finti.csv = segnali di acquisto per ogni dominio

Crea UN solo script (Python se è installato, altrimenti Node.js) chiamato "flusso" che faccia tutta la catena in un colpo solo, poi eseguilo. Non modificare i due file di partenza.

1. PULIZIA: togli le agenzie chiuse (permanentlyClosed = true), i franchising (nel nome c'è "Franchising" o "Rete") e i doppioni (stesso dominio del sito: tieni la prima riga). Scrivi le righe tolte in "scartate.csv" con la colonna "motivo".
2. UNIONE: collega ogni agenzia ai suoi segnali usando il dominio del sito (senza https:// e senza www.).
3. PUNTEGGIO di priorità: annunci_nuovi_30gg 3 o più +2; offerta_lavoro_aperta = sì +2; nuova_sede_o_servizio = sì +2; voto 4,5 o più +1; 20 recensioni o più +1; recensione_negativa_recente NON toglie punti. Priorità: Alta da 5 in su, Media 3-4, Bassa 0-2. Colonna "gancio": il segnale positivo più forte (nuova sede/servizio, offerta di lavoro, annunci nuovi). Una recensione negativa non è mai un gancio.
4. FOGLIO: "agenzie_priorita.csv" per Google Sheets in italiano (separatore punto e virgola, decimali con la virgola), ordinato per punteggio, colonne: agenzia, comune, provincia, email, voto, recensioni, punteggio, priorita, gancio.
5. MAPPA: "mappa.html" senza internet e senza librerie (SVG), punti per latitudine/longitudine, verde Alta, arancione Media, grigio Bassa, nome al passaggio del mouse, legenda, scritta "SIMULAZIONE – agenzie inventate", tabella sotto. Tutto in italiano.

Alla fine aprimi la mappa e riassumi in chat: righe iniziali, scartate e perché, quante Alta/Media/Bassa e le prime 3 agenzie con punteggio e gancio.
```
