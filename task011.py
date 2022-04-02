your_balance: int = 20000  # global


def my_new_balance(monthly_income: int, tax_in_percents: int, compulsory_expenses: int) -> str:
    profit: int = round(monthly_income * (1 - tax_in_percents / 100) - compulsory_expenses)  # enclosed

    def output() -> str:
        your_name: str = 'Azat'  # local
        return your_name + ', your new balance is ' + str(profit + your_balance)

    return output()


if __name__ == '__main__':
    print(my_new_balance(50000, 13, 15000))

