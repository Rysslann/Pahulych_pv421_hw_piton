import requests

BASE_URL = "https://fakestoreapi.com"
def get_data(endpoint):
    return requests.get(f"{BASE_URL}{endpoint}").json()
def display_list(items):
    for i in items:        print(f"{i["id"]} - {i["title"]}")

def get_ch_user():
    ch_user = input("Please enter number products: ")    if type(ch_user) == str:
        print("You choice incorrect!")        get_ch_user()
    elif int(ch_user) >= 21 or int(ch_user) <= 0:        print("You choice incorrect!")
        get_ch_user()
    return int(ch_user)
def main():
    products = get_data('/products')    display_list(products)
    ch_user = get_ch_user()    print("It's Worked! ", get_data(f"/products/{ch_user}"))

if __name__ == "__main__":    main()