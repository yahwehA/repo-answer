
def search_item(items_list, i):

    if i in items_list:

        return items_list.index(i)

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:

    index_item = search_item(items_list, find_item)

    if index_item is not None:

             print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")

    else:

            print(f"Товар '{find_item}' не найден в списке.")
