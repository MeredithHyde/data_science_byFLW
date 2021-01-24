import time
import requests
import json
import re



def getCurrentTime():

    a = time.asctime()
    b = a.split(" ")
    c = b[3].split(":")
    ant = b[1] + b[2] + c[0] + c[1] + c[2]
    return ant

def get_comment(weibo_id, url, headers, number):
    count = 0

    ans=[]
    # 判断爬取数目是否足够
    while count < number:
        # 判断是否是第一组，第一组不加max_id
        if count == 0:
            # print('是第一组')
            try:
                url = url + weibo_id + '&mid=' + weibo_id + '&max_id_type=0'
                print(url)
                web_data = requests.get(url, headers=headers)
                js_con = web_data.json()
                # 获取连接下一页评论的max_id
                max_id = js_con['data']['max_id']
                print(max_id)
                comments_list = js_con['data']['data']
                for commment_item in comments_list:
                    comment = commment_item["text"]
                    # 删除表情符号
                    label_filter = re.compile(r'</?\w+[^>]*>', re.S)
                    comment = re.sub(label_filter, '', comment)
                    ans.append(comment)
                    time.sleep(0.001)
                    count += 1
                    # print("已获取" + str(count) + "条评论。")
            except Exception as e:
                print(str(count) + "遇到异常")
                break
        else:
            # print('不是第一组')
            try:
                url = url + weibo_id + 'max_id=' + str(max_id) + '&max_id_type=0'
                web_data = requests.get(url, headers=headers)
                js_con = web_data.json()
                # 获取连接下一页评论的max_id
                max_id = js_con['data']['max_id']
                comments_list = js_con['data']['data']
                for commment_item in comments_list:
                    comment = commment_item["text"]
                    # 删除表情符号
                    label_filter = re.compile(r'</?\w+[^>]*>', re.S)
                    comment = re.sub(label_filter, '', comment)
                    ans.append(comment)
                    time.sleep(0.001)
                    count += 1
                    # print("已获取" + str(count) + "条评论。")
            except Exception as e:
                print(str(count) + "遇到异常")
                break
    return ans

#
def get_contents(weibo_id, url, headers):
    try:
        dic={}
        url=url+weibo_id
        print(url)

        data=requests.get(url,headers)
        data=data.text

        pattern = re.compile(r'"created_at": ".*"')
        time = str(pattern.findall(data)[0]).split('"created_at": ')[1]
        time=time[1:len(time)-1]
        print("时间：" + time)

        pattern=re.compile(r'"reposts_count": \d*')
        reposts=int(str(pattern.findall(data)[0]).split(": ")[1])
        print("转发数：" ,reposts)

        pattern = re.compile(r'"comments_count": \d*')
        comments = int(str(pattern.findall(data)[0]).split(": ")[1])
        print("评论数：", comments)

        pattern = re.compile(r'"attitudes_count": \d*')
        likes = int(str(pattern.findall(data)[0]).split(": ")[1])
        print("点赞数：",likes)

        # pattern = re.compile(r'"page_title": "#.*#"')
        # page_title = str(pattern.findall(data)[0]).split(": ")[1]
        # page_title=(page_title)[1:len(page_title)-1]
        # print("引用标题："+page_title)

        pattern = re.compile(r'"status_title": ".*"')
        status_title = str(pattern.findall(data)[0]).split('"status_title": ')[1]
        status_title= "【"+(status_title)[1:len(status_title) - 1]+"】"
        print("标题："+status_title)

        pattern = re.compile(r'"text": .*\n')
        text = str(pattern.findall(data)[0]).split(r'"text": ')[1]
        text=(text)[1:len(text) - 1]

        label_filter = re.compile(r'</?\w+[^>]*>', re.S)
        text = re.sub(label_filter, '', text)

        # text = re.sub(r'</.*?>', '', text)
        # text = re.sub(r'<img.*?>', '', text)
        # text=re.sub(r'<span.*?\">','',text)
        # text=re.sub(r'<a.*?>','',text)

        print("正文："+text)

        dic['address']=url
        dic['time']=time
        dic['title']=status_title
        dic['content']=text
        dic['likes_count']=likes
        dic['comments_count'] = comments
        dic['reposts_count'] = reposts
        return dic
    except Exception as e:
        print("遇到异常")








    #地址 str

    #微博内容 str

    #点赞数 int

    #评论数 int

    #转发数 int

    # req1=re.sub(r'<.*>',"",req)



if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    js=[]
    content_url = 'https://m.weibo.cn/detail/'
    comment_url = 'https://m.weibo.cn/comments/hotflow?id='
    number = 10  # 爬取评论量

    with open('id_data\\new_first.txt') as f:
        ids=f.read().split(' ')

    for i in range(0,len(ids)):
        if(ids[i].endswith('\n')):
            ids[i]=ids[i].split('\n')[0]

    for weibo_id in ids:
        dic=get_contents(weibo_id, content_url, headers)
        comments=get_comment(weibo_id,comment_url,headers,number)
        dic['comments']=comments
        js.append(dic)
        print('爬取完成：'+dic['time'])
        time.sleep(0.01)
    print(js)
    # sort_keys = True,
    js=json.dumps(js,indent=4,separators=(',',':'),ensure_ascii=False)
    print(js)

    t=getCurrentTime()
    with open("json_data\\"+t+".json",'w+',encoding='utf-8') as f:
        f.write(js)
    print("爬取成功！")