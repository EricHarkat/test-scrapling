from scrapling import Fetcher

fetcher = Fetcher()

BASE_URL = "https://quotes.toscrape.com"
url_courante = BASE_URL + "/"

toutes_les_citations = []
numero_page = 1

# On boucle tant qu'il y a une page suivante
while url_courante:
    print(f"--- Page {numero_page} : {url_courante}")
    page = fetcher.get(url_courante)

    # Extraction des citations de cette page (même logique qu'avant)
    for quote in page.css(".quote"):
        texte  = quote.css(".text")[0].text
        auteur = quote.css(".author")[0].text
        tags   = [tag.text for tag in quote.css(".tag")]
        toutes_les_citations.append({"texte": texte, "auteur": auteur, "tags": tags})

    # Cherche le bouton "Next" — s'il n'existe pas, next_btn est une liste vide
    next_btn = page.css(".next a")
    if next_btn:
        # urljoin() construit l'URL complète à partir du chemin relatif (/page/2/)
        url_courante = next_btn[0].urljoin(next_btn[0].attrib["href"])
        numero_page += 1
    else:
        # Plus de bouton "Next" = dernière page, on arrête la boucle
        url_courante = None

print(f"\nTotal : {len(toutes_les_citations)} citations sur {numero_page} pages\n")

for c in toutes_les_citations:
    print(f"{c['auteur']} — {c['texte'][:60]}...")
    print(f"  Tags : {', '.join(c['tags'])}")
