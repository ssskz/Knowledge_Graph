from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim import corpora#语料库
from gensim.models import LdaModel#lda模型
import fenci
import json

print("请输入公文文本内容:")
content_x = input()
fenci_x = fenci.seg_sentence(content_x)
#存放要分类的词
train = []
train.append([w for w in fenci_x.split()])
dictionary = corpora.Dictionary(train)#词典
corpus = [dictionary.doc2bow(text) for text in train]#文档词频率矩阵（稀疏矩阵），词袋
lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=1, passes=100)#计算好的话题模型
for topic in lda.print_topics(num_words = 15):
    termNumber = topic[0]
    #print(topic[0], ':', sep='')
    listOfTerms = topic[1].split('+')
    lst_topic = [] 
    for term in listOfTerms:
        listItems = term.split('*')
        lst_topic.append(listItems[1])
        #print('  ', listItems[1], '(', listItems[0], ')', sep='')
    output_topic = ''
    for word in lst_topic:
        if word != '\t':
            output_topic += word
output_topic_x = output_topic.replace('"',"")
#print(output_topic_x)
#访问JSON数据库
datasets = '../../datasets/gongwen/gongwen_output_lda.json'
with open(datasets,'r',encoding='utf-8') as data:
    data_topics = json.load(data)
cosine_sim_all = []
for data_topic in data_topics:
    dict = {}
    output_topic_y = data_topic.get('topic','') 
    #将两个句子转换为特征向量
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform([output_topic_x, output_topic_y])
    #计算余弦相似度
    cosine_sim = cosine_similarity(X[0], X[1])
    id = data_topic.get('id','') 
    dict[id] = cosine_sim[0][0]
    cosine_sim_all.append(dict)

print(cosine_sim_all)