
from __future__ import unicode_literals, print_function
import plac
import random
from pathlib import Path
import spacy
from tqdm import tqdm
from spacy.training.example import Example
import re 
#import resume when it compiles successfully 

from tkinter import * 
from tkinter import messagebox

def clear(): 
    my_text.delete(1.0,END)


def get_text(): 
    t=my_text.get(1.0,END)
    
    nlp = spacy.load('C:\Codes\projectExp\expModel') 
    disp ='' 
    dictionary_pass = dict() 
    for line in t.splitlines():
        for sen in line.split('.'):  
            doc = nlp(sen.lower())
            for ent in doc.ents: 
                disp += "Keyword : {0} {1}\n".format(ent.text,ent.label_)
                dictionary_pass[ent.label_] = ent.text  
    
    #call resume.rafaysFunction(dictionary_pass)
    messagebox.showinfo("Import keywords found",disp)

root = Tk()
root.title('Job Description Analyser')
root.geometry('500x450')





my_text =Text(root,width =60,height=20)

my_text.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()


clear_button=Button(button_frame,text="Clear", command = clear)
clear_button.grid(row=0,column=0)
get_text_button=Button(button_frame,text ="Get Screening Results", command=get_text)
get_text_button.grid(row=0,column =1,padx=20)
my_label=Label(root,text='')
my_label.pack(pady=20) 


root.mainloop() 

