from selenium.webdriver.common.by import By
from pages.pagebase import PageBase


class PageOrderManageMinix:
    def order_manage(self):
        if not getattr(self, '_add_product', None):
            self._order_manage = PageOrderManage(self.driver)
        return self._order_manage


"""
订单管理页
"""


class PageOrderManage(PageBase):
    """"订单状态"""

    def click_order_state(self):
        self.click((By.CSS_SELECTOR, 'div[class="search-left-button"]>div:nth-child(1)>span>button>span>span'))

    # 点击清除状态
    def click_eliminate_order_state(self):
        loc = self.find_element_func((By.XPATH, "//span[text()='清除']")[2])
        loc.click()

    # 点击待付款状态
    def click_to_be_pay_state(self):
        self.click_find_element((By.XPATH, "//span[text()='待付款']"))

    # 点击待处理状态
    def click_pending_state(self):
        self.click_find_element((By.XPATH, "//span[text()='待处理']"))

    # 点击已付款状态
    def click_paid_state(self):
        self.click_find_element((By.XPATH, "//span[text()='已付款']"))

    # 点击已完成状态
    def click_completed_state(self):
        self.click_find_element((By.XPATH, "//span[text()='已完成']"))

    # 点击已取消状态
    def click_cancel_state(self):
        self.click_find_element((By.XPATH, "//span[text()='取消']"))

    """退款状态"""

    def click_refund_state(self):
        self.click((By.CSS_SELECTOR, 'div[class="search-left-button"]>div:nth-child(2)>span>button>span>span'))

    # 未退款
    def click_no_refund(self):
        self.click_find_element((By.XPATH, "//span[text()='未退款']"))

    # 点击部分退款
    def click_part_refund(self):
        self.click_find_element((By.XPATH, "//span[text()='部分退款']"))

    # 点击已退款
    def click_completed_refund(self):
        self.click_find_element((By.XPATH, "//span[text()='已退款']"))

    """发货状态"""

    def click_undelivered(self):
        self.click_find_element((By.XPATH, "//span[text()='未发货']"))

    def click_partial_delivery(self):
        self.click_find_element((By.XPATH, "//span[text()='部分发货']"))

    def click_delivered(self):
        self.click_find_element((By.XPATH, "//span[text()='已发货']"))

    # 更多筛选器
    def click_more_selects(self):
        self.click_find_element((By.XPATH, "//span[text()='更多筛选器']"))

    # 订单排序
    def click_order_sort(self):
        self.click_find_element((By.CSS_SELECTOR, 'i[class="el-icon-sort"]'))

    # 输入搜索订单号
    def input_order_search(self, order_id):
        self.input((By.CSS_SELECTOR, 'input[placeholder="筛选订单"]'), order_id)

    # 选中订单列表中全部订单
    def click_all_order_list(self):
        self.click_find_element((By.CSS_SELECTOR, 'th>div>label>span>span'))

    # 选中订单列表中第一个订单
    def click_fist_order(self):
        self.click_find_element((By.CSS_SELECTOR, 'tr>td:nth-child(1)>div>label>span>span'))

    # 获取订单id
    def get_order_id(self):
        return self.text((By.CSS_SELECTOR, 'td:nth-child(2)>div>div>div:nth-child(1)'))

    # 获取订单支付时间
    def get_order_payment_time(self):
        return self.text((By.CSS_SELECTOR, 'td:nth-child(3)>div>div'))

    # 获取订单支付客户邮箱
    def get_order_customer_email(self):
        self.click((By.CSS_SELECTOR, 'td:nth-child(4)>div>div'))
        return self.text((By.CSS_SELECTOR, 'a[class="next-list__item"]'))

    # 获取订单支付客户姓名
    def get_order_customer_name(self):
        self.click((By.CSS_SELECTOR, 'td:nth-child(4)>div>div'))
        return self.text((By.CSS_SELECTOR, 'div[class="edit__content-wrapper"]>div>ul>li:nth-child(1)'))

    # 获取订单支付金额
    def get_order_total(self):
        return self.text((By.CSS_SELECTOR, 'td:nth-child(5)>div>div'))

    # 获取订单状态
    def get_order_state(self):
        return self.text((By.CSS_SELECTOR, 'td:nth-child(6)>div>div[class="el_table_p el-table-p-ststusB"]'))

    # 获取订单发货状态
    def get_order_delivered(self):
        return self.text((By.CSS_SELECTOR, 'td:nth-child(7)>div>div'))

    # 获取订单退款状态
    def get_order_refund(self):
        return self.text((By.CSS_SELECTOR, 'td:nth-child(8)>div>div'))

    # 获取订单产品数量
    def get_order_delivery_mode(self):
        return self.text((By.CSS_SELECTOR, 'td:nth-child(10)>div>span'))

    # 获取订单配送方式
    def get_order_number(self):
        return self.text((By.CSS_SELECTOR, 'td:nth-child(9)>div>div'))

    """
    综合合业务（添加无注册订单)
    """
