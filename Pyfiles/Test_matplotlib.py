# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# fig=plt.figure('成交价',figsize=(16,9),dpi=80)
# plt.show()

plt.figure(1) #调用figure函数创建figure(1)对象,可以省略,这样那plot时,它就自动建一个啦;

t = np.arange(0.0, 2.0, 0.1)
s = np.sin(2*np.pi*t)
plt.plot(t, s, 'r--o', label = 'sinx')

plt.legend()  #显示右上角的那个label,即上面的label = 'sinx'
plt.xlabel('time (s)')    #设置x轴的label，pyplot模块提供了很直接的方法，内部也是调用的上面当然讲述的面向对象的方式来设置；
plt.ylabel('voltage (mV)')   #设置y轴的label;
#plt.xlim(-1,3)      #可以自己设置x轴的坐标的范围哦;
#plt.ylim(-1.5,1.5)   #同上;
plt.title('About as simple as it gets, folks')
plt.grid(True)   #显示网格;

plt.show()   #显示出figure;