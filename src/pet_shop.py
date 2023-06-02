# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop,amount):
    pet_shop["admin"]["total_cash"] += amount
    return pet_shop

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop,amount):
    pet_shop["admin"]["pets_sold"] += amount
    return pet_shop["admin"]["pets_sold"]

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop,breed):
    return [pet for pet in pet_shop["pets"] if pet["breed"] == breed]

def find_pet_by_name(pet_shop,name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop,name):
    pet_shop["pets"] = [pet for pet in pet_shop["pets"] if pet["name"] != name]

def add_pet_to_stock(pet_shop,new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer,pet):
    if customer["cash"] >= pet["price"]:
        return True
    return False

def sell_pet_to_customer(pet_shop,pet,customer):
    if pet:
        if customer_can_afford_pet(customer,pet):
            add_or_remove_cash(pet_shop,pet["price"])
            add_pet_to_customer(customer,pet)
            remove_customer_cash(customer,pet["price"])
            increase_pets_sold(pet_shop,1)
            remove_pet_by_name(pet_shop,pet["name"])