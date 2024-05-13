from neo4j import GraphDatabase

# 定义Neo4j数据库连接函数
def connect_to_neo4j(url, user, password):
    driver = GraphDatabase.driver(url, auth=(user, password))
    return driver

#查询数据库中所有的三元组
def gongwen_kg_information():
    result_gomngwen = []
    # Neo4j数据库连接信息
    url = "neo4j://localhost:7687"
    user = "neo4j"
    password = "123456"
    driver = connect_to_neo4j(url, user, password)
    with driver.session() as session:
        result = session.run("MATCH (p:Person)-[r:actor]-(m:Movie) return p,m")
        for record in result:
            node_properties_p = record["p"]._properties
            node_properties_m = record["m"]._properties
            triplet = (node_properties_p.get("name"),"actor",node_properties_m.get("title"))
            result_gomngwen.append(triplet)
    return result_gomngwen
    