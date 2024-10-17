import os

def ensure_directory_exists(directory_path):

    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
            print(f"Каталог '{directory_path}' был создан.")
        except Exception as e:
            print(f"Ошибка при создании каталога: {e}")
    else:
        print(f"Каталог '{directory_path}' уже существует.")


ensure_directory_exists('new_directory')