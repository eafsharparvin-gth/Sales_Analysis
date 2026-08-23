import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
# ijade DataSet. ( 4 Table dade avalie ), bad save dar excel foldere: data, jahate estefade.

products =  [
    ["P001", "Green Tea", "Tea", 2.8],
    ["P002", "Black Tea", "Tea",2.4],
    ["P003", "Chamomile Tea", "Tea", 3.2],
    ["P004", "Honey 250g", "Honey", 5.5],
    ["P005", "Honey 500g", "Honey", 9.8],
    ["P006", "Raisins", "Dried Fruits", 4.2],
    ["P007", "Pistachio", "Nuts", 11.5],
    ["P008", "Almond", "Nuts", 8.6],
    ["P009", "Saffron", "Spice", 15],
    ["P010", "Herbal Mix", "Herbal", 3.9]
    ]

products_df = pd.DataFrame(
    products,
    columns = [
    "Product_ID",
    "Product",
    "Category",
    "Unit_Cost"
    ]
)

products_df.to_excel(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\data\products.xlsx", index=False)
print(products_df.head())

customers = [
    ["C001", "Alborz Market", "Tehran", "Retail"],
    ["C002", "Shirin Store", "Shiraz", "Wholesale"],
    ["C003", "Pars Food", "Isfahan", "Retail"],
    ["C004", "Mehr Shop", "Mashhad", "Retail"],
    ["C005", "Sabz Market", "Tabriz", "Wholesale"],
    ["C006", "Atlas Store", "Tehran", "Retail"],
    ["C007", "Ariana Food", "Shiraz", "Wholesale"],
    ["C008", "Baran Market", "Mashhad", "Retail"],
    ["C009", "Negin Shop", "Isfahan", "Retail"],
    ["C010", "Kian Store", "Tabriz", "Wholesale"],
    ["C011", "Omid Market", "Tehran", "Retail"],
    ["C012", "Dorsa Shop", "Shiraz", "Retail"],
    ["C013", "Rayan Food", "Mashhad", "Wholesale"],
    ["C014", "Setare Store", "Isfahan", "Retail"],
    ["C015", "Yas Market", "Tehran", "Wholesale"]
]

customers_df = pd.DataFrame(
    customers, columns= [
        "Customer_ID",
        "Customer",
        "City",
        "Customer_Type"
    ]
)

customers_df.to_excel(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\data\customers.xlsx", index=False)
print(customers_df.head())

salespersons = []

names_ = [
    "James",
    "Michael",
    "David",
    "Daniel",
    "William"
]

region_ = [
    "North",
    "South",
    "East",
    "West",
    "Central"
]

for i in range(5):
    salespersons.append(
        [
            f"S{i+1:03}",
            names_[i],
            region_[i]
        ]
    )
salespersons_df = pd.DataFrame(
    salespersons,
    columns=[
        "Salesperson_ID",
        "Salesperson",
        "Region"
    ]
)

salespersons_df.to_excel(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\data\salespersons.xlsx", index=False)
print(salespersons_df)

# tolide dataset 100 adadi Orders:
number_of_orders = 100
orders = [] # liste khalie sefaresh ha
# az inja be bad ba random mikhaim kar konim
start_date = datetime(2025, 1 ,1) # tarife tarikhe shoru,
for i in range(number_of_orders):
    order_id = f"O{i+1:03}" # az 1 start kon ta 100 be surate se sefr... 0001, 0002... 0100.
    #print(order_id)
    customer_id = random.choice(customers_df["Customer_ID"])
    product_id = random.choice(products_df["Product_ID"])
    unit_price = products_df.loc[
        products_df["Product_ID"] == product_id,
        "Unit_Cost"
    ].iloc[0] # masalan tamam satr haei ke P004 hastano peyda mikone, az un satr faghat Unit_Cost ro barmidare,
    # chon faghat yek meghdar peyda mishe hamun meghdare aval ro barmidare.
    #print(order_id,product_id,unit_price) # test az order id ta inja. ok
    salesperson_id = random.choice(salespersons_df["Salesperson_ID"])

    random_days = random.randint(0,180)# be hamrahe satre paein:
    order_date = start_date + timedelta(days=random_days) #ye adad 0-180 misaze bad un tedad ro be 1.1.2025 ezafe mikone
    quantity = random.randint(1,25)
    discount = random.choice([0,0,0,5,10,15]) # karesh: be surate tasadofi yeki az maghadiresho entekhab mikone,
    # chon 3 ta 0 gozashtim ehtemale sefareshe bedune takhfif bihtare mesle vagheyat.
    # hengame mohasebe ham : discount/ 100 , chon bedune darsad neveshtim tu list maghadiro.
    #print(order_id,product_id,unit_price,quantity,discount) # teste discount

    #print(order_id,customer_id,product_id,salesperson_id,order_date.date(), quantity) #test order_date.date(): jahate hazfe sotune saat.

#  az satre 102 ta 116 dar bala dataye 4 sotune misaze ke har sotun marbut be ye chize.
## hal berim soraghe tarikhe tasadofi ( ke dar bala az satre 118 - 110 ezafe mikonim:..)
### bad mirim soraghe quantity: az satre 116, --> dobare baraye test quantity ro ham be entehaye print ezafe mikonim,
### sotune 6 ham baz mishe havie meghdare tasadofi baraye har satr.
#### unit_price: tasadofi ino dg tolid nemikonim, gheymate har mahsul tuye jadvale product moshakhase bayad bere az un jadval bekhune.
#### dakhele halghe bala bad az product_id ezafe mikonim:

## marhale bad: ---> Total Amount : bakhshi ke KPI ha badan az hamin sotun estefade mikonan.
# 1) mohasebe mablaghe takhfif:
    discount_amount = (unit_price * quantity * (discount / 100))
# 2) mohasebe mablaghe nahaei:
    total_amount = (unit_price * quantity ) - discount_amount
# 3) herfei ta: aashare pul ta 2 ragham bashe.
    total_amount = round(total_amount, 2)
    ## badan in 2  sotuno ham ezafe kardim:
    payment_method = random.choice([
        "Cash",
        "Card",
        "Online"
    ])
    order_status = random.choice([
        "Delivered",
        "Delivered",
        "Delivered",
        "Pending",
        "Cancelled"
    ])

    warehouse_ID = random.choice(["W001", "W002", "W003"])
#print(order_id,unit_price,quantity,discount,total_amount) # test
## ---> 3 marhale nahaei va aslie sakhte dataset: --->
    orders.append([
    order_id,
    customer_id,
    product_id,
    salesperson_id,
    order_date.date(),
    quantity,
    unit_price,
    discount,
    payment_method,
    order_status,
    total_amount,
    warehouse_ID
    ])
# etmame halghe bala !!!
orders_df = pd.DataFrame(
    orders,
    columns= [
        "Order_ID",
        "Customer_ID",
        "Product_ID",
        "Salesperson_ID",
        "Order_Date",
        "Quantity",
        "Unit_price",
        "Discount",
        "Payment_Method",
        "Order_Status",
        "Total_Amount",
        "warehouse_ID"
    ]
)

print(orders_df.head()) # test
orders_df.to_excel(r"D:\Program\pycharm\my projects\p04 Sales Performance Analysis\data\orders.xlsx", index=False)