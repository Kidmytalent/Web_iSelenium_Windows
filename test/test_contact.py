# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: test_contact.py
# @Date: 2021/10/24  11:50


from Web_iSelenium_Windows.test.main_page import MainPage


class TestContact:
    def setup(self):     # setup 用来 从 首页（main_page.py) 开始 往下运行
        self.mainpage = MainPage()

    def test_add_member(self):  # 测试用例 下面 大多是 变量实例化，添加， 传入参数 .......----   pytest 的知识
        username = "aaa_04"
        account = "aaaa_04"
        phonenum = "13011111124"    # 这里 是 test 测试用例 调用前面 AddMemberPage里面的 add_member 方法 进行多次 添加成员操作。
        # 这是执行测试用例，需要给不同的变量资源

        #  这里原本这样写，因为我们既 需要 从 goto_add_member() 去调用 add_member 方法，添加好 成员到 通讯录，又要满足从通讯录 查找确认姓名在里面
        #  但有不能同时在一条 语句调用 add_member 和 get_member 方法， 所以用下面  page, names 分开调用
        # self.mainpage.goto_add_member().add_member()
        # self.mainpage.goto_add_member().get_member()
        pages = self.mainpage.goto_add_member()
        pages.add_member(username,account,phonenum)   # 这里有报错过， 只需一个参数，给了3个，或 4个----犯错的原因， 这里已经不是 把参数给死了，而是 活的----add_member 方法那里没有 添加变量 username, account, phone  --- pytest知识
        names= pages.get_member()   # names 到这里，已经在add_member.py 中的 get_member 做了处理，不做处理，前面得到的names会是一个 包含很多元素且包含很多属性值杂乱的列表
        print(names)                # 所以，如果不知道保存在names 里面的元素 是什么，可以打印一下出来
        assert username in names    # 因为这里要 验证 前面添加成员的名字在 names 里面，所以names 是个 保存着 遍历 eles_list(用兄弟节点定位到的多个元素集合)这个集合的，
        # 而且只是 带 title 的 元素列表，title就是谷歌定位分析上面的用户名名称
