# -*- coding: utf-8 -*-
# @Author: Kid
# @FileName: addmember_page.py
# @Date: 2021/10/24  11:52


from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Web_iSelenium_Windows.test.base_page import BasePage


class AddMemberPage(BasePage):   # 继承前没有括号
    # 这里 的 init 也放到 BasePage， 也删掉， 同样继承 BasePage
    # def __init__(self, driver:WebDriver):
    #     self.driver = driver
    ###
    def add_member(self, username, account, phonenum):

        '''
        添加联系人，详细信息
        :return:
        '''

        #  改造 find  方法， 已封装， 上面的注释掉

        self.find(By.ID, "username").send_keys(username)
        # 输入  账号
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        # 输入   手机号
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        # 点击 保存, 当页面上 有相同属性的元素有 多个时， 通过 find_elements  找到的 是第一个元素
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()  # 还是遗漏了 点 '.'
        return True

        #  验证保存是否成功的
    def get_member(self):
        '''
        获取所有的联系人姓名
        :return:
        '''

        # 显示等待已封装, 下面进行改造
        locator = (By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")
        self.wait_for_click(10, locator)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")))
        # 上面WebDriverWait的显示等待里面的复选框（并没有点击）是为了验证 是否正确进入了“通讯录“这个页面，即：找到了复选框就证明了正确进入了 需要的 通讯录 页面，也可以找其他元素，比如姓名，来验证

        #  改造， 这里是 finds  方法，别写错 find
        # find_elements 查找 页面上相同属性的所有元素。[element1, element2....]
        # eles_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")  # 理解已截图，所以这一步得到是一个兄弟节点集合，也就是姓名列表，所以需要从列表中遍历并追加条件如 title选出自己要的姓名
        eles_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        print(eles_list)
        # 用 eles_list去接收 上面搜索定位到的 节点集合
        names = []   # 将下面遍历 eles_list 拿到的元素保存在names这里，  将集合的所有names 组成一个列表（----通过 遍历的 ele.追加属性拿到的就是一个列表）
        for ele in eles_list:    # 遍历集合里面的一个个 元素 （要的names）
            names.append(ele.get_attribute("title"))     #  追加属性值为title，title 是谷歌里面定位的元素class-id里面有对应的用户名就是 title，每个 遍历到的 元素需要title 符合自己 上面传入的其中一个参数，如 aaa_01

        return names    # 最后返回的是 names ，测试用例 那里 需要判断的是 用户名 如 aaa_01 是否在names里面

