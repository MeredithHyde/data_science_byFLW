import json

import jieba
from wordcloud import wordcloud

if __name__ == '__main__':

    key='alla'

    with open('other_data\\psy_dic.json','r',encoding="utf-8") as f:
        psy_dic=json.loads(f.read())
    psy_list=list(psy_dic.keys())
    print(psy_list)

    psy_words = []
    # for i in range(1,5):
    with open('other_data\\IDF' + key + '.json', 'r', encoding="utf-8") as f:
        data = json.loads(f.read())
    for sentence in data:
        words = list(sentence.keys())
        # print(words)
        for word in words:
            if word in psy_list:
                psy_words.append(word)
                break


    wc=wordcloud.WordCloud(font_path='msyh', width=3840, height=2160,background_color='white')
    wc.generate(" ".join(psy_words))
    wc.to_file('pic\\'+key+'(word)-keywords.png')