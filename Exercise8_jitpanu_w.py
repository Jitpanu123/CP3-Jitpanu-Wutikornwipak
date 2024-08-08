usernameinput = input('Username : ')
passwordinput = input('Password : ')
if usernameinput == '1234' and passwordinput == '5678' :
    print('---Welcome to Myshop---')
    print('My item')
    print('1.Sanwich 10 baht')
    print('2.Hotdog 15 baht')
    print('3.Burger 30 baht')
    userselect = int(input('Please choose item : '))
    if userselect == 1 :
        quantity1 = int(input('Quantity >>>'))
        print('summary = ',10*quantity1)
    elif userselect == 2 :
        quantity2 = int(input('Quantity >>>'))
        print('summary = ', 15 * quantity2)
    elif userselect == 3 :
        quantity3 = int(input('Quantity >>>'))
        print('summary = ', 30 * quantity3)
print('Thank you!!!')