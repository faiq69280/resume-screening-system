from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
from tqdm import tqdm
from spacy.training.example import Example
import re 




model = None
output_dir=Path("C:\Codes\projectExp\expModel")
n_iter=100

ner = None 
nlp = None 

nlp = spacy.load('C:\Codes\projectExp\expModel')  
print("Loaded model '%s'" % nlp)


text = 'also like named entity recognition\nI love shiny and i love ggplot.topic modelling will also do. and i also love kubernetes. recurrent neural networks also'
print('Sample text for tesing : ', text)
print('results : ')
for line in text.splitlines():
    for sen in line.split('.'):  
        doc = nlp(sen.lower())
        print('Entities', [(ent.text, ent.label_) for ent in doc.ents])
        


