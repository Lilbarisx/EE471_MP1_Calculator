from custom_classes import Calculator

calc = Calculator()
# Demonstrate (10 + 5) * 2 / 3
calc.add(10, 5)        # 10 + 5 = 15
calc.multiply(calc._current_val, 2)  # 15 * 2 = 30
calc.divide(calc._current_val, 3)    # 30 / 3 = 10.0
print(calc._current_val)
