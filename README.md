# MeShop自动化测试项目

本项目采用`allure`+`pytest`作为框架

##项目启动

在项目根目录下执行控制台执行

``` shell
# 执行所有的测试
pytest
# 执行case里的单条用例的测试
pytest test01_shop_login.py
# 执行第一条测试用例失败，停止测试
pytest -x
# 执行测试用例时显示具体用例名称
pytest -v
# 执行完用例后，生成在线测试报告
allure serve report
# 生成测试报告 cmd打开工程目录report文件夹目录输入命令
allure generate report/ -o report/html
# 删除历史报告生成新报告 
allure generate report/ -o report/html --clean
```