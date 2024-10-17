import os
import time

def file_stats(filepath):
    if not os.path.isfile(filepath):
        raise ValueError(f"Файл '{filepath}' не существует.")
    
    file_info = os.stat(filepath)
    
    file_size = file_info.st_size  
    last_modified_time = time.ctime(file_info.st_mtime)  
    file_name, file_extension = os.path.splitext(os.path.basename(filepath)) 

    stats = {
        'size': file_size,
        'last_modified': last_modified_time,
        'name': file_name,
        'extension': file_extension,
    }
    
    return stats

filepath = 'example.txt'  
print(file_stats(filepath))