# Pal Breeding Planner

A fast, filterable breeding planner for **Palworld**. Mark the Pals you own, pick the one you want, and get the shortest breeding route.

Preview: https://whichfahim.github.io/pal-breeding-planner/

## Features

- **Path finder**: the fewest breeds needed to reach any Pal from the ones you own, shown as ordered steps, plus every parent pair that produces it.
- **Calculator**: pick two parents to see the child (including gender-specific combos), and see what one Pal makes with every Pal you own.
- **My Pals**: track your collection, bulk-mark by filter, import or export a palworld.gg `?own=` link.
- **Filters on every tab**: owned status, element, rarity and work suitability (multi-select, match any or all), plus sorting by Paldex number, name, element, rarity, breed power, breeds needed or work level.
- Light and dark themes, works on phones, and your collection is saved in your browser.

## Accuracy

Breeding follows the same rules as palworld.gg: breed power averaging, nearest-power child with tie-breaking, unique combos and gender-specific combos. Every one of the ~41,000 parent pairs was checked against palworld.gg's own logic. Terraria crossover Pals are not included.

## Project layout

```
index.html            built, self-contained app (this is what gets hosted)
build.py              rebuilds index.html from src/ and data/
src/template.html     markup, styles and app code
data/pals.txt         id|name|paldex|variant|rarity|breed power|ignore|elements|work levels|mount
data/combos.txt       unique breeding combos: parentA parentB child [genderA genderB]
data/pal-icons.json   Pal icons as data URIs
data/ui-icons.json    element and work icons as data URIs
data/default-owned.txt starting collection for first-time visitors
```

Edit anything in `src/` or `data/`, then run:

```
python build.py
```

No dependencies or build tools beyond Python 3.

## Hosting

`index.html` is a single static file, so it runs on GitHub Pages, Netlify, Cloudflare Pages or any static host.

## Credits

Breeding data and icons via [palworld.gg](https://palworld.gg). Palworld and all Pal artwork © Pocketpair, Inc. This is an unofficial fan project and is not affiliated with or endorsed by Pocketpair.
