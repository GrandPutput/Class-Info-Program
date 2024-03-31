#prints menu choices
def print_menu():
    print('Please Enter Choice:')
    print('v - View Class info')
    print('s - Select Class')
    print('q - Quit')

#prints all classes info
def print_classes(a, b, c):
    for key, value in a.items():
       x = value
       y = b[key]
       z = c[key]
       print(key, '|', 'Classroom:', x, '|', 'Instructor:', y, '|', 'Time:', z)

#selects class info by name
def print_class_info(a, b, c, choice):
    x = a[choice]
    y = b[choice]
    z = c[choice]
    print(choice, '|', 'Classroom:', x, '|', 'Instructor:', y, '|', 'Time:', z)

def run_choice(choice):
  if choice == 'v':
    print('Classes Information:')
    print_classes(room_nums, instructors, times) 

  elif choice == "s":
    classes = ['CSC101', 'CSC102', 'CSC103', 'NET110', 'COM241']
    print('Class List:\n CSC101\n CSC102\n CSC103\n NET110\n COM241')
    c = input('Please Choose A Class:')
    if c in classes:
        print_class_info(room_nums, instructors, times, c)
    else:
       print('Invalid Class')
    

#Program Run
room_nums = {'CSC101' : 3004, 'CSC102' : 4501, 'CSC103' : 6755, 'NET110' : 1244, 'COM241' : 1411}
instructors = {'CSC101' : 'Haynes', 'CSC102' : 'Alvarado', 'CSC103' : 'Rich', 'NET110' : 'Burke', 'COM241' : 'Lee'}
times = {'CSC101' : '8:00 a.m.', 'CSC102' : '9:00 a.m.', 'CSC103' : '10:00 a.m.', 'NET110' : '11:00 a.m.', 'COM241' : '1:00 p.m.'}


menu_choices = ['v', 's', 'q']

# while loop that prints the menu until user enters q - quit
print_menu()
while True:
    menu_choice = input('Choose an option: ')
    print()
    if menu_choice == 'q':
      print('Goodbye!')
      break
    else:
      if menu_choice in menu_choices:
        run_choice(menu_choice)
        print()
        print_menu()
        print()
      else:
        print('Choose a menu option!\n')