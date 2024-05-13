import matplotlib.pyplot as plt
# 指定中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
#统计公文的长度分布
import json
import re
import jieba
from collections import Counter
import matplotlib.pyplot as plt

def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        texts = [item['content'] for item in data]
        names = [item['name'][:-6] for item in data]
    return texts,names
def clean_and_tokenize(texts):
    cleaned_texts = []
    for text in texts:
        # 去除标点符号和特殊符号
        text = re.sub(r'[^\w\s]', '', text)
        # 使用jieba进行中文分词
        tokens = jieba.lcut(text)
        cleaned_texts.append(tokens)
    return cleaned_texts
def remove_stopwords_and_count_length(cleaned_texts):
    stopwords = set()  # 你需要准备一个停用词表
    lengths = []
    for tokens in cleaned_texts:
        # 去除停用词
        tokens = [word for word in tokens if word not in stopwords]
        # 统计文本长度
        length = len(tokens)
        lengths.append(length)
    #print(lengths)
    return lengths
def plot_line_chart(lengths,names):
    # 提取长度和数量
    print(lengths)
    print(names)
    word_counts = {}
    for word, count in zip(names, lengths):
        if word in word_counts:
            word_counts[word].append(count)
        else:
            word_counts[word] = [count]
    print(word_counts)
    labels = list(word_counts.keys())
    values = list(word_counts.values())
    # 绘制折线图
    for label, value in zip(labels, values):
        plt.plot(range(1, len(value) + 1), value, label=label)
    # 添加标题和标签
    plt.title('公文分类文本长度统计折线图')
    plt.xlabel('公文分类数量')
    plt.ylabel('文本长度')
    # 添加图例
    plt.legend()
    # 显示图形
    plt.show()

if __name__ == '__main__':
    # 示例JSON文件名
    filename = '../../datasets/gongwen/gongwen_output.json'
    # 读取JSON文件并提取文本数据
    texts,names = read_json(filename)
    # 数据清洗和分词
    cleaned_texts = clean_and_tokenize(texts)
    # 去除停用词并统计文本长度
    lengths = remove_stopwords_and_count_length(cleaned_texts)
    # 绘制折线图
    plot_line_chart(lengths,names)