from tabulate import tabulate
from datetime import datetime

rows_in_plane = []

total = []
a = []
number_of_tickets = 0
ticket_class = ["ECONOMY", "FIRST CLASS", "BUSINESS"]
header = "Name", "Age", "Gender", "Ticket Class", "Date and Time"

while True:

    number_of_ticket = int(input("How many seats are you buying:>>"))

    for i in range(number_of_ticket):
        name = str.upper(input("Type your full name as it appears in your passport:>>>"))
        age = input("Type your age:>>")
        gender = input("M or F:>>")
        ticket_ = str.upper(input("Select your ticket class: ECONOMY | FIRST CLASS | BUSINESS:>>"))
        today = datetime.now()
        total.append([name, age, gender, ticket_, today.strftime("%d/%m/%Y %H:%M:%S")])

    for j in range(number_of_ticket):
        n = "X"
        rows_in_plane += n

    if len(rows_in_plane) >= 100:
        print("There are no more seats available")

    print("\n")
    print(tabulate(total, headers=header))
    print("\n\nThese are the number of seats you've booked")
    print(rows_in_plane)
    print("\nThe number of seats available are:>>", 100 - len(rows_in_plane))

    break
