# Simple python program using conditional statements, looping , performing
# operations such as Insert , Update, Delete, Display, Sorting and searching on
# Datatypes like List, Tuple, Set, Dictionary.


def search(data):
    x = int(input("Enter search element: "))
    for i in range(len(data)):
        if data[i] == x:
            print(f"Element found at {i}")
            return
    print("Element not Found!!")

def sort(data):
    for i in range(len(data) - 1):
        flag=False
        for j in range(len(data) - i- 1):
            if data[j] > data[j+1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag=True
        if not flag:
            return
            
def update(data, key):
    if key in data or key in range(len(data)):
        x = int(input("Enter a new value: "))
        data[key] = x
    else:
        print("Key not found")

# List Operations     
my_list = []

def list_op():
    print("List operations: ")
    print("1.Insert\n2.Delete\n3.Update\n4.Search\n5.Sort\n6.Display\n7.Return to main")
    while True:
        ch = int(input("Enter choice: "))
        if ch == 1:
            x = int(input("Enter element: "))
            my_list.append(x)
        elif ch == 2:
            ele = int(input("Enter element to be deleted: "))
            try:
                my_list.remove(ele)
            except:
                print(f"Element {ele} not found")
        elif ch == 3:
            index = int(input("Enter index: "))
            update(my_list, index)
        elif ch == 4:
            search(my_list)
        elif ch == 5:
            sort(my_list)
        elif ch == 6:
            print(my_list)
        elif ch == 7:
            break
        else:
            print("Invalid choice")
        
# Tuple Operations         
tup = tuple()

def tuple_op():
    print("Enter tuple: ")
    tup = tuple(int(i) for i in input().split())
    print("1.Display\n2.Search\n3.Exit")
    while True:
        ch = int(input("Enter the choice: "))
        if ch == 1:
            print(tup)
        elif ch == 2:
            search(tup)
        elif ch == 3:
            break
        else:
            print("Invalid choice")


# Set Operations 
my_set = set()

def set_op():
    print("1.Add\n2.Remove\n3.Search\n4.Display\n5.exit")
    while True:
        ch = int(input("Enter choice: "))
        if ch == 1:
            my_set.add(int(input("Enter element: ")))
        elif ch == 2:
            try:
                my_set.remove(int(input("Enter element: ")))
            except:
                print("Element not found")
        elif ch == 3:
            ele = int(input("Enter search element: "))
            if ele in my_set:
                print("Element found in the set")
            else:
                print("Element not found")
        elif ch == 4:
            print(my_set)
        elif ch == 5:
            return
        else:
            print("Invalid choice")

# Dictionary Operations 
my_dict = {}

def dict_op():
    print("1.Insert\n2.Update\n3.Delete\n4.Search\n5.Display\n6.exit")
    while True:
        ch = int(input("Enter your choice: "))
        if ch == 1:
            key = input("Enter key: ")
            value = int(input("Enter value: "))
            my_dict[key] = value
        elif ch == 2:
            key = input("Enter key: ")
            update(my_dict, key)
        elif ch == 3:
            key = input("Enter key to be deleted: ")
            if key in my_dict:
                del my_dict[key]
            else:
                print("Key not found")
        elif ch == 4:
            ele = int(input("Enter value: "))
            flag = False
            for key, value in my_dict.items():
                if value == ele:
                    print(f"Element found at {key}")
                    flag = True
            if not flag:
                print("Element Not Found")
        elif ch == 5:
            print(my_dict)
        elif ch == 6:
            break
        else:
            print("Invalid choice")

# Main Menu
while True:
    print("1.List\n2.Tuples\n3.Set\n4.Dictonary\n5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        list_op()
    elif ch == 2:
        tuple_op()
    elif ch == 3:
        set_op()
    elif ch == 4:
        dict_op()
    elif ch==5:
        break
    else:
        print("Invalid choice")