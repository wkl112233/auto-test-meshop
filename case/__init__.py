import logging
import logging.config
import os
from tempfile import TemporaryDirectory
import allure
import pytest

from tools.get_driver import GetDriver


class TestBase:
    """
    测试基类
    """

    def setup_class(self) -> None:
        """
        初始化
        :return:
        """
        # 获取driver
        self.logger = logging.getLogger(type(self).__name__)
        if not getattr(self, 'url', None):
            raise ValueError("%s must have a url" % type(self).__name__)
        self.driver = GetDriver.get_web_driver(self.url)

    def teardown_class(self) -> None:
        """
        结束
        :return:
        """
        self.logger.info("关闭 web driver")
        # 关闭driver
        GetDriver.close_web_driver()

    def screenshot(self) -> None:
        """
        生成页面快照
        :return:
        """
        self.logger.info("正在截图操作")
        # 在临时目录生成图片
        with TemporaryDirectory() as dirname:
            file_path = os.path.join(dirname) + "err.png"
            self.driver.get_screenshot_as_file(file_path)
            self.logger.info("正在将图片写入报告操作")
            with open(file_path, "rb") as f:
                # allure.attach("描述", f.read(), allure.attachment_type.PNG)
                allure.attach.file(source=file_path, name="实时截图",
                                   attachment_type=allure.attachment_type.PNG)
