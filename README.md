# Speechdata.ai public catalogue inventory

A machine-readable index of public conversational speech dataset listings. Use it to shortlist catalogue entries by language, country or region and open the corresponding source page.

This snapshot contains 60 catalogue entries covering 49 distinct language names, described on Speechdata.ai as 60 languages and dialects. The listed entries total 73,000 audio hours and 7,250 listed speakers, summed across entries. The listed unit prices range from USD 60 to USD 95 per audio hour. These are catalogue totals and list prices, not claims about independent observations, a test split or a downloadable open corpus.

## What the files contain

`inventory.csv` and `inventory.json` contain the same records. Each record has a stable catalogue slug, title, language, named variant when present, country, region, listed hours, listed speaker count, the public dataset-page URL and list price in USD per audio hour. Hours are audio hours; speakers are the aggregate listed speaker count for that corpus, not individual speaker records. Prices are a dated inventory field and should be checked on the source page before a purchase. A blank variant means no separate variant label is specified in the catalogue; it does not establish that all dialects are covered.

`catalogue.py` reads the local CSV, filters by language, country or region, and prints a shortlist. It does not download audio, contact a service or need an API key.

```sh
python3 catalogue.py --language English
python3 catalogue.py --country India
python3 catalogue.py --region Europe
python3 catalogue.py --verify
```

## Scope and source

This is inventory metadata only. It includes no speech recordings, transcripts, individual speaker records, consent documents or training/evaluation results. The source is the public [Speechdata.ai catalogue](https://www.speechdata.ai/datasets); every entry links its own dataset page. Snapshot date: 14 October 2026. Check those pages for current details before procurement.

The listed commercial corpora remain available through their provider's separate licensing process. This inventory does not grant a licence to any speech recording or transcript, promise stock or delivery dates, or establish a permitted use beyond the published source. [Speechdata.ai](https://www.speechdata.ai/) also offers collection and annotation. [Spirelight.ai](https://www.spirelight.ai/) is the parent company's site.
