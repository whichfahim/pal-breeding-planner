"""Build index.html from src/template.html and the data files. Run: python build.py"""
import json, pathlib
root = pathlib.Path(__file__).parent
read = lambda p: (root / p).read_text(encoding="utf-8")
page = read("src/template.html")
owned = ",".join(l.strip() for l in read("data/default-owned.txt").splitlines() if l.strip())
page = (page.replace("__PALS__", read("data/pals.txt"))
            .replace("__COMBOS__", read("data/combos.txt"))
            .replace("__OWNED__", owned)
            .replace("__ICONS__", read("data/pal-icons.json"))
            .replace("__UIICON__", read("data/ui-icons.json"))
            .replace("__TOUCHICON__", read("data/touch-icon.txt").strip()))
i = page.index("</style>") + len("</style>")
html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="description" content="Palworld breeding path finder, breeding calculator and Pal collection tracker.">\n'
        + page[:i] + "\n</head>\n<body>\n" + page[i:] + "\n</body>\n</html>\n")
(root / "index.html").write_text(html, encoding="utf-8")
print(f"index.html written ({len(html)//1024} KB)")
