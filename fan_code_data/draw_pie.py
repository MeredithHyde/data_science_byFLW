import json

from matplotlib.font_manager import FontProperties #字体管理器
import pandas as pd
import matplotlib.pylab as plt
if __name__ == '__main__':
    key='1'
    with open('final_data\\'+key+'.json','r',encoding="utf-8") as f:
        data=json.loads(f.read())

    fig,axes=plt.subplots()

    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']#中文显示
    # 记录每一个饼状图的比例
    size=[]

    #定义饼状图的标签
    label='喜悦','积极','愤怒','伤感','焦虑'
    for word in label:
        size.append(data[word])

    #定义每一块的颜色
    colors=['deeppink','gold','firebrick','mediumslateblue','khaki']
    explode=(0,0.1,0,0,0)
    axes.pie(size,labels=label, explode=explode,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
    axes.axis('equal')

    plt.show()
    # fig.savefig('pic\\11.png')