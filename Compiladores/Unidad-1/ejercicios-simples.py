# Total Expenses
'''
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this'''

expenses = [2200,2350,2600,2130,2190]

print(f"In Feb you spent {expenses[2] - expenses[1]} more dollars compared to Jan")

print(f'The first three months you spent {expenses[1] + expenses[2] + expenses[3]}')

def exactly_spent():
    spent = 2200

    if spent in expenses:
        print(f"You spent exactly 2000 on month {expenses.index(spent)}") # Returns the position of the month in the array
    else: 
        print("You didnt spent exactly 2000 dollars on any month")

exactly_spent()