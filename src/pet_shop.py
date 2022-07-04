# 1.
def get_pet_shop_name(shop_name):
    return shop_name["name"]
    # return self.cc_pet_shop["name"] 
        # I dont need to specify by typing self.cc_pet_shop because I am not passing in the argument 
        # I am giving the base template so I just put here's that variable i needed to get 
        #  and this is the key value key to get the right bit.

# 2.
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]
    # breakpoint() is amazing...??? maybe? We'll see
    # inside 

# 3 & 4.
def add_or_remove_cash(pet_shop, pet_price):
    if pet_shop["admin"]["pets_sold"] >= 0:
        pet_shop["admin"]["total_cash"] += pet_price
    else: 
        pet_shop["admin"]["total_cash"] -= pet_price
    # there is a use case for the if else statement even though it's not necessary for this functionality

# 5.
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# 6.
def increase_pets_sold(pet_shop, sold_pets):
    pet_shop["admin"]["pets_sold"] = sold_pets

# 7.
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# 8 & 9
def get_pets_by_breed(pet_shop, searching_breed):
    found_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == searching_breed:
            found_pets.append(pet)
            # APPEND!!!!! NOT AMEND
    return found_pets

# 10 & 11
# def find_pet_by_name(pet_shop, name):
#     for pet in pet_shop["pets"]:
#         if pet["name"] == name: # you can refer to either searched name or pet["name"] first
#             return pet

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet


# 12.
def remove_pet_by_name(pet_shop, name):
    pet_to_delete = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet_to_delete)
# refer to the previous function because we need that function anyway and we shouldn't assign an additional action to a function. It should just have one.



# 13.
def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)


# 14.
def get_customer_cash(customer):
    return customer["cash"]


# 15.
def remove_customer_cash(customer, amount):
    customer["cash"] -= amount


# 16.
def get_customer_pet_count(customer):
    return len(customer["pets"])


# 17.
def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)


# 18, 19, 20
def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet["price"]

# 21, 22, 23
def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)
