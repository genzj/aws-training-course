import hashlib, base64, json
from datetime import datetime
from urllib import request, parse
from pprint import pprint


# 和风天气签名生成算法-Python版本
# params API调用的请求参数集合的关联数组（全部需要传递的参数组成的数组），不包含sign参数
# secret 用户的认证 key
# return string 返回参数签名值
def sign(params, secret):
    canstring = ''
    #先将参数以其参数名的字典序升序进行排序
    params = sorted(params.items(), key=lambda item:item[0])
    #遍历排序后的参数数组中的每一个key/value对
    for k,v in params:
        if( k != 'sign' and k != 'key' and v != '') :
         canstring +=  k + '=' + v + '&'
    canstring = canstring[:-1]
    canstring += secret
    md5 = hashlib.md5(canstring.encode('utf-8')).digest()
    return base64.b64encode(md5)


def utctimestamp():
    unix_time_source = datetime(1970, 1, 1)
    n = datetime.utcnow()
    return int((n - unix_time_source).total_seconds())


def get_json(url):
    response = request.urlopen(url)
    body = response.read().decode('utf8')
    return json.loads(body)

def hefeng(city):
    params = {
        "location": city,
        "username": "HE1601211533111623",
        "t": str(utctimestamp())
    }
    params['sign'] = sign(params, 'd5bd328dd36844bbb20c0e4905568e8e')
    query = parse.urlencode(params)
    url = 'https://free-api.heweather.com/s6/weather/now?' + query

    return get_json(url)
    

def openweathermap(city):
    params = {
        "q": city,
        "appid": "18bc2f96c466fc82cd607d43eb152055",
        "units": "metric",
    }
    url = 'https://api.openweathermap.org/data/2.5/weather?' + parse.urlencode(params)
    return get_json(url)


def lambda_handler(event, context):
    city = event["city"]
    answer = {
        "hefeng": hefeng(city),
        "openweathermap": openweathermap(city)
    }
    pprint(answer)
    return json.dumps(answer)
