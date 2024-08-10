money = int(input('money for check :'))
def vat_cal(money) :
    result = money + (money*7/100)
    return result
print('summary total :',vat_cal(money))
