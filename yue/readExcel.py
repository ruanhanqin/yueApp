#!/usr/bin/env python
# -*-encoding: utf-8-*-

"""
读取经纬度文件
"""
import xlrd

"""
读取经纬度excel表
"""


class ReadExcel():
    def __init__(self):
        self.lnglat = []
        self.excel = None
        self.sheet = None

    def init(self):
        self.excel = xlrd.open_workbook(u'./经纬度.xlsx')
        self.sheet = self.excel.sheet_by_index(0)

    def read_excel(self):
        """
        读取经纬度excel表
        :return:
        """
        self.init()
        rows = self.sheet.nrows
        for i in range(rows):
            self.lnglat.append(self.sheet.row_values(i)[0:1][0])
        return self.lnglat