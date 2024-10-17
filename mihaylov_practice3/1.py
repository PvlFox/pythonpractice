from datetime import datetime

def datetime_info(date_str):

    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    
    formatted_date = date_obj.strftime('%d-%m-%Y')
    day_of_week = date_obj.strftime('%A')  
    next_year = date_obj.year + 1
    next_year_date = datetime(next_year, 1, 1)  
    days_until_next_year = (next_year_date - date_obj).days  

    info = {
        'Дата': formatted_date,
        'День недели': day_of_week,
        'Дней до следующего года': days_until_next_year
    }
    
    return info

date_str = '2024-10-17'
print(datetime_info(date_str))