import os
import json
import random
from datetime import datetime
from urllib.parse import urlparse
from fake_headers import Headers

import eventlet
requests = eventlet.import_patched('requests.__init__')
time = eventlet.import_patched('time')
#import redis

#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

import settings

num_requests = 0
header_id = []

#redis = redis.StrictRedis(host=settings.redis_host, port=settings.redis_port, db=settings.redis_db)
stack = []

def post_request(url, obj, return_soup=True):
    # global request building and response handling

    #url = format_url(url)

    #if "picassoRedirect" in url:
    #    return None  # skip the redirect URLs

    #global num_requests
    #if num_requests >= settings.max_requests:
    #    raise Exception("Reached the max number of requests: {}".format(settings.max_requests))
    try:
        
        r = requests.post(url, data=obj,  headers={'Content-Type': 'application/x-www-form-urlencoded'})
    except RequestException:
        print("WARNING: Request for {} failed, trying again.".format(url))
        return post_request(url, obj)  # try request again, recursively
    
    #num_requests += 1
    
    if r.status_code != 200:
        os.system('say "Got non-200 Response"')
        print("WARNING: Got a {} status code for URL: {}".format(r.status_code, url))
        return None
    
    
    
    if return_soup:
        return BeautifulSoup(r.text, "lxml"), r.text
    return r

def getSimilarity(url, obj, return_soup=True):
    # global request building and response handling

    #url = format_url(url)

    #if "picassoRedirect" in url:
    #    return None  # skip the redirect URLs

    #global num_requests
    #if num_requests >= settings.max_requests:
    #    raise Exception("Reached the max number of requests: {}".format(settings.max_requests))
    try:
        
        r = requests.post(url, data=obj,  headers={'Content-Type': 'application/x-www-form-urlencoded'})
    except RequestException:
        print("WARNING: Request for {} failed, trying again.".format(url))
        return post_request(url, obj)  # try request again, recursively
    
    #num_requests += 1
    
    if r.status_code != 200:
        os.system('say "Got non-200 Response"')
        print("WARNING: Got a {} status code for URL: {}".format(r.status_code, url))
        return None
    
    
    
    if return_soup:
        return r.json()
    return r

def testAPI():
    try:
        r = requests.get('http://127.0.0.1:3001/api/godomall/order')
        #r = requests.get('https://www.google.com')
    except RequestException:
        print("WARNING: Request for db insertion failed, trying again.")


def getDB(dbURL):
    #print(dbURL)
    #print(obj)
    #dbURL = 'http://127.0.0.1:3001/api/godomall/order'
    try:
        #headers = {'Content-Type': 'text/text; charset=utf-8'}
        r = requests.get(dbURL)
    except RequestException:
        print("WARNING: Request for {} failed, trying again.".format(dbURL))
        #print("WARNING: Request for db insertion failed, trying again.")
        #print(obj)
        return getDB(dbURL)  # try request again, recursively

    if r.status_code != 200:
        os.system('say "Got non-200 Response"')
        print("WARNING: Got a {} status code for URL: {}".format(r.status_code, obj))
        return None
    else:
        print("get request success")
        return r.json()
    return None

def save_DB(dbURL, obj):
    #print(dbURL)
    #print(obj)
    #dbURL = 'http://127.0.0.1:3001/api/godomall/order'
    try:
        #headers = {'Content-Type': 'text/text; charset=utf-8'}
        #print(obj)
        r = requests.post(dbURL, data=obj)
    except RequestException:
        print("WARNING: Request for {} failed, trying again.".format(dbURL))
        #print("WARNING: Request for db insertion failed, trying again.")
        #print(obj)
        return save_DB(dbURL, obj)  # try request again, recursively

    if r.status_code != 200:
        os.system('say "Got non-200 Response"')
        #print("WARNING: Got a {} status code for URL: {}".format(r.status_code, obj))
        #print(r.request.text)
        print("WARNING: Got a {} status code for URL".format(r.status_code))
        return None
    else:
        #print(r)
        print("insert success")
    return None
    
def isGoodsNo(dbURL, goodsNo):
    #print(dbURL)
    #print(obj)
    dbURL = 'http://127.0.0.1:3001/api/godomall/product/goodsno/'+goodsNo
    #print(dbURL)
    try:
        #headers = {'Content-Type': 'text/text; charset=utf-8'}
        r = requests.get(dbURL)
    except RequestException:
        print("WARNING: Request for {} failed, trying again.".format(dbURL))
        #print("WARNING: Request for db insertion failed, trying again.")
        #print(obj)
        return getGoodsNo(dbURL, goodsNo)  # try request again, recursively

    if r.status_code != 200:
        os.system('say "Got non-200 Response"')
        print("WARNING: Got a {} status code for URL".format(r.status_code))
        return None
    else:
        print("get request success")
        
    if r.text == '[]':
        return False
    else:
        return True

def format_url(url):
    # make sure URLs aren't relative, and strip unnecssary query args
    u = urlparse(url)

    scheme = u.scheme or "https"
    host = u.netloc or "www.amazon.com"
    path = u.path

    if not u.query:
        query = ""
    else:
        query = "?"
        for piece in u.query.split("&"):
            k, v = piece.split("=")
            if k in settings.allowed_params:
                query += "{k}={v}&".format(**locals())
        query = query[:-1]

    return "{scheme}://{host}{path}{query}".format(**locals())

"""
def log(msg):
    # global logging function
    if settings.log_stdout:
        try:
            print "{}: {}".format(datetime.now(), msg)
        except UnicodeEncodeError:
            pass  # squash logging errors in case of non-ascii text
"""

def get_proxy():
    proxy_url = settings.proxy_db_url + str(random.randint(1, settings.proxy_num))
    #print("proxy print")
    #print(proxy_url)
    
    try:
        r = requests.get(proxy_url)
    except RequestException:
        print("WARNING: Request for {} failed, trying again.".format(proxy_url))
        return make_request_cfg(proxy_url)  # try request again, recursively

    #print(r.text)
    json_data = json.loads(r.text)

    #formatting in sentence, think!
    """
    return {
        "http": "socks5://" + json_data['ip'] + ":" + json_data['port'],
        "https": json_data['ip'] + ":" + json_data['port']
    }
    """
    return {
        "http": "socks5://" + json_data['ip'] + ":" + json_data['port']
    }



def save_DB_cfg(obj):
    #dbURL = 'http://localhost:3000/api/productmap_config/update/'
    dbURL = 'http://localhost:3000/api/productmap_config_competitors/'

    #dbURL = 'http://ec2-52-87-191-124.compute-1.amazonaws.com:3000/api/productmap_config/update/'
    #dbURL = 'http://ec2-52-87-191-124.compute-1.amazonaws.com:3000/api/productmap_config/'
    

    try:
        r = requests.post(dbURL, data=obj)
    except RequestException:
        #log("WARNING: Request for {} failed, trying again.".format(url))
        print("WARNING: Request for db insertion failed, trying again.")
        return save_DB_cfg(obj)  # try request again, recursively

    if r.status_code != 200:
        os.system('say "Got non-200 Response"')
        print("WARNING: Got a {} status code for URL: {}".format(r.status_code, obj))
        return None
    else:
        #print(obj)
        print("insert success with header id: {}".format(get_header_id()))
    return None




def enqueue_url_cfg(u):
    stack.append(u)
    


def dequeue_url_cfg():
    return stack.pop()

def get_queue_url_length():
    #print(len(stack))
    return len(stack)

def get_header_id():
    id = header_id.pop()
    header_id.append(id)
    return id

def set_header_id(id):
    if len(header_id) != 0:
        header_id.pop()
    header_id.append(id)
#    header_id = id
    #print("header_id changed to id:{}".format(get_header_id()))

if __name__ == '__main__':
    # test proxy server IP masking
    r = make_request_cfg('https://api.ipify.org?format=json', return_soup=False)
    #print r.text