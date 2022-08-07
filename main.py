# welcome to healthmangement programe
print('Enter Your Client code')
print('1 for naman, 2 for Gautam, 3 for Pratik')
def get():
    import datetime
    return datetime.datetime.now()
client_code = int(input())
if client_code == 1:
    print('Welcome Mr. Naman\n')
    print('Please Select Your action:\nPress 1 for Log\nPress 2 for retrieve')
    n1 = int(input())
    if n1 == 1:
        print('Please Select Your action:\nPress 1 for Diet\nPress 2 for exercise')
        n2= int(input())
        if n2 == 1:
            n3 = open('namanfood','a')
            n4 = input("Type here to add\n")
            n3.write(str([str(get())])+':'+n4+'\n')
            print('sucessfully added')
        else:
            n3 = open('namanexercise', 'a')
            n4 = input("Type here to add\n")
            n3.write(str([str(get())]) + ':' + n4 + '\n')
            print('sucessfully added')
    else:
        print('Select Your action\nPress 1 for Diet\n Press 2 for exercise')
        n2 = int(input())
        if n2 == 1:
            n3 = open('namanfood',)
            n4 = n3.readlines()
            print(n4)
        else:
            n3 = open('namanexercise',)
            n4 = n3.readlines()
            print(n4)

elif client_code == 2:
    print('Welcome Mr. Gautam\n')
    print('Please Select Your action:\nPress 1 for Log\nPress 2 for retrieve')
    n1 = int(input())
    if n1 == 1:
        print('Please Select Your action:\nPress 1 for Diet\nPress 2 for exercise')
        n2= int(input())
        if n2 == 1:
            n3 = open('gautamfood','a')
            n4 = input("Type here to add\n")
            n3.write(str([str(get())])+':'+n4+'\n')
            print('sucessfully added')
        else:
            n3 = open('gautamexercise', 'a')
            n4 = input("Type here to add\n")
            n3.write(str([str(get())]) + ':' + n4 + '\n')
            print('sucessfully added')
    else:
        print('Select Your action\nPress 1 for Diet\n Press 2 for exercise')
        n2 = int(input())
        if n2 == 1:
            n3 = open('gautamfood',)
            n4 = n3.readlines()
            print(n4)
        else:
            n3 = open('gautamexercise',)
            n4 = n3.readlines()
            print(n4)
else:
    print('Welcome Mr. Pratik\n')
    print('Please Select Your action:\nPress 1 for Log\nPress 2 for retrieve')
    n1 = int(input())
    if n1 == 1:
        print('Please Select Your action:\nPress 1 for Diet\nPress 2 for exercise')
        n2= int(input())
        if n2 == 1:
            n3 = open('pratikfood', 'a')
            n4 = input("Type here to add\n")
            n3.write(str([str(get())])+':'+n4+'\n')
            print('sucessfully added')
        else:
            n3 = open('pratikexercise', 'a')
            n4 = input("Type here to add\n")
            n3.write(str([str(get())]) + ':' + n4 + '\n')
            print('sucessfully added')
    else:
        print('Select Your action\nPress 1 for Diet\n Press 2 for exercise')
        n2 = int(input())
        if n2 == 1:
            n3 = open('pratikfood',)
            n4 = n3.readlines()
            print(n4)
        else:
            n3 = open('pratikexercise',)
            n4 = n3.readlines()
            print(n4)



