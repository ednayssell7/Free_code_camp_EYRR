hours_worked = input(f'how many hours worked today?: ')
hour_rate = input(f'what is the rate?:')
try:
    hours_worked = float(hours_worked)
    hour_rate = float(hour_rate)
except:
    print(f'error, please enter a numeric input')
    quit()

def payment(hours, rate):
    if hours > 8:
        pay = hours * rate
        pay = float(pay)
        extra_pay = (hours - 8) * (rate*0.5)
        salary = pay + extra_pay
        salary = float(salary)
        print(f'Base Salary: ${pay} + extra hour payment: ${extra_pay}')
        return salary
    else:
        salary = hours * rate
        salary = float(salary)
        return salary 

final_pay= payment(hours_worked, hour_rate)

print(f'Total salary for the day: $', final_pay)
