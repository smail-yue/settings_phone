from Base.Base import Base
import Page

class Page_seach(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    #搜索开始
    def start_search(self):
        #点击搜索按钮
        self.click_element(Page.sea_button)

    #输入搜索内容
    def input_search(self,text):
        self.input_element(Page.sea_input,text)

    #返回按钮
    def stop_search(self):
        self.click_element(Page.ret_button)