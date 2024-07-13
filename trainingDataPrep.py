






def concatenateTuples(t1,t2): 
    text1 = t1[0]
    text2 = t2[0]

    r_text = text1 + text2
    r_entities = t1[1]['entities'].copy() 

    for i,j,ent in t2[1]['entities']: 
        r_entities.append((i+len(text1),j + len(text1),ent))
    return (r_text,{'entities':r_entities})





def prepareData(trainingData): 
    newData = trainingData.copy() 

    for tuple_index in range(len(trainingData)): 
        for _combine in range(len(trainingData)):
            if _combine == tuple_index: 
                continue
            result_text = trainingData[tuple_index][0] + trainingData[_combine][0]
            f = lambda xyz : (xyz[0] + len(trainingData[tuple_index][0]),xyz[1]+len(trainingData[tuple_index][0]),xyz[2]) 
            entities = trainingData[tuple_index][1]['entities'].copy() + list(map(f,trainingData[_combine][1]['entities']))
            newData.append((result_text,{'entities':entities}))
    return newData


def assignIndexing(superString,subString,label): 
    indexes = list() 
    for _index in range(len(superString)): 
        if _index + len(subString) <= len(superString) and superString[_index:_index + len(subString)] == subString:
            indexes.append((_index,_index + len(subString),label))
    return indexes 






R = [('boy loves r language .',{'entities' : [(10,20,'R Language')]})
,('he luvs ggplot .',{'entities' : [(8,14,'R Language')]}), 
('shiny is also his favorite .',{'entities': [(0,5,'R Language')]}), 
('the candidate also likes cran .',{'entities' : [(25,29,'R Language')]}),
('his dplyr expertise should atleast be on a sufficient level .',{'entities':[(4,9,'R Language')]}),
('another requirement is tidyr .',{'entities':[(23,28,'R Language')]}), 
('lubridate is another requirement .',{'entities':[(0,9,'R Language')]}),
('candidate is also expected to know knitr .',{'entities':[(35,40,'R Language')]}) 
]
NLP = [('boy loves natural language processing ', {'entities':[(10,37, 'NLP')]}), 
('he also likes nlp ',{'entities': [(14,17,'NLP')]}), 
('topic modeling is also a preffered skill ',{'entities': [(0,14,'NLP')]}),
('the candidate also likes lda ',{'entities': [(25,28,'NLP')]}), 
('candidate is also expected to know named entity recognition . ',{'entities':[(35,59,'NLP')]}), 
('another requirement is pos tagging . ',{'entities':[(23,34,'NLP')]}), 
('his word2vec expertise should atleast be on a sufficient level . ',{'entities': [(4,12,'NLP')]}), 
('word embedding also required . ',{'entities': [(0,14,'NLP')]}),
('he luvs lsi . ',{'entities' : [(8,11,'NLP')]}),
('expertise in spacy is also a must ', {'entities': [(13,18,'NLP')]}),
('know gensim and then know yourself ',{'entities':[(5,11,'NLP')]}), 
('git gud at nltk ',{'entities': [(11,15,'NLP')]}),
('learn nmf ',{'entities': [(6,9,'NLP')]}), 
('prioritise doc2vec and other tech ',{'entities':[(11,18,'NLP')]}),
('get expertise in cbow ',{'entities': [(17,21,'NLP')]}),
('should be familiar with bag of words ',{'entities':[(24,36,'NLP')]}), 
('another quality is skip gram . ',{'entities':[(19,28,'NLP')]}),
('familarity with bert is mandatory . ', {'entities':[(16,20,'NLP')]}),
('skill with sentiment analysis is also required . ',{'entities':[(11,29,'NLP')]}), 
('must have worked with chat bot applications . ', {'entities':[(22,30,'NLP')]})
]

Stats = [('skill in statistical models is required. ',{'entities': assignIndexing('skill in statistical models is required. ','statistical models','Statistics')}),
('one should be good at statistical modeling . ', {'entities': assignIndexing('one should be good at statistical modeling . ','statistical modeling','Statistics')}), 
('skill in probability is also desired ', {'entities': assignIndexing('skill in probability is also desired ','probability','Statistics')}), 
('normal distribution is also required ', {'entities': assignIndexing('normal distribution is also required ','normal distribution','Statistics')}), 
('our candidates should be able to work with poisson distribution ', {'entities': assignIndexing('our candidates should be able to work with poisson distribution ','poisson distribution','Statistics')}), 
('expertise with survival models is also assumed ', {'entities': assignIndexing('expertise with survival models is also assumed ','survival models','Statistics')}),
('we also assume that you are somewhat familiar with hypothesis testing ', {'entities': assignIndexing('we also assume that you are somewhat familiar with hypothesis testing', 'hypothesis testing','Statistics')}), 
('bayesian inference is a good to have skill ', {'entities': assignIndexing('bayesian inference is a good to have skill ','bayesian inference', 'Statistics')}), 
('factor analysis is a well soughtout capability ',{'entities':assignIndexing('factor analysis is a well soughtout capability ','factor analysis','Statistics')}), 
('should be capable of creating forecasting ', {'entities': assignIndexing('should be capable of creating forecasting ','forecasting','Statistics')}), 
('familiarity with markov chain models is also assumed ', {'entities': assignIndexing('familiarity with markov chain models is also assumed ','markov chain','Statistics')}),
('should have carried out monte carlo simulaions ', {'entities': assignIndexing('should have carried out monte carlo simulaions ','monte carlo','Statistics')})
]


ML = [('skill in machine learning is required ',{'entities': assignIndexing('skill in machine learning is required ','machine learning','Machine Learning')}), 
('must know linear regression ', {'entities': assignIndexing('must know linear regression', 'linear regression', 'Machine Learning')}), 
('must understand logistic regression ', {'entities': assignIndexing('must understand logistic regression ', 'logistic regression', 'Machine Learning')}), 
('familiarity with K means is also assumed ', {'entities': assignIndexing('familiarity with K means is also assumed ','K means', 'Machine Learning')}), 
('random forest we love. ',{'entities': assignIndexing('random forest we love. ','random forest','Machine Learning')}), 
('one should have worked with xgboost ', {'entities': assignIndexing('one should have worked with xgboost ','xgboost','Machine Learning')}),
('must have worked with svm ', {'entities': assignIndexing('must have worked with svm ','svm','Machine Learning')}), 
('familiarity with naive bayes is assumed ',{'entities': assignIndexing('familiarity with naive bayes is assumed ','naive bayes','Machine Learning')}), 
('should able to deal with dimensions using pca ', {'entities': assignIndexing('should able to deal with dimensions using pca ','pca','Machine Learning')}), 
('should work with decision trees ', {'entities': assignIndexing('should work with decision trees ','decision trees','Machine Learning')}),
('svd technique should be there ', {'entities': assignIndexing('svd technique should be there ','svd','Machine Learning')}), 
('must know how to work with ensemble models ', {'entities': assignIndexing('must know how to work with ensemble models ','ensemble models','Machine Learning')}), 
('must have built a boltzman machine ',{'entities': assignIndexing('must have built a boltzman machine ','boltzman machine','Machine Learning')})
]

DL = [('skill in neural network is required ', {'entities':assignIndexing('skill in neural network is required ','neural network','Deep Learning')}),
('must know keras ', {'entities': assignIndexing('must know keras ','keras','Deep Learning')}), 
('familiarity with theano is assumed ',{'entities': assignIndexing('familiarity with theano is assumed ','theano','Deep Learning')}),
('must have developed face detection model ',{'entities':assignIndexing('must have developed face detection model ','face detection','Deep Learning')}), 
('neural networks expertise required ',{'entities': assignIndexing('neural networks expertise required ','neural networks','Deep Learning')}), 
('convolutional neural network expertise assumed ', {'entities': assignIndexing('convolutional neural network expertise assumed ','convolutional neural network','Deep Learning')}), 
('cnn expertise also required ', {'entities': assignIndexing('cnn expertise also required ', 'cnn', 'Deep Learning')}), 
('recurrent neural networks expertise required ', {'entities': assignIndexing('recurrent neural networks expertise required ','recurrent neural networks','Deep Learning')}), 
('rnn expertise required ', {'entities': assignIndexing('rnn expertise required ','rnn','Deep Learning')}), 
('should have worked with object detection libraries ', {'entities': assignIndexing('should have worked with object detection libraries ','object detection','Deep Learning')}), 
('yolo good stuff ', {'entities': assignIndexing('yolo good stuff ','yolo','Deep Learning')}),
('should understand gpu processing ',{'entities': assignIndexing('should understand gpu processing ','gpu','Deep Learning')}), 
('should have worked with cuda ',{'entities': assignIndexing('should have worked with cuda ','cuda','Deep Learning')}), 
('must have developed tensorflow models ', {'entities': assignIndexing('must have developed tensorflow models ','tensorflow','Deep Learning')}), 
('must have developed lstm related works ', {'entities': assignIndexing('must have developed lstm related works ','lstm','Deep Learning')}), 
('proficiency with gan is also required ', {'entities': assignIndexing('proficiency with gan is also required ','gan', 'Deep Learning')}), 
('should also work with opency ',{'entities': assignIndexing('should also work with opency ','opency','Deep Learning')})
]

PY = [('python skill is in demand ',{'entities': assignIndexing('python skill is in demand ','python','Python Language')}), 
('should have experience with frameworks like flask ', {'entities': assignIndexing('should have experience with frameworks like flask ','flask','Python Language')}), 
('must know django ', {'entities': assignIndexing('must know django ','django','Python Language')}), 
('must know how to work with pandas library ', {'entities': assignIndexing('must know how to work with pandas library ','pandas','Python Language')}),
('numpy expertise requried ', {'entities': assignIndexing('numpy expertise requried ','numpy','Python Language')}),
('scikitlearn should understand  ', {'entities': assignIndexing('scikitlearn should understand  ','scikitlearn','Python Language')}),
('sklearn understanding required ', {'entities': assignIndexing('sklearn understanding required ','sklearn','Python Language')}), 
('matplotlib understanding also required ', {'entities': assignIndexing('matplotlib understanding also required ', 'matplotlib', 'Python Language')}), 
('scipy should be a skill ', {'entities': assignIndexing('scipy should be a skill ', 'scipy', 'Python Language')}), 
('must have familiarity with bokeh ', {'entities': assignIndexing('must have familiarity with bokeh ','bokeh', 'Python Language')}), 
('should have working knowledge of statsmodel ', {'entities': assignIndexing('should have working knowledge of statsmodel ','statsmodel','Python Language')})
]
DE = [('laws should be understandable ',{'entities': assignIndexing('laws should be understandable ','laws', 'Data Engineering')}), 
('must also know ec2 ', {'entities': assignIndexing('must also know ec2 ', 'ec2','Data Engineering')}), 
('must also understand amazon redshift ', {'entities': assignIndexing('must also understand amazon redshift ','amazon redshift','Data Engineering')}), 
('must understand and work with s3 ', {'entities': assignIndexing('must understand and work with s3 ','s3','Data Engineering')}), 
('must also work with docker ',{'entities': assignIndexing('must also work with docker ','docker','Data Engineering')}), 
('should have experience dealing with kubernetes ', {'entities': assignIndexing('should have experience dealing with kubernetes ','kubernetes','Data Engineering')}), 
('should have working knowledge of scala ', {'entities': assignIndexing('should have working knowledge of scala ','scala','Data Engineering')}), 
('should have familiarity with teradata ', {'entities': assignIndexing('should have familiarity with teradata ','teradata','Data Engineering')}),
('should also know about google big query ', {'entities': assignIndexing('should also know about google big query ','google big query','Data Engineering')}),
('should also know laws lambda ', {'entities': assignIndexing('should also know laws lambda ','laws lambda', 'Data Engineering')}), 
('should also work with laws emr ', {'entities': assignIndexing('should also work with laws emr ', 'laws emr','Data Engineering')}), 
('understanding of hive also required ', {'entities':assignIndexing('understanding of hive also required ','hive','Data Engineering')}), 
('must have some familiarity with hadoop ', {'entities': assignIndexing('must have some familiarity with hadoop ','hadoop','Data Engineering')}),
('understanding of sql is integral ', {'entities': assignIndexing('understanding of sql is integral ','sql','Data Engineering')})
]



trainingSets = [R,NLP,Stats,ML,DL,PY,DE]



#for test in DE:
    #print(test)
    #print('===============') 
#    l = test[1]['entities'][0][0]
#    h = test[1]['entities'][0][1]
#    print(test[0],test[0][l:h])

#data = prepareData(trainingData)
#for check in data:
#    print(check[0]) 
#    print('For this text, following are the entities and their indexes: ')
#    for ent in check[1]['entities']: 
#        print('(',ent[0],ent[1],')',check[0][ent[0]:ent[1]])
#    print('==============================================================')    

def getData():
 
    global trainingSets

    
    trainingData = list() 

    preparedSets = list()
    for i in trainingSets:
        k = prepareData(i) 
        preparedSets.append(k)  
        trainingData += k 
    
    #for p_index in range(len(preparedSets)):
    #    for el in preparedSets[p_index]: 
    #       for p_index2 in range(p_index+1,len(preparedSets)):
    #           for el2 in preparedSets[p_index2]: 
    #              trainingData.append(concatenateTuples(el,el2)) 


    return trainingData 






  
    #return prepareData(trainingData)

#for i in getData(): 
#    print(i)
#    print('=============================================================================')