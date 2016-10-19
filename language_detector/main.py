# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    
    globalcount = 0
    lang = ""
    
    for dictionary in languages:
        
        count = 0
        for word in text.split():
            
            if word in dictionary['common_words']:
                count += 1
                
            
        #print(dictionary['name'], count)
        if count > globalcount:
            globalcount = count
            lang = dictionary['name']
    
    
    return lang

text = """
            # spanish
            Lionel Andrés Messi Cuccittini (Rosario, 24 de junio de 1987),
            conocido como Leo Messi, es un futbolista argentino11 que juega
            como delantero en el Fútbol Club Barcelona y en la selección
            argentina, de la que es capitán.

            # german
            Messi spielt seit seinem 14. Lebensjahr für den FC Barcelona.
            Mit 24 Jahren wurde er Rekordtorschütze des FC Barcelona, mit 25
            der jüngste Spieler in der La-Liga-Geschichte, der 200 Tore
            erzielte.
        """
