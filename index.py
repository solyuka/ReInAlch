# Анализатор экранного времени за неделю.
# Данные: минуты экранного времени по дням, норма 150 минут.
# Каждая функция объявлена в одну строку: в коде нет строк, заканчивающихся
# двоеточием, поэтому редактор не может "нарастить" отступы при вставке.

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
minutes = [120, 95, 200, 150, 180, 240, 210]
NORM = 150


def total(values): return sum(values)
def average(values): return total(values) / len(values)
def above_norm(values, norm): return [value for value in values if value > norm]
def share(part, whole): return round(part / whole * 100, 2)
def minimum(values): return min(values)
def maximum(values): return max(values)
def spread(values): return maximum(values) - minimum(values)
def max_day(days, values): return days[values.index(maximum(values))]


# Вызываем функции по очереди и сохраняем результаты.
total_minutes = total(minutes)
average_minutes = average(minutes)
days_above_norm = above_norm(minutes, NORM)
share_above_norm = share(len(days_above_norm), len(minutes))
min_minutes = minimum(minutes)
max_minutes = maximum(minutes)
spread_minutes = spread(minutes)
top_day = max_day(days, minutes)

# Итоговый отчёт: каждое число — результат своей функции.
print(f"Всего за неделю: {total_minutes} минут")
print(f"Среднее в день: {round(average_minutes, 2)} минут")
print(f"Дней выше нормы: {len(days_above_norm)}")
print(f"Доля дней выше нормы: {share_above_norm}%")
print(f"Минимум: {min_minutes} минут")
print(f"Максимум: {max_minutes} минут")
print(f"Размах: {spread_minutes} минут")
print(f"День с максимумом: {top_day}")
