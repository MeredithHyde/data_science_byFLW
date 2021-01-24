import pygal

#准备数据
if __name__ == '__main__':

    data =[[5,4.0,5,5,5],
    [4.8,2.8,4.8,4.8,4.9],
    [4.5,2.9,4.6,4.0,4.9],
    [4.0,4.8,4.9,4.0,5],
    [3.0,4.2,2.3,3.5,2],
    [4.8,4.3,3.9,3.0,4.5]]

    #准备标签
    labels = ['Java','C','C++','Python','C#','PHP']

    #创建pygal.Radar对象(雷达图)

    radar = pygal.Radar()

    #采用循环为雷达图添加数据

    for i,per in enumerate(labels):

    radar.add(labels[i],data[i])

    radar.x_labels = ['平台健壮性','语法易用性','社区活跃度','市场份额','未来趋势']

    radar.title = '编程语言对比图'

    #控制各得分点的大小

    radar.dots_size = 8

    #设置将图例放在底部

    radar.legend_at_bottom = True

    #指定将数据图例输出到SVG文件中

    radar.render_to_file('pic\\language.svg')

