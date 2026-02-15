import os
import sys


def list_directory_contents(path):
    if not os.path.exists(path):
        print(f"Ошибка: путь '{path}' не существует.")
        return

    if not os.path.isdir(path):
        print(f"Ошибка: '{path}' не является директорией.")
        return

    folders = []
    files = []

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):
            folders.append(item)
        elif os.path.isfile(full_path):
            files.append(item)

    print(f"\nСодержимое директории '{path}':\n")

    print("Папки:")
    for folder in folders:
        print(f"- {folder}")

    print("\nФайлы:")
    for file in files:
        print(f"- {file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Ошибка: укажите путь к директории.")
        print("Пример: python script.py /home/user/documents")
    else:
        directory_path = sys.argv[1]
        list_directory_contents(directory_path)
