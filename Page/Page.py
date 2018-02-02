from Page.seach_setting import Page_seach
class Page(object):
    def __init__(self,driver):
        self.driver=driver
    def Page_obj(self):
        return Page_seach(self.driver)