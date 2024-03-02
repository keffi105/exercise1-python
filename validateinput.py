# sign in details
while True:
    print('please enter your name')
    name = input()
    if name.isupper():
        break
    print('please enter your name in capital letters')
while True:
    print('enter your age')
    age = input()
    if age.isdecimal():
        break
    print('please enter number of your age')
while True:
    print('type in your password')
    password = input()
    if password.istitle():
        break
    print('password must contain uppercase,lowercase and number')

