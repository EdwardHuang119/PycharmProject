# -*- coding: utf-8 -*-
import tushare as ts
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas
# 读取Tushare的版本
# vs = ts.__version__
# print(vs)


# 获取个股历史交易数据：get_k_data
BasicData = ts.get_stock_basics()
# F=BasicData.ix['601398']
# print(F)
timeToMarket_spr = str(BasicData.ix['601398']['timeToMarket'])
print(timeToMarket_spr)
# # 被折磨太久了，获取了日期之后因为是一个byte类型的所以在strptime中无法读取，然后所以最终还是用了STR函数转变成了字符。python3是没有decode的。
# timeToMarket_spr_type = type(timeToMarket_spr)
# print(timeToMarket_spr_type)
# timeToMarket_real = time.strptime(timeToMarket_spr,'%Y%m%d')
# print(timeToMarket_real)
# FristDate = time.strftime('%Y-%m-%d',timeToMarket_real)
# # 如上是拆解如下的函数的过程，涉及到返回8为日期字符转换为真正可用日期格式的方法
FristDate = time.strftime('%Y-%m-%d',time.strptime(timeToMarket_spr,'%Y%m%d'))
Today = time.strftime('%Y-%m-%d',time.localtime())
# # 1、尝试使用get_k_data
# print(FristDate,Tod
# df1 = ts.get_k_data('601398', ktype='d', start=FristDate, end=Today)
# # df1 = ts.get_k_data('601398',ktype='m')
# # df1=ts.get_k_data('600848', ktype='W') #获取周k线数据
# # df1=ts.get_k_data('600848', ktype='M') #获取月k线数据
# # df1=ts.get_k_data('600848', ktype='5') #获取5分钟k线数据
# # df1=ts.get_k_data('600848', ktype='15') #获取15分钟k线数据
# # df1=ts.get_k_data('600848', ktype='30') #获取30分钟k线数据
# # df1=ts.get_k_data('600848', ktype='60') #获取60分钟k线数据
# print(df1)
# df1.to_excel(r'G:\Stock_Date\Test\Ex_get_k_date.xlsx')

# # 1.5学习开图，展现获取的信息的图形展示
# # 开启一个双图例的窗口，定义为211和212
# plt.figure('走势图', figsize=(12, 8), dpi=80)
# ax1 = plt.subplot(211)
# ax2 = plt.subplot(212)
# # ax1（211窗口）显示最高价和最低价曲线
# plt.sca(ax1)
# # 显示网格：grid='on'
# df1.close.plot(color='black', grid='on')
# # df1.high.plot(color='red', grid='on')
# # df1.low.plot(color='blue', grid='on')
# # ax2（212窗口）显示成交量曲线
# plt.sca(ax2)
# df1.volume.plot(color='orange', grid='on')
# plt.show()

# # 2、尝试使用get_hist_date
# df1h = ts.get_hist_data('601398', ktype='d', start=FristDate, end=Today)
# df1h.to_excel(r'G:\Stock_Date\Test\Ex_get_hist_date.xlsx')
# df1h=ts.get_hist_data('600848', ktype='W') #获取周k线数据
# df1h=ts.get_hist_data('600848', ktype='M') #获取月k线数据
# df1h=ts.get_hist_data('600848', ktype='5') #获取5分钟k线数据
# df1h=ts.get_hist_data('600848', ktype='15') #获取15分钟k线数据
# df1h=ts.get_hist_data('600848', ktype='30') #获取30分钟k线数据
# df1h=ts.get_hist_data('600848', ktype='60') #获取60分钟k线数据
# df1h=ts.get_hist_data('sh')#获取上证指数k线数据，其它参数与个股一致，下同
# df1h = ts.get_hist_data('sz')#获取深圳成指k线数据
# df1h=ts.get_hist_data('hs300')#获取沪深300指数k线数据
# df1h=ts.get_hist_data('sz50')#获取上证50指数k线数据
# df1h=ts.get_hist_data('zxb')#获取中小板指数k线数据
# df1h=ts.get_hist_data('cyb')#获取创业板指数k线数据
# print(df1h)
# # 获取历史复权数据：get_stock_basics
df2 = ts.get_stock_basics()
# print(df2)
df2.to_excel(r'G:\Stock_Date\Test\Ex_get_stock_basics.xlsx')
# # 公开上市首日：timeToMarket
# fd = df2.ix['600167']['timeToMarket']
# print(fd)
#
# # 获取个股以往交易历史的分笔数据明细
# df3 = ts.get_tick_data('600167', date='2017-05-04')
# # 显示最近的30笔交易数据
# print(df3.head(30))

# # 获取大单交易数据，默认为大于等于400手，数据来源于新浪财经：get_sina_dd
# df4 = ts.get_sina_dd('601398', date='2018-05-31', vol=500)
# # print(df4)

# # 开启一个双图例的窗口，定义为211和212
# plt.figure(2, figsize=(12, 8), dpi=80)
# # ax1 = plt.subplot(211)
# # ax2 = plt.subplot(212)
# # # ax1（211窗口）显示最高价和最低价曲线
# # plt.sca(ax1)
# # # 显示网格：grid='on'
# # df1.high.plot(color='red', grid='on')
# # df1.low.plot(color='blue', grid='on')
# #
# # # ax2（212窗口）显示成交量曲线
# # plt.sca(ax2)
# # df1.volume.plot(color='orange', grid='on')
# # plt.show()


