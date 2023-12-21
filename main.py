import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)




def get_users():

    url = f"http://localhost:5292/api/products"
    response = requests.get(url,verify=False)
    if response.status_code == 200:
        jprint(response.json())
        print('-----------------------------------------------------------------------------------------------')
    else:
        print("error Unable to fetch data " + "     status_code " +  str(response.status_code))
    # Example usage
        
def get_user(id):

    url = f"http://localhost:5292/api/products/{id}"
    response = requests.get(url,verify=False)
    if response.status_code == 200:
        jprint(response.json())
        print('-----------------------------------------------------------------------------------------------')
        return response.json()
    else:
        print("error Unable to fetch data " + "    status_code " +  str(response.status_code))

def post_user(item):

    url = f"http://localhost:5292/api/products"
    
   
    headers = {'content-type': 'application/json; charset=UTF-8'}

    response = requests.post(url, data=json.dumps(item), headers=headers,verify=False)

    if response.status_code == 201:
        print("Product added")
        get_users()
        print('-----------------------------------------------------------------------------------------------')
    else:
        print("error Unable to post data " + "    status_code " +  str(response.status_code))
    

def put_user(id, item):

    url = f"http://localhost:5292/api/products/{id}"
    
    
    headers = {'content-type': 'application/json; charset=UTF-8'}

    response = requests.put(url, data=json.dumps(item), headers=headers, verify=False)

    if response.status_code == 204:
        print("Product added")
        get_users()
        print('-----------------------------------------------------------------------------------------------')
    else:
        print("error Unable to update data " + "    status_code " +  str(response.status_code))

def delete_user(id):

    url = f"http://localhost:5292/api/products/{id}"
    
    

    headers = {'Content-Type': 'application/json; charset=UTF-8'}

    response = requests.delete(url, headers=headers, verify=False)

    if response.status_code == 204:
        print("Product Deleted")
        get_users()
        print('-----------------------------------------------------------------------------------------------')
    else:
        print("error Unable to delete data " + "    status_code " + str(response.status_code))


def add_and_validate(val, key, item):

    if(key == "title"):
        while ( (val.isalnum()) == False ):
            print("enter a valid value: ")
            val = input()
        item[key] = val
    
    elif(key == "price"):
        while ( (val.isdigit()) == False or int(val) <= 0 ):
            print("enter a valid value: ")
            val = input()
        item[key] = val
    elif(key == "description"):
        while ( (val.isalnum()) == False ):
            print("enter a valid value: ")
            val = input()
        item[key] = val
    elif(key == "category"):
        while ( (val.isalnum()) == False ):
            print("enter a valid value: ")
            val = input()
        item[key] = val
    elif(key == "image"):
        while ( (val.isalnum()) == False ):
            print("enter a valid value: ")
            val = input()
        item[key] = val
    elif(key == "rating"):
        while ( (val.isdigit()) == False or int(val) <= 0 or int(val)>5):
            print("enter a valid value: ")
            val = input()
        item[key] = val 
    elif(key == "count"):
        while ( (val.isdigit()) == False or int(val) <= 0 ):
            print("enter a valid value: ")
            val = input()
        item[key] = val 
    










wantToContinue = True

while(wantToContinue):

    print("Enter your choice ")
    print("1.Show All Products\n2.Add a new product\n3.Upadate a Product\n4.Delete a product\n")

    ch = int(input())

    if(ch == 1):
        get_users()

    elif(ch == 2):

        keys = ["title", "price","description","category","image","rating","count"]
        item = {}

        for key in keys:
            print("enter "+key)
            val = input()
            add_and_validate(val,key,item)
        
        post_user(item)

    elif(ch == 3):
        print("enter the product id :")
        id = int(input())
        item = dict(get_user(id))
        item.pop("id")

        for key, val in item.items():
            print("Do you want to make changes in "+key+" (y/n)" )
            print("Current value - "+ str(val))
            ans = input()
            if(ans == 'y' ):
                print("enter new value : ")
                new_val = input()
                add_and_validate(new_val,key,item)
                
        put_user(id, item)

    elif(ch == 4):
        print("enter the product id :")
        id = int(input())
        delete_user(id)
    else:
        print("Enter a valid Choice")

    print("Do you want to continue? (y/n) ")
    choice = input()

    if(choice != 'y'):
        wantToContinue = False

    

