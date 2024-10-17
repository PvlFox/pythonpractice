import statistics

def analyze_list(lst):
    max_value = max(lst)
    min_value = min(lst)
    avg_value = sum(lst) / len(lst)
    med_value = statistics.median(lst)
    
    answers = {
        "Максимум": max_value,
        "Минимум": min_value,
        "Среднее": avg_value,
        "Медиана": med_value,
    }
    
    return answers

input_str = input("Введите числа:")
lst = list(map(int, input_str.split()))


result = analyze_list(lst)
print(result)
