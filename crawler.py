import sys
import json
from datetime import datetime, date, timedelta
import eventlet
import threading
import time
import csv
import xml.etree.ElementTree as elemTree
import xmltodict
import ast

import settings
import productMap
#from models import ProductRecord
from helpers_config import post_request, save_DB, getDB, testAPI, isGoodsNo, getSimilarity
#from tree import CategoryTree
from anytree import Node, RenderTree, search, Walker


pool = eventlet.GreenPool(settings.max_threads)
pile = eventlet.GreenPile(pool)


def godomallPSearch():
    url = 'http://openhub.godo.co.kr/godomall5/goods/Goods_Search.php'
    partner_key = 'JUUwJUZGJUE2JUFFVjJsJTk1'
    key = 'JTJDJTAwJTFEJTEwJUY2MiU5Q0FYbCU3RSVDN3ElN0UlRUYlQUQlRDh3JUU3JTAwJTlBJUU0JUNGJTQwJUY3SCVBQ2clRjAlMEMxJTEyJTA1JUU4JUQ0JUEx'
    goodsNm = 'toy'
    obj = { 
        'partner_key': partner_key,
        'key' : key,
        'page'  : 9,
        'size'  : 100
    }
    page, html = post_request(url, obj)
    #print(page)

    #f = open("sample.txt", 'w', encoding='UTF-8')
    #f.write(str(html))
    #f.close()

    #f = open("sample2.txt", 'w', encoding='UTF-8')
    
    

    tree = elemTree.fromstring(html)

    #print(tree.iter(tag='order_data'))
    
    productData = []
    dbURL = 'http://127.0.0.1:3001/api/godomall/product'
    goodsNoURL = 'http://127.0.0.1:3001/api/godomall/product/goodno'

    for product in tree.iter(tag='goods_data'):
        #print(product.tag)
        productObject = {}
        for key in product:
            #print(key.tag, key.text)
                
            if key.tag != 'kcmarkInfo' and key.tag != 'mileageGroupMemberInfo' and key.tag != 'goodsDiscountGroupMemberInfo' and key.tag != 'goodsMustInfoData' and key.tag != 'goodsDescription' and key.tag != 'goodsDescriptionMobile' and key.tag != 'detailInfoDeliveryDirectInput':
                productObject[key.tag] = key.text

        
        
        productString = str(productObject).replace('\'', '"').replace('None', '""')
        #print(productString)
        #print('\n\n\n\n')
        #f.write(productString)
        #f.write('\n\n\n\n')
        

        productJson = json.loads(productString)
        #print(jsongOrder)
        #f.write(str(productJson))
        #f.write('\n\n\n\n')
        #print(productJson['goodsNo'])
        #print(isGoodsNo(goodsNoURL, productJson['goodsNo']))
        
        if isGoodsNo(goodsNoURL, productJson['goodsNo']):
            print('goodsNo exists')
        else:
            save_DB(dbURL, productJson)
        
    #f.close()    


def godomallProductTree():
    dbURL = 'http://127.0.0.1:3001/api/godomall/product'
    products = getDB(dbURL)

    print(len(products))
    
    all_node_set = []
    root = Node("root", data=0)
    all_node_set.append(root)

    index = 0
    for product in products:
        #print(product['goodsNo'], product['allCateCd'])
        goodsNo = product['goodsNo']
        allCateCd = 'root|' + product['allCateCd'] + '|' + product['goodsNo']
        category = allCateCd.split('|')
        #print(category)
        for i in range(0, len(category)-1):
            #print(category[i], category[i+1])
            #print(search.findall(root, lambda node:  node.name == category[i]), search.findall(root, lambda node:  node.name == category[i+1]))

            if search.find(root, lambda node:  node.name == category[i]):
                if not search.find(root, lambda node:  node.name == category[i+1]):
                    #parent exists, children exist, pass
                
                    #parent exists, children not exist, add
                    parent = search.find(root, lambda node:  node.name == category[i])
                    children = category[i+1]
                    new_node = Node(children, parent = parent)
                    all_node_set.append(new_node)
            else:
                #parent not exists, connect to root
                parent = search.find(root, lambda node:  node.name == category[i])
                children = category[i+1]
                new_node = Node(children, parent = parent)
                all_node_set.append(new_node)

    #print(root.children)
    #print(root)
    #print(all_node_set)

    #print(len(root.children))
    
    a = search.find(root, lambda node:  node.name == '1000006090')
    b = search.find(root, lambda node:  node.name == '1000006091')
    w = Walker()
    print(w.walk(a, b), len(w.walk(a,b)))
    upwards, common, downwards = w.walk(a,b)
    #print(upwards, len(upwards))
    #print(common, len(common))
    #print(downwards, len(downwards))
    similarity = len(upwards) + len(downwards)
    print(similarity)

    #f = open("simTable.txt", 'w', encoding='UTF-8')
    simTable = {}
    productsX = products
    productsY = products
    for productX in productsX:
        x = search.find(root, lambda node:  node.name == productX['goodsNo'])
        simTable[x.name] = {}
        for productY in productsY:
            y = search.find(root, lambda node:  node.name == productY['goodsNo'])
            upwards, common, downwards = w.walk(x,y)
            similarity = len(upwards) + len(downwards)
            #simTable[x.name][y.name] = similarity
            #f.write(str(x.name) + ',' + str(y.name) + ',' + str(similarity) + '\n')
            dbURL = 'http://127.0.0.1:3001/api/godomall/similarity'
            sim = {}
            sim['goodsNoX'] = x.name
            sim['goodsNoY'] = y.name
            sim['similarity'] = similarity
            
            save_DB(dbURL, sim)
            
        time.sleep(10)
    #print(simTable)

    
    #f.write(str(simTable))
    #f.close()





def godomallOSearch():
    url = 'http://openhub.godo.co.kr/godomall5/order/Order_Search.php'
    partner_key = 'JUUwJUZGJUE2JUFFVjJsJTk1'
    owner_key = 'JTJDJTAwJTFEJTEwJUY2MiU5Q0FYbCU3RSVDN3ElN0UlRUYlQUQlRDh3JUU3JTAwJTlBJUU0JUNGJTQwJUY3SCVBQ2clRjAlMEMxJTEyJTA1JUU4JUQ0JUEx'
    

    day = timedelta(days = 1)
    startDate = date(2016, 11, 10)
    #startDate = date(2017, 12, 4)
    #pivot = date(2017,12,5)
    #while(startDate < pivot):
    while(date.today() > startDate):
        print('[GET] ' + str(startDate) + ' data')
        obj = { 
            'partner_key': partner_key,
            'key' : owner_key,
            'dateType' : 'order',
            'startDate': startDate.isoformat(),
            'endDate' : startDate.isoformat(),
            'orderStatus' : 's1'
        }  
        #print(obj)                

        page, html = post_request(url, obj)
        
        tree = elemTree.fromstring(html)

        #print(tree.iter(tag='order_data'))
        
        orderData = []
        dbURL = 'http://127.0.0.1:3001/api/godomall/order'
        
        for order in tree.iter(tag='order_data'):
            #print(order.tag)
            orderObject = {}
            for key in order:
                #print(key.tag, key.text)
                if key.tag == 'orderNo' or key.tag == 'memNo' or key.tag == 'orderIp' or key.tag == 'orderEmail' or key.tag == 'orderDate':
                    orderObject[key.tag] = key.text
                elif key.tag == 'orderGoodsData':
                    #print(key.attrib['idx'])
                    #print('----------------')
                    orderGoodsData = {}
                    for subKey in key:
                        if subKey.tag == 'goodsNm' or subKey.tag == 'goodsCnt' or subKey.tag == 'goodsPrice' or subKey.tag == 'goodsNo':
                            orderGoodsData[subKey.tag] = subKey.text
                            #orderObject[str(key.tag + '_' + subKey.tag)] = subKey.text.replace('"', '\"')
                            orderObject[subKey.tag] = subKey.text
                    #print(orderObject)
                    #orderObject[key.tag][key.attrib['idx']] = orderGoodsData
                    orderString = str(orderObject).replace('\'', '"').replace('None', '""')
                    #orderString = str(orderObject)
                    #print(orderString)
                    
                    if orderObject['goodsNo'] in productMap.products:
                        try:
                            jsongOrder = json.loads(orderString)
                            #print(jsongOrder)
                            save_DB(dbURL, jsongOrder)
                        except:
                            print('[ERROR] ' + str(startDate) + ' data')
                            f = open("sample.txt", 'w', encoding='UTF-8')
                            f.write(str(orderString))
                            f.close()
                
        startDate += day

    
def godomallTest():
    
    url = 'http://openhub.godo.co.kr/godomall5/order/Order_Search.php'
    partner_key = 'JUUwJUZGJUE2JUFFVjJsJTk1'
    owner_key = 'JTJDJTAwJTFEJTEwJUY2MiU5Q0FYbCU3RSVDN3ElN0UlRUYlQUQlRDh3JUU3JTAwJTlBJUU0JUNGJTQwJUY3SCVBQ2clRjAlMEMxJTEyJTA1JUU4JUQ0JUEx'
    

    day = timedelta(days = 1)
    #startDate = date(2016, 11, 10)
    #startDate = date(2017, 6, 10)
    #pivot = date(2017,6,11)
    #while(startDate < pivot):
    
    #print('[GET] ' + str(startDate) + ' data')
    obj = { 
        'partner_key': partner_key,
        'key' : owner_key,
        'dateType' : 'order',
        'orderNo' : '1711161615016774'
     
    }  
    #print(obj)                

    page, html = post_request(url, obj)
    print(html)
    f = open("sample2.txt", 'w', encoding='UTF-8')
    f.write(str(html))
    f.close()

def godomallOrderRSById():
    dbURL = 'http://127.0.0.1:3001/api/godomall/order'
    orders = getDB(dbURL)

    #print(len(orders))
    orderMap = []
    subOrderMap = {}
    for order in orders:
        subOrderMap = {}
        if order['memNo'] != '0':
            subOrderMap['id'] = order['memNo']
        elif order['orderEmail'] != '':
            subOrderMap['id'] = order['orderEmail']
        else:
            subOrderMap['id'] = order['orderIp']
        #subOrderMap['goodsNm'] = order['goodsNm']
        #subOrderMap['orderDate'] = order['orderDate']
        #subOrderMap['goodsCnt'] = order['goodsCnt']
        #subOrderMap['goodsPrice'] = order['goodsPrice']
        subOrderMap['goodsNo'] = order['goodsNo']
        orderMap.append(subOrderMap)

    #print(orderMap)
    
    orderById = {}
    for order in orderMap:
        #print(order)
        subOrderById = {}
        #subOrderById['goodsNm'] = order['goodsNm'] 
        #subOrderById['orderDate'] = order['orderDate'] 
        #subOrderById['goodsCnt'] = order['goodsCnt'] 
        #subOrderById['goodsPrice'] = order['goodsPrice'] 
        subOrderById['goodsNo'] = order['goodsNo'] 
        if order['id'] in orderById.keys():
            orderById[order['id']].append(subOrderById)
        else:
            orderById[order['id']] = [subOrderById]
        #if len(orderById) >= 200:
        #    break
            
    print(len(orderById))
    #print((orderById))
    
    #for userId in orderById.keys():
    #    print(userId, orderById[userId])

    clusters = {}
    clusters[0] = '16295'
    clusters[1] = '20274'
    clusters[2] = '23370'
    clusters[3] = '27562'
    clusters[4] = '1524'
    clusters[5] = '4017'
    clusters[6] = '1890'
    clusters[7] = '32164'
    clusters[8] = '1960'
    clusters[9] = '4926'
    clusters[10] = '27625'
    clusters[11] = '25143'
    clusters[12] = '31320'
    clusters[13] = '1356'
    clusters[14] = '5025'
    clusters[15] = '14446'
    clusters[16] = '17951'
    clusters[17] = '4326'
    clusters[18] = '3889'
    clusters[19] = '17884'
    clusters[20] = '29545'
    clusters[21] = '17543'
    clusters[22] = '31554'
    clusters[23] = '4834'
    clusters[24] = '10618'
    clusters[25] = '3838'
    clusters[26] = '22907'
    clusters[27] = '32340'
    clusters[28] = '28362'
    clusters[29] = '3818'
    clusters[30] = '14249'
    clusters[31] = '11332'

    #print(orderById.keys())
    for key in orderById.keys():
        print(key)
        min = 9999
        clusterNo = 32
        
        simURL = 'http://127.0.0.1:3001/api/godomall/similarity/goodsno'
        #print(orderById[key])
        xList = orderById[key]
        
        for idx in clusters:
            #print(clusters[idx], orderById[clusters[idx]])
            #print(clusters[idx])
            yList = orderById[clusters[idx]]
            #print(yList)

            sum = 0
            avg = 0

            for productX in xList:
                for productY in yList:
                    jsonObj = {}
                    jsonObj['goodsNoX'] = productX['goodsNo']
                    jsonObj['goodsNoY'] = productY['goodsNo']
                    #print(simURL, jsonObj)
                    similarityObj = getSimilarity(simURL, jsonObj)
                    if similarityObj:
                        sum += int(similarityObj['similarity'])

            avg = sum / (len(xList) * len(yList))
            #print(idx, avg)
            if avg < min:
                min = avg
                clusterNo = idx
        dbURL = 'http://127.0.0.1:3001/api/godomall/cluster/user'
        jsonObj = {}
        jsonObj['user'] = key
        jsonObj['clusterNo'] = clusterNo
        jsonObj['distance'] = min
        post_request(dbURL, jsonObj)
        print('user: ', key, ' clusterNo: ', clusterNo, ' distance :', min)
    #print(clusters[13])
    """
    for userIdX in orderById.keys():
        #print(userIdX, orderById[userIdX])
        
        userSimilarityTable = {}
        xList = orderById[userIdX]
        #print('x: ' + str(xList))
        #print('x: ' + str(xList), len(xList))
        for userIdY in orderById:
            
            yList = orderById[userIdY]
            #print('y:' + str(yList))
            #print('y: ' + str(yList), len(yList))
            sum = 0
            num = len(xList) * len(yList)
            simURL = 'http://127.0.0.1:3001/api/godomall/similarity/goodsno'
            for productX in xList:
                for productY in yList:
                    #print('-------------')
                    #print(productX, productY)
                    jsonObj = {}
                    jsonObj['goodsNoX'] = productX['goodsNo']
                    jsonObj['goodsNoY'] = productY['goodsNo']
                    #print(simURL, jsonObj)
                    similarityObj = getSimilarity(simURL, jsonObj)
                    #print(similarityObj)
                    #print(similarityObj['similarity'])
                    if similarityObj:
                        sum += int(similarityObj['similarity'])
                        #print(similarityObj['similarity'], sum)
            avg = sum / num
            #print(sum, avg)
            #print('-------------')
            
            userSimObj = {}
            userSimObj['userX'] = userIdX
            userSimObj['userY'] = userIdY
            userSimObj['similarity'] = avg
            userSimURL = 'http://127.0.0.1:3001/api/godomall/similarity/user'
            ret = post_request(userSimURL, userSimObj)
            print(userIdX, userIdY, avg)
        #time.sleep(10)
    """
def godomallOrderRSByProduct():
    dbURL = 'http://127.0.0.1:3001/api/godomall/order'
    orders = getDB(dbURL)

    #print(len(orders))
    orderMap = []
    subOrderMap = {}
    for order in orders:
        subOrderMap = {}
        if order['memNo'] != '0':
            subOrderMap['id'] = order['memNo']
        elif order['orderEmail'] != '':
            subOrderMap['id'] = order['orderEmail']
        else:
            subOrderMap['id'] = order['orderIp']
        subOrderMap['goodsNm'] = order['goodsNm']
        subOrderMap['orderDate'] = order['orderDate']
        subOrderMap['goodsCnt'] = order['goodsCnt']
        subOrderMap['goodsPrice'] = order['goodsPrice']
        subOrderMap['goodsNo'] = order['goodsNo']
        orderMap.append(subOrderMap)

    #print(orderMap)
    
    orderByProduct = {}
    for order in orderMap:
        #print(order)
        subOrderByProduct = {}
        subOrderByProduct['goodsNm'] = order['goodsNm'] 
        subOrderByProduct['orderDate'] = order['orderDate'] 
        subOrderByProduct['goodsCnt'] = order['goodsCnt'] 
        subOrderByProduct['goodsPrice'] = order['goodsPrice'] 
        subOrderByProduct['id'] = order['id'] 
        if order['goodsNo'] in orderByProduct.keys():
            orderByProduct[order['goodsNo']].append(subOrderByProduct)
        else:
            orderByProduct[order['goodsNo']] = [subOrderByProduct]
            
    #print(orderByProduct)
    for order in orderByProduct.keys():
        #print(orderByProduct[order])
        print(order)

if __name__ == '__main__':
    print('starting')
    if len(sys.argv) > 1 and sys.argv[1] == "pSearch":
        print("product search")
        godomallPSearch()

    if len(sys.argv) > 1 and sys.argv[1] == "oSearch":
        print("order search")
        godomallOSearch()

    if len(sys.argv) > 1 and sys.argv[1] == "oRecommendId":
        print("order recommend")
        godomallOrderRSById()

    if len(sys.argv) > 1 and sys.argv[1] == "oRecommendProduct":
        print("Product recommend")
        godomallOrderRSByProduct()

    if len(sys.argv) > 1 and sys.argv[1] == "productTree":
        print("product tree")
        godomallProductTree()

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        print("order search")
        godomallTest()