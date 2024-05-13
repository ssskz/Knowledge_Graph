from collections import defaultdict
import contection_kg

# 定义Jaccard Similarity函数
def jaccard_similarity(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / (union - intersection) if (union - intersection) else 0

if __name__ == '__main__':
    # 输入的三元组三元组的集合表示
    input_triplet = ("法律", "包含", "司法")
    input_set = set(input_triplet)
    # 用字典存储三元组与相似度的对应关系
    similarity_scores = defaultdict(float)
    
    graph_db = contection_kg.gongwen_kg_information()
    print(graph_db)
    # 计算输入三元组与图数据库中所有三元组的相似度
    for triplet in graph_db:
        triplet_set = set(triplet)
        similarity_scores[triplet] = jaccard_similarity(input_set, triplet_set)

    # 获取相似度最高的前5个三元组
    top5_similar_triplets = sorted(similarity_scores, key=similarity_scores.get, reverse=True)[:12]

    # 打印相似度最高的前5个三元组
    for i, triplet in enumerate(top5_similar_triplets, 1):
        print(f"Top {i}: {triplet} - Similarity Score: {similarity_scores[triplet]}")
