import json
import re

import jieba
from wordcloud import wordcloud

if __name__ == '__main__':

    with open('json_data\\4.json','r',encoding="utf-8") as f:
        data=json.loads(f.read())

    with open('other_data\\a','r',encoding="utf-8") as sf:
        stopWords=sf.read().split("\n")


    sentence=[]

    for i in range(0,len(data)):            #put all comments together
        for comment in data[i]['comments']:
            parts=re.split('[^\w\u4e00-\u9fff]+',comment)#过滤非中文和非英文
            for ele in parts:
                if len(ele) >0:
                    sentence.append(ele)

    presentive=[]
    for i in sentence:
        if i not in stopWords:
            presentive.append(i)

    wc=wordcloud.WordCloud(font_path='msyh', width=1920, height=1080,background_color='white')
    wc.generate(" ".join(presentive))
    wc.to_file('pic\\a_period(sentence).png')