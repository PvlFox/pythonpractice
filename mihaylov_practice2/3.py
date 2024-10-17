def symmetric_difference(set1, set2):
    return set1 ^ set2

def get_set_from_input(prompt):
    input_string = input(prompt)
    return set(map(int, input_string.split()))

set1 = get_set_from_input("Введите элементы первого множества: ")
set2 = get_set_from_input("Введите элементы второго множества: ")

result = symmetric_difference(set1, set2)
print(f"Симметрическая разность: {result}")