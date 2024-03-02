birthday = {'aliyu':'13', 'fatima':'22', 'joy':'30'}
while True:
    print('enter a name: (blank to quite)')
    name = input()
    if name == '':
        break
    if name in birthday:
        print(birthday[name] + ' is the birthday of ' + name)
    else:
        print(' i do not have birthday infomation for ' + name)
        print('what is your birthday?')
        Bday = input()
        birthday[name] = Bday
        print('birthday database updated')


