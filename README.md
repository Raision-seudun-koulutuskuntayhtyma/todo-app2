# todo-app2
Todo-ohjelma Djangolla

## Asennus

1. Luo virtuaaliympäristö:
   ```sh
   python3 -m venv venv
   ```
2. Aktivoi virtuaaliympäristö.
   - Voit tehdä tämän esim. VS Codesta ja avata sen jälkeen
     uuden terminaali-ikkunan, jossa venv on aktiivinen.
   - Vaihtoehtoisesti aja joko `. venv/bin/activate` (Linux & Mac)
     tai `venv\scripts\activate.ps1` (Windows).
3. Asenna projektin tarvimat riippuvuudet (requirements):
   ```sh
   pip install -r requirements.txt
   ```
4. Alusta tietokanta
   ```sh
   python manage.py migrate
   ```
5. Luo pääkäyttäjä
   ```sh
   python manage.py createsuperuser
   ```

## API

Sisältää myös Django Rest Frameworkilla tehdyn rajapinnan, jota
käyttävä React applikaatio on repossa:
https://github.com/Raision-seudun-koulutuskuntayhtyma/react-todo/
