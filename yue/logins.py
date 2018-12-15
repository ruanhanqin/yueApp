#!/usr/bin/env python
# -*-encoding: utf-8-*-


import requests
from json import loads
import time

g_headers = None
g_token = None
login_ip = '117.136.79.45,192.168.43.27'


class Login():
    def __init__(self, session):
        """
        init headers,
        :param session:
        """
        self.headers = {
            'User-Agent': 'YueHuaYueYou/2.1.16 (iPhone; iOS 9.3.2; Scale/2.00)',
            'Host': 'api.yuepingtai.com'
        }
        global g_headers
        g_headers = self.headers
        self.session = session

    def get_temp_token(self):
        """
        get temp token
        :return: temp token
        """
        temp_token_url = 'https://api.yuepingtai.com/usr/v1/u/getTempToken'
        get_temp_token_data = {
            'clientVersionCode': '2.1.16',
            'deviceId': '9E7C722B-4265-4AE0-9C56-9E3B3371B953',
            'deviceType': 'iPhone 6s',
            'loginIp': login_ip,
            'sysfrom': 'ios'
        }
        response = self.session.post(temp_token_url, data=get_temp_token_data, headers=self.headers)
        if response.status_code == 200:
            return loads(response.text)['data']

    def login(self):
        """
        login
        :return: None
        """
        login_url = 'https://api.yuepingtai.com/usr/v1/u/login'
        login_data = {
            'cipher': 'b0eacde6d8f7d45eb9aa84540777670b',
            'clientVersionCode': '2.1.16',
            'deviceId': '9E7C722B-4265-4AE0-9C56-9E3B3371B953',
            'deviceType': 'iPhone 6s',
            'loginIp': login_ip,
            'mobile': '13640842074',
            'sysfrom': 'ios',
            'tempToken': self.get_temp_token()
        }
        response = self.session.post(login_url, data=login_data, headers=self.headers)
        if response.status_code == 200:
            global g_token
            g_token = loads(response.text)['data']['token']

    def update_lonlat(self, lng, lat):
        """
        更新经纬度位置信息
        update longitude,latitude
        :return: None
        """
        update_url = 'https://api.yuepingtai.com/usr/v1/u/updateLonLat'
        update_data = {
            'clientVersionCode': '2.1.16',
            'deviceId': '9E7C722B-4265-4AE0-9C56-9E3B3371B953',
            'deviceType': 'iPhone 6s',
            'lat': lat,
            'lng': lng,
            'loginIp': login_ip,
            'sysfrom': 'ios',
            'token': g_token
        }
        response = self.session.post(update_url, data=update_data, headers=self.headers)
        if response.status_code == 200:
            pass
            print('updateLonLat success! ')
        else:
            print('updateLonLat failed! ')
            pass
