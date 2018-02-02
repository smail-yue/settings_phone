import  sys,os,allure
sys.path.append(os.getcwd())
from Base.read_data import  ret_yaml_data
from Base.init_driver import init_driver
import pytest
from Page.Page import Page
# 导入数据
def package_param_data():
    list_data=[]
    yaml_data=ret_yaml_data("search_data").get("Search_data")
    print("<<<<<<<<<<<<<<<<<<<<<<<<",yaml_data)
    for i in yaml_data:
        list_data.append((i,yaml_data.get(i).get("input_text"),yaml_data.get(i).get("expect_data")))
        print(yaml_data.get(i).get("input_text"))
    return list_data

class Test_search(object):
    def setup_class(self):
        self.driver=init_driver()
        self.search_obj=Page(self.driver).Page_obj()
        # 点击搜索按钮
        self.search_obj.start_search()
    def teardown_class(self):
        # 点击返回按钮
        self.search_obj.stop_search()
        #结束搜索
        self.driver.quit()

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="我是001")
    @pytest.mark.parametrize('test_id,input_text,expect_data',package_param_data())
    def test_2case(self,test_id,input_text,expect_data):
        allure.attach("描述","我在001里面")
        print("test_id",test_id)
        #输入测试用例
        self.search_obj.input_search(input_text)
        self.driver.get_screenshot_as_file("./screenshot/%s.png" %test_id)
        assert expect_data==456


