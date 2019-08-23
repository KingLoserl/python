#1、_xxx 不能用于’from module import *’ 以单下划线开头的表示的是protected类型的变量。即保护类型只能允许其本身与子类进行访问。
#2、__xxx 双下划线的表示的是私有类型的变量。只能是允许这个类本身进行访问了。连子类也不可以
#3、__xxx___ 定义的是特列方法。像__init__之类的

#idea使用python的两个小问题
#1. Unused import statement  因为导入的包没有被使用
#2. 解释器配置  project structure --->project---->sdk

import collections
from random import choice
print ("hello")
Card=collections.namedtuple('card',['rank','suit'])
#namedtuple需要两个参数，分别是tuple的名字和其中域的名字。比如在上例中，tuple的名字是“Animal”，它包括三个域，分别是“name”、“age”和“type”。

class FrenchDeck:
    ranks=[str(n) for n in range(2,11)]+list('JQKA')
    suits='today is good day'.split()

#系统方法
    def __init__(self): # 构造方法
        self.cards=[Card(rank,suit) for suit in  self.suits for rank in  self.ranks]
    def __int__(self):
        self.cards=[Card(rank,suit) for suit in  self.suits for rank in  self.ranks]
    def __len__(self):  #长度方法
        return len(self.cards)
    def __getitem__(self, item): #获取子项
        return self.cards[item]

print('---------------自定义系统函数使用--------------------------------')
deck=FrenchDeck()
print(len(deck))
print(deck.suits)
print(deck[0])
print(deck[-1])

#内置随机函数
print('------随机行数使用-----------------------')
print(choice(deck))

#省略显示过长内容
for card in deck: # doctest: +ELLIPSIS
    print(card)
print(deck[:3])
print(deck[1::2])

#in运算符
print(Card('3', 'today') in deck)#没有实现__container__方法  判断是否存在