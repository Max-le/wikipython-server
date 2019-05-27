from wiki import *
import fetcher
import scan
import pycountry
from bs4 import BeautifulSoup
import json

# word = 'Aachen' 
# wikilink = 'https://fr.wikipedia.org/wiki/Aix-la-Chapelle'
# related_pages = get_related_wiki_pages(word)
# page = wikipedia.page(related_pages[0])
# print('Found a page with title : '+page.title)
# list_links = scrap_all_languages_links(get_wiki_html_page(page.title, 'en'))
# print_array(list_links)
# print("Found "+retrieve_target_language_link(list_links, 'fr'))
# print(title_wiki_page(wikilink))
# my_dico = {'Chat': 'Animal à 4 patttes.', 
#         'Chien': 'Animal à 4 pattes mais intelligent.'} 

# print_dict(my_dico)
# request.get_wiktionary_data('Run')
x = json.dumps(scan.extract_defs_and_translations('word_data.txt', 'German'))
print(x)
# language = pycountry.languages.get(name='Englishh')

