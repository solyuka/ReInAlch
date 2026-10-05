# РЕЗЕРВНАЯ ВЕРСИЯ (те же значения, что в index.py).
# Тела функций записаны в одну строку, поэтому в файле нет строк,
# заканчивающихся двоеточием: если редактор платформы разъезжается
# с отступами и выдаёт "unexpected indent" — используйте этот файл.

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
minutes = [120, 95, 200, 150, 180, 240, 210]
NORM = 150


def total(values): return sum(values)
def average(values): return round(total(values) / len(values), 2)
def above_norm(values, norm): return [value for value in values if value > norm]
def share(part, whole): return round(part / whole * 100, 2)
def minimum(values): return min(values)
def maximum(values): return max(values)
def spread(values): return maximum(values) - minimum(values)
def max_day(days, values): return days[values.index(maximum(values))]


total_minutes = total(minutes)
average_minutes = average(minutes)
minutes_above_norm = above_norm(minutes, NORM)
share_above_norm = share(len(minutes_above_norm), len(minutes))
min_minutes = minimum(minutes)
max_minutes = maximum(minutes)
spread_minutes = spread(minutes)
top_day = max_day(days, minutes)

print(f"Всего за неделю: {total_minutes} минут")
print(f"Среднее в день: {average_minutes} минут")
print(f"Дней выше нормы: {len(minutes_above_norm)}")
print(f"Доля дней выше нормы: {share_above_norm}%")
print(f"Минимум: {min_minutes} минут")
print(f"Максимум: {max_minutes} минут")
print(f"Размах: {spread_minutes} минут")
print(f"День с максимумом: {top_day}")
