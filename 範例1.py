# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:11:33 2021

@author: user
"""

price=0
item = input("請點餐:(A，B，C)")
item = item.upper()#轉大寫
#item = item.lower()#轉小寫
if item == "A":
    price=130
    food=input("是否加點購可樂(Y/N)?")
    food=food.upper()
    if food=="Y":
       
       price+=30
elif item =="B":
        price=115
        food=input("是否加點購可樂(Y/N)?")
        food=food.upper()
        if food=="Y":
           
           price+=30
elif item =="C":
     price = 80
     food == input("是否換大薯(Y/N)?")
     if food =="Y":
         price+=15
     q=input("捐款吧！！")
     if q =="Y":
            money=int(input("金額:"))
            price+=money
else:
    print("選項錯誤")
print(price)
            
    
