from pyfiglet import Figlet
import qrcode

def show_list():
    for i in range(len(products)):
        print(products[i])

def show_menu():
    print('1- Add product')
    print('2- Edit product')
    print('3- Delet product')
    print('4- Serach')
    print('5- Show list')
    print('6- Buy')
    print('Exit')

f=Figlet(font='standard')
print(f.rendertext('omid store'))

def load():
    file= open('database.txt', 'r')
    data = file.read()
    product_list = data.split('\n')

    PRODUCTS=[]
    for i in range(len(product_list)):
        product_info = product_list[i].split(',')
        my_dict = {}
        my_dict['id'] = product_info[0]
        my_dict['Name'] = product_info[1]
        my_dict['Price'] = product_info[2]
        my_dict['Count'] = product_info[3]
        products.append(my_dict)
    print('Welcome')

def add_product():
    
    while True:
        
        new_product_id = input('pls enter the \'id Code\' of new product: ')
        c = 0
        for i in range(len(products)):
            
            if new_product_id == products[i]['id']:
                print('This ID has been taken, pls enter another id code')
                c += 1
        
        if c != 1 :
            break

    name = input('Pls enter the name of product: ')
    price = input('pls enter the price of product: ')
    count = input('pls enter the count of product: ')
    new_product_dict = {}
    new_product_dict['id'] = new_product_id
    new_product_dict['Name'] = name
    new_product_dict['Price'] = price
    new_product_dict['Count'] = count
    products.append(new_product_dict)

def edit():
    
    product_id = input('Pls enter the product ID that you want to edit: ')
    c = 0
    
    for i in range(len(products)):
        if product_id == products[i]['id']:
            products[i]['Name'] = input('New name: ')
            products[i]['Price'] = input('New price: ')
            products[i]['Count'] = input('New count: ')
            c += 1
            break

    if c != 1:
        print('This ID does not exist')

def search_by_name():
    
    c = 0
    name = input('Enter the name of product: ')

    for i in range(len(products)):
        if name == products[i]['Name']:
            print(products[i])
            c += 1
            break

    if c == 0:
        print('Can\'t find this name in products')

def delete_product():
    c = 0
    product_id = input('Pls enter the product ID: ')
    for i in range(len(products)):
        if product_id == products[i]['id']:
            products.pop(i)
            c += 1
            print('This product was deleted')
            break

    if c == 0:
        print('This ID does not exist in products')

def buy_product():
    
    sum = 0
    product_list = []
    user_choice = 'y'
    
    while user_choice == 'y':
        c = 0
        product_id = input('Pls enter product id: ')
        
        for i in range(len(products)):
            if products[i]['id'] == product_id:
                c = +1
                count = input('Pls enter count: ')
                
                if int(count) > int(products[i]['Count']):
                    print(f"We have not enough of this item, we only have {int(products[i]['Count'])} of this item ")
                
                else:
                    product_dict = {}
                    product_dict['Name'] = products[i]['Name']
                    product_dict['Price'] = products[i]['Price']
                    product_dict['Count'] = str(count)
                    product_list.append(product_dict)

                    price = int(count) * int(products[i]['Price'])
                    sum += price

                    products[i]['Count'] = str(int(products[i]['Count']) - int(count))
                    
                user_choice = input('Do you want continue?(y/n)')            
                if user_choice == 'n':
                    print('You buy this items:')
                    for i in range(len(product_list)):
                        print(product_list[i])
                    print(f"The amount you must pay is: {sum}")
                    break
            
        if c == 0 :
            print('We have not this item')

def make_qrcode():
    
    c = 0
    user_input = input('pls enter code ID of product: ')
    
    for i in range(len(products)):
        if user_input == products[i]['id']:
            c += 1
            qr_file = qrcode.make(products[i])
            qr_file.save('myQR.png')
            print('Qrcode created')
            break
    
    if c == 0:
        print('We can\'t find this item in products')

def exit_program():
    
    new_str = ""

    for i in range(len(products)):
        if i == (len(products)-1):
            new_id = products[i]['id']
            new_name = products[i]['Name']
            new_price = products[i]['Price']
            new_count = products[i]['Count']
            str = new_id + ',' + new_name + ',' + new_price + ',' + new_count
            new_str += str

        else:
            new_id = products[i]['id']
            new_name = products[i]['Name']
            new_price = products[i]['Price']
            new_count = products[i]['Count']
            str = new_id + ',' + new_name + ',' + new_price + ',' + new_count + '\n'
            new_str += str

    data = open('database.txt','w')
    data.write(new_str)
    data.close()
    exit()

products = []

load()


while True:

    show_menu()
    choice = int(input('Pleas choose your number : '))

    if choice == 1:
        add_product()

    elif choice == 2:
        edit()

    elif choice == 3:
        show_list()

    elif choice == 4:
        search_by_name()

    elif choice == 5:
        make_qrcode()

    elif choice == 6:
        delete_product()

    elif choice == 7:
        buy_product()

    elif choice == 8:
        exit_program()