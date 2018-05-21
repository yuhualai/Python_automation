#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'hualai yu'

import xlrd


class OpertionExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '/Users/yuhualai/Desktop/shert.xlsx'
            self.sheet_id = 0

    # self.data = self.get_data()

    # 获取内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_line(self):
        return self.get_data().nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, row, col):
        return self.get_data().cell_value(row, col)


if __name__ == '__main__':
    opers = OpertionExcel()
    print(opers.get_line())
    print(opers.get_cell_value(4, 2))
