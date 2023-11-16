name = 'alice'
age = '2'
print('what is your name')    # ask for their name
name = input()
if name == 'alice':
    print('hello alice.')
    print('what is your age')
    age = input()
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
else:
    print('you are vampire')