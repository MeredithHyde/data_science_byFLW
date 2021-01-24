import json
import math

if __name__ == '__main__':

    key = '3'
    psy = {}
    with open('psy\\' + key + '.json', 'r', encoding='utf-8')as f:
        data = json.loads(f.read())
    # psy['喜悦'] = data['喜悦']
    # psy['积极'] = data['积极']
    # psy['愤怒'] = data['愤怒'] + data["厌恶"]
    # psy['伤感'] = data['伤感']
    # psy['焦虑'] = data['焦虑']
    countlist=list(data.values())
    print(countlist)
    sum =0
    for i in countlist:
        sum+=i
    keylist=list(data.keys())
    for k in keylist:
        psy[k]=data[k]/sum


    js = json.dumps(psy, indent=4, separators=(',', ':'), ensure_ascii=False)
    with open('psy\\评论关键词心态统计频率' + key + '.json', 'w+', encoding='utf-8') as f:
        f.write(js)
        print(js)