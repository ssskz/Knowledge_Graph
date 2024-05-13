import jieba
import re
import json
# 定义停用词列表
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords
# 对句子进行分词
def seg_sentence(sentence):
    sentence = re.sub('[^\u4e00-\u9fa5]+', '', sentence)#正则表达式去掉特殊字符

    sentence_seged = jieba.lcut(sentence.strip())#使用三种模式之一的精确模式
    stopwords = stopwordslist('./stopwords.txt')  # 这里加载停用词的路径
    outstr = ''#输出变量
    for word in sentence_seged:#不在停用表中的词就拼接到outstr
        if word not in stopwords and word.__len__() > 1:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

#  inputs即是读入原文本，outputs即是新建一个文本，统一用utf-8
with open('../../datasets/gongwen/gongwen_output.json', 'r', encoding='utf-8') as inputs:
    data_content = json.load(inputs)
output_json_file = '../../datasets/gongwen/gongwen_output_fenci.json'

file_data = []
for line in data_content:
    content = line.get('content', '')
    line_seg = seg_sentence(content)  # 这里的返回值是分词后字符串
    file_dict = {}
    file_dict['id'] = line.get('id', '')
    file_dict['name'] = line.get('name', '')
    file_dict['content'] = line.get('content', '')
    file_dict['fenci'] = line_seg
    file_data.append(file_dict)
# 将数据保存到JSON文件
with open(output_json_file, 'w', encoding='utf-8') as json_file:
    json.dump(file_data, json_file, ensure_ascii=False, indent=4)
