Returning Tuples for Unpacking
** Recall we can loop through a list of tuples and "unpack" the values within them**

stock_prices = [('AAPL',200),('GOOG',300),('MSFT',400)]
for item in stock_prices:
    print(item)
('AAPL', 200)
('GOOG', 300)
('MSFT', 400)
for stock,price in stock_prices:
    print(stock)
AAPL
GOOG
MSFT
for stock,price in stock_prices:
    print(price)
200
300
400
Similarly, functions often return tuples, to easily return multiple results for later use.

Let's imagine the following list:

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]
The employee of the month function will return both the name and number of hours worked for the top performer (judged by number of hours worked).

def employee_check(work_hours):
# Set some max value to intially beat, like zero hours
    current_max = 0
    # Set some empty value before the loop
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    
    # Notice the indentation here
    return (employee_of_month,current_max)
employee_check(work_hours)
('Cassie', 800)