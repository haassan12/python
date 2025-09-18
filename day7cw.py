grocery =["milk","bread","eggs",]
def add_item(item):
    grocery.insert(1,item)
    grocery.pop()
    return grocery
add_item("chocolate")
print(grocery)


lambda itm: print(f'item :{itm}')
for itm in grocery:
    print(f'item :{itm}')




   





