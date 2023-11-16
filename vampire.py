name = 'alice'
age = '2'
print('what is your name')    # ask for their name
name = input()
print('what is your age')
age = input()
if name == 'alice':
    print('hello alice.')

elif int(age) < 12:
    print('You are not Alice, kiddo.')
elif int(age) > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif int(age) > 100:
    print('You are not Alice, grannie.')
else:
    print('you are vampire')
