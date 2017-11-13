from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        # 隐式等待
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 杜金龙听说有一个很酷的在线待办事项应用
        # 我去看了这个应用的首页
        self.browser.get("http://localhost:8000")

        # 我注意到网页的标题和头部都包含“To-Do”这个词
        assert 'To-Do' in self.browser.title,"Browser title was " + self.browser.title
        self.fail('finish the test!')

        # 应用邀请我输入一个待办事项

        # 我在文本框中输入了“buy peacock feathers”(购买孔雀羽毛)
        # 我的爱好是使用假蝇做児钓鱼

        # 我按回车后，页面更新了
        # 待办事项表格中显示了“1：Buy peacock feathers”

        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 我输入“Use peacock feathers to make a fly”
        # 我做事很有条理

        # 页面再次刷新，我的清单中显示了这两个待办事项

        # 我想知道这个网站是否会记住我的待办清单
        # 我看到网站为我生成了一个唯一的URL
        # 而且页面中有一些文字解说这个功能

        # 我访问那个URL，发现我的待办事项列表还在

        # 我很满意，去睡觉了

#assert 'Django' in browser.title

if __name__ == "__main__":
    unittest.main(warnings='ignore')
