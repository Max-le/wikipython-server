import collections, wikipedia, requests, re, pycountry
from bs4 import BeautifulSoup
def print_array(array):
        if (isinstance(array, collections.Sequence) and (array != []) ):
                for item in array:
                        print(item)
        elif array == [] :
                print("This array is empty.")
        else:
                raise Exception("The input is not a collection.")
        return
def print_dict(dictionary):
        if (isinstance(dictionary, dict )):
                for key in dictionary:
                        print(key + " => "+dictionary[key])
        else:
                raise Exception("Input is not a dictionary.")
#Returns symbol ( alpha_2 ) if name given and vice-versa
def convert_lang_code(lang):
        if pycountry.languages.get(name=lang):
                return pycountry.languages.get(name=lang).alpha_2
        elif pycountry.languages.get(alpha_2=lang):
                return pycountry.languages.get(alpha_2=lang).name
def get_iso_alpha2(lang):
        try:
            language = pycountry.languages.lookup(lang) 
            return language.alpha_2
        except LookupError: 
                print("LookupError")
def get_iso_name(lang):
        try:
            language = pycountry.languages.lookup(lang) 
            return language.name
        except LookupError: 
                print("LookupError")
def language_exists(lang):
        try:
                pycountry.languages.lookup(lang)
                return True
        except LookupError:
                return False
        


def ask_user_keyword():
    word = input('Enter the file that you want to find : ')
    if (word != ""):
        print('Your search word : '+word)
        return word
    else:
        raise Exception('Search keyword is empty.')
def get_related_wiki_pages(subject):
        return wikipedia.search(subject)
def get_wiki_html_page(page_title, lang):
        wiki_link = 'https://'+lang+'.wikipedia.org/wiki/'+page_title
        r = requests.get(wiki_link)
        return r.text
def scrap_all_languages_links(htmlpage):
        soup = BeautifulSoup(htmlpage, 'html.parser') 
        links = []
        for link in soup.find_all('a', 'interlanguage-link-target' ):
                links.append(link.get('href'))
        return links
def retrieve_target_language_link(list_links, target_language):
        for link in list_links:                
                match = re.search(target_language+'.wikipedia.org', link)
                if match: return link
        return
def title_wiki_page(wiki_url):
        return wiki_url.split("/")[-1]

def get_translated_page(wikipage, lang ):
        if (isinstance(wikipage, wikipedia.WikipediaPage) != True):
                raise Exception('Error, the parameter must be a WikipediaPage object.')
        

