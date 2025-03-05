import csv

def load_exchange_rates(file_path):
    exchange_rates = {}
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                currency, rate = row[0].strip().upper(), float(row[1])
                exchange_rates[currency] = rate
    except Exception as e:
        print(f"Error loading exchange rates: {e}")
    return exchange_rates

def convert_currency(amount, currency, rates):
    return amount * rates.get(currency, None) if currency in rates else None

def main():
    file_path = r"C:\Users\tin\Desktop\2nd Year\2nd term\Integrated Programming and Technologies\Activity_4B\currency.csv"

    rates = load_exchange_rates(file_path)
    
    try:
        amount = float(input("How much dollar do you have? "))
        currency = input("What currency you want to have? ").strip().upper()

        converted_amount = convert_currency(amount, currency, rates)
        
        if converted_amount is not None:
            print(f"\nDollar: {amount:.2f} USD")
            print(f"{currency}: {converted_amount:.6f}")
        else:
            print("Currency not found in exchange rates.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
