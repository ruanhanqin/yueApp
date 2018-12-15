#!/usr/bin/env python
# -*-encoding: utf-8-*-


from yue import logins
from yue import processData
from yue import saveData
from yue import readExcel
import requests
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtWidgets
from yue.yueui import *

'''
lng:116.323066
lat:39.989956
'''
lng = ''
lat = ''


class Ui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)

    def crawl(self):
        self.messagelabel.setText("开始获取数据.....")
        print('读取经纬度excel表数据')
        read_excel = readExcel.ReadExcel()
        global lng_lat
        global shop_list
        global lng  # 经纬度
        global lat
        lng_lat = read_excel.read_excel()
        lng = self.longitudelineEdit.text()
        lat = self.laditudelineEdit.text()

        if lng_lat is None:  # 如果没有经纬度表时，读取输入框的经纬度
            lng0 = str(lng)
            lat0 = str(lat)
            s = lng0 + ',' + lat0
            lng_lat = [s, ]

        session = requests.Session()
        login = logins.Login(session=session)
        login.login()

        for item in lng_lat:
            shop_list = []
            lng = item.split(',')[0]
            lat = item.split(',')[1]
            login.update_lonlat(lng, lat)
            print('正在获取数据..........请耐心等待.....')

            print('经度:', lng, '纬度:', lat)
            pro_data = processData.ProcessData(session=session)
            self.messagelabel.setText("数据获取中.....")
            try:
                for i in range(30):
                    response = pro_data.query_solr_merchant_list(lng, lat, page_num=i + 1)
                    sl = pro_data.parser_solr_merchant_list(response)
                    shop_list = shop_list + sl
            except Exception as e:
                print(e)
            try:
                filename = item.replace(',', '_') + '.xlsx'
                write = saveData.SaveData(filename)
                write.init()
                write.save_to_file(shop_list)
                print('Write to Excel Success!', '[' + item + ']')
            except Exception as e:
                print(e)
        print('所有数据获取完成......')
        self.messagelabel.setText("数据获取完成写入文件sellerMessage.xlsx...")
        QMessageBox.information(self,
                                "提示",
                                "数据获取完成!",
                                QMessageBox.Yes | QMessageBox.No)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
