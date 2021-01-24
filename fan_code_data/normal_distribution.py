import math
import json
import time

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import poisson, norm,expon,invweibull

if __name__ == '__main__':


    comments_count=[]

    k = '4'
    with open('pure_json_data\\' + k + '.json', 'r', encoding="utf-8") as f:
        data = json.loads(f.read())
    for i in range(len(data)):
        comments_count.append(data[i]["comments_count"])


    fig, ax = plt.subplots(1, 1,sharex='all',sharey='all')
    mu=np.mean(comments_count)
    v=np.std(comments_count)
    print("样本均值:",mu)
    print("样本方差:",v)



    n, bins, patches = plt.hist(comments_count, bins=2000, facecolor='c', edgecolor='b', alpha=0.8)

    c = 10.6
    mean, var, skew, kurt = invweibull.stats(c, moments='mvsk')
    x = np.linspace(invweibull.ppf(0.01, c),
                    invweibull.ppf(0.99, c), 100)
    ax.plot(x, invweibull.pdf(x, c),
            'r-', lw=5, alpha=0.6, label='invweibull pdf')
    rv = invweibull(c)
    ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
    vals = invweibull.ppf([0.001, 10000, 0.999], c)
    np.allclose([0.001, 10000, 0.999], invweibull.cdf(vals, c))
    r = invweibull.rvs(c, size=1000)

    # mean, var, skew, kurt = expon.stats(moments='mvsk')
    # x = np.linspace(expon.ppf(0.01),
    #                 expon.ppf(0.99), 100)
    # ax.plot(x, expon.pdf(x),
    #         'r-', lw=0.05, alpha=0.6, label='expon pdf')
    # rv = expon()
    # ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')
    # vals = expon.ppf([0.001, 1000, 0.999])
    # np.allclose([0.001, 1000, 0.999], expon.cdf(vals))
    # r = expon.rvs(size=1000)

    ax.legend(loc='best', frameon=False)
    plt.show()
















