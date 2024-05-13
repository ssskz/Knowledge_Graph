import os
import json
import time
import uuid
from docx import Document

# 定义文件夹路径
folder_path = '../../meta_data/gongwen/'
output_json_file = '../../datasets/gongwen/gongwen_output.json'

file_data = []

# 遍历文件夹下的docx文件
for filename in os.listdir(folder_path):
    if filename.endswith('.docx'):
        file_dict = {}
        file_dict['id'] = str(int(time.time())) + '_' + str(uuid.uuid4())
        file_dict['name'] = filename
        
        # 读取docx文件内容
        doc_path = os.path.join(folder_path, filename)
        doc = Document(doc_path)
        content = ''
        for paragraph in doc.paragraphs:
            content += paragraph.text + '\n'
        file_dict['content'] = content
        
        file_data.append(file_dict)

# 将数据保存到JSON文件
with open(output_json_file, 'w', encoding='utf-8') as json_file:
    json.dump(file_data, json_file, ensure_ascii=False, indent=4)