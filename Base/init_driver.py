from appium import webdriver
def init_driver():
    # 需要先开启appnium服务
    desired_caps = {}
    # 设备信息
    # 系统
    desired_caps['platformName'] = 'Android'
    # 版本
    desired_caps['platformVersion'] = '5.1'
    # 设备号
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app信息
    # 包名
    desired_caps['appPackage'] = 'com.android.settings'
    # 启动名
    desired_caps['appActivity'] = '.Settings'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver