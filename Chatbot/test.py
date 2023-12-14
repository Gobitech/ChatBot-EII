import pyrebase
from datetime import date
from firebase import firebase
from datetime import datetime
import re

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
Today = today.strftime("%Y-%m-%d")
user_name = "thai4362"


def StrToDate(Date):
    datetime_object = datetime.strptime(Date, "%Y-%m-%d")
    return datetime_object


def get_spending_day(user_name, today, Type, value):
    child = "User/" + user_name + "/" + f"{StrToDate(today).month}" "/" + f"{today}"
    data = Firebase.get(child, Type)
    return data.get(value)


def get_spending_month(user_name, month, value):
    child = "User/" + user_name + "/" + f"{month}"
    data = Firebase.get(child, "Summary")
    return data.get(value)


def get_total_month(user_name, date):
    child = "User/" + user_name + "/" + f"{StrToDate(date).month}" + "/" + "Summary"
    data = Firebase.get(child, "Total spending")
    return data


def get_total_day(user_name, today):
    child = "User/" + user_name + "/" + f"{StrToDate(today).month}"
    data = Firebase.get(child, f"{today}")
    return data.get("Total")


def get_salary(user_name, month):
    child = "User/" + user_name + "/" + f"{month}"
    data = Firebase.get(child, "Summary")
    return data.get("Salary")


def updata_user(user_name, month, date, Type, cost):
    try:
        total_price = get_spending_day(user_name, date, Type, "Total")

    except:
        total_price = 0
    try:
        value_month = get_spending_month(user_name, month, Type)
        if value_month == None:
            value_month = 0
    except:
        value_month = 0
    try:
        list_cost = get_spending_day(user_name, date, Type, "Cost")

    except:
        list_cost = []

    try:
        total_day = get_total_day(user_name, date)

    except:
        total_day = 0
    try:
        total_month = get_total_month(user_name, date)
    except:
        total_month = 0
    value_month += cost
    total_month += cost
    total_price += cost
    list_cost.append(cost)
    dataset = {"Cost": list_cost, "Total": total_price}
    total_day += cost

    database.child("User").child(user_name).child(month).child(date).child(Type).set(
        dataset
    )
    database.child("User").child(user_name).child(month).child(date).child("Total").set(
        total_day
    )
    database.child("User").child(user_name).child(month).child("Summary").child(
        "Total spending"
    ).set(total_month)
    database.child("User").child(user_name).child(month).child("Summary").child(
        Type
    ).set(value_month)


def updata_salary_user(user_name, date, salary):
    database.child("User").child(user_name).child(StrToDate(date).month).child(
        "Summary"
    ).child("Salary").set(salary)


def change_money(k_money, m_money):
    if k_money != None and m_money != None:
        k_money = int([float(x) for x in re.findall(r"-?\d+\.?\d*", k_money)][0]) * 1000
        m_money = (
            int([float(x) for x in re.findall(r"-?\d+\.?\d*", m_money)][0]) * 1000000
        )
        money = k_money + m_money
        return money
    else:
        if k_money != None:
            return (
                int([float(x) for x in re.findall(r"-?\d+\.?\d*", k_money)][0]) * 1000
            )
        else:
            return (
                int([float(x) for x in re.findall(r"-?\d+\.?\d*", m_money)][0])
                * 1000000
            )


def check_spending(user_name, month, today):
    text = ""
    try:
        Salary = get_salary(user_name, month)
        if Salary == None:
            text = "Bạn chưa cập nhật lương tháng này! Vui lòng cập nhật lương để hổ trợ việc đo lường"
            return text
    except:
        Salary = -1
        text = "Bạn chưa cập nhật lương tháng này! Vui lòng cập nhật lương để hổ trợ việc đo lường"
        return text
    try:
        Total_spending = get_total_day(user_name, today)
        if Total_spending == None:
            Total_spending = 0
    except:
        Total_spending = 0

    if Salary == Total_spending:
        text = "Bạn đã sử dụng hết lương tháng này!! Vui lòng hạn chế sủ dụng tiền lại hoặc cố gắng tìm thêm thu nhập cho tháng này!! :>"
        return text
    elif Salary < Total_spending:
        text = "Bạn đã sử dụng lố tiền lương tháng này!! Vui lòng hạn chế sủ dụng tiền lại hoặc cố gắng tìm thêm thu nhập cho tháng này!! :>"
        return text


def statistical_day(user_name, Today):
    List_data = []
    food = None
    personal = None
    recreation = None
    housing = None
    try:
        print("hello")
        food = get_spending_day(user_name, Today, "food_section", "Total")
    except:
        food = 0
    try:
        personal = get_spending_day(user_name, Today, "personal_section", "Total")
    except:
        personal = 0
    try:
        recreation = get_spending_day(user_name, Today, "recreation_section", "Total")
    except:
        recreation = 0
    try:
        housing = get_spending_day(user_name, Today, "housing_section", "Total")
    except:
        housing = 0

    List_data.append(food)
    List_data.append(personal)
    List_data.append(recreation)
    List_data.append(housing)
    return List_data


print(Today)
print(statistical_day(user_name, Today))
