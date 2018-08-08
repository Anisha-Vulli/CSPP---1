'''

Author: Anisha Vulli
Date: 08 Aug 2018 

'''
def paying_debt(balance_up, annual_interest_rate, guess_num):
    '''function for paying debt'''
    balance_copy = balance_up

    iterator_i = 1
    while iterator_i <= 12:
        montly_interest_rate = annual_interest_rate / 12
        monthly_unpaid_balance = balance_copy - guess_num
        balance_copy = monthly_unpaid_balance + (montly_interest_rate * monthly_unpaid_balance)
        iterator_i += 1
    return balance_copy

def paying_debt_off_in_a_year(balance_up, annual_interest_rate):
    '''function for paying deft off in a year'''
    approximation_val = 0.03
    montly_interest_rate = annual_interest_rate /12.0
    high_val = (balance_up * (1 + montly_interest_rate) ** 12) / 12.0
    low_val = balance_up / 12
    middle_val = (low_val + high_val) / 2.0

    while abs(paying_debt(balance_up, annual_interest_rate, middle_val)) >= approximation_val:
        if approximation_val <= paying_debt(balance_up, annual_interest_rate, middle_val):
            low_val = middle_val
        else:
            high_val = middle_val
        middle_val = (low_val + high_val) / 2.0
    min_pay = middle_val
    return "Lowest Payment: "+str(round(min_pay, 2))


def paying_debt_off_in_a_year(balance, annualInterestRate):


def main():
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print(paying_debt_off_in_a_year(data[0],data[1]))
    
if __name__ == "__main__":
    main()
