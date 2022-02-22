# wikipython-server
This is the server side ( working as an API ) of the app Wikipython, which provides translations based on Wiktionary's data

## Start the Flask server 
In Terminal : 
```
export FLASK_APP=server.py
flask run
```
--- 
HOW TO USE THE API : 

Send a GET request to route /translate with params : "word" ( the word to translate ) and "lang" the target language
Example : localhost:5000/translate?word=meaning&lang=German

The back-end of the app ( python server) is accessible at https://wiki-python-server.herokuapp.com
