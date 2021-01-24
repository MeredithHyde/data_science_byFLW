import json

import numpy as np
from matplotlib.font_manager import FontProperties #字体管理器
import pandas as pd
import matplotlib.pylab as plt
if __name__ == '__main__':
    key='1'

    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']#中文显示

    with open('final_data\\'+key+'.json','r',encoding="utf-8") as f:
        data=json.loads(f.read())

    # 记录每一个饼状图的比例
    size=[]

    #定义饼状图的标签
    label='喜悦','积极','愤怒','伤感','焦虑'
    for word in label:
        size.append(data[word])

    x = np.array(label)
    y = np.array(size)
    # plt.plot(x, y, 'r', lw=2)
    # =========================================

    # =========================================
    x = np.array(label)
    y = np.array(size)
    plt.bar(x, y, 0.2, alpha=0.5, color='r')
    plt.show()

    # #定义每一块的颜色
    # colors=['yellowgreen','gold','lightskyblue','lightcoral','blue']
    # plt.pie(size,labels=label,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
    # plt.axis('equal')
    #
    # plt.show()