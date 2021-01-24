import json
import re
if __name__ == '__main__':

    key='4'
    new_data=[]
    ill=[]
    select_list = ['']

    # any(str in p1 for str in select_list)

    with open('json_data\\'+key+'.json', 'r', encoding="utf-8") as f:
        data = json.loads(f.read())
        print("打开__条微博：",len(data))
    for i in range(0,len(data)):
        s=data[i]["content"]
        if any(str in s for str in select_list):
            new_data.append(data[i])
        else:
            ill.append(data[i])

    js = json.dumps(new_data, indent=4, separators=(',', ':'), ensure_ascii=False)

    with open('pure_json_data\\'+key+'.json', 'w+', encoding='utf-8') as f:
        f.write(js)
    print("筛选后剩余__条微博：",len(new_data))
    for i in ill:
        print(i["content"])




