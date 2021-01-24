import json

import jieba
from wordcloud import wordcloud

if __name__ == '__main__':
    key='1'


    with open('pure_json_data\\'+key+'.json','r',encoding="utf-8") as f:
        data=json.loads(f.read())

    with open('other_data\\a','r',encoding="utf-8") as sf:
        stopWords=sf.read().split("\n")


    all_contents=''

    for i in data:            #put all comments together
        for content in i['content']:
            all_contents+=content

    word=jieba.cut(all_contents)            #use jieba api to break down all words so can be put in use
    presentive=[]
    for i in word:
        if i not in stopWords:
            presentive.append(i)

    wc=wordcloud.WordCloud(font_path='msyh', width=1920, height=1080,background_color='white')
    wc.generate(" ".join(presentive))
    wc.to_file('pic\\'+key+'_period(word).png')