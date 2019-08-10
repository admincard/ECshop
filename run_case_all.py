#掌握使用HTMLTestRunnerPlugins类 生成测试报
import unittest
import HTMLTestRunnerPlugins
import time,os

BASE_PATH = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0] # 获取当前目录--获取项目目录
SCRIPTS_FILE = os.path.join(BASE_PATH,'Ecshop--5','scripts')  # 将"scripts"文件夹添加到当前目录
REPORT_FILE = os.path.join(BASE_PATH,'Ecshop--5','report')  # 将"scripts"文件夹添加到当前目录

#用例文件夾的路徑
case_dir=SCRIPTS_FILE

#建立测试报告存放地址
report_dir=REPORT_FILE

#将需要执行的测试用例添加到测试套件中
discover = unittest.defaultTestLoader.discover(case_dir,pattern='test_*.py')

#使用HTMLTestRunnerPlugins执行测试用例并生成测试报告
now = time.strftime("%Y_%m_%d %H_%M_%S")
file = open(report_dir+'\\'+now+'report.html','wb')

#执行测试
runner = HTMLTestRunnerPlugins.HTMLTestRunner(
                            title='接口自动化测试报告',
                            description='报告详细描述',
                            verbosity=2,
                            stream=file,
                            retry=0
                            )
runner.run(discover)
file.close()
