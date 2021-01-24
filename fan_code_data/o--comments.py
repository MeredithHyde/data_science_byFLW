# 完整爬取微博评论程序，只需要修改微博id即可
import time

import requests
import json
import re


# 爬取微博评论写入weibo_comment.txt
def get_comment(weibo_id, ourl, headers, number):
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
                continue
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
                continue

    return ans

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    url = 'https://m.weibo.cn/comments/hotflow?id='
    weibo_id = '4463660589976405'  # 微博id
    number = 19  # 爬取评论量

    print(get_comment(weibo_id, url, headers, number))
