import time
import pages
from pages.pagebase import PageBase


class PageAdminIndexMinix:
    """
    后台主页(暂时为后台左侧菜单项）
    """

    def admin_index(self):
        if not getattr(self, '_admin_index', None):
            self._admin_index = PageAdminIndex(self.driver)
        return self._admin_index


class PageAdminIndex(PageBase):
    """
    点击产品管理
    """

    def click_product_manage(self):
        self.click(pages.admin.pdm)

    """
    点击所有产品
    """

    def click_all_product(self):
        self.click(pages.admin.all_products)

    """
    点击产品系列
    """

    def click_product_family(self):
        self.click(pages.admin.product_family)
        time.sleep(2)

    """
    点击产品排序
    """

    def click_product_sequencing(self):
        self.click(pages.admin.product_sequencing)

    """
    点击产品评论
    """

    def click_product_reviews(self):
        self.click(pages.admin.product_reviews)

    """
    点击订单管理
    """

    def click_order_management(self):
        self.click(pages.admin.order_management)

    """
    点击订单列表
    """

    def click_order_list(self):
        self.click(pages.admin.order_list)

    """
    点击弃单列表
    """

    def click_discard_list(self):
        self.click(pages.admin.discard_list)

    """
    点击营销管理
     """

    def click_marketing_management(self):
        self.click(pages.admin.marketing_management)

    """
    点击邮件营销
    """

    def click_mail_marketing(self):
        self.click(pages.admin.mail_marketing)

    """
    点击营销代码管理
    """

    def click_marketing_code(self):
        self.click(pages.admin.marketing_code)

    """
    点击数据跟踪
    """

    def click_data_tracking(self):
        self.click(pages.admin.data_tracking)

    """
    点击多币种管理
    """

    def click_multi_currency(self):
        self.click(pages.admin.multi_currency)

    """
    点击应用管理
    """

    def click_app_manage(self):
        self.click(pages.admin.app_manage)

    """
    点击应用列表
    """

    def click_app_list(self):
        self.click(pages.admin.app_list)
