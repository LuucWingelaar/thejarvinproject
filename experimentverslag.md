# Verslag experiment Luuc

## Een kort experiment!

Alvast een klein stukje achtergrond: het doel is om een programma te maken dat de functionaliteiten van Jarvis Lyrics aanvult.

Van docent Erik Hekman had ik begrepen dat het voor ons projectteam handig zou zijn om te experimenteren met de Groq LLM API, hiermee zouden dan liedjes gegenereerd kunnen worden door een LLM. 

### Waarom Ollama?
Toen ik probeerde in te loggen bij Groq via GitHub, werkte dit echter niet. Hierdoor ging ik kijken naar alternatieven, en toen bedacht ik mij om met een **lokaal LLM** te werken. 

Dit is beter voor privacy, gezien er geen data gestuurd wordt naar buiten, alles runt volledig lokaal. [^3]

### Het experiment zelf

Zodoende ben ik aan de slag gegaan met Ollama in Python, in eerste instantie met een klein stukje code, waardoor een liedje gegenereerd kon worden.

Mijn eerste poging wilde hij echter niet genereren, gezien het topic "drugs" was, hiermee bedoelde ik medicijnen, oeps!

Maar toen ik op een gegeven moment een iets generieker thema, liefde, probeerde, werkte dit wel. 

Uiteindelijk wilde ik ook user input toevoegen zodat gebruikers zelf teksten kunnen maken! De uiteindelijke code is [hier](https://github.com/LuucWingelaar/thejarvinproject/blob/main/firstexperiment.py) te vinden!

Een ding dat op dit moment nog niet werkt is het aanhouden van een rijmschema, dit zit niet ingebouwd in Jarvis, voor nu ook niet in mijn generator. Dit is echter wel geprobeerd.


## Hoe werkt Jarvis Lyrics? 

Jarvis Lyrics is niets minder dan een GPT-3 wrapper [^1].

Dit betekent dat Jarvis een soort tussenpersoon is tussen de gebruiker en een taalmodel (van wat wij weten, GPT-3 van OpenAI [^1], [^2])

De gebruiker maakt een soort prompt in de UI, Jarvis verpakt die prompt met extra parameters (genre, taal, stijl, "chaos"), stuurt deze naar het taalmodel als API‑call en geeft deze uiteindelijk terug aan de gebruiker als lyrics [^2]

## Vervolgstappen

Uit de interviews met studenten kwamen de volgende dingen aan het licht die deze studenten prettig zouden vinden binnen Jarvis AI of een andere songwritinghulp.

### Controle over rijmschema's 
Een veelgehoorde wens is de mogelijkheid om zelf het rijmschema te kunnen aanpassen. De studenten willen bijvoorbeeld kunnen kiezen tussen structuren als AABB of ABAB, om zo in lijn te blijven met de rest van de tekst. Dit zou in principe goed te doen moeten zijn, gezien dit voornamelijk prompt engineering is.

### Hergebruik van eerdere teksten
De studenten hebben aangegeven dat het prettig zou zijn om eerdere teksten die zij geschreven hebben te kunnen gebruiken zodat het LLM hiervan leert, dit is redelijk lastig te implementeren (gezien er vaak meerdere nummers zijn, en niet 1 standaard format hiervoor). Maar het is het proberen waard.

### Aanpasbare tekstlengte
De mogelijkheid om zelf de lengte van de tekst te bepalen (zoals het aantal coupletten of regels) werd ook als een belangrijke toevoeging genoemd. Dit geeft hen meer controle over het eindresultaat. Dit is prima te doen, het komt neer op prompt engineering.

### Inclusie en exclusie van bepaalde woorden
Tot slot is er voortgekomen dat het voor gebruikers wenselijk is om filters tegen/voor specifieke woorden af te kunnen dwingen (die erin moeten voorkomen) of juist uit te sluiten. Ook dit is goed te doen, een lijst van niet te gebruiken woorden passeren aan de LLM moet goed te doen zijn.


## Bronnen:

[^1]: [GPT‑3 Demo. (z.d.). Jarvis Lyrics. https://gpt3demo.com/apps/jarvis-lyrics](https://gpt3demo.com/apps/jarvis-lyrics)
[^2]: [Shinde, P. (17 augustus 2025). How to build a ChatGPT Wrapper (2025 Edition). Make SaaS Better. https://makesaasbetter.com/chatgpt-wrapper/](https://makesaasbetter.com/chatgpt-wrapper/)
[^3]: [Zonneveld, D (7 mei 2025). Take control: Local LLMs and the fight for data privacy | Hypersolid. https://www.hypersolid.com/articles/local-llms-and-the-fight-for-data-privacy](https://www.hypersolid.com/articles/local-llms-and-the-fight-for-data-privacy)
