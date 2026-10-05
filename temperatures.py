"""Перепады температуры в горном посёлке за неделю.

Дневные температуры: 9, 14, 7, 18, 11, 3, 16 градусов.
Программа выводит три строки: самое тёплое значение, самое холодное
и размах — разницу между максимумом и минимумом.
"""

temperatures = [9, 14, 7, 18, 11, 3, 16]

max_temp = max(temperatures)
min_temp = min(temperatures)
spread = max_temp - min_temp

print(f"{max_temp}")
print(f"{min_temp}")
print(f"{spread}")
