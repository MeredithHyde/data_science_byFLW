import time
import jieba

from crawlertool.io import file
import json
from wordcloud import WordCloud

from wordcloud import wordcloud

if __name__ == '__main__':
    key='4'
    psy={}
    with open('psy\\'+key+'.json','r',encoding='utf-8')as f:
        data=json.loads(f.read())
    psy['喜悦']=data['喜悦']
    psy['积极']=data['积极']
    psy['愤怒']=data['愤怒']+data["厌恶"]
    psy['伤感']=data['伤感']
    psy['焦虑']=data['焦虑']

    js=json.dumps(psy, indent=4, separators=(',', ':'), ensure_ascii=False)
    with open('final_data\\'+key+'.json', 'w+', encoding='utf-8') as f:
        f.write(js)
        print(js)




    # A=1
    # from pylab import *
    # from mpl_toolkits.mplot3d import Axes3D
    #
    # fig = figure()
    # ax = Axes3D(fig)
    # X = np.arange(-4, 4, 0.25)
    # Y = np.arange(-4, 4, 0.25)
    # X, Y = np.meshgrid(X, Y)
    # R = np.sqrt(X ** 2 + Y ** 2)
    # Z = np.sin(R)
    #
    # ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='Accent')
    #
    # show()
    ###################################
    # d=[]
    # time1=time.time()
    # for s in range(4, 0,-1):
    #     with open('pure_json_data\\' + str(s) + '.json', 'r', encoding='utf-8') as js:
    #         dic = json.loads(js.read())
    #         for i in dic:
    #             d.append(i["content"])
    #
    #
    #
    # jsonfile = json.dumps(d, indent=4, separators=(',', ':'), ensure_ascii=False)
    # print(jsonfile)
    # with open('pure_json_data\\all_contents.json', 'w',encoding='utf-8') as f:
    #     f.write(jsonfile)
    # print(time.time()-time1)
    # print("所有评论",len(d))
    ###########################################
    # with open('json_data\\all.json', 'r', encoding='utf-8') as js:
    #     data=json.loads(js.read())
    # count=0
    # for weibo in data:
    #     count+=len(weibo['comments'])
    # print("总微博数：",len(data))
    # print("总评论数：",count)

    # a=time.asctime()
    # b=a.split(" ")
    # c=b[3].split(":")
    # time=b[1]+b[2]+c[0]+c[1]+c[2]




    #
    # with open('first_stage.json','r',encoding="utf-8") as f:
    #     data=json.loads(f.read())
    # with open('a','r',encoding="utf-8") as sf:
    #     a=sf.read().split("\n")
    #     print(a)
    #
    #
    #
    #
    #
    # all_comments=''
    # for i in range(0,len(data)):
    #     for c in data[i]['comments']:
    #         all_comments+=c
    #
    # word=jieba.cut(all_comments)
    # remain=[]
    # for i in word:
    #     if i not in a:
    #         remain.append(i)
    #
    # wc=wordcloud.WordCloud(font_path='msyh', width=1920, height=1080,background_color='white')
    # wc.generate(" ".join(remain))
    # wc.to_file('2.png')


    # with open("2803301701.json",'r',encoding="utf-8") as f:
    #     data = json.load(f)
    #     print(data[7])
    # for i in data:
    #     print(i)
    # print(len(data))
    # with open('id.txt') as f:
    #     ids=f.read().split(',')
    #     for i in ids:
    #         i=i.split('\n')[0]
    # print(len(ids))
    # for i in ids:
    #     print(i)
    # print(str(time.time())[11:15])
    # a='222'
    # print(len(a.split(' ')))


    # dic={}
    # dic["time"]='202001022'
    # dic['content']="axecfdcefge"
    # a=[]
    # for i in range(0,5):
    #     a.append("sds")
    # dic['comments']=a
    # print(dic)
    #
    # li=[]
    # li.append(dic)
    # li.append(dic)
    # print(li)
    #
    # mm=json.dumps(li,sort_keys=True,indent=4,separators=(',',':'))
    # with open("ax.json",'w') as ff:
    #     ff.write(mm)
    #
    #


