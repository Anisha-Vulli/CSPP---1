'''

Author : Anisha Vulli
Date: 08 Aug 2018


'''

def payingDebtOffInAYear(balance, annualInterestRate, monthlyPaymentRate):
	''' Function used to calucuate credit card balance ''' 
    i = 1
    balance_copy = balance
    while i <= 12:
        monthly_intr_rate = annual_interest_rate / 12.0
        min_monthly_pay = monthly_payment_rate * prev_balance
        monthly_unpaid_bal = prev_balance - min_monthly_pay
        balance_copy = monthly_unpaid_bal + (monthly_intr_rate * monthly_unpaid_bal)
        i += 1
    return "Remaining balance: " + str(round(balance_copy, 2))


def main():
	''' Main function '''
	data = input()
	data = data.split(' ')
	data = list(map(float, data))
	print(payingDebtOffInAYear(data[0],data[1],data[2]))

if __name__== "__main__":
	main()

