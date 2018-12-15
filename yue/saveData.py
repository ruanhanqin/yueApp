#!/usr/bin/env python
# -*-encoding: utf-8-*-
# @file: saveData.py
# @time: 2018/6/13 11:09
# @author:ruan
# @email:990687261@qq.com

import xlwt


class SaveData():
    def __init__(self, filename):
        self.filename = filename
        self.excel = None
        self.sheet = None

    def init(self):
        self.excel = xlwt.Workbook(encoding='utf-8', style_compression=0)
        self.sheet = self.excel.add_sheet('sellerMessage', cell_overwrite_ok=True)
        tb_head = ['userName', 'Tel', 'shopName', 'Address']  # 表头信息
        for i, item in enumerate(tb_head):
            self.sheet.write(0, i, item)  # 写入表头信息

    def save_to_file(self, shop_list):
        count = 1
        table = self.excel.get_sheet(0)
        for item in shop_list:
            for i, j in enumerate(item):
                table.write(count, i, item[j])  # 写入数据 count:行，i：列，item[j] 数据
            count += 1  # 下一行
        self.excel.save(self.filename)  # 保存文件
        print('写入文件成功',self.filename)