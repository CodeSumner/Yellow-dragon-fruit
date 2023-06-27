#https://replit.com/@CodeSumner/boilerplate-budget-app#budget.py
class Category:
    #categories = [] # class variable
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.spent = 0.00
        #Category.categories.append(str(self.name))
        

    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": amount, "description": description})
        return self.ledger
    
    def withdraw(self, amount, description = ''):
        amount = round(amount, 2)
        if self.get_balance() > amount:
            self.spent += amount
            self.spent = round(self.spent, 2)
            amount = - amount
            self.ledger.append({"amount": amount, "description": description})  
            return True
        else:
          return False
    
    def get_balance(self):
        current_balance = 0
        for amount in self.ledger:
            current_balance += float(amount["amount"])
        return current_balance
    
    def transfer(self, transfer_amount, Category):
        transfer_amount = round(transfer_amount, 2)
        if self.get_balance() >= transfer_amount:
            self.withdraw(transfer_amount, ("Transfer to " + str(Category.name)))
            Category.deposit(transfer_amount, ("Transfer from " + str(self.name)))
            return True
        else:
            return False
        
    def check_funds(self, amount):
        amount = round(amount, 2)
        if amount > self.get_balance():
            return False
        else:
            return True
        
    # creat buget object.    
    def __str__ (self):
         # creat stars row.
        title_line = ""
        star_line = ""
        l = []
        for i in range((30 - len(self.name))//2):
            star_line += "*"
        if len(self.name)%2 != 0:
            title_line += (star_line + self.name + star_line) + "*" +'\n'
        else:
            title_line += (star_line + self.name + star_line) +'\n'


        # creat amount and description list from ledger dictionary and reverse it.
        for item in self.ledger:
            for val in item.values():
                l.append(val)
        l.reverse()

        # creat rows below the stars row.
        j = len(l)
        s = ''
        gap = ''
        total = ''
        while j > 0:
            if (30 - len(str(l[j-2]))- 7) > 0:
                for k in range(30 - len(str(l[j-2]))-len(str(format(l[j-1],".2f")) )):
                    gap += ' '
                s += str(l[j-2]) + gap + str(format(l[j-1],".2f")) + '\n'
                gap = ''
            if (30 - len(str(l[j-2]))- 7) <= 0:
                for k in range(7-len(str(format(l[j-1],".2f")))):
                    gap += ' '
                s += str(l[j-2])[:23] + gap + str(format(l[j-1],".2f")) + '\n'
                gap = ''
            j -= 2
        
        # connect all the rows.
        total += "Total: " + str(format(self.get_balance(),".2f"))
        title_line += s + total
        return title_line
    
        
def create_spend_chart(categories):
    # ceate categories name list.
    categories_name = []
    for i in range(len(categories)):
        categories_name.append(categories[i].name)
    
    # ceate categories name and spent percentage dictionary.
    spents = {}
    sum = 0.00
    percentage_spent = 0
    for i in range(len(categories_name)):
        sum += categories[i].spent  
    for i in range(len(categories_name)):
        percentage_spent = int(categories[i].spent/sum*100) 
        spents[categories_name[i]] = percentage_spent  
   
    # set variables
    e = 100
    t = 0
    o = [] # the row of "o" list.
    percentages = []
    dash = ''
    blank1 = ''
    blank2 = " "
    row1 = '' # the rows on the dash row.
    row2 = '' # the rows of letters.
    row3 = '' # the rows of letters and blanks.
    chart = '' # the whole rows.
    name_letter = [] # letters of name list.
    name_letters = [] # letters of names list.

    # create percentages list.
    for val in spents.values():
        percentages.append(val)

    # create the rows on the dash row.
    while e >= 0:
        for i in range(len(percentages)):
            o.append('')
            if percentages[i] < e:
                o[i] += (' ' + ' ')
            else:
                o[i] += (' ' + 'o')              
        if e == 100:
            row1 += str(e) + "|" + ''.join([str(elem) for elem in o]) + '\n'
            o =  [] 
        if len(str(e)) == 2:
            row1 += " " + str(e) + "|" + ''.join([str(elem) for elem in o]) + '\n'
            o = []
        if len(str(e)) == 1:
            row1 += " " + " " + str(e) + "|" + ''.join([str(elem) for elem in o]) + '\n'
            o = []
        e -= 10

    # creat dash row.
    for i in range(10):
        dash += "_"

    # creat blanks
    for i in range(4):
        blank1 += " "

    # create list of name letters.
    for key in spents.keys():
        name_letter = [ i for i in key]
        # set all the name letters list the same length.
        for i in range(len(max(categories_name, key = len))-len(key)):
            name_letter.append(' ')
        name_letters.append(name_letter) # ceate lists of names letters list, lists in list.
    # create letter rows below dashs using for while nest loop.
    while t < len(max(categories_name, key = len)):
        for i in range(len(name_letters)):
            row2 += blank2 + name_letters[i][t] 
        row3 += blank1 + row2 + '\n'
        row2 = ''
        t +=1  
    chart += "Percentage spent by category" + '\n' + row1 + blank1 + dash + '\n' + '\n' + row3
    return chart


food = Category("Food")
food.deposit(900, "deposit")
entertainment = Category("Entertainment")
entertainment.deposit(900, "deposit")
business = Category("Business")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(food)
print(business)
print(entertainment)
print(create_spend_chart([entertainment, business, food]))


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
business = Category("Business")
entertainment = Category("Entertainment")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(business)
print(food)
print(entertainment)
print(clothing)
print(auto)
print(create_spend_chart([business, food, entertainment, clothing, auto]))
