import pyrebase
from datetime import date
from firebase import firebase

Firebase = firebase.FirebaseApplication(
    "https://chateii-default-rtdb.asia-southeast1.firebasedatabase.app/", None
)

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
today = date.today()
firebase = pyrebase.initialize_app(config)
database = firebase.database()

user_name = "gobi1708"


def get_user_data(user_name, today, Type, value):
    child = "User/" + user_name + "/" + f"{today}"
    data = Firebase.get(child, Type)
    return data.get(value)


def get_total_day(user_name, today):
    child = "User/" + user_name + "/" + f"{today}"
    data = Firebase.get(child, "Total")
    return data.get("Total day")


def updata_salary_user(user_name, date, salary):
    database.child("User").child(user_name).child(date.month).child("Salary").set(
        salary
    )


updata_salary_user(user_name, today, 200000)


def updata_user(user_name, date, Type, cost):
    try:
        total_price = get_user_data(user_name, date, Type, "Total")

    except:
        total_price = 0
    try:
        list_cost = get_user_data(user_name, date, Type, "Cost")

    except:
        list_cost = []

    try:
        total_day = get_total_day(user_name, date)

    except:
        total_day = 0

    total_price += cost
    list_cost.append(cost)
    dataset = {"Cost": list_cost, "Total": total_price}

    total_day += cost
    dataset_day = {"Total day": total_day}
    database.child("User").child(user_name).child(date.month).child(date).child(
        Type
    ).set(dataset)
    database.child("User").child(user_name).child(date.month).child(date).child(
        "Total"
    ).set(dataset_day)


updata_user(user_name, today, "food_section", 40)
