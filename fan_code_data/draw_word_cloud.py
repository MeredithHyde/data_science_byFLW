import json

import jieba
from wordcloud import wordcloud

if __name__ == '__main__':


    with open('json_data\\4.json','r',encoding="utf-8") as f:
        data=json.loads(f.read())

    with open('other_data\\a','r',encoding="utf-8") as sf:
        stopWords=sf.read().split("\n")


    all_comments=''

    for i in range(0,len(data)):            #put all comments together
        for comment in data[i]['comments']:
            all_comments+=comment

    word=jieba.cut(all_comments)            #use jieba api to break down all words so can be put in use
    presentive=[]
    for i in word:
        if i not in stopWords:
            presentive.append(i)

    wc=wordcloud.WordCloud(font_path='msyh', width=1920, height=1080,background_color='white')
    wc.generate(" ".join(presentive))
    wc.to_file('pic\\4rd_period(word).png')