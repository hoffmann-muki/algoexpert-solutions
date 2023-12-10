from collections import Counter

def generateDocument(characters, document):
    document_counter = Counter(document)
    characters_counter = Counter(characters)
    for key in document_counter.keys():
        num_characters = characters_counter.get(key)
        if num_characters is None or num_characters < document_counter.get(key):
            return False 
    return True
