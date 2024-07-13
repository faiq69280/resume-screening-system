from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
from tqdm import tqdm
from spacy.training.example import Example
from spacy.tokens import Doc

import trainingDataPrep
#NLP data set Preparation 

#TRAIN_DATA = [
#    ('Who is Nishanth', {
#        'entities': [(7, 15, 'PERSON')]
#    }),
#     ('Who is Kamal Khumar?', {
#        'entities': [(7, 19, 'PERSON')]
#    }),
#    ('I like London and Berlin.', {
#        'entities': [(7, 13, 'LOC'), (18, 24, 'LOC')]
#    })
#]



#TRAIN_DATA = jobDescriptionHandle.getTrainingData() 
TRAIN_DATA = trainingDataPrep.getData() 


model = None
output_dir=Path("C:\Codes\projectExp\expModel")
n_iter=100

ner = None 
nlp = None 

if model is not None:
    nlp = spacy.load(model)  
    print("Loaded model '%s'" % model)
else:
    nlp = spacy.blank('en')  
    print("Created blank 'en' model")

#set up the pipeline

if 'ner' not in nlp.pipe_names:
    nlp.add_pipe('ner')
    ner = nlp.get_pipe('ner')
else:
    ner = nlp.get_pipe('ner')


for _, annotations in TRAIN_DATA:
    for ent in annotations.get('entities'):
        ner.add_label(ent[2])

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
with nlp.disable_pipes(*other_pipes):  # only train NER
    examples = []
    for text, annots in TRAIN_DATA:
        examples.append(Example.from_dict(nlp.make_doc(text.lower()), annots))
    nlp.initialize(lambda: examples)
    for i in range(20):
       random.shuffle(examples)
       for batch in spacy.util.minibatch(examples, size=8):
           nlp.update(batch)


for text, _ in TRAIN_DATA:
    doc = nlp(text.lower())
    print('Entities', [(ent.text, ent.label_) for ent in doc.ents])


if output_dir is not None:
    output_dir = Path(output_dir)
    if not output_dir.exists():
        output_dir.mkdir()
    nlp.to_disk(output_dir)
    print("Saved model to", output_dir)
