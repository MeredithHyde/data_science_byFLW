import json
import random
import time

import requests

if __name__ == "__main__":

    headers = {
        'Host': 'm.weibo.cn',
        'User-Agent': '',
        'referer': 'https://m.weibo.cn/detail/4463660589976405',
        'Cookie': 'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhIh4zsKBLYqrhgQH.LTWly5NHD95QEe0eRSozfS0n7Ws4Dqcjki--ci-2RiKyWi--Ri-2RiKn7i--4i-z4iKysP0zE1Btt; _T_WM=33510257507; _TTT_USER_CONFIG_H5=%7B%22ShowMblogPic%22%3A1%2C%22ShowUserInfo%22%3A1%2C%22MBlogPageSize%22%3A10%2C%22ShowPortrait%22%3A1%2C%22CssType%22%3A0%2C%22Lang%22%3A1%7D; MLOGIN=1; SCF=ArfZ_hYk3OFRyB5H-PKbPVzBuzSaNl4QqdidkotZcdz353SwvS_cIQjdokOmQ_FkELP1Ip7s5FXcyAOlCDASZBM.; SUB=_2A25NDVpFDeRhGeRN6FoX8ivLwzyIHXVuDmYNrDV6PUJbktAKLXTckW1NU7-E7FEE7EAMFmztZtTpkZnL7--3rSk6; WEIBOCN_FROM=1110006030; XSRF-TOKEN=c98000; M_WEIBOCN_PARAMS=oid%3D4463660589976405%26luicode%3D20000061%26lfid%3D4463660589976405%26uicode%3D20000061%26fid%3D4463660589976405',
    }

    res=requests.get("https://m.weibo.cn/comments/hotflow?id=4595579064425706&mid=4595579064425706&max_id_type=0")
    re=requests.get('https://m.weibo.cn/comments/hotflow?id=4595579064425706&mid=4595579064425706&max_id_type=04595579064425706max_id=145033838451771&max_id_type=04595579064425706max_id=145033838451771&max_id_type=0')
    print(res.json())
    print(re.json())

    # js=json.dumps(res.json(),indent=4,separators=(',',':'),ensure_ascii=False)
    # with open(str(time.time())[11:15]+".json",'w+',encoding='utf-8') as f:
    #     f.write(js)



