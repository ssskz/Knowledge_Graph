from gensim import corpora#语料库
from gensim.models import LdaModel#lda模型
import json

#gensim是python的一个可以创建和查询语料库的自然语言处理库

fp = open('../../datasets/gongwen/gongwen_output_fenci.json','r',encoding='utf-8')
output_json_file = '../../datasets/gongwen/gongwen_output_lda.json'
data_content = json.load(fp)

file_data = []
for line in data_content:#加载词
    file_dict = {}
    file_dict['id'] = line.get('id', '')
    file_dict['name'] = line.get('name', '')
    file_dict['content'] = line.get('content', '')
    file_dict['fenci'] = line.get('fenci', '')
    train = []#存放要分类的词
    if line.get('fenci', '') != '':
        line = line.get('fenci', '').split()
        train.append([w for w in line])

    dictionary = corpora.Dictionary(train)#词典

    corpus = [dictionary.doc2bow(text) for text in train]#文档词频率矩阵（稀疏矩阵），词袋

    lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=1, passes=100)#计算好的话题模型
    # num_topics：主题数目
    # passes：训练伦次
    # num_words：每个主题下输出的term的数目
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
    file_dict['topic'] = output_topic
    file_dict['topic'] = file_dict['topic'].replace('"', "")
    file_data.append(file_dict)
    
# 将数据保存到JSON文件
with open(output_json_file, 'w', encoding='utf-8') as json_file:
    json.dump(file_data, json_file, ensure_ascii=False, indent=4)


