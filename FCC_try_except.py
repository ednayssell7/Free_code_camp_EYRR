hours_worked = input(f'how many hours worked today?: ')
hour_rate = input(f'what is the rate?:')
hours_worked = float(hours_worked)
hour_rate = float(hour_rate)

def payment(hours, rate):
    if hours > 8:
        pay = hours * rate
        extra_pay = (hours - 8) * (rate*0.5)
        salary = pay + extra_pay
        print(f'Base Salary: ${pay} + extra hour payment: ${extra_pay}')
        return salary
    else:
        salary = hours * rate
        return salary 

final_pay= payment(hours_worked, hour_rate)

print(f'Total salary for the day: $', final_pay)
