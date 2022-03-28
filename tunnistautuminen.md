# Tunnistautumistapoja

## Basic

HTTP Basic Authentikaatiossa annetaan jokaisen API-kutsun mukana
käyttäjätunnus ja salasana.  Se sopii yleensä vain testaamiseen,
mutta todellisissa sovelluksissa se ei ole hyvä vaihtoehto.


## Token

Token-authentikaatiossa käyttäjätunnus ja salasana vaihdetaan
ensin API-serverin muodostamaan tokeniin ja tätä tokenia
käytetään sitten jokaisessa API-kutsussa.


## Sessio

Sessio-authentikaatiossa käytetään selaimen Cookieksi tallennettua
sessio-id:tä.  Tämä sopii esim. Django-backendin API-kutsujen
testaamiseen selaimella.
