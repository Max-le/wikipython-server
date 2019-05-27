# wikipython-server
This is the server side ( working as an API ) of the app Wikipython, which provides translations based on Wiktionary's data

--- 
HOW TO USE THE API : 

Send a GET request to route /translate with params : "word" ( the word to translate ) and "lang" the target language
Example : localhost:5000/translate?word=meaning&lang=German

The app is deployed at https://cryptic-gorge-83791.herokuapp.com