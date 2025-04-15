import numpy as np
from scipy.optimize import minimize

# Функція, яку потрібно мінімізувати (довжина огорожі)
# x[0] -> a (сторона паралельна річці)
# x[1] -> b (сторони перпендикулярні річці)
def fence_length(x):
  """Обчислює довжину огорожі."""
  a = x[0]
  b = x[1]
  return a + 2 * b

# Обмеження: площа повинна дорівнювати 1000 м²
# a * b = 1000  =>  a * b - 1000 = 0
constraint = ({'type': 'eq', 'fun': lambda x: x[0] * x[1] - 1000})

# Межі для змінних a та b (повинні бути позитивними)
# Використовуємо невелике позитивне число замість 0, щоб уникнути потенційних проблем
bounds = ((1e-9, None), (1e-9, None)) # a > 0, b > 0

# Початкове наближення для a та b
initial_guess = [10, 100] # Наприклад, a=10, b=100 (площа = 1000)

# Виклик функції мінімізації
# SLSQP (Sequential Least Squares Programming) - хороший метод для задач з обмеженнями та межами
result = minimize(fence_length, initial_guess, method='SLSQP', bounds=bounds, constraints=constraint)

# Виведення результатів
if result.success:
  optimal_a, optimal_b = result.x
  min_length = result.fun
  print("Оптимізацію успішно завершено.")
  print(f"Оптимальні розміри:")
  print(f"  Сторона 'a' (паралельна річці): {optimal_a:.2f} м")
  print(f"  Сторона 'b' (перпендикулярна річці): {optimal_b:.2f} м")
  print(f"Мінімальна довжина огорожі: {min_length:.2f} м")
  # Перевірка площі
  print(f"Перевірка площі: {optimal_a * optimal_b:.2f} м²")
else:
  print("Помилка оптимізації:")
  print(result.message)
