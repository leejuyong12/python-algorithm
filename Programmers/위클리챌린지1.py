# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    total_price = 0
    for x in range(1, count+1):
        total_price += price * x
        
    my_money = money - total_price
    if my_money < 0:
        return -my_money
    else:
        return 0

solution(3, 20, 4)