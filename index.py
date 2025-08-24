print("welcome to smart mobile phone store assisstant")
product_catalog={
    "mobiles" : [23500 ,56],
    "laptop" : [50000,19 ],
    "tablet" :[42000,5 ]
}
def view_prododucts():
  print("\navailable products:")
  for items,[price,stock] in product_catalog.items():
      alert="[low stock]" if stock < 5 else""
      print(f"{items.title()}  -Rs{price}   In stock{stock}{alert}")
#view_prododucts()

def add_product():
  items=input("type the product name")
  price=input("enter product price")
  stock=input("no of products available")
  product_catalog[items]=(price,stock)
  print(f"{items.title()}  -Rs{price}   {stock}\tsuccessfully added" )

#add_product()
def purchase_items():
  cart={}
  while True:
    items=input("enter the item you want to purchase(or write 'done' if shopping complete)\t " ).lower()
    if items=='done':
      break
    if items not in  product_catalog:
      print("item not found")
      continue
    quantity=int(input("Enter quantity"))
    price,stock=product_catalog[items]
    if quantity >stock:
      print(f"only {stock} available in stocks.")
      continue

    cart[items]=price,stock
    product_catalog[items]=(price,stock-quantity)

  generate_bill(cart)

def generate_bill(cart):
    print("\n---bills---")
    total=0
    for items,(price,quantity) in cart.items():
     item_total= quantity*price
     total +=item_total
     print(f"{items.title()}\t{quantity}*Rs{price}\t=\t{item_total}")
     print(f"total: {total}")
     print("thanks for shopping")
     print("hope you come again")

def main_menu():
  while True:
    print("\nMain menu")
    print("1.View products")
    print("2.Add/update products")
    print("3.Purchase items")
    print("4.Exit")
    choice=input("enter your choice = ")
    if choice=='1':
      view_prododucts()
    elif choice=='2':
      add_product()
    elif choice=='3':
      purchase_items()
    elif choice=='4':
      print("good bye!")
      break
    else:
      print("invalid choice, please try again!")
main_menu() 

