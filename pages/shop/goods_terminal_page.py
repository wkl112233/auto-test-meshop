import time

import allure
from selenium.webdriver.common.keys import Keys

from pages.pagebase import PageBase
import pages


class PageGoodsInfoMinix:
    """
    商品终端页
    """

    def goods_info(self):
        if not getattr(self, '_goods_info', None):
            self._goods_info = PageGoodsInfo(self.driver)
        return self._goods_info


class PageGoodsInfo(PageBase):
    @allure.step("操作:点击加入购车按钮")
    def click_add_cart(self):
        """点击加入购车"""
        element = self.find_element_func(pages.shop.add_cart)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.click(pages.shop.add_cart)

    @allure.step("操作:点击立即购买按钮")
    def click_buy_now(self):
        """点击立即购买"""
        # element = self.find_element_func(pages.shop.buy_now)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # time.sleep(3)
        self.click(pages.shop.buy_now)

    @allure.step("操作:点击必选区颜色")
    def click_color_button(self):
        """点击必选区颜色"""
        self.driver.execute_script("$('div[data-key=\"Farbe\"]>button[aria-expanded=\"false\"]').click()")

    @allure.step("操作:切换颜色")
    def click_switch_colors_button(self):
        """点击切换选择颜色按钮"""
        self.click(pages.shop.switch_colors_but)

    @allure.step("操作:选择颜色")
    def click_sure_goods_color(self):
        """点击确定选择颜色按钮"""
        self.click(pages.shop.sure_goods_color)

    def select_goods_length(self, index, text):
        """选择数据线长度"""
        with allure.step("操作:选择必选区的数据线长度"):
            allure.attach('{}'.format(text), name="选择 {}".format(text))
        self.base_sku_select_goods_ul(table_index=index, click_text=text)

    def select_goods_type(self, e_index, k_text):
        """选择机型"""
        with allure.step("操作:选择必选区的手机机型"):
            allure.attach('{}'.format(k_text), name="选择 {}".format(k_text))
        self.base_sku_select_goods_ul(table_index=e_index, click_text=k_text)

    @allure.step("操作:增加商品数量")
    def click_add_goods(self):
        """加商品数量"""
        self.click_find_element(pages.shop.add_goods_plus)

    @allure.step("操作:减少商品数量")
    def click_minus_goods(self):
        """减商品数量"""
        self.click_find_element(pages.shop.minus_goods)

    def input_goods_count(self, count):
        """输入商品数量"""
        with allure.step("操作:清除商品数量输入框内容后进行输入指定数量"):
            allure.attach('{}'.format(count), name="输入 {}".format(count))
        element = self.find_element_func(pages.shop.input_goods)
        self.click_find_element(pages.shop.input_goods)
        time.sleep(2)
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.BACK_SPACE)
        time.sleep(2)
        element.send_keys(count)

    @allure.step("操作:增加MINI购物车商品数量")
    def click_mini_add_goods_plus(self):
        """加MINI商品数量"""
        self.click_find_element(pages.shop.mini_add_goods_plus)

    @allure.step("操作:减少MINI购物车商品数量")
    def click_mini_minus_goods(self):
        """减MINI商品数量"""
        self.click_find_element(pages.shop.mini_minus_goods)

    def input_mini_input_goods(self, count):
        """输入MINI商品数量"""
        with allure.step("操作步骤:清除MINI购物车商品数量，输入指定商品数量"):
            allure.attach('{}'.format(count), name="输入 {}".format(count))
        element = self.find_element_func(pages.shop.mini_input_goods)
        self.click_find_element(pages.shop.mini_input_goods)
        time.sleep(2)
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.BACK_SPACE)
        time.sleep(2)
        element.send_keys(count)

    def select_goods_sku(self, e_index, k_text):
        """组合业务方法（商品必选区选择）"""
        self.logger.info("正在调用选择商品必选区选择业务方法，机型名称：{} 选择的机型: {} ".
                         format(e_index, k_text))
        self.click_color_button()
        time.sleep(3)
        self.click_switch_colors_button()
        time.sleep(2)
        self.click_sure_goods_color()
        time.sleep(2)
        # self.select_goods_length(index, text)
        # time.sleep(2)
        self.select_goods_type(e_index, k_text)

    def select_goods_cart_buy(self, e_index, k_text):
        """组合业务，商品加入购物车"""
        self.logger.info("正在调用选择商品加入购物车业务方法，机型名称：{} 选择的机型: {} ".
                         format(e_index, k_text))
        self.click_color_button()
        time.sleep(3)
        self.click_switch_colors_button()
        time.sleep(2)
        self.click_switch_colors_button()
        time.sleep(2)
        self.click_sure_goods_color()
        time.sleep(2)
        # self.select_goods_length(index, text)
        # time.sleep(2)
        self.select_goods_type(e_index, k_text)
        time.sleep(1)
        self.click_add_cart()

    def select_test_goods_cart_buy(self, index, text, e_index, k_text):
        """组合业务，测试商品加入购物车"""
        self.logger.info("正在调用选择商品加入购物车业务方法，机型接口：{} 数据线长度：{} 机型名称：{} 选择的机型: {} ".
                         format(index, text, e_index, k_text))
        self.click_color_button()
        time.sleep(3)
        self.click_switch_colors_button()
        time.sleep(2)
        self.click_switch_colors_button()
        time.sleep(2)
        self.click_sure_goods_color()
        time.sleep(2)
        self.select_goods_length(index, text)
        time.sleep(2)
        self.select_goods_type(e_index, k_text)
        time.sleep(1)
        self.click_add_cart()

    def select_goods_buy_now(self, e_index, k_text):
        """组合业务，商品立即购买去地址页"""
        self.logger.info("正在调用选择商品立即购买业务方法，机型名称：{} 选择的机型: {} ".
                         format(e_index, k_text))
        self.click_color_button()
        time.sleep(3)
        self.click_switch_colors_button()
        time.sleep(2)
        self.click_switch_colors_button()
        time.sleep(2)
        self.click_sure_goods_color()
        time.sleep(2)
        # self.select_goods_length(index, text)
        # time.sleep(2)
        self.select_goods_type(e_index, k_text)
        time.sleep(2)
        self.click_buy_now()
        time.sleep(3)

    def select_test_goods_buy_now(self, index, text, e_index, k_text):
        """组合业务，测试商品立即购买去地址页"""
        self.logger.info("正在调用选择商品加入购物车业务方法，机型接口：{} 数据线长度：{} 机型名称：{} 选择的机型: {} ".
                         format(index, text, e_index, k_text))
        self.click_color_button()
        time.sleep(3)
        self.click_switch_colors_button()
        time.sleep(2)
        self.click_switch_colors_button()
        time.sleep(2)
        self.click_sure_goods_color()
        time.sleep(2)
        self.select_goods_length(index, text)
        time.sleep(2)
        self.select_goods_type(e_index, k_text)
        time.sleep(1)
        self.click_buy_now()
        time.sleep(3)
