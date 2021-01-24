import csv
import json

import pandas as pd
import xlrd
import openpyxl
import re
if __name__ == '__main__':

    key = '4'
    hit_dic={}
    hit_dic['喜悦'],hit_dic['积极'],hit_dic['愤怒'],hit_dic['伤感'],hit_dic['焦虑'],hit_dic['厌恶'],hit_dic['惊奇']=0,0,0,0,0,0,0


    with open('other_data\\IDF'+key+'.json','r',encoding='utf-8') as f:
        data=json.loads(f.read())
        f.close()

    ##读取心态字典
    with open('other_data\\psy_dic.json','r',encoding='utf-8') as f:
        psy_dic=json.loads(f.read())
        psy_words=list(psy_dic.keys())
        f.close()

    for sentence in data:
        words=list(dict(sentence).keys())   #将所有有序键转为列表,即所有的词语按重要到不重要排序
        # print(words)
        for word in words:
            if word in psy_dic:
                hit_dic[psy_dic[word]]+=1
                break
    print(hit_dic)
    js = json.dumps(hit_dic, indent=4, separators=(',', ':'), ensure_ascii=False)
    print(js)

    with open("psy\\" + key + ".json", 'w+', encoding='utf-8') as f:
        f.write(js)
    print("储存成功！")
