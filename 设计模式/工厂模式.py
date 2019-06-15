# -*- coding:utf-8 -*-

'''
处理对象创建，客户端可以申请一个对象而不用知道对象被哪个class创建。可以方便地解耦对象的使用和创建。有两种实现，工厂方法和抽象工厂
'''

'''
method(工厂方法)  执行单独的函数，通过传参提供需要的对象的信息
'''
import json
import xml.etree.ElementTree as etree


class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    """ 工厂方法 """
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)


'''
Abstract Factory(抽象工厂: 解决复杂对象创建问题)
工厂方法适合对象种类较少的情况，如果有多种不同类型对象需要创建，使用抽象工厂模式
'''


class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        """ 不同类型玩家遇到的障碍不同 """
        print('{} the Frog encounters {} and {}!'.format(
            self, obstacle, obstacle.action()))


class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t----Frog World -----'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}!'.format(
            self, obstacle, obstacle.action()))


class Ork:
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kill it'


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Wizard World -------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment:
    """ 抽象工厂，根据不同的玩家类型创建不同的角色和障碍 (游戏环境)
    这里可以根据年龄判断，成年人返回『巫师』游戏，小孩返回『青蛙过河』游戏"""

    def __init__(self, factory, name):
        factory = factory(name)
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


if __name__ == '__main__':
    GameEnvironment(WizardWorld, 'risa')#.play()
    # GameEnvironment(FrogWorld, 'risa').play()