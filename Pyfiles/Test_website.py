# -*- coding: utf-8 -*-
import webbrowser
# chrome = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
# webbrowser.register('chrome', Chrome('chrome'))
# webbrowser.get('chrome_path').open("www.dangdang.com")
# webbrowser.open("http://weibo.com")

# 在windows下面直接可以固定某个路径，但是unix怎么处理?目前除了默认为chrome为默认浏览器暂时没办法了。
chromePath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'            #  例如我的：C:\***\***\***\***\Google\Chrome\Application\chrome.exe
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))   #这里的'chrome'可以用其它任意名字，如chrome111，这里将想打开的浏览器保存到'chrome'
webbrowser.get('chrome').open('http://weibo.com')

