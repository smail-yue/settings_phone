from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    def __init__(self,driver):
        self.driver=driver

    # 定位页面元素
    def wait(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))

    #点击元素
    def click_element(self,loc):
        self.wait(loc).click()

    #点击输入按钮
    def input_element(self,loc,text):
        self.wait(loc).send_keys(text)