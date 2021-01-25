import math
import json
import time

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import poisson, norm, expon, f, chi2

if __name__ == '__main__':


    comments_count=[]

    k = '4'
    with open('pure_json_data\\' + k + '.json', 'r', encoding="utf-8") as sf:
        data = json.loads(sf.read())
    for i in range(len(data)):
        comments_count.append(data[i]["comments_count"])


    x = np.array(comments_count)

    # n, bins, patches = plt.hist(x, 20, density=1, facecolor='blue', alpha=0.75)  #第二个参数是直方图柱子的数量
    # mu = np.mean(x)  # 计算均值
    # sigma = np.std(x)
    mu,sigma=norm.fit(comments_count)
    # p1=stats.normaltest(x)
    # print(p1)
    i=1
    while i<100000:
        i*=2
        num_bins =i  # 直方图柱子的数量
        n, bins, patches = plt.hist(x, num_bins, density=1, alpha=0.75)
        # 直方图函数，x为x轴的值，normed=1表示为概率密度，即和为一，绿色方块，色深参数0.5.返回n个概率，直方块左边线的x值，及各个方块对象
        y = norm.pdf(bins, mu, sigma)  # 拟合一条最佳正态分布曲线y

        p_norm=list(stats.kstest(comments_count,y))
        print("H0：假设评论数服从正态分布，H1：评论数不服从正态分布，p=",p_norm[1])
        if(p_norm[1]<0.05):
            print('否定H0，接受H1')
        else:
            print("接受H0")



        # p_f = list(stats.kstest(comments_count, z))
        # print("H0：假设评论数服从F分布，H1：评论数不服从F分布，p=", p_norm[1])
        # if (p_norm[1] < 0.05):
        #     print('否定H0，接受H1')
        # else:
        #     print("接受H0")


        #
        plt.grid(True)
        plt.plot(bins, y, 'r--')  # 绘制y的曲线
        plt.xlabel('values')  # 绘制x轴
        plt.ylabel('Probability')  # 绘制y轴
        plt.title('Histogram : $\mu$=' + str(round(mu, 2)) + ' $\sigma=$' + str(round(sigma, 2)))  # 中文标题 u'xxx'
        # plt.subplots_adjust(left=0.15)#左边距
        # plt.savefig('pic\\高斯拟合'+k+'.png')
        plt.show()
        time.sleep(0.001)


















