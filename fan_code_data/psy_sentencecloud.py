import json
import re

import jieba
from wordcloud import wordcloud

if __name__ == '__main__':
    key='all'

    with open('json_data\\'+'1'+'.json','r',encoding="utf-8") as f:
        data=json.loads(f.read())
        f.close()

    with open('other_data\\stop','r',encoding="utf-8") as sf:
        stopWords=sf.read().split("\n")

    with open('other_data\\psy_dic.json','r',encoding='utf-8') as df:
        emotionwords=list(json.loads(df.read()).keys())
        print(emotionwords)


    sentence=[]

    # for i in range(0,len(data)):            #put all comments together
    #     for comment in data[i]['comments']:
    #         parts=re.split('[^\w\u4e00-\u9fff]+',comment)#过滤非中文和非英文
    #         for ele in parts:
    #             if len(ele) >0:
    #                 sentence.append(ele)

    ##########################################################################
    with open('pure_json_data\\all_comments.json','r',encoding="utf-8") as f:
        data_all=json.loads(f.read())
    for content in data_all:
        sentences=re.split('[^\w\u4e00-\u9fff]+',content)
        for ele in sentences:
                if len(ele) >0:
                    sentence.append(ele)
    print(sentence)

    ###########################################################################

    presentive=[]
    for i in sentence:
        if any(word in i for word in emotionwords):
        # for word in emotionwords:
        #     if word in sentence:
            presentive.append(i)
        #         break
    print(presentive)
    wc=wordcloud.WordCloud(font_path='msyh', width=3840, height=2160,background_color='white')
    wc.generate(" ".join(presentive))
    wc.to_file('pic\\'+key+'(sentence)-keywords.png')