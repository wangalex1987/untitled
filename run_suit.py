import unittest,time,os,test
import HTMLTestRunner_PY3
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(test.test_login))
print(os.getcwd())
report_path= "./report/tpshop{}.html".format(time.strftime('%Y%m%d %H%M%S'))
with open(report_path, mode='wb') as f:

    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title="tpshop注册登录接口功能测试",
                                               description="这是一个更加美观的报告，前提是连上互联网")
    runner.run(suite)