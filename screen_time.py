"""Анализатор экранного времени за неделю.

Данные: экранное время по дням, норма — 150 минут.
Сначала объявляем функции для каждого показателя, затем вызываем их
и печатаем итоговый отчёт: каждое число берётся из своей функции.
"""

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
minutes = [120, 95, 200, 150, 180, 240, 210]
NORM = 150


def total(values):
    """Сумма всех значений."""
    result = 0
    for value in values:
        result += value
    return result


def average(values):
    """Среднее значение."""
    return total(values) / len(values)


def above_norm(values, norm):
    """Список значений выше нормы."""
    return [value for value in values if value > norm]


def share(part, whole):
    """Доля части от целого в процентах."""
    return part / whole * 100


def minimum(values):
    """Минимальное значение."""
    return min(values)


def maximum(values):
    """Максимальное значение."""
    return max(values)


def spread(values):
    """Размах: разница между максимумом и минимумом."""
    return maximum(values) - minimum(values)


def max_day(days, values):
    """Название дня с максимальным значением."""
    return days[values.index(maximum(values))]


# Вызываем функции по очереди и сохраняем результаты.
total_minutes = total(minutes)
average_minutes = average(minutes)
days_above_norm = above_norm(minutes, NORM)
share_above_norm = share(len(days_above_norm), len(minutes))
min_minutes = minimum(minutes)
max_minutes = maximum(minutes)
spread_minutes = spread(minutes)
top_day = max_day(days, minutes)

# Итоговый отчёт: каждое число — результат соответствующей функции.
print(f"Всего за неделю: {total_minutes} минут")
print(f"Среднее в день: {round(average_minutes, 2)} минут")
print(f"Дней выше нормы: {len(days_above_norm)}")
print(f"Доля дней выше нормы: {round(share_above_norm, 2)}%")
print(f"Минимум: {min_minutes} минут")
print(f"Максимум: {max_minutes} минут")
print(f"Размах: {spread_minutes} минут")
print(f"День с максимумом: {top_day}")
