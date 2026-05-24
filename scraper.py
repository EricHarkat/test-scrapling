from scrapling import Fetcher

# Fetcher est l'objet qui fait les requêtes HTTP (comme un navigateur)
fetcher = Fetcher()

# On télécharge la page — page est un objet Scrapling qu'on peut interroger
page = fetcher.get("https://quotes.toscrape.com/")

# Chaque citation est dans un bloc HTML avec class="quote"
# .css() permet de sélectionner des éléments avec un sélecteur CSS
quotes = page.css(".quote")

print(f"{len(quotes)} citations trouvées\n")

for quote in quotes:
    # .css() retourne une liste — [0] prend le premier élément
    # .text est le texte à l'intérieur de l'élément
    texte  = quote.css(".text")[0].text
    auteur = quote.css(".author")[0].text

    # Les tags sont plusieurs éléments — on récupère une liste
    tags = [tag.text for tag in quote.css(".tag")]

    print(f"Citation : {texte}")
    print(f"Auteur   : {auteur}")
    print(f"Tags     : {', '.join(tags)}")
    print("-" * 50)
