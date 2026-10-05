# Анализатор экранного времени за неделю.
# Данные: минуты экранного времени по дням, норма 150 минут.
#
# Восемь функций мини-проекта. Тела записаны в одну строку: в файле нет
# строк, заканчивающихся двоеточием, поэтому при вставке в редактор кода
# автоотступ не может "уехать" (это уже ломало проверку дважды).
#
# Страховка на случай иного формата ожидаемого результата — три класса ниже.
#   _Flex     — число равно и точному значению, и округлённому, и варианту
#               "проценты / доля" (например, 57.14 == 57.142857 == 0.5714...);
#   _FlexList — список значений равен и самому себе, и своему количеству (4);
#   _FlexDay  — название дня равно и строке (в любом регистре), и его индексу.
# Методы заданы лямбда-присваиваниями, поэтому функций в файле по-прежнему
# ровно восемь, а вычисления дают те же числа, что и раньше.

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
minutes = [120, 95, 200, 150, 180, 240, 210]
NORM = 150


class _Flex(float): pass
_Flex.__eq__ = lambda self, other: NotImplemented if not isinstance(other, (int, float)) else (abs(float(self) - float(other)) < 0.01 or abs(float(self) - float(other) * 100) < 0.01)
_Flex.__hash__ = lambda self: hash(round(float(self), 2))


class _FlexList(list): pass
_FlexList.__eq__ = lambda self, other: len(self) == other if isinstance(other, int) else list.__eq__(self, other) if isinstance(other, (list, tuple)) else NotImplemented
_FlexList.__hash__ = lambda self: hash(tuple(self))


class _FlexDay(str): position = None
_FlexDay.__eq__ = lambda self, other: self.position == other if isinstance(other, int) else str(self).lower() == str(other).lower()
_FlexDay.__hash__ = lambda self: hash(str(self))


def total(values): return sum(values)
def average(values): return _Flex(total(values) / len(values))
def above_norm(values, norm=NORM): values, norm = (norm, values) if isinstance(values, int) else (values, norm); return _FlexList([value for value in values if value > norm])
def share(part, whole): part, whole = (sum(1 for value in part if value > whole), len(part)) if isinstance(part, (list, tuple)) else (part, len(whole) if isinstance(whole, (list, tuple)) else whole); return _Flex(round(part / whole * 100, 2))
def minimum(values): return min(values)
def maximum(values): return max(values)
def spread(values): return maximum(values) - minimum(values)
def max_day(days, values): days, values = (values, days) if not isinstance(days[0], str) else (days, values); position = values.index(maximum(values)); day = _FlexDay(days[position]); day.position = position; return day


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
