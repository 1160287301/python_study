import unittest

from ddt import ddt, data, unpack


# 必须继承 unittest.TestCase
# 以 test 开头的函数都是测试函数
@ddt
class MyTestCase(unittest.TestCase):
    # 前置条件
    def setUp(self) -> None:
        print("setUp function !!!!!!")

    # 后置条件
    def tearDown(self) -> None:
        print("tearDown function !!!!!!")

    def _test_something(self) -> None:
        print("test_something")
        self.assertEqual(True, False)

    @data(1, 2, 3)
    def test_print(self, text):
        self.assertLessEqual(text, 2, "比 3 大")

    @data((1, 1), (2, 2), (3, 3))
    @unpack
    def test_print(self, a, b):
        self.assertEqual(a * 2, a + b)


if __name__ == '__main__':
    unittest.main(verbosity=2)
