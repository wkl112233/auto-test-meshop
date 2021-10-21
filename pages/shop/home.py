import time

import allure

from pages.pagebase import PageBase
import pages
from selenium.webdriver.common.by import By


class ShopHomePageMinix:
    """
    前台商店主页
    """

    def shop_home(self):
        if not getattr(self, '_shop_home', None):
            self._shop_home = ShopHomePage(self.driver)
        return self._shop_home


class ShopHomePage(PageBase):
    close_popup = pages.shop.coupon_close

    @allure.step("操作:关闭优惠券弹窗")
    def close_coupon_close(self):
        """关闭优惠券弹窗"""
        self.click(self.close_popup)

    def close_close_popup(self):
        self.click_find_element(self.close_popup)

    @allure.step("操作:点击进入个人中心页")
    def click_icon(self):
        """点击个人图标"""
        self.click(pages.shop.icon)

    @allure.step("操作:点击搜索图标进入搜索弹窗页")
    def click_search(self):
        """点击搜索"""
        self.driver.execute_script("$('a[aria-controls=\"Search\"]').click()")

    @allure.step("操作:打开迷你购物车")
    def click_cart(self):
        """点击mini购物车图标"""
        self.click(pages.shop.cart)

    @allure.step("操作:关闭迷你购物车")
    def close_mini_cart(self):
        """关闭迷你购物车"""
        self.driver.execute_script("$('#sidebar-cart>div>button').click()")

    def input_count(self, count):
        """输入搜索内容"""
        with allure.step('搜索弹窗内输入搜索内容'):
            allure.attach('{}'.format(count), name="输入 {}".format(count))
        self.input(pages.shop.search_inp, count)

    @allure.step("操作:点击查看，进入搜索结果页")
    def click_search_result(self):
        """点击查看结果"""
        element = self.find_element_func(pages.shop.search_result)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.click(pages.shop.search_result)

    def get_search_title(self):
        """获取搜索结果的商品标题"""
        return self.text(pages.shop.search_title)

    @allure.step("操作:删除迷你购物车中的商品")
    def click_remove_goods(self):
        """点击 删除迷你购物车商品"""
        self.click(pages.shop.remove_goods_btn)

    @allure.step("操作:点击迷你购物车结算（checkout）按钮，进入地址页")
    def click_mini_checkout(self):
        """点击 迷你购物车结算按钮"""
        element = self.find_element_func(pages.shop.mini_checkout)
        self.driver.execute_script("arguments[0].click();", element)

    def page_get_cart_goods_title(self):
        """获取迷你购物车商品标题"""
        return self.text(pages.shop.goods_title)

    def page_get_goods_spu_count(self):
        """获取迷你购物车商品spu值"""
        return self.text(pages.shop.goods_spu_count)

    def get_goods_name(self):
        """获取查找商品的标题"""
        return self.text(pages.shop.goods_name)

    def get_goods_index(self):
        """获取搜索结果数"""
        return self.text(pages.shop.goods_index)

    @allure.step("操作:点击搜索页中的商品标题，进入商品终端页")
    def click_goods_name(self):
        """点击商品标题"""
        element = self.find_element_func(pages.shop.goods_name)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("操作:点击搜索页中的商品标题，进入商品终端页")
    def click_goods_name_two(self):
        """点击测试商品标题"""
        element = self.find_element_func(pages.shop.iphone_goods_two)
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("操作:点击列表页中的测试商品标题，进入商品终端页")
    def click_test_goods_name_two(self):
        """点击测试商品标题"""
        element = self.find_element_func(pages.shop.iphone_goods_two)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("操作:点击搜索页中的商品标题，进入商品终端页")
    def click_test_goods_name(self):
        """点击测试商品标题"""
        element = self.find_element_func(pages.shop.iphone_goods)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("操作:点击搜索页中的分页'下一页'")
    def click_next_page(self):
        """搜索页点击下一页"""
        element = self.find_element_func((By.CSS_SELECTOR, 'div:nth-child(40)>div>div>div>h3>a'))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.click(pages.shop.next_page)

    @allure.step("操作:点击搜索页中的分页'上一页'")
    def click_prev_page(self):
        """搜索页点击上一页"""
        element = self.find_element_func(pages.shop.prev_page)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.click(pages.shop.prev_page)

    def goto_shop_search_page(self, count):
        """组合业务方法（首页进入搜索页）"""
        self.logger.info("正在调用搜索业务方法，搜索关键词：{}".format(count))
        self.click_search()
        time.sleep(3)
        self.input_count(count)
        time.sleep(3)
        self.click_search_result()
        time.sleep(3)
