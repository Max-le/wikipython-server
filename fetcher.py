import requests

def get_wiktionary_data(word):
    word = word.lower()
    url = 'https://wiktionary.org/wiki/'+word+'?action=raw'
    print('url : '+url)
    result = requests.get(url)
    open('word_data.txt', 'wb').write(result.content)

