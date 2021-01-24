import csv
import json

import pandas as pd
import xlrd
import openpyxl
import re
if __name__ == '__main__':
    emotionwords=['喜悦','积极','愤怒','伤感','焦虑','焦虑','厌恶','惊奇']

    key = '1'
    hit_dic={}
    for w in emotionwords:
        hit_dic[w]={}
        hit_dic[w]["count"]=0

    with open('other_data\\'+key+'.json','r',encoding='utf-8') as f:
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
                hit_dic[psy_dic[word]]["count"]+=1
                if word not in hit_dic[psy_dic[word]].keys():
                    hit_dic[psy_dic[word]][word]=1
                else:
                    hit_dic[psy_dic[word]][word] += 1
                break
    print(hit_dic)

    for w in emotionwords:
        temp=sorted(hit_dic[w].items(), key=lambda x: x[1], reverse=True)
        hit_dic[w]={}
        for i in temp:
            hit_dic[w][i[0]]=i[1]


    js = json.dumps(hit_dic, indent=4, separators=(',', ':'), ensure_ascii=False)
    print(js)

    with open("psy\\keywords" + key + ".json", 'w+', encoding='utf-8') as f:
        f.write(js)
    print("储存成功！")

