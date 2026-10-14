#!/usr/bin/env python3
"""Filter a local public catalogue inventory without downloading speech data."""
import argparse
import csv
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--language')
parser.add_argument('--country')
parser.add_argument('--region')
parser.add_argument('--verify', action='store_true')
args = parser.parse_args()
path = Path(__file__).resolve().with_name('inventory.csv')
with path.open(newline='', encoding='utf-8') as stream:
    rows = list(csv.DictReader(stream))

if args.verify:
    if len({r['slug'] for r in rows}) != len(rows):
        raise SystemExit('Duplicate catalogue slug')
    for row in rows:
        for key in ('listed_audio_hours', 'listed_speaker_count', 'price_per_audio_hour_usd'):
            if int(row[key]) <= 0:
                raise SystemExit(f'Invalid {key} for {row["slug"]}')
        if row['catalogue_url'] != 'https://www.speechdata.ai/datasets/' + row['slug']:
            raise SystemExit(f'Unexpected source URL for {row["slug"]}')
    sibling = path.with_suffix('.json')
    source_rows = json.loads(sibling.read_text(encoding='utf-8'))
    normalised = [{**row, 'listed_audio_hours': int(row['listed_audio_hours']),
                   'listed_speaker_count': int(row['listed_speaker_count']),
                   'price_per_audio_hour_usd': int(row['price_per_audio_hour_usd'])} for row in rows]
    if normalised != source_rows:
        raise SystemExit('CSV and JSON disagree')
    print(json.dumps({'datasets': len(rows),
                      'distinct_languages': len({r['language'] for r in rows}),
                      'listed_audio_hours': sum(int(r['listed_audio_hours']) for r in rows),
                      'listed_speaker_count': sum(int(r['listed_speaker_count']) for r in rows),
                      'min_price_per_audio_hour_usd': min(int(r['price_per_audio_hour_usd']) for r in rows),
                      'max_price_per_audio_hour_usd': max(int(r['price_per_audio_hour_usd']) for r in rows)}, indent=2))
else:
    for key in ('language', 'country', 'region'):
        selected = getattr(args, key)
        if selected:
            rows = [r for r in rows if r[key].casefold() == selected.casefold()]
    for row in rows:
        print(f'{row["name"]} | {row["country"]} | {row["listed_audio_hours"]} listed hours | {row["catalogue_url"]}')
