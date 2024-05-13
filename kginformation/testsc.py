import ahocorasick

#构建领域
def build_actree(wordlist):
    actree = ahocorasick.Automaton()
    for index,word in enumerate(wordlist):
        actree.add_word(word,(index,word))
    actree.make_automaton()

    return actree


if __name__ == '__main__':
#特征(关键词--实体词)
    region_words = ['中国','GPT-4','ChatGLM','文心一言','智普AI','百度','OpenAI']
    region_tree = build_actree(wordlist=region_words)

    query = "百度的文心一言和OpenAI的GPT-4哪家更加强大"

    region_wds = []
    for end_index, (insert_order, original_value) in region_tree.iter(query):
        start_index = end_index - len(original_value) + 1
        region_wds.append( {"start":start_index,"offset":end_index,"term":original_value} )

    print("query = ",query)
    print('query parser ')
    for data in region_wds:
        print(data)