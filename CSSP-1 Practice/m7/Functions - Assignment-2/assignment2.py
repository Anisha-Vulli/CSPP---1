'''

Author: Anisha Vulli
Date: 08 Aug 2018
'''


def paying_debt_off_in_a_year(balance, annual_interest_rate):
    '''function to calculate the lowest monthly payment '''
    monthly_interest_rate = annual_interest_rate / 12
    monthly_payment = 0
    new_balance = balance
    while new_balance > 0:
        monthly_payment += 10
        new_balance = balance
        month = 1
        while month <= 12 and new_balance > 0:
            new_balance -= monthly_payment
            new_balance += (monthly_interest_rate * new_balance)
            month += 1
    return "Lowest Payment: " + str(monthly_payment)

def main():
	data = input()
	data = data.split(' ')
	data = list(map(float, data))
	print(paying_debt_off_in_a_year(data[0], data[1]))
	
if __name__ == "__main__":
	main()