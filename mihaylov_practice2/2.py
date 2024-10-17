def turple_stats(tpl):
    total_sum = sum(tpl)
    avg_value = total_sum / len(tpl)
    unique = tuple(set(tpl))
    return (total_sum, avg_value, unique)


input_str = input("Введите числа: ")
tpl = tuple(map(int, input_str.split()))

result = turple_stats(tpl)
print(result)