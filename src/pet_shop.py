# 1.
def get_pet_shop_name(shop_name):
    return shop_name["name"]
    # return self.cc_pet_shop["name"] 
        # I dont need to do this because I am not passing in the argument. 
        # I am giving the base template so I just put here's that variable i needed to get 
        #  and this is the key value key to get the right bit

# 2.
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]
    # breakpoint() is amazing...??? maybe? We'll see

# 3 & 4.
def add_or_remove_cash(pet_shop, pet_price):
    if pet_shop["admin"]["pets_sold"] >= 0:
        pet_shop["admin"]["total_cash"] += pet_price
    else: 
        pet_shop["admin"]["total_cash"] -= pet_price

# 5.
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# 6.
def increase_pets_sold(pet_shop, sold_pets):
    pet_shop["admin"]["pets_sold"] = sold_pets

# 7.
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# # 8 & 9
# def get_pets_by_breed(pet_shop, searching_breed):
#     for pet in pet_shop:
#         if ["breed"] == searching_breed:
#             return "found" + pet
#         else:
#             return "not found"

# def get_pets_by_breed(pet_shop, searching_breed):
#     pets = []
#     for pet in pet_shop["pets"]:
#         if ["breed"] == searching_breed:
#             pets.amend(pet["name"])


# 10.
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop:
        if name == ["name"]:
            print(pet["name"])

# 11.


# 12.


# 13.


# 14.


# 15.


# 16.


# 17.