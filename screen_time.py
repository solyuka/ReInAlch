# Анализатор экранного времени за неделю.
# Данные: минуты экранного времени по дням, норма 150 минут.
# Вычисления — в функциях, отчёт только печатает их результаты.

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
    """Среднее значение, округлённое до двух знаков."""
    return round(total(values) / len(values), 2)


def above_norm(values, norm):
    """Список значений выше нормы."""
    result = []
    for value in values:
        if value > norm:
            result.append(value)
    return result


def share(part, whole):
    """Доля части от целого в процентах, округлённая до двух знаков."""
    return round(part / whole * 100, 2)


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
    position = values.index(maximum(values))
    return days[position]


# Вызываем функции по очереди и сохраняем результаты.
total_minutes = total(minutes)
average_minutes = average(minutes)
minutes_above_norm = above_norm(minutes, NORM)
share_above_norm = share(len(minutes_above_norm), len(minutes))
min_minutes = minimum(minutes)
max_minutes = maximum(minutes)
spread_minutes = spread(minutes)
top_day = max_day(days, minutes)

# Итоговый отчёт: каждое число — результат своей функции, без пересчётов.
print(f"Всего за неделю: {total_minutes} минут")
print(f"Среднее в день: {average_minutes} минут")
print(f"Дней выше нормы: {len(minutes_above_norm)}")
print(f"Доля дней выше нормы: {share_above_norm}%")
print(f"Минимум: {min_minutes} минут")
print(f"Максимум: {max_minutes} минут")
print(f"Размах: {spread_minutes} минут")
print(f"День с максимумом: {top_day}")
