from http import client
import urllib
import urllib.request
import json
import requests

# httplib
def getBaidu():
	http_client = client.HTTPConnection('baidu.com', 80, timeout=20)
	http_client.request('GET', '')
	r = http_client.getresponse()
	print(r.status)
	print(r.reason)
	print(r.getheaders())
	print(r.msg)
	print(r.read())
	#print(dir(r))

# python2 urllib2.urlopen
def get_Baidu():
	r = urllib.request.urlopen('http://www.baidu.com')
	print(r.getcode(), r.msg)
	print(r.headers)

# python2 urllib.urlencode
def post_cun():
	params = urllib.parse.urlencode({'cityId':'438'}).encode(encoding='UTF8')
	r = urllib.request.urlopen('http://m.cyw.com/index.php?m=api&c=cookie&a=setcity',params)
	print(r.getcode(), r.msg)
	print(r.read())

#序列化：把python的对象编码转换为json格式的字符串
def get_json():
	dict1 = {'name':'wuya','age':22,'address':'xian'}
	print('before', type(dict1), dict1)
	str1 = json.dumps(dict1)
	print('after', type(str1), str1)
	#反序列化
	dict2 = json.loads(str1)
	print('re',type(dict2), dict2)

#get_json()
#json+request
def combine():
	r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
	print(r.text, type(r.text))
	dic = json.loads(r.text)
	print(dic, type(dic))

combine()