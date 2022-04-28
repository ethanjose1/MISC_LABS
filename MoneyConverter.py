# Official Name:  Ethan Jose
# Nickname:  Mandy
# email: edjose@syr.edu
# Assignment: Assignment 9, problem A.
# Date: Nov 5,, 2020
# MONEY CONVERTER

class Money:

    #initializes the value variable
    def __init__(self, value):
        self.value = value

    #sets value variable to a dollar amount(amt)
    def setDollars(self, amt):
        self.value = 0 * self.value
        self.value = self.value + amt

    #displays the value variable with a dollar sign and 2 decimal places
    def displayDollars(self):
        money = self.value
        print('${:,.2f}'.format(money))

    #sets value to a euro amount then returns the 
    def setEuros(self, amt):
        self.value = 0 * self.value
        self.value = round(((amt + self.value) * 1.14), 5)


    def displayEuros(self):
        money = self.value * 0.877193
        print('€{:,.2f}'.format(money))


if __name__ == '__main__':
    b = Money(324.65)
    b.displayDollars()
    b.displayEuros()
    print()

    c = Money(0)
    c.setEuros(10)
    c.displayEuros()
    c.displayDollars()
    print()

    d = Money(35.62)
    d.displayDollars()
    d.displayEuros()
    d.setEuros(62.08)
    d.displayEuros()
    print()

    e = Money(45.67)
    e.displayEuros()
    e.setEuros(15)
    e.displayEuros()
    e.displayDollars()
    print()

    f = Money(228.47)
    f.setDollars(230)
    f.displayDollars()
    f.displayEuros()
    print()

    g = Money(11129)
    g.displayEuros()
    g.setEuros(35)
    g.displayEuros()
    g.displayDollars()










