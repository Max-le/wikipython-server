
## BACK-END SERVER ##

from flask import Flask, request, render_template, Response
from wiki import *
from flask_cors import CORS

from bs4 import BeautifulSoup
import wikipedia
import scan, fetcher, json
import google_images_fetcher
app = Flask(__name__)
CORS(app)

@app.route('/')

def home():
    return render_template("home.html")
@app.route('/', methods=['POST'])

def my_form_post():
    word = request.form['text']
    lang = 'German'
    payload = {'word': word, 'lang': lang}
    r = requests.get("https://cryptic-gorge-83791.herokuapp.com/translate", params=payload)
    print(r.url)
    result = json.loads(r.text)
    return render_template("home.html", data=result)
@app.route('/translate')
def translate():
    word = request.args.get('word')
    lang = request.args.get('lang')
    fetcher.get_wiktionary_data(word)
    dico = scan.extract_defs_and_translations('word_data.txt', lang)
    data =  json.dumps(dico, indent=4 )
    return Response(data, mimetype='text/json')
@app.route("/image")
def image():
    query_image = request.args.get('word')
    number_results = request.args.get('number')
    list_url_images = google_images_fetcher.search(query_image, number_results)
    data =  json.dumps(list_url_images, indent=4 )
    return Response(data, mimetype='text/json')

@app.route('/list')
def list():
    word_to_translate = request.args.get('word')
    print(word_to_translate)
    related_pages = get_related_wiki_pages(word_to_translate)
    wiki_page = wikipedia.page(related_pages[0])
    return render_template("base.html", data=related_pages)
@app.route("/translateWP")
def translateWP():
    word_to_translate = request.args.get('word')
    print("Received  : "+word_to_translate)
    related_pages = get_related_wiki_pages(word_to_translate)
    wiki_page = wikipedia.page(related_pages[0])
    list_links = scrap_all_languages_links(get_wiki_html_page(wiki_page.title, 'en'))
    link_target_language = retrieve_target_language_link(list_links,'fr')
    translated_word = title_wiki_page(link_target_language)
    
    return translated_word
