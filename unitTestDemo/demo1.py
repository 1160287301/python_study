import unittest

from ddt import ddt, data, unpack, file_data
import yaml


# 必须继承 unittest.TestCase
# 以 test 开头的函数都是测试函数
# @ddt
class MyTestCase(unittest.TestCase):
    # 前置条件
    # def setUp(self) -> None:
    #     print("setUp function !!!!!!")

    # 后置条件
    # def tearDown(self) -> None:
    #     print("tearDown function !!!!!!")

    def test_something(self) -> None:
        print("test_something")
        self.assertEqual(True, False)

    # @data(1, 2, 3)
    # def test_print(self, text):
    #     self.assertLessEqual(text, 3, "比 3 大")
    #
    # @data((1, 1), (2, 2), (3, 3))
    # @unpack
    # def test_print1(self, a, b):
    #     self.assertEqual(a * 2, a + b)
    #
    # @file_data("test.yml")
    # def test_print2(self, a):
    #     print(a)

    def test_step1(self):
        print("step_1")

    def test_step2(self):
        print("step_2")

    def test_step3(self):
        print("step_3")


if __name__ == '__main__':
    # unittest.main()

    # 构造测试套件
    # suite = unittest.TestSuite()
    # test_cases = [MyTestCase("test_step1"), MyTestCase("test_step2"), MyTestCase("test_step3")]
    # suite.addTests(test_cases)
    # # 执行测试 verbosity 参数可以控制输出的错误报告的详细程度，
    # # 默认是 1；如果设为 0，则不输出每一用例的执行结果；如果设为 2，则输出详细的执行结果
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    suite = unittest.TestSuite()
    suite.addTest(MyTestCase("test_step1"))  # 使用addTest()添加测试类下面的单个测试方法
    suite.addTest(MyTestCase("test_step2"))
    unittest.TextTestRunner(verbosity=1).run(suite)