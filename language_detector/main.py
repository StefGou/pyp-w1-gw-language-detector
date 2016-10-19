# -*- coding: utf-8 -*-

def detect_language(text, languages):
    
    globalcount = 0
    lang = ""
    
    for dictionary in languages:
        
        count = 0
        for word in text.split():
            
            if word in dictionary['common_words']:
                count += 1
                    
        if count > globalcount:
            globalcount = count
            lang = dictionary['name']
    
    
    return lang
