'''
_______________#########_______________________ 
______________############_____________________ 
______________#############____________________ 
_____________##__###########___________________ 
____________###__######_#####__________________ 
____________###_#######___####_________________ 
___________###__##########_####________________ 
__________####__###########_####_______________ 
________#####___###########__#####_____________ 
_______######___###_########___#####___________ 
_______#####___###___########___######_________ 
______######___###__###########___######_______ 
_____######___####_##############__######______ 
____#######__#####################_#######_____ 
____#######__##############################____ 
___#######__######_#################_#######___ 
___#######__######_######_#########___######___ 
___#######____##__######___######_____######___ 
___#######________######____#####_____#####____ 
____######________#####_____#####_____####_____ 
_____#####________####______#####_____###______ 
______#####______;###________###______#________ 
________##_______####________####______________ 

Descripttion: 猜数字游戏 
version: 0.1
Author: 崩布猪
Date: 2024-02-16 21:12:29
LastEditors: 崩布猪
LastEditTime: 2024-02-16 21:21:09
'''

import random

answer = random.randint(1,100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入您猜的数字:'))
    if number > answer:
        print('太..太大了啊喂(#`O\′)')
    elif number < answer:
        print('小小的泄恨可爱')
    else:
        print('恭喜您才对了')
        print('猜了%d次猜猜对 杂鱼~杂鱼~' % counter)
        break
    if counter > 8:
        print('哦 老伙计 你已经猜了七次了。快休息一下吧')