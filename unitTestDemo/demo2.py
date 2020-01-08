# -*- coding:utf-8 -*-

import unittest

class SuiteSample1(unittest.TestCase):
    """测试套件中添加测试用例"""
    @classmethod
    def setUpClass(cls):
        print("Start")

    @classmethod
    def tearDownClass(cls):
        print("End")

    def test_01(self):
        print(1)

    def test_02(self):
        print(2)

    def test_03(self):
        print(3)

if __name__ == '__main__':
    # 构造测试套件
    suite = unittest.TestSuite()
    # # 向测试套件中添加测试用例：方法一
    # suite.addTest(SuiteSample1("test_03"))
    # suite.addTest(SuiteSample1("test_02"))
    # 向测试套件中添加测试用例：方法二
    tests = [SuiteSample1("test_03"), SuiteSample1("test_02")]
    suite.addTests(tests)
    # 执行测试用例
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)