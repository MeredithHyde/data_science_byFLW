import re



if __name__ == '__main__':

    with open('raw_data\\first-virus.txt','r',encoding='utf-8') as f:
        rawData=f.read()
        f.close()
    with open('id_data\\first.txt','r',encoding='utf-8') as f:
        IDlist=f.read().split(' ')

    print(rawData)

    pattern=re.compile('comment/.*?uid')
    comment=pattern.findall(rawData)
    print("有__个：",len(comment))
    for i in comment:
        print(i)
        start=i.index('/')+1
        end=i.index('?')
        print(start,end)
        temp=i[start:end]
        if temp not in IDlist:
            IDlist.append(i[start:end])
    for i in IDlist:
        print(i)

    store=" ".join(IDlist)

    with open('id_data\\new_first.txt','w') as f:
        f.write(store)
        f.close()
