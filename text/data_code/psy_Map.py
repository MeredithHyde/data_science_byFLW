import csv
import json

import pandas as pd
import xlrd
import openpyxl
import re

from crawlerByID import getCurrentTime


def get_psy(psy_id):
    if psy_id in ['PA','PE']:#赞扬 安心
        return '喜悦'
    if psy_id in ['PD','PH','PG','PB','PK']:#尊敬 赞扬 相信 喜爱 祝愿
        return '积极'
    if psy_id in ['NA']:#愤怒
        return '愤怒'
    if psy_id in ['NB','NJ','NH','PF']:#悲伤 失望 愧疚 思
        return '伤感'
    if psy_id in ['NI','NC','NG']:#慌 恐惧 羞
        return '焦虑'
    if psy_id in ['NE','ND','NN','NK','NL']:#烦闷 憎恶 贬责 妒忌 怀疑
        return '厌恶'
    if psy_id in ['PC']:#惊奇
        return '惊奇'
    return '异常'



if __name__ == '__main__':
    psy_dic={}
    with open('psy\\fell.txt','r',encoding='utf-8') as f:
        for line in f:

            pattern=re.compile(r'\t')

            words=re.split(pattern,line)
            print(words)
            word=words[0]
            psy_id=words[4]
            psy=get_psy(psy_id)
            print(psy)
            psy_dic[word]=psy
        f.close()

    a=0
    js = json.dumps(psy_dic, indent=4, separators=(',', ':'), ensure_ascii=False)
    print(js)

    t = getCurrentTime()
    with open("other_data\\psy_dic.json", 'w+', encoding='utf-8') as f:
        f.write(js)

































        # if row['情感分类'] in ['PA', 'PE']:
        #     Happy.append(row['词语'])
        # if row['情感分类'] in ['PD', 'PH', 'PG', 'PB', 'PK']:
        #     Good.append(row['词语'])
        # if row['情感分类'] in ['PC']:
        #     Surprise.append(row['词语'])
        # if row['情感分类'] in ['NB', 'NJ', 'NH', 'PF']:
        #     Sad.append(row['词语'])
        # if row['情感分类'] in ['NI', 'NC', 'NG']:
        #     Fear.append(row['词语'])
        # if row['情感分类'] in ['NE', 'ND', 'NN', 'NK', 'NL']:
        #     Disgust.append(row['词语'])
        # if row['情感分类'] in ['NAU']:
        #     Anger.append(row['词语'])

