# list of my cat names
catname = []
while True:
    print('enter your catname' + str(len(catname) + 1) +
          '(or enter nothing to end command:)')
    name = input()
    if name == '':
        break
catname = catname + [name]
print('the catname are:')
for name in catname:
    print(' ' + catname)