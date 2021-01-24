import json
import math
import re

import jieba
from wordcloud import wordcloud

from crawlerByID import getCurrentTime

if __name__ == '__main__':

    k='4'

    with open('pure_json_data\\'+k+'.json','r',encoding="utf-8") as f:
        data=json.loads(f.read())

    with open('other_data\\a','r',encoding="utf-8") as sf:
        stopWords=sf.read().split("\n")
    # tf
    TF=[]
    comments=[]

    for i in range(len(data)):
        for comment in data[i]['comments']:
            comments.append(comment)



##IDF
    wordList = jieba.lcut("".join(comments))
    wordList_noRepeat=[]
    N=len(comments)
    print("总评论数：",N)
    IDF={}


    for i in wordList:
        if i not in wordList_noRepeat:
            wordList_noRepeat.append(i)

    for word in wordList_noRepeat:
        IDF[word]=1
        for comment in comments:
            if word in comment :
                IDF[word]+=1

        IDF[word]=math.log(N/IDF[word],2)
    print(IDF)
#TF

    for i in range(len(comments)):
        words=jieba.lcut(comments[i])
        n=len(words)
        temp={}
        for word in words:

            if word not in temp.keys():
                temp[word]=1
            else:
                temp[word]+=1
        for word in words:
            if word in IDF.keys():
                temp[word]=(temp[word]/n)*IDF[word]
        l = sorted(temp.items(), key=lambda x: x[1], reverse=True)

        dic={}
        for i in range(len(l)):
            dic[l[i][0]]=l[i][1]
        TF.append(dic)

    print(TF)

    js = json.dumps(TF, indent=4, separators=(',', ':'), ensure_ascii=False)
    print(js)

    t = getCurrentTime()
    with open("other_data\\" + t + ".json", 'w+', encoding='utf-8') as f:
        f.write(js)






    # N=0
    # all_comments=''
    #
    # for i in range(0,len(data)):            #put all comments together
    #     for comment in data[i]['comments']:
    #         all_comments+=comment
    #     N+=len(data[i]['comments'])
    #
    # print("总评论数：",N)
    # word=jieba.lcut(all_comments)            #use jieba api to break down all words so can be put in use
    #
    # dic={}
    #
    # for i in word:
    #     if not i.isalnum():
    #         continue
    #     if i not in dic.keys():
    #         dic[i]=1
    #     else:
    #         dic[i]+=1
    #
    # l=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    # print(l)
    #
    # dic={}
    # for i in range(len(l)):
    #     dic[l[i][0]]=l[i][1]
    # print(dic)


    # presentive=[]
    # for i in word:
    #     if i not in stopWords:
    #         presentive.append(i)
    #
    # wc=wordcloud.WordCloud(font_path='msyh', width=1920, height=1080,background_color='white')
    # wc.generate(" ".join(presentive))
    # wc.to_file('pic\\4rd_period(word).png')