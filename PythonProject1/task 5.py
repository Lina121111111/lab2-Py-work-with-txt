
numers = list(range(1, 21))

# Фильтрация четных чисел
kazhdoe_chisla = list(filter(lambda x: x % 2 == 0, numers))

# Увеличение каждого числа на 10
uv_chisla = list(map(lambda x: x + 10, kazhdoe_chisla))

# Сортировка по убыванию
sort_chisla = sorted(uv_chisla, reverse=True)

# Вывод результатов
print("Chetnye_chisla:", kazhdoe_chisla)
print("Uvelichenie_chisla:", uv_chisla)
print("Otsotr_chisla_po_ubyvaniyu:", sort_chisla)