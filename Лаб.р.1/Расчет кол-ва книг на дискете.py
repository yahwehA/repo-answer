size = 1.44
page = 100
soccer = 50
arm = 25
weight_of_one_symbol = 4
weight = page * soccer * arm * weight_of_one_symbol
answer = size * 1024 * 1024 / weight
print("Количество книг, помещающихся на дискету:", round(answer))