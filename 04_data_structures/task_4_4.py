# -*- coding: utf-8 -*-
'''
Задание 4.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

VLAN1 = command1.split(' ')
VLAN2 = command2.split(' ')

VLAN1 = VLAN1[4].split(',')
VLAN2 = VLAN2[4].split(',')

VLAN1 = set(VLAN1)
VLAN2 = set(VLAN2)

INTERSECT = VLAN1 & VLAN2
INTERSECT = list(INTERSECT)



print(INTERSECT)


