import os
from wiki import print_dict

# Get rid of unuseful markers ( prettifies )
def prettify(string):
    return string.replace('{','').replace('}', '').replace('trans-top|', '').replace("\n", "")

     
# Returns a dictionary contaning [ definition =>  word]
def extract_defs_and_translations(filename, target_lang):
    translations = dict()
    if (os.path.isfile(filename) == False): raise Exception('Couldn\'t find '+filename)
    with open ( filename, ('rt')) as lines:
        current_definition = ''
        for line in lines:
            if line.find('trans-top') != -1:
                current_definition = prettify(line)
            if line.find('* '+target_lang) != -1:
                word = prettify(line)
                word = word.replace("* "+target_lang + ": ", "")
                word = structure_word(word)
                translations[current_definition] = word
    print(translations)
    return translations

#Example : 't+|de|Sprecher|m, t+|de|Sprecherin|f'


##TO-DO : Solve case when there's a qualifier
def structure_word(raw):
    words = raw.split(',')
    cleaned_words = []
    for word in words:
        components = word.split('|')
        if (len(components) > 2): 
            word = {
                'type':components[0],
                'lang':components[1],
                'translation':components[2],
                "gender":""
            }
        
        if len(components) == 4:
            word["gender"] = components[3]
        cleaned_words.append(word)
    return cleaned_words

