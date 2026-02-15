import os
import sys

if len(sys.argv) < 2:
    print("Ошибка: укажите путь к директории.")
    sys.exit(1)
path = sys.argv[1]

if os.path.exists(path) and os.path.isdir(path):
    print(f"Содержимое директории '{path}':\n")
    items = os.listdir(path)
    folders = [i for i in items if os.path.isdir(os.path.join(path, i))]
    files = [i for i in items if os.path.isfile(os.path.join(path, i))]  
    
    print("Папки:")
    for f in folders:
        print(f"- {f}")

    print("\nФайлы:")
    for f in files:
        print(f"- {f}")
else:
    print(f"Ошибка: путь '{path}' не найден или не является директорией.")