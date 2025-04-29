from collections import Counter

with open('clinic_links_3.txt', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

# Считаем повторы
counter = Counter(lines)

# Фильтруем только те, что встречаются больше одного раза
duplicates = [link for link, count in counter.items() if count > 1]

if duplicates:
    print("🔁 Найдены дубликаты:")
    for dup in duplicates:
        print(f"{dup} — {counter[dup]} раз(а)")
else:
    print("✅ Все строки уникальны")