# 1. Tuple yaratish va uning bir nechta elementlariga murojaat qilish
my_tuple = ("olma", "banan", "anor", "gilos", "shaftoli")
print("Tuple:", my_tuple)
print("1-element:", my_tuple[0])
print("3-element:", my_tuple[2])

# 2. Tuple ichidagi berilgan elementning indeksini aniqlash
element = "anor"
index = my_tuple.index(element)
print(f"'{element}' elementining indeksi:", index)

# 3. Set yaratish va unga foydalanuvchi kiritgan elementni qo‘shish
my_set = {"qovun", "tarvuz", "olcha"}
new_element = input("Setga qo‘shmoqchi bo‘lgan elementni kiriting: ")
my_set.add(new_element)
print("Yangilangan set:", my_set)

# 4. Setlar ustida kesishish va farq amallarini bajarish
set1 = {"olma", "banan", "gilos", "shaftoli"}
set2 = {"banan", "gilos", "tarvuz", "qovun"}

kesishma = set1.intersection(set2)
farq = set1.difference(set2)

print("Setlar kesishmasi:", kesishma)
print("Setlar farqi (set1 - set2):", farq)

# 5. Set ichidagi barcha elementlarni ekranga chiqarish
print("Set1 elementlari:")
for item in set1:
    print(item)
