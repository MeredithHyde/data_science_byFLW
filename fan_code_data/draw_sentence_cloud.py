import json
import re

import jieba
from wordcloud import wordcloud

if __name__ == '__main__':
    key='1'

    with open('json_data\\'+key+'.json','r',encoding="utf-8") as f:
        data=json.loads(f.read())

    with open('other_data\\stop','r',encoding="utf-8") as sf:
        stopWords=sf.read().split("\n")

    with open('other_data\\psy_dic.json','r',encoding='utf-8') as df:
        emotionwords=list(json.loads(df.read()).keys())
        print(emotionwords)


    sentence=[]

    for i in range(0,len(data)):            #put all comments together
        for comment in data[i]['comments']:
            parts=re.split('[^\w\u4e00-\u9fff]+',comment)#过滤非中文和非英文
            for ele in parts:
                if len(ele) >0:
                    sentence.append(ele)

    presentive=[]
    for i in sentence:
        for word in emotionwords:
            if word in sentence:
                presentive.append(i)
                break
    print(presentive)
    wc=wordcloud.WordCloud(font_path='msyh', width=1920, height=1080,background_color='white')
    wc.generate(" ".join(presentive))
    wc.to_file('pic\\'+key+'sentence(key).png')