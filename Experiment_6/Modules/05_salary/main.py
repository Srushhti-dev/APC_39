import salary
basic = float(input("Basic salary: "))
allowance = float(input("Allowance: "))
rate = float(input("Deduction percentage: "))
gross = salary.gross_salary(basic, allowance)
deduction = salary.deductions(gross, rate)
print("Gross:", gross)
print("Deduction:", deduction)
print("Net:", salary.net_salary(gross, deduction))
