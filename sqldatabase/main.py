from management import Add
from management import View
from management import Delete

print('''
Enter the action:
[1] Add
[2] Delete
[3] View
    ''')
action = input()
if action == '1':
    Add()
elif action == '2':
    Delete()
elif action == '3':
    View()
else:
    print('Unknown action')