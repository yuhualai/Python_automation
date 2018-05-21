#encoding:utf-8

import argparse
import fmovice.movice as MV

def Search_Movice(keyword):
    wrong_return = u'暂未找到 [%s] 相关的百度云资源，回复电影名称的关键词试试。\n\n比如想看电影一个叫欧维的男人决定去死，可以回复关键词 [欧维] 或者 [一个叫] 等等。'%keyword

    try:
        result_list = MV.search_movice(keyword.encode('utf-8'))
        if result_list:
            return u'搜索电影[%s]的百度云资源如下:\n\n'%keyword + '\n\n'.join(result_list)
        else:
            return wrong_return
    except:
        return wrong_return

def main():
    temp,keyword = argparse.ArgumentParser().parse_known_args()

    if keyword:
        if len(keyword) >= 2:
            print('仅支持单参数查询，将自动忽略第一个以后的参数')
        print(Search_Movice(keyword[0]))
    else:
        print('请输入关键词查询！')