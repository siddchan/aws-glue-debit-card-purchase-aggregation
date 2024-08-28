import csv 
from random import randint, choice 

#define customer and bank names
customer_names = ["Alice Thomas", "Emma Thomas", "Emma White", "Robert Martin",
                               "Sophia Jackson", "James Brown", "Robert Johnson",
                               "Sophia Harris", "William Smith", "Michael Taylor"]

bank_names = ["State Bank of India", "HDFC Bank", "ICICI Bank", "Axis Bank", "Punjab National Bank"]

# define card types

card_types = ["VISA", "MasterCard", "RuPay"]

#define number of transaction per day
transaction_per_day = 15

# dictionary to store customer info(combined)
customer_info = {}

def generate_transaction(customer_name, current_date):
    """generate a mock transaction record with a specific date """
    if customer_name not in customer_info:
        card_number = f"{randint(1000, 9999)}-{randint(1000, 9999)}-{randint(1000, 9999)}-{randint(1000, 9999)}"
        bank_name = choice(bank_names)
        customer_info[customer_name] = {
            "customer_id" : randint(1000000000, 9999999999), #10-digit customer ID
            "debit_card_number": card_number,
            "debit_card_type": choice(card_types),
            "bank_name": bank_name,
        }

    # use retrieved info and add customer name

    transaction_data = customer_info[customer_name].copy
    transaction_data['name'] = customer_name

    # set transaction date to current day

    transaction_date = str(current_date)
    amount = round(randint(10, 100) + randint(0,99) / 100, 2) # up to 2 decimal places
    transaction_data['transaction_date'] = transaction_date
    transaction_data["amount_spend"] = amount
    return transaction_data


def generate_transactions(num_transactions, current_date):
    """generates a list of mock transaction records for a specific date"""
    transactions = []
    for _ in range(num_transactions):
        transactions.append(generate_transaction(choice(customer_names), current_date))
    return transactions

def write_to_csv(data, filename):
    """writes data to a csv file"""
    with open(filename, 'w', newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = ["customer_id", "name", "debit_card_number", "debit_card_type",
                                                      "bank_name", "transaction_date", "amount_spend"])
        writer.writeheader()
        writer.writerows(data)
    return

def generate_data(current_date, date_str):
    """"generate data and create csv files"""
    transactions = generate_transactions(transaction_per_day, current_date)
    write_to_csv(transactions, f"/tmp/transactions_{date_str}.csv")
    print(f"Generate mock transactionm data transactions _{date_str}.csv and saved in csv files")
    return

    