import pyrebase
from datetime import date
from datetime import datetime
from datetime import date
from datetime import timedelta

#####################get data from getinfo file################
import getinfo
# import stockinfo
# import coffeeinfo
import gasinfo
import curprice
import goldinfo
import meatinfo
import termsdata

##############################################################

terms = termsdata
data = getinfo
# stock = stockinfo
# coffee = coffeeinfo
gas = gasinfo
price = curprice
gold = goldinfo
meat = meatinfo

##################connect with firebase######################
config = {
    "apiKey": "AIzaSyDEiIoNNcXQQfY39hweZYD-7Kszay54ysA",
    "authDomain": "chateii.firebaseapp.com",
    "projectId": "chateii",
    "databaseURL": "https://chateii-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "storageBucket": "chateii.appspot.com",
    "messagingSenderId": "894785067698",
    "appId": "1:894785067698:web:b32bd733c4df58b1ddc7ab",
    "measurementId": "G-2VHTVEWWC5",
}

firebase = pyrebase.initialize_app(config)
database = firebase.database()


########################get today##################


def get_yesterday():
    today = date.today()
    yesterday = today - timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d")


def get_today():
    now = datetime.now()  # current date and time
    d = now.strftime("%Y-%m-%d")
    return d


today = get_today()
########################setdata#####################


#######################Analyse######################
# # stock
# stock_analyse = {
#     "Stock_daily_analy": stock.stock_daily_analise(),
#     "stock_weekly_analy": stock.stock_weekly_analise(),
# }
# # coffee
# coffee_analyse = {
#     "price_coffee_detail": coffee.coffee_daily_price(True),
#     "price_cofffee_summary": coffee.coffee_daily_price(False),
# }
# gold
gold_analyse = {
    "price_gold_detail": gold.gold_daily_price(True),
    "price_gold_summary": gold.gold_daily_price(False),
}
# meat
meat_analyse = {
    "price_meat_detail": meat.pig_daily_price(True),
    "price_meat_summary": meat.pig_daily_price(False),
}


#######################Price######################
# coffee
# coffee_name, coffee_average_price, coffee_change = coffee.data_coffee_table()
# gas
gas_name, gas_price, gas_change = gas.data_gas_table()

# curprice
talbe_price = price.bang_gia_ngoai_te()

# gold
(
    gold_name,
    gold_price_buy_td,
    gold_price_sell_td,
    gold_price_buy_yd,
    gold_price_sell_yd,
) = gold.data_gold_table()

##################Terms####################
# stock
# list_data_terms = terms.data_thuatngu_stock()

###################updata####################

##################Analyse####################
# stock
# database.child("ANALYSE").child(today).child("stock").set(stock_analyse)
# coffee
# database.child("ANALYSE").child(today).child("coffee").set(coffee_analyse)
# gold
database.child("ANALYSE").child(today).child("gold").set(gold_analyse)
# meat
database.child("ANALYSE").child(today).child("meat").set(meat_analyse)


##################Price####################
# gold
for i in range(len(gold_name) - 2):
    gold_data = {
        "price buy today": gold_price_buy_td[i],
        "price sell today": gold_price_sell_td[i],
        "price buy yesterday": gold_price_buy_yd[i],
        "price sell yesterday": gold_price_sell_yd[i],
    }
    database.child("PRICE").child(today).child("gold").child(gold_name[i]).set(
        gold_data
    )


# coffee
# for i in range(len(coffee_name) - 1):
#     coffee_data = {"average price": coffee_average_price[i], "change": coffee_change[i]}
#     database.child("PRICE").child(today).child("coffee").child(coffee_name[i]).set(
#         coffee_data
#     )


# gas
for i in range(len(gas_name)):
    gas_data = {"change": gas_change[i], "price": gas_price[i]}
    database.child("PRICE").child(today).child("gas").child(gas_name[i]).set(gas_data)

# currency price
for i in range(len(talbe_price)):
    price_data = {
        "Purchase price": talbe_price[i][1],
        "Transfer price": talbe_price[i][2],
        "Price": talbe_price[i][3],
    }
    database.child("PRICE").child(today).child("price").child(talbe_price[i][0]).set(
        price_data
    )

##################Terms####################

# stock
# for i in list_data_terms:
#     data_terms = {"terms": i[1], "type": i[2]}
#     database.child("TERMS").child(i[0]).set(data_terms)
