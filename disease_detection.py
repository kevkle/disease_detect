
from config import *



def matching_codes(string):

    var = "not found"

    string_list = string.split()

    if len(string_list) == 3:  # Fall des split up words
        if 'des' in string_list:
            if string_list[2][-2:] == 'es':  # 2. Fall kann zweifach auftreten mit es oder s als Endungszusatz
                string_list[2] = string_list[2][:-2] # Hier nehmen wir die ursprüngliche Form des Nominativs an, Zungengrundes => Zungengrund
            elif string_list[2][-1:] == 's':
                string_list[2] = string_list[2][:-1]

        string_list.pop(1)
        assert len(string_list) == 2

        for word in disease_dict.keys():
            if string_list[0].lower() in word.lower() and string_list[1].lower() in word.lower(): # Suchen der beiden Wörter des nicht zusammengesetzen Wortes im compound word
                var = disease_dict[word]

    elif len(string_list) == 1: # Fall zusammengesetztes Nomen

        for word in disease_dict.keys():
            if string_list[0].lower() == word.lower():
                var = disease_dict[word]


    return var








