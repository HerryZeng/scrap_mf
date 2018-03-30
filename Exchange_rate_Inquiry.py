#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import pprint
from urllib.parse import urlencode
from urllib.request import urlopen


# ----------------------------------
# 货币汇率调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/23
# ----------------------------------

def main():
    # 配置您申请的APPKey
    # appkey = "*********************"
    appkey = "7984fe89ab39e4e367ff87f1752c0822"

    # 1.人民币牌价
    # request1(appkey, "GET")

    # 2.外汇汇率
    # request2(appkey, "GET")

    request3(appkey, "GET")


# 人民币牌价
def request1(appkey, m="GET"):
    # url = "http://web.juhe.cn:8080/finance/exchange/rmbquot"
    url = "http://web.juhe.cn:8080/finance/exchange/rmbquot"
    params = {
        "key": appkey,  # APP Key
        "type": "0",  # 两种格式(0或者1,默认为0)

    }
    params = urlencode(params)
    if m == "GET":
        f = urlopen("%s?%s" % (url, params))
    else:
        f = urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")

    # 外汇汇率


def request2(appkey, m="GET"):
    url = "http://web.juhe.cn:8080/finance/exchange/frate"
    params = {
        "key": appkey,  # APP Key
        "type": "0",  # 两种格式(0或者1,默认为0)

    }
    params = urlencode(params)
    if m == "GET":
        f = urlopen("%s?%s" % (url, params))
    else:
        f = urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))

    else:
        print("request api error")


# 查询货币列表

def request3(appkey, m="GET"):
    # url = "http://web.juhe.cn:8080/finance/exchange/frate"
    url = "http://op.juhe.cn/onebox/exchange/list"
    params = {
        "key": appkey,  # APP Key
        "type": "0",  # 两种格式(0或者1,默认为0)

    }
    params = urlencode(params)
    if m == "GET":
        f = urlopen("%s?%s" % (url, params))
    else:
        f = urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            # pprint(res["result"])
            # print(type(res["result"]))

            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(res["result"]['list'])
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))

    else:
        print("request api error")


if __name__ == '__main__':
    main()
