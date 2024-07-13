#process data 


import pandas as pd 
import re 

def findIndexes(super_string,sub_string):
    indexes = list()  
    for index in range(len(super_string)):
        if index + len(sub_string) <= len(super_string):
           if sub_string == super_string[index:index+len(sub_string)]: 
              indexes.append((index,index + len(sub_string)))
    return indexes   


def removeSpaces(string): 
    filtered = ''
    for c in string: 
        if c != '\n':
            filtered += str(c)
    return filtered 



def loadDescriptions(): 
    f = open('JDs.txt','r')
    text = f.read() 
    return text.split('@')

def getProcessedJDs():
    JDs = loadDescriptions()
    return [removeSpaces(jd.lower()) for jd in JDs]


def findSinLetterWord(query,text):
    match_objs = list() 
    symbs = [';','.',',',' ']
    for s1 in symbs: 
        for s2 in symbs: 
            match_objs.append(re.finditer('{0}({1}){2}'.format(s1,query,s2),text)) 

    indices = set() 
    for m in match_objs: 
        for match in m: 
           indices.add((match.start(),match.end())) 
  

    return list(indices)




def getTrainingData(): 
   JDs =['The candidate should be well versed in NLP.Topic Modeling is also a desired quality.The candidate is also expected to know lda and should have some experience in dealing with named entity recognition models.Pos Tagging is also a desirable skill. Data Preprocessing techniques such as word2vec are also plus points.'] 

   df = pd.read_csv('keywords.csv')
   df = df.astype(str)
   entities = df.columns

   TRAIN_DATA = list() 
   for jd in JDs: 
       #for each jd, get the entities
       ent_indexes = list()  
       for en in entities:
           searchList = list(df[en])
           if en.lower() not in map(lambda x: x.lower(),searchList): 
              searchList.append(en)
           for query in searchList:
               indexes = list() 
               #if len(query) > 1: 
               #   indexes = findIndexes(jd,query.lower())
               #else:
               #   indexes = findSinLetterWord(query.lower(),jd)
               
               if query == 'nan': 
                   continue 
               print(query)
               print(jd.lower())    
               indexes = findSinLetterWord(query.lower(),jd.lower())

               for i,j in indexes: 
                   ent_indexes.append((i,j,en))            
       TRAIN_DATA.append((jd,{'entities':ent_indexes}))
   return TRAIN_DATA

#TRAIN = getTrainingData() 

#for t in TRAIN: 
#     for en in t[1]['entities']: 
#         print(en[2],t[0][en[0]:en[1]])
#     print('==================')

search_base = dict() 
search_base['NLP'] = ['nlp','word2vec','topic modeling','natural language processing']
for keyw in search_base['NLP']:
    print(findSinLetterWord(keyw,'The candidate should be well versed in NLP.Topic Modeling is also a desired quality.The candidate is also expected to know lda and should have some experience in dealing with named entity recognition models.Pos Tagging is also a desirable skill. Data Preprocessing techniques such as word2vec are also plus points'.lower()))
