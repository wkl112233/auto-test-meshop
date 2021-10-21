# _*_ coding: utf-8 _*_
import logging
from telnetlib import EC
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class PageBase:
    """
    初始化 -> 解决driver
    """

    def __init__(self, driver):
        self.logger = logging.getLogger(type(self).__name__)
        self.driver = driver

    def find_element_func(self, location, timeout=30, poll=.5):
        """
        元素定位方法
        :param location: 定位信息
        :param timeout: 超时时长
        :param poll: 方法执行间隔
        :return: 元素对象
        """
        self.logger.info("正在查找：{}元素，访问频率：{} 超时时间：{}".format(location, poll, timeout))
        element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll). \
            until(lambda x: x.find_element(location[0], location[1]))
        return element

    def click(self, location):
        """元素点击方法"""
        self.logger.info("正在准备对：{}元素执行点击操作".format(location))
        element = self.find_element_func(location)  # 定位目标元素
        element.click()  # 调用点击方法
        self.logger.info("对：{}元素执行点击操作完成".format(location))

    def input(self, location, text):
        """元素输入方法"""
        element = self.find_element_func(location)  # 定位目标元素
        self.logger.info("正在准备对：{}元素执行清空操作".format(location))
        element.clear()  # 调用清空方法
        self.logger.info("对：{}元素执行清空操作完成！".format(location))
        self.logger.info("正在准备对：{}元素执行输入：{} 操作".format(location, text))
        element.send_keys(text)  # 调用输入方法
        self.logger.info("对：{}元素执行输入：{} 操作完成！".format(location, text))

    def use_js(self, js):
        """调用js"""
        self.logger.info("准备执行{} 脚本！".format(js))
        self.driver.execute_script(js)
        self.logger.info("执行{} 脚本完成！".format(js))

    def dismiss_alert(self):
        """弹窗 alert——取消"""
        self.driver.switch_to.alert.dismiss()

    def is_alert(self):
        """弹出判断"""
        try:
            result = WebDriverWait(self.driver, timeout=5, poll_frequency=.5).until(EC.alert_is_present())
            return result
        except:
            return False

    def move_to_loc(self, loc):
        """鼠标移到元素上"""
        try:
            element = self.find_element_func(loc)
            self.logger.info("正在准备移动到{}元素".format(loc))
            ActionChains(self.driver).move_to_element(element).perform()
            self.logger.info("移动到{}元素完成".format(loc))
        except Exception as e:
            self.logger.info("Failed to move_to_loc the element with %s" % e)
            raise

    def scorll_to_loc_by_js(self, loc):
        """滚动条定位到元素上"""
        self.driver.execute_script("arguments[0].scrollIntoView();", loc)

        # def stop_loading(self):
        """停止加载"""
        # win32api.keybd_event(27, 0, 0, 0)
        # win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)
        return

    def text(self, location):
        """
        :param location: 为列表或元祖
        :return: 元素的文本值
        """
        text = self.find_element_func(location).text
        self.logger.info("正在对:{}元素获取文本操作, 获取的文本值：{}".format(location, text))
        return text

    def base_sku_select_goods_ul(self, click_text, table_index):
        """下拉框定位方法"""
        # 1. 定位input 注意：{}需要在单引号中
        location = By.CSS_SELECTOR, "button[table-index='{}']".format(table_index)
        self.logger.info("正在准备点击：{} 元素！".format(location))
        self.click(location)
        self.logger.info("{} 元素，执行点击完毕！".format(location))
        # 2. 暂停1秒
        time.sleep(1)
        # 3. 定位具体文本
        text_loc = By.CSS_SELECTOR, "[data-value='{}']".format(click_text)
        self.logger.info("正在准备点击：{} 元素！".format(text_loc))
        time.sleep(2)
        self.click(text_loc)
        self.logger.info("{} 元素，执行点击完毕！".format(text_loc))

    def base_if_text_exists_element(self, text):
        """判断当前页面是否包含指定字符串元素"""
        # 组合文本元素定位信息
        loc = By.XPATH, "//*[text()='{}']".format(text)
        try:
            self.logger.info("正在准备查找：{}元素".format(loc))
            # 查找元素 查找时间为5秒内，等待30秒
            self.find_element_func(loc, timeout=5)
            self.logger.info("找到包含:{}文本的元素啦！".format(text))
            print("找到包含:{}文本的元素啦！".format(text))
            # 返回True  代表存在
            return True
        except:
            print("没有找到，包含：{}文本的元素！".format(text))
            self.logger.info("没有找到，包含：{}文本的元素！".format(text))
            # 返回False 代表不存在
            return False

    def base_if_exists_element(self, ele_id):
        """判断当前页面是否包含指定元素"""
        # 组合ID元素定位信息
        loc = By.CSS_SELECTOR, "#{}".format(ele_id)
        try:
            self.logger.info("正在准备查找：{}元素".format(loc))
            # 查找元素 查找时间为5秒内，等待30秒
            self.find_element_func(loc, timeout=5)
            self.logger.info("找到id包含:{}的元素啦！".format(ele_id))
            print("找到id包含:{}的元素啦！".format(ele_id))
            # 返回True  代表存在
            return True
        except:
            print("没有找到，id包含：{}的元素！".format(ele_id))
            self.logger.info("没有找到，id包含：{}文本的元素！".format(ele_id))
            # 返回False 代表不存在
            return False

    def base_if_text_down_element(self, text):
        """判断当前页面是否包含指定下架字符串元素"""
        # 组合文本元素定位信息
        loc = By.XPATH, '//span[@class="el-tag el-tag--info el-tag--light"][text()="{}"]'.format(text)
        try:
            self.logger.info("正在准备查找：{}元素".format(loc))
            # 查找元素 查找时间为5秒内，等待30秒
            self.find_element_func(loc, timeout=5)
            self.logger.info("找到包含:{}文本的元素啦！".format(text))
            print("找到包含:{}文本的元素啦！".format(text))
            # 返回True  代表存在
            return True
        except:
            print("没有找到，包含：{}文本的元素！".format(text))
            self.logger.info("没有找到，包含：{}文本的元素！".format(text))
            # 返回False 代表不存在
            return False

    def click_red_find_element(self, loc):
        """红框定位点击"""
        element = self.find_element_func(loc)
        self.logger.info("红框标注查找的：{}元素".format(loc))
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 2px solid red;")
        time.sleep(2)
        self.logger.info("正在移动到查找的：{}元素".format(loc))
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
        self.logger.info("正在准备点击：{}元素".format(loc))
        element.click()
        self.logger.info("{} 元素，执行点击完毕！".format(loc))

    def click_find_element(self, loc):
        element = self.find_element_func(loc)
        self.logger.info("正在移动到查找的：{}元素".format(loc))
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
        self.logger.info("正在准备点击：{}元素".format(loc))
        element.click()
        self.logger.info("{} 元素，执行点击完毕！".format(loc))
