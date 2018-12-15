#!/usr/bin/env python
# -*-encoding: utf-8-*-


from yue.logins import g_headers, g_token, login_ip
from json import loads, load
import time


class ProcessData():
    def __init__(self, session):
        """
        class init
        :param session:  requests session
        """
        self.session = session
        self.headers = g_headers

    def query_solr_merchant_list(self, lng, lat, page_num):
        """
        query shop list
        :return: shop list message
        """
        query_url = 'https://api.yuepingtai.com/solr/v1/feignSolr/querySolrMerchant'
        query_data = {
            'clientVersionCode': '2.1.16',
            'deviceId': '9E7C722B-4265-4AE0-9C56-9E3B3371B953',
            'deviceType': 'iPhone 6s',
            'latitude': lat,
            'loginIp': login_ip,
            'longitude': lng,
            'pageNum': page_num, # 页码 一页显示10条商家信息
            'pageSize': '10',
            'sortType': '4',
            'sortWay': '2',
            'sysfrom': 'ios',
            'token': g_token
        }
        print('query lnglat',lng,' ',lat)
        response = self.session.post(query_url, data=query_data, headers=self.headers)
        if response.status_code == 200:
            # print(loads(response.text))
            return response.text
        else:
            return None

    def parser_solr_merchant_list(self, response):
        """
        处理商家信息
        parser shop list message
        :param response:
        :return: shop list
        """
        shop_list = []
        if response:
            resJson = loads(response)
            for i in range(10): # 一页10条商家信息
                username = resJson['data']['merchantList'][i]['username']
                tel = self.get_customer_service_tel(username)
                shopname = resJson['data']['merchantList'][i]['shopName']
                address = resJson['data']['merchantList'][i]['address']
                info = dict()
                info['UserName'] = username
                info['Tel'] = tel
                info['ShopName'] = shopname
                info['Address'] = address
                shop_list.append(info)
                time.sleep(0.8)
        return shop_list

    def get_customer_service_tel(self, username):
        """
        根据username 获取商家电话
        get shop phoneNumber
        :param shoplist:  shop list
        :return: shop message dict
        """
        tel_url = 'https://api.yuepingtai.com/usr/v1/storeUser/loadCustomerServiceTel'
        tel_data = {
            'clientVersionCode': '2.1.16',
            'deviceId': '9E7C722B-4265-4AE0-9C56-9E3B3371B953',
            'deviceType': 'iPhone 6s',
            'loginIp': login_ip,
            'sysfrom': 'ios',
            'token': g_token,
            'username': username
        }
        response = self.session.post(tel_url, data=tel_data, headers=self.headers)
        if response.status_code == 200:
            if response.text:
                telJson = loads(response.text)
                try:
                    tel = telJson['data']['tel']
                except Exception as e:
                    tel = None
            else:
                tel = None
        else:
            return None
        return tel

