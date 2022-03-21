import matplotlib.pyplot as plt

class Income():
    '''
    A class that represents the income of a person for a whole year.

    Attributes:
    -----------
    year : int
        year of the salary
    month : int
        month of the salary
    salary : float
        salary amount
    bonus : float
        bonus amount
    
    Methods:
    --------
    monthly_income(month):
        calculates and return the total income for a specific month. Total income = salary + bonus
    add_income(year, month, salary = 0.0, bonus = 0.0):
        allows to add income data (i.e. salary and bonus) for a specific month/year.
    update_salary(year, month, salary):
        allows to change the salary for a specific month/year.
    update_bonus(year, month, bonus):
        allows to change bonus for a specific month/year.
    '''

    def __init__(self, year, month, salary, bonus):
        '''
        Constructs the income database of the account for the whole year. It creates a placeholder/container for salary, 
        bonus and total income for every month of the year and initializes all values with 0.

        Parameters:
        -----------
        year : int
            year in which that salary/bonus was given
        month : int
            month in which that salary/bonus was given
        salary : float
            amount of salary for that month
        bonus : float
            amount of bonus for that month
        '''
        try:
            if isinstance(year, int) or year == None:
                self.year = year
            else:
                raise Exception("Invalid Year: Please enter a valid integer value for year")
            if month !=None and month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                                              'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if isinstance(salary, float) or isinstance(salary, int) or salary == None:
                self.__salary = salary
            else:
                raise Exception("Invalid Salary: Please enter a valid integer or float value for salary")
            if isinstance(bonus, float) or isinstance(bonus, int) or bonus == None:
                self.__bonus = bonus
            else:
                raise Exception("Invalid Bonus: Please enter a valid integer or float value for bonus")
            self.income = {self.year: {"January": {"salary": 0.0, "bonus": 0.0, "total": 0.0}, 
                                       "February": {"salary": 0.0, "bonus": 0.0, "total": 0.0}, 
                                       "March": {"salary": 0.0, "bonus": 0.0, "total": 0.0}, 
                                       "April": {"salary": 0.0, "bonus": 0.0, "total": 0.0}, 
                                       "May": {"salary": 0.0, "bonus": 0.0, "total": 0.0}, 
                                       "June": {"salary": 0.0, "bonus": 0.0, "total": 0.0}, 
                                       "July": {"salary": 0.0, "bonus": 0.0, "total": 0.0}, 
                                       "August": {"salary": 0.0, "bonus": 0.0, "total": 0.0}, 
                                       "September": {"salary": 0.0, "bonus": 0.0, "total": 0.0}, 
                                       "October": {"salary": 0.0, "bonus": 0.0, "total": 0.0}, 
                                       "November": {"salary": 0.0, "bonus": 0.0, "total": 0.0}, 
                                       "December": {"salary": 0.0, "bonus": 0.0, "total": 0.0},
                                       "Total": {"salary": 0.0, "bonus": 0.0, "total": 0.0}}}
            if salary != None:
                self.income[year][month]["salary"] = salary
            if bonus != None:
                self.income[year][month]["bonus"] = bonus
            if salary != None and bonus != None:
                self.income[year][month]["total"] = self.__salary + self.__bonus
            if salary != None:
                self.income[year]["Total"]["salary"] = self.__salary 
            if bonus != None:
                self.income[year]["Total"]["bonus"] = self.__bonus
            if salary != None and bonus != None:
                self.income[year]["Total"]["total"] = self.__salary + self.__bonus
        except Exception as e:
            print(e)

    def __str__(self):
        '''
        Returns/displays a table with income data for the whole year.
        '''
        try:
            display = ("*" * 60
                + "\n {:s}".format((" " * 20) + "INCOME - " + str(self.year)) 
                + "\n{a:<15s} {b:<15s} {c:<15s} {d:<15s}".format(a="MONTH", b="SALARY", c="BONUS", d="TOTAL") 
                + "\n" + ("*" * 60) + "\n")
            for val in self.income[self.year].items():
                display += "{a:<15s} {b:<15.2f} {c:<15.2f} {d:<15.2f}".format(a=val[0], b=val[1]["salary"], c=val[1]["bonus"], \
                            d=val[1]["total"]) + "\n" 
            display += ("*" * 60) + "\n"
            print(display)
        except Exception as e:
            print(e)

    def monthly_income(self, month):
        '''
        Returns the total income for the specified month.

        Parameters:
        -----------
        month : str
            month for which total income needs to be determined
        '''
        try:
            return "Total income in " + str(month) + ": ${}".format(self.income[self.year][month]["total"])
        except Exception as e:
            print(e)

    def add_income(self, month, salary, bonus):
        '''
        Allows to add income data and records it in the database.

        Parameters:
        -----------
        month : str
            month of the year for income has to be added
        salary : float
            amount of salary for that month
        bonus : float
            amount of bonus for that month 
        '''
        try:
            if month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                             'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if not isinstance(salary, float) and not isinstance(salary, int):
                raise Exception("Invalid Salary: Please enter a valid integer or float value for salary")
            if not isinstance(bonus, float) and not isinstance(bonus, int):
                raise Exception("Invalid Bonus: Please enter a valid integer or float value for bonus")
            self.income[self.year][month]["salary"] += salary
            self.income[self.year][month]["bonus"] += bonus
            self.income[self.year][month]["total"] += (salary + bonus)
            self.income[self.year]["Total"]["salary"] += salary
            self.income[self.year]["Total"]["bonus"] += bonus
            self.income[self.year]["Total"]["total"] += (salary + bonus)
            return "Income has been added"
        except Exception as e:
            print(e)
    
    def update_salary(self, month, salary):
        '''
        Allows to change/update the salary amount for a particular month.

        Parameters:
        -----------
        month : str
            month for which the salary needs to be changed
        salary : float
            correct amount of salary
        '''
        try:
            if month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                             'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if not isinstance(salary, float) and not isinstance(salary, int):
                raise Exception("Invalid Salary: Please enter a valid integer or float value for salary")
            temp = self.income[self.year][month]["salary"]
            self.income[self.year][month]["salary"] = salary
            self.income[self.year][month]["total"] += (salary - temp)
            self.income[self.year]["Total"]["salary"] += (salary - temp)
            self.income[self.year]["Total"]["total"] += (salary - temp)
            return "Salary has been updated"
        except Exception as e:
            print(e)
    
    def update_bonus(self, month, bonus):
        '''
        Allows to change/update the bonus amount for a partciular month.

        Parameters:
        -----------
        month : str
            month for which bonus needs to be changed
        bonus : float
            correct amount of bonus
        '''
        try:
            if month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                             'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if not isinstance(bonus, float) and not isinstance(bonus, int):
                raise Exception("Invalid Bonus: Please enter a valid integer or float value for bonus")
            temp = self.income[self.year][month]["bonus"]
            self.income[self.year][month]["bonus"] = bonus
            self.income[self.year][month]["total"] += (bonus - temp)
            self.income[self.year]["Total"]["bonus"] += (bonus - temp)
            self.income[self.year]["Total"]["total"] += (bonus - temp)
            return "Bonus has been updated"
        except Exception as e:
            print(e)

class Expense():
    '''
    A class that represents the expenses of a person for a whole year.

    Attributes:
    -----------
    year : int
        year in which expenses occured
    month : int
        month in which expenses occured
    rent : float
        amount of rent for a month
    grocery : float
        total grocery expenditures of a month
    auto : float
        total auto expenditures of a month
    medical : float
        total medical expenditures of a month
    other : float
        any other expenditures of a month

    Methods:
    --------
    monthly_expenses(month):
        calculates and return the total expenses for a specific month. Total expenses = rent + grocery + auto + medical + other
    add_expenses(year, month, rent, grocery, auto, medical, other):
        allows to add expenses data for a specific month/year.
    update_rent(year, month, rent):
        allows to change the rent amount for a specific month/year
    update_grocery(year, month, grocery):
        allows to change the total grocery expenditures for a specific month/year.
    update_auto_expenses(year, month, auto):
        allows to change the total auto expenditures for a specific month/year.
    update_medical_expenses(year, month, medical):
        allows to change the total medical expenditures for a specific month/year.
    update_other_expenses(year, month, other):
        allows to change the amount of other expenses for a specific month/year.
    '''
    
    def __init__(self, year, month, rent, grocery, auto, medical, other):
        '''
        Constructs the expense database of the account for the whole year. It creates a placeholder/container for rent, grocery, auto, medical
        and other expenses for every month of the year and initializes all values with 0.

        Parameters:
        -----------
        year : int
            year in whcih expneses occured
        month : int
            month in which expenses occured
        rent : float
            amount of rent for a month
        grocery : float
            total grocery expenditures of a month
        auto : float
            total auto expenditures of a month
        medical : float
            total medical expenditures of a month
        other : float
            any other expenditures of a month
        '''
        try:
            if isinstance(year, int) or year == None:
                self.year = year
            else:
                raise Exception("Invalid Year: Please enter a valid integer value for year")
            if month !=None and month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                                              'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if isinstance(rent, float) or isinstance(rent, int) or rent == None:
                self.__rent = rent
            else:
                raise Exception("Invalid Rent: Please enter a valid integer or float value for rent")
            if isinstance(grocery, float) or isinstance(grocery, int) or grocery == None:
                self.__grocery = grocery
            else:
                raise Exception("Invalid Grocery: Please enter a valid integer or float value for grocery expenses")
            if isinstance(auto, float) or isinstance(auto, int) or auto == None:
                self.__auto = auto
            else:
                raise Exception("Invalid Auto: Please enter a valid integer or float value for auto expenses")
            if isinstance(medical, float) or isinstance(medical, int) or medical == None:
                self.__medical = medical
            else:
                raise Exception("Invalid Medical: Please enter a valid integer or float value for medical expenses")
            if isinstance(other, float) or isinstance(other, int) or other == None:
                self.__other = other
            else:
                raise Exception("Invalid Other: Please enter a valid integer or float value for other expenses")
            self.expenses = {self.year: {"January": {"rent": 0.0, "grocery": 0.0, "auto": 0.0, "medical": 0.0, "other": 0.0, "total": 0.0}, 
                                         "February": {"rent": 0.0, "grocery": 0.0, "auto": 0.0, "medical": 0.0, "other": 0.0, "total": 0.0}, 
                                         "March": {"rent": 0.0, "grocery": 0.0, "auto": 0.0, "medical": 0.0, "other": 0.0, "total": 0.0}, 
                                         "April": {"rent": 0.0, "grocery": 0.0, "auto": 0.0, "medical": 0.0, "other": 0.0, "total": 0.0}, 
                                         "May": {"rent": 0.0, "grocery": 0.0, "auto": 0.0, "medical": 0.0, "other": 0.0, "total": 0.0}, 
                                         "June": {"rent": 0.0, "grocery": 0.0, "auto": 0.0, "medical": 0.0, "other": 0.0, "total": 0.0}, 
                                         "July": {"rent": 0.0, "grocery": 0.0, "auto": 0.0, "medical": 0.0, "other": 0.0, "total": 0.0}, 
                                         "August": {"rent": 0.0, "grocery": 0.0, "auto": 0.0, "medical": 0.0, "other": 0.0, "total": 0.0}, 
                                         "September": {"rent": 0.0, "grocery": 0.0, "auto": 0.0, "medical": 0.0, "other": 0.0, "total": 0.0}, 
                                         "October": {"rent": 0.0, "grocery": 0.0, "auto": 0.0, "medical": 0.0, "other": 0.0, "total": 0.0}, 
                                         "November": {"rent": 0.0, "grocery": 0.0, "auto": 0.0, "medical": 0.0, "other": 0.0, "total": 0.0}, 
                                         "December": {"rent": 0.0, "grocery": 0.0, "auto": 0.0, "medical": 0.0, "other": 0.0, "total": 0.0}, 
                                         "Total": {"rent": 0.0, "grocery": 0.0, "auto": 0.0, "medical": 0.0, "other": 0.0, "total": 0.0}}}
            if rent != None:
                self.expenses[year][month]["rent"] = rent
            if grocery != None:
                self.expenses[year][month]["grocery"] = grocery
            if auto != None:
                self.expenses[year][month]["auto"] = auto
            if medical != None:
                self.expenses[year][month]["medical"] = medical
            if other != None:
                self.expenses[year][month]["other"] = other 
            if rent != None and grocery != None and auto != None and medical != None and other != None:
                self.expenses[year][month]["total"] = self.__rent + self.__grocery + self.__auto + self.__medical + self.__other
                self.expenses[year]["Total"]["total"] = self.__rent + self.__grocery + self.__auto + self.__medical + self.__other
        except Exception as e:
            print(e)

    def __str__(self):
        '''
        Returns/displays a table with all the expenses of whole year.
        '''
        try:
            display = (("*" * 109)
            + "\n {:s}".format((" " * 43) + "EXPENSES - " + str(self.year))
            + "\n{a:<15s} {b:<15s} {c:<15s} {d:<15s} {e:<15s} {f:<15s} {g:<15s}".format(a="MONTH", b="RENT", c="GROCERY", d="AUTO", e="MEDICAL", \
            f="OTHER", g="TOTAL") 
            + "\n" + ("*" * 109) + "\n")
            for val in self.expenses[self.year].items():
                display += "{a:<15s} {b:<15.2f} {c:<15.2f} {d:<15.2f} {e:<15.2f} {f:<15.2f} {g:<15.2f}".format(a=val[0], b=val[1]["rent"], \
                c=val[1]["grocery"], d=val[1]["auto"], e=val[1]["medical"], f=val[1]["other"], g=val[1]["total"]) + "\n" 
            display += ("*" * 109) + "\n"
            print(display)
        except Exception as e:
            print(e)

    def monthly_expenses(self, month):
        '''
        Returns the total expenses for the specified month.

        Parameters:
        -----------
        month : str
            month for which total expneses need to be determined 
        '''
        try:
            return "Total expenses in " + str(month) + ": ${}".format(self.expenses[self.year][month]["total"])
        except Exception as e:
            print(e)

    def add_expenses(self, month, rent, grocery, auto, medical, other):
        '''
        Allows to add expenses and records it in the database.

        Parameters:
        -----------
        month : int
            month in which expenses occured
        rent : float
            amount of rent for a month
        grocery : float
            total grocery expenditures of a month
        auto : float
            total auto expenditures of a month
        medical : float
            total medical expenditures of a month
        other : float
            any other expenditures of a month
        '''
        try:
            if month !=None and month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                                              'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if not isinstance(rent, float) and not isinstance(rent, int) and rent != None:
                raise Exception("Invalid Rent: Please enter a valid integer or float value for rent")
            if not isinstance(grocery, float) and not isinstance(grocery, int) and grocery != None:
                raise Exception("Invalid Grocery: Please enter a valid integer or float value for grocery expenses")
            if not isinstance(auto, float) and not isinstance(auto, int) and auto != None:
                raise Exception("Invalid Auto: Please enter a valid integer or float value for auto expenses")
            if not isinstance(medical, float) and not isinstance(medical, int) and medical != None:
                raise Exception("Invalid Medical: Please enter a valid integer or float value for medical expenses")
            if not isinstance(other, float) and not isinstance(other, int) and other != None:
                raise Exception("Invalid Other: Please enter a valid integer or float value for other expenses")
            self.expenses[self.year][month]["rent"] += rent
            self.expenses[self.year][month]["grocery"] += grocery
            self.expenses[self.year][month]["auto"] += auto
            self.expenses[self.year][month]["medical"] += medical
            self.expenses[self.year][month]["other"] += other
            self.expenses[self.year][month]["total"] += (rent + grocery + auto + medical + other)
            self.expenses[self.year]["Total"]["rent"] += rent
            self.expenses[self.year]["Total"]["grocery"] += grocery
            self.expenses[self.year]["Total"]["auto"] += auto
            self.expenses[self.year]["Total"]["medical"] += medical
            self.expenses[self.year]["Total"]["other"] += other
            self.expenses[self.year]["Total"]["total"] += (rent + grocery + auto + medical + other)
            return "Expenses have been added"
        except Exception as e:
            print(e)
    
    def update_rent(self, month, rent):
        '''
        Allows to change/update the rent amount for a particular month.

        Parameters:
        -----------
        month : str
            month for which the rent needs to be changed
        rent : float
            correct amount of rent
        '''
        try:
            if month !=None and month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                                              'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if not isinstance(rent, float) and not isinstance(rent, int):
                raise Exception("Invalid Rent: Please enter a valid integer or float value for rent")
            temp = self.expenses[self.year][month]["rent"] 
            self.expenses[self.year][month]["rent"] = rent
            self.expenses[self.year][month]["total"] += (rent - temp)
            self.expenses[self.year]["Total"]["rent"] += (rent - temp)
            self.expenses[self.year]["Total"]["total"] += (rent - temp)
            return "Rent has been updated"
        except Exception as e:
            print(e)

    def update_grocery(self, month, grocery):
        '''
        Allows to change/update the grocery expenditures for a particular month.

        Parameters:
        -----------
        month : str
            month for which the grocery expenditures needs to be changed
        grocery : float
            correct amount of grocery expenditures
        '''
        try:
            if month !=None and month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                                              'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if not isinstance(grocery, float) and not isinstance(grocery, int):
                raise Exception("Invalid Grocery: Please enter a valid integer or float value for grocery expenses")
            temp = self.expenses[self.year][month]["grocery"] 
            self.expenses[self.year][month]["grocery"] = grocery
            self.expenses[self.year][month]["total"] += (grocery - temp)
            self.expenses[self.year]["Total"]["grocery"] += (grocery - temp)
            self.expenses[self.year]["Total"]["total"] += (grocery - temp)
            return "Grocery has been updated"
        except Exception as e:
            print(e)
    
    def update_auto_expenses(self, month, auto):
        '''
        Allows to change/update auto expenditures for a particular month.

        Parameters:
        -----------
        month : str
            month for which the auto expenditures needs to be changed
        auto : float
            correct amount of auto expensitures
        '''
        try:
            if month !=None and month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                                              'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if not isinstance(auto, float) and not isinstance(auto, int):
                raise Exception("Invalid Auto: Please enter a valid integer or float value for auto expenses")
            temp = self.expenses[self.year][month]["auto"] 
            self.expenses[self.year][month]["auto"] = auto
            self.expenses[self.year][month]["total"] += (auto - temp)
            self.expenses[self.year]["Total"]["auto"] += (auto - temp)
            self.expenses[self.year]["Total"]["total"] += (auto - temp)
            return "Auto expenses have been updated"
        except Exception as e:
            print(e)
    
    def update_medical_expenses(self, month, medical):
        '''
        Allows to change/update medical expenditures for a particular month.

        Parameters:
        -----------
        month : str
            month for which the auto expenditures needs to be changed
        auto : float
            correct amount of auto expenditures
        '''
        try:
            if month !=None and month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                                              'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if not isinstance(medical, float) and not isinstance(medical, int):
                raise Exception("Invalid Medical: Please enter a valid integer or float value for medical expenses")
            temp = self.expenses[self.year][month]["medical"] 
            self.expenses[self.year][month]["medical"] = medical
            self.expenses[self.year][month]["total"] += (medical - temp)
            self.expenses[self.year]["Total"]["medical"] += (medical - temp)
            self.expenses[self.year]["Total"]["total"] += (medical - temp)
            return "Medical expenses have been updated"
        except Exception as e:
            print(e)

    def update_other_expenses(self, month, other):
        '''
        Allows to change/update the amount of other expenses for a particular month.

        Parameters:
        -----------
        month : str
            month for which other expenses needs to be changed
        other : float
            correct amount of other expenses
        '''
        try:
            if month !=None and month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                                              'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if not isinstance(other, float) and not isinstance(other, int):
                raise Exception("Invalid Other: Please enter a valid integer or float value for other expenses")
            temp = self.expenses[self.year][month]["other"] 
            self.expenses[self.year][month]["other"] = other
            self.expenses[self.year][month]["total"] += (other - temp)
            self.expenses[self.year]["Total"]["other"] += (other - temp)
            self.expenses[self.year]["Total"]["total"] += (other - temp)
            return "Other expenses have been updated"
        except Exception as e:
            print(e)

class Investment():
    '''
    A class that represents the investments of a person for a whole year.

    Attributes:
    -----------
    year : int
        year in which investments were done
    month : int
        month in which investments were done
    stocks : float
        money invested in stocks in a given month
    crypto : float
        money invested in crypto currency in a given month
    retirement_fund : float
        retirement fund contribution of a given month
    realstate : float
        money inevested in realstate in a given month

    Methods:
    --------
    monthly_investment(month):
        calculates and return the total investment for a specific month. Total investment = stocks + crypto + retirement_fund + realstate
    add_investment(month, stocks, crypto, retirement_fund, realstate):
        allows to add investment data for a specific month/year.
    update_stocks(month, stocks):
        allows to change the amount of stocks investment for a specific month/year
    update_crypto(month, crypto):
        allows to change the amount of crypto investment for a specific month/year.
    update_retirement_fund(month, retirement_fund):
        allows to change the 401K contribution for a specific month/year.
    update_realstate(month, realstate):
        allows to change the real state investment for a specific month/year.
    '''

    def __init__(self, year, month, stocks, crypto, retirement_fund, realstate):
        '''
        Constructs the investment database of the account for the whole year. It creates a placeholder/container to record value of money invested 
        in stocks, crypto currency, 401K and real state for the whole year and initializes all values with 0.

        Parameters:
        -----------
        year : int
            year in which investments were done
        month : int
            month in which investments were done
        stocks : float
            money invested in stocks in a given month
        crypto : float
            money invested in crypto currency in a given month
        retirement_fund : float
            retirement fund contribution of a given month
        realstate : float
            money inevested in realstate in a given month
        '''
        try:
            if isinstance(year, int) or year == None:
                self.year = year
            else:
                raise Exception("Invalid Year: Please enter a valid integer value for year")
            if month !=None and month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                                              'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if not isinstance(stocks, float) and not isinstance(stocks, int) and stocks != None:
                raise Exception("Invalid Stocks: Please enter a valid integer or float value for stock investment")
            if not isinstance(crypto, float) and not isinstance(crypto, int) and crypto != None:
                raise Exception("Invalid Crypto: Please enter a valid integer or float value for crypto investment")
            if not isinstance(retirement_fund, float) and not isinstance(retirement_fund, int) and retirement_fund != None:
                raise Exception("Invalid 401K: Please enter a valid integer or float value for 401K contribution")
            if not isinstance(realstate, float) and not isinstance(realstate, int) and realstate != None:
                raise Exception("Invalid Realstate: Please enter a valid integer or float value for real state investment")
            self.investments = {self.year: {"January": {"stocks": 0.0, "crypto": 0.0, "retirement_fund": 0.0, "realstate": 0.0, "total": 0.0}, 
                                            "February": {"stocks": 0.0, "crypto": 0.0, "retirement_fund": 0.0, "realstate": 0.0, "total": 0.0}, 
                                            "March": {"stocks": 0.0, "crypto": 0.0, "retirement_fund": 0.0, "realstate": 0.0, "total": 0.0}, 
                                            "April": {"stocks": 0.0, "crypto": 0.0, "retirement_fund": 0.0, "realstate": 0.0, "total": 0.0}, 
                                            "May": {"stocks": 0.0, "crypto": 0.0, "retirement_fund": 0.0, "realstate": 0.0, "total": 0.0}, 
                                            "June": {"stocks": 0.0, "crypto": 0.0, "retirement_fund": 0.0, "realstate": 0.0, "total": 0.0}, 
                                            "July": {"stocks": 0.0, "crypto": 0.0, "retirement_fund": 0.0, "realstate": 0.0, "total": 0.0}, 
                                            "August": {"stocks": 0.0, "crypto": 0.0, "retirement_fund": 0.0, "realstate": 0.0, "total": 0.0}, 
                                            "September": {"stocks": 0.0, "crypto": 0.0, "retirement_fund": 0.0, "realstate": 0.0, "total": 0.0}, 
                                            "October": {"stocks": 0.0, "crypto": 0.0, "retirement_fund": 0.0, "realstate": 0.0, "total": 0.0}, 
                                            "November": {"stocks": 0.0, "crypto": 0.0, "retirement_fund": 0.0, "realstate": 0.0, "total": 0.0}, 
                                            "December": {"stocks": 0.0, "crypto": 0.0, "retirement_fund": 0.0, "realstate": 0.0, "total": 0.0}, 
                                            "Total": {"stocks": 0.0, "crypto": 0.0, "retirement_fund": 0.0, "realstate": 0.0, "total": 0.0}}}
            if stocks != None:
                self.investments[year][month]["stocks"] = stocks
            if crypto != None:
                self.investments[year][month]["crypto"] = crypto
            if retirement_fund != None:
                self.investments[year][month]["retirement_fund"] = retirement_fund
            if realstate != None:
                self.investments[year][month]["realstate"] = realstate
            if stocks != None and crypto != None and retirement_fund != None and realstate != None:
                self.investments[year][month]["total"] = (stocks + crypto + retirement_fund + realstate)
                self.investments[year]["Total"]["stocks"] = stocks
                self.investments[year]["Total"]["crypto"] = crypto
                self.investments[year]["Total"]["retirement_fund"] = retirement_fund
                self.investments[year]["Total"]["realstate"] = realstate
                self.investments[year]["Total"]["total"] = (stocks + crypto + retirement_fund + realstate)
        except Exception as e:
            print(e)

    def __str__(self):
        '''
        Returns/displays a table with all the investements for the whole year.
        '''
        try:
            display = (("*" * 96)
            + "\n {:s}".format((" " * 33) + "INVESTMENTS - " + str(self.year))
            + "\n{a:<15s} {b:<15s} {c:<15s} {d:<20s} {e:<15s} {f:<15s}".format(a="MONTH", b="STOCKS", c="CRYPTO", d="RETIREMENT FUND", \
            e="REALSTATE", f="TOTAL") 
            + "\n" + ("*" * 96) + "\n")
            for val in self.investments[self.year].items():
                display += "{a:<15s} {b:<15.2f} {c:<15.2f} {d:<20.2f} {e:<15.2f} {f:<15.2f}".format(a=val[0], b=val[1]["stocks"], \
                c=val[1]["crypto"], d=val[1]["retirement_fund"], e=val[1]["realstate"], f=val[1]["total"]) + "\n" 
            display += ("*" * 96) + "\n"
            print(display)
        except Exception as e:
            print(e)

    def monthly_investment(self, month):
        '''
        Returns the total amount invested in a given month.

        Parameters:
        -----------
        month : str
            month for which total invested amount need to be determined 
        '''
        try:
            return "Total investment in " + str(month) + ": ${}".format(self.investments[self.year][month]["total"])
        except Exception as e:
            print(e)

    def add_investment(self, month, stocks, crypto, retirement_fund, realstate):
        '''
        Allows to add investments and records it in the database.

        Parameters:
        -----------
        year : int
            year in which investments were done
        month : int
            month in which investments were done
        stocks : float
            money invested in stocks in a given month
        crypto : float
            money invested in crypto currency in a given month
        retirement_fund : float
            retirement fund contribution of a given month
        realstate : float
            money invested in realstate in a given month
        '''
        try:
            if month !=None and month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                                              'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if not isinstance(stocks, float) and not isinstance(stocks, int) and stocks != None:
                raise Exception("Invalid Stocks: Please enter a valid integer or float value for stock investment")
            if not isinstance(crypto, float) and not isinstance(crypto, int) and crypto != None:
                raise Exception("Invalid Crypto: Please enter a valid integer or float value for crypto investment")
            if not isinstance(retirement_fund, float) and not isinstance(retirement_fund, int) and retirement_fund != None:
                raise Exception("Invalid 401K: Please enter a valid integer or float value for 401K contribution")
            if not isinstance(realstate, float) and not isinstance(realstate, int) and realstate != None:
                raise Exception("Invalid Realstate: Please enter a valid integer or float value for real state investment")
            self.investments[self.year][month]["stocks"] += stocks
            self.investments[self.year][month]["crypto"] += crypto
            self.investments[self.year][month]["retirement_fund"] += retirement_fund
            self.investments[self.year][month]["realstate"] += realstate
            self.investments[self.year][month]["total"] += (stocks + crypto + retirement_fund + realstate) 
            self.investments[self.year]["Total"]["stocks"] += stocks
            self.investments[self.year]["Total"]["crypto"] += crypto
            self.investments[self.year]["Total"]["retirement_fund"] += retirement_fund
            self.investments[self.year]["Total"]["realstate"] += realstate
            self.investments[self.year]["Total"]["total"] += (stocks + crypto + retirement_fund + realstate)
            return "Investments have been added"
        except Exception as e:
            print(e)
    
    def update_stocks(self, month, stocks):
        '''
        Allows to change/update the amount of money invested in stocks for a particular month.

        Parameters:
        -----------
        month : str
            month for which stock investment needs to be changed
        stocks : float
            correct amount of stock investment
        '''
        try:
            if month !=None and month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                                              'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if not isinstance(stocks, float) and not isinstance(stocks, int) and stocks != None:
                raise Exception("Invalid Stocks: Please enter a valid integer or float value for stock investment")
            temp = self.investments[self.year][month]["stocks"] 
            self.investments[self.year][month]["stocks"] = stocks
            self.investments[self.year][month]["total"] += (stocks - temp)
            self.investments[self.year]["Total"]["stocks"] += (stocks - temp)
            self.investments[self.year]["Total"]["total"] += (stocks - temp)
            return "Stocks have been updated"
        except Exception as e:
            print(e)
    
    def update_crypto(self, month, crypto):
        '''
        Allows to change/update the amount of money invested in crypto currencies for a particular month.

        Parameters:
        -----------
        month : str
            month for which crypto investment needs to be changed
        crypto : float
            correct amount of crypto investment
        '''
        try:
            if month !=None and month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                                              'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if not isinstance(crypto, float) and not isinstance(crypto, int) and crypto != None:
                raise Exception("Invalid Crypto: Please enter a valid integer or float value for crypto investment")
            temp = self.investments[self.year][month]["crypto"] 
            self.investments[self.year][month]["crypto"] = crypto
            self.investments[self.year][month]["total"] += (crypto - temp)
            self.investments[self.year]["Total"]["crypto"] += (crypto - temp)
            self.investments[self.year]["Total"]["total"] += (crypto - temp)
            return "Crypto investment has been updated"
        except Exception as e:
            print(e)
    
    def update_retirement_fund(self, month, retirement_fund):
        '''
        Allows to change/update the amount of money invested in 401K for a particular month.

        Parameters:
        -----------
        month : str
            month for which 401K investment needs to be changed
        retirement_fund : float
            correct amount of 401K investment
        '''
        try:
            if month !=None and month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                                              'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if not isinstance(retirement_fund, float) and not isinstance(retirement_fund, int) and retirement_fund != None:
                raise Exception("Invalid 401K: Please enter a valid integer or float value for 401K contribution")
            temp = self.investments[self.year][month]["retirement_fund"] 
            self.investments[self.year][month]["retirement_fund"] = retirement_fund
            self.investments[self.year][month]["total"] += (retirement_fund - temp)
            self.investments[self.year]["Total"]["retirement_fund"] += (retirement_fund - temp)
            self.investments[self.year]["Total"]["total"] += (retirement_fund - temp)
            return "Retirement_fund has been updated"
        except Exception as e:
            print(e)
    
    def update_realstate(self, month, realstate):
        '''
        Allows to change/update the amount of money invested in real state for a particular month.

        Parameters:
        -----------
        month : str
            month for which real state investment needs to be changed
        realstate : float
            correct amount of real state investment
        '''
        try:
            if month !=None and month not in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', \
                                              'October', 'November', 'December']:
                raise Exception("Invalid Month: Please enter a valid month like January, February etc.")
            if not isinstance(realstate, float) and not isinstance(realstate, int) and realstate != None:
                raise Exception("Invalid Realstate: Please enter a valid integer or float value for real state investment")
            temp = self.investments[self.year][month]["realstate"] 
            self.investments[self.year][month]["realstate"] = realstate
            self.investments[self.year][month]["total"] += (realstate - temp)
            self.investments[self.year]["Total"]["realstate"] += (realstate - temp)
            self.investments[self.year]["Total"]["total"] += (realstate - temp)
            return "Realstate investment has been updated"
        except Exception as e:
            print(e)

class Budget(Income, Expense, Investment):
    '''
    A subclass of Income, Expense and Investment classes and represents income, expenses and investments of a person for a whole year.

    Attributes:
    -----------
    year : int
        year for which budget needs to be managed

    Methods:
    --------
    cash_flow():
        calculates and returns a table of cash flow values for each month of the year. Also plots data on a bar graph.
            Cash Flow = Income - Expenses
    net_worth():
        calculates and returns a table of total net worth of the account every month for the whole year. Also plots data on a bar graph.
            Net Worth (in month N) = Income (in month N) - Expenses (in month N) + Investements (in month N) + net worth (in month N-1)
    '''

    def __init__(self, year):
        '''
        Constructs the income, expenses and investement database of the account for the whole year by calling the __init__ function of parent
        classes.

        Parameters:
        -----------
        year : int
            year for which budget needs to be managed 
        '''
        try:
            self.__year = year
            Income.__init__(self, year = self.__year, month = None, salary = None, bonus = None)
            Expense.__init__(self, year = self.__year, month = None, rent = None, grocery = None, auto = None, medical = None, other = None)
            Investment.__init__(self, year = self.__year, month = None, stocks = None, crypto = None, retirement_fund = None, realstate = None)
        except Exception as e:
            print(e)

    def __str__(self):
        '''
        Returns/displays three tables, one for each income, expenses and investements data, for the whole year.
        '''
        try:
            Income.__str__(self)
            Expense.__str__(self)
            Investment.__str__(self)
            return ""
        except Exception as e:
            print(e)

    def cash_flow(self):
        '''
        Calculates and returns a table of cash flow values for each month of the year. Also plots data on a bar graph.

                    Cash Flow = Income - Expenses            
        '''
        try:
            cf_list = []
            in_list = []
            ex_list = []
            for val_income in self.income[self.__year].items():
                in_list.append(val_income[1]["total"])  
            for val_expense in self.expenses[self.__year].items():
                ex_list.append(val_expense[1]["total"])
            i = 0
            while i < len(in_list):
                cf_list.append(in_list[i]-ex_list[i])
                i += 1
            display = (("*" * 140)
                        + "\n{:50s}".format((" " * 58) + "CASH FLOW - " + str(self.__year))
                        + "\n" + ("*" * 140) 
                        + "\n{a:<10s} {b:<10s} {c:<10s} {d:<10s} {e:<10s} {f:<10s} {g:<10s} {h:<10s} {i:<10s} {j:<10s} {k:<10s} {l:<10s} {m:<10s}"
                            .format(a="January", b="February", c="March", d="April", e="May", f="June", g="July", h="August", i="September", \
                                j="October", k="November", l="December", m="Total") + "\n") 
            for val in cf_list:
                display += "{a:<11.0f}".format(a=val)
            display += "\n" + ("*" * 140)
            print(display)
            fig = plt.figure()
            ax = fig.add_axes([0,0,1,1])
            x_ax = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            y_ax = cf_list
            y_ax.pop()
            ax.bar(x_ax, y_ax)
            plt.show()
        except Exception as e:
            print(e)
    
    def net_worth(self):
        '''
        Calculates and returns a table of total net worth of the account every month for the whole year. Also plots data on a bar graph.
            
            Net Worth (in month N) = Income (in month N) - Expenses (in month N) + Investements (in month N) + net worth (in month N-1)
        '''
        try:
            nw_list = []
            in_list = []
            ex_list = []
            inv_list = []
            for val_income in self.income[self.__year].items():
                in_list.append(val_income[1]["total"])  
            for val_expense in self.expenses[self.__year].items():
                ex_list.append(val_expense[1]["total"])
            for val_investment in self.investments[self.__year].items():
                inv_list.append(val_investment[1]["total"])
            i = 0
            while i < len(in_list):
                if i == 0:
                    nw_list.append(in_list[i] - ex_list[i] + inv_list[i])
                else:
                    nw_list.append(in_list[i] - ex_list[i] + inv_list[i] + nw_list[i-1])
                i += 1
            nw_list.pop()
            display = (("*" * 140)
                        + "\n{:50s}".format((" " * 58) + "NET WORTH - " + str(self.__year))
                        + "\n" + ("*" * 140) 
                        + "\n{a:<10s} {b:<10s} {c:<10s} {d:<10s} {e:<10s} {f:<10s} {g:<10s} {h:<10s} {i:<10s} {j:<10s} {k:<10s} {l:<10s}"
                            .format(a="January", b="February", c="March", d="April", e="May", f="June", g="July", h="August", i="September", \
                            j="October", k="November", l="December") + "\n") 
            for val in nw_list:
                display += "{a:<11.0f}".format(a=val)
            display += "\n" + ("*" * 140)
            print(display)
            fig = plt.figure()
            ax = fig.add_axes([0,0,1,1])
            x_ax = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            y_ax = nw_list
            ax.bar(x_ax, y_ax)
            plt.show()
        except Exception as e:
            print(e)
    
class budget_manager():
    '''
    This is the manager class that provides following functionality to facilitate budget management:

        1- Allows the manager to specify the number of accounts that needs to be managed and instantiates objects of Budget class for each user
        account. An object of budget class mainatins user data for income, expense and invetsments for whole year.
        2- Allows manager to fill income data for all the acounts all at once. Similarly allows to fill expense and investment data as well.
        3- Allows manager to change individual data entries (i.e. salary, bonus, rent, grocery, stocks etc.) for each user account.
        4- Let's manager to see (display) the budget data (i.e. income, expense and investment data) for all accounts for the whole year.
        5- Let's manager to see (display) the cash_flow and net_worth of all the accounts.        

    Attributes:
    -----------
    year : int
        year for which budget needs to be managed for the accounts
    accounts : int
        number of accounts that will be managed 
    name : str
        name for each of the account that will be managed
    
    Methods:
    --------
    get_accounts():
        displays budget data (i.e. income, expense and investment data) for all the accounts
    fill_income():
        allows manager to fill income data for all users at once for whole year.
    fill_expenses():
        allows manager to fill expense data for all users at once for whole year.    
    fill_investments():
        allows manager to fill investment data for all users at once for whole year.
    accounts_snapshot():
        displays cash_flow and net_worth data for all account for the whole year and also plots data on bar graph.  
    change_an_entry():
        allows manager to change a data entry for any of the user account.
    '''

    def __init__(self):
        '''
        Asks manager to specify the number of accounts that needs to be managed and instantiates object of Budget class for each user
        account that was requested by manager. An object of budget class mainatins user data for income, expense and invetsments for whole year.
        
        Parameters:
        -----------
        accounts : int
            take input from manager for the number of accounts
        year : int
            take input from manager on the year for which buget needs to be managed
        name : str
            take input from manager for the account holder's names
        '''
        try:
            self.account_name = []
            self.accounts = int(input("How many accounts you will be managing:  "))
            self.year = int(input("For which year you will be managing the budget:  "))
            i = 0
            while i < self.accounts:
                name = input("Enter the account holder name:    ")
                self.account_name.append(name) 
                i += 1
            self.account_list =  [Budget(self.year) for i in self.account_name]
        except Exception as e:
            print(e)

    def get_accounts(self):
        '''
        Allows manager to display budget data (i.e. income, expense and investment data) for all the accounts that he/she is managing.
        '''
        try:
            i = 0
            while i < len(self.account_list):
                print((" " * 16) + "***Budget for "+ self.account_name[i] + "***")
                print(self.account_list[i])
                i += 1
        except Exception as e:
            print(e)
    
    def fill_income(self):
        '''
        Allows manager to fill income data of the whole year for all the accounts that he/she is managing.
        '''
        try:
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            i = 0
            j = 0
            while i < self.accounts:
                while j < 12:
                    name = self.account_name[i]
                    month = months[j]
                    salary = float(input("What is the salary of " + name + " for the month of " + month + " :  "))
                    bonus = float(input("What is the bonus of " + name + " for the month of " + month + " :  "))
                    self.account_list[i].add_income(months[j], salary, bonus)
                    j += 1
                j = 0
                i += 1
        except Exception as e:
            print(e)
    
    def fill_expenses(self):
        '''
        Allows manager to fill expenses of the whole year for all the accounts that he/she is managing.
        '''
        try:
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            i = 0
            j = 0
            while i < self.accounts:
                while j < 12:
                    name = self.account_name[i]
                    month = months[j]
                    rent = float(input("What is the rent of " + name + " for the month of " + month + " :  "))
                    grocery = float(input("What are grocery expenses of " + name + " for the month of " + month + " :  "))
                    auto = float(input("What are auto expenses of " + name + " for the month of " + month + " :  "))
                    medical = float(input("What are medical expenses of " + name + " for the month of " + month + " :  "))
                    other = float(input("What are other expenses of " + name + " for the month of " + month + " :  "))
                    self.account_list[i].add_expenses(months[j], rent, grocery, auto, medical, other)
                    j += 1
                j =0
                i += 1
        except Exception as e:
            print(e)

    def fill_investments(self):
        '''
        Allows manager to fill investment data of the whole year for all the accounts that he/she is managing.
        '''
        try:
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
            i = 0
            j = 0
            while i < self.accounts:
                while j < 12:
                    name = self.account_name[i]
                    month = months[j]
                    stocks = float(input("What is the stock investment of " + name + " for the month of " + month + " :  "))
                    crypto = float(input("What is the crypto investment of " + name + " for the month of " + month + " :  "))
                    retirement_fund = float(input("What is the 401K contribution of " + name + " for the month of " + month + " :  "))
                    realstate = float(input("What is the realstate investment of " + name + " for the month of " + month + " :  "))
                    self.account_list[i].add_investment(months[j], stocks, crypto, retirement_fund, realstate)
                    j += 1
                j =0
                i += 1
        except Exception as e:
            print(e)
    
    def accounts_snapshot(self):
        '''
        Displays cash_flow and net_worth data (also plots data on bar-graphs) for all the accounts.
        '''
        try:
            i = 0
            while i < self.accounts:
                print((" " * 54) + "***CASH FLOW for "+ self.account_name[i] + "***")
                self.account_list[i].cash_flow()
                print((" " * 54) +"***NET WORTH of "+ self.account_name[i] + "***")
                self.account_list[i].net_worth()
                i += 1
        except Exception as e:
            print(e)
    
    def change_an_entry(self):
        '''
        Allows manager to change a data entry for any of the user account that he/she is managing.
        '''
        try:
            account = input("Which account you want to update:  ")
            if account not in self.account_name:
                raise Exception("Invalid Account: You are not managing this account: " + account + 
                                ". Please enter an account name from this list: ", self.account_name)
            month = input("Which month you want to update:  ")
            value = input("Which parameter you want tp update:  ")
            new_value = float(input("What is the new value: "))
            name_index = self.account_name.index(account)
            name = self.account_list[name_index]
            if value[:3].lower() == "sal":
                name.update_salary(month, new_value)
            elif value[:3].lower() == "bon":
                name.update_bonus(month, new_value)
            elif value[:3].lower() == "ren":
                name.update_rent(month, new_value)
            elif value[:3].lower() == "gro":
                name.update_grocery(month, new_value)
            elif value[:3].lower() == "aut":
                name.update_auto_expenses(month, new_value)
            elif value[:3].lower() == "med":
                name.update_medical_expenses(month, new_value)
            elif value[:3].lower() == "oth":
                name.update_other_expenses(month, new_value)
            elif value[:3].lower() == "sto":
                name.update_stocks(month, new_value)
            elif value[:3].lower() == "cry":
                name.update_crypto(month, new_value)
            elif value[:3].lower() == "ret":
                name.update_retirement_fund(month, new_value)
            else:
                value[:3].lower() == "rea"
                name.update_realstate(month, new_value)
        except Exception as e:
            print(e)
    
