from itertools import product
import string

def generate_letter_combinations(target_sum, mapping):
    letters = list(mapping.keys())
    max_len = len(letters)
    results = []

    for length in range(1, max_len + 1):
        for combo in product(letters, repeat=length):
            combo_sum = sum(mapping[char] for char in combo)
            if combo_sum == target_sum:
                results.append(''.join(combo))
    return results

def sort_combinations(combinations, sort_by="alphabetical"):
    if sort_by == "alphabetical":
        return sorted(combinations)
    elif sort_by == "length":
        return sorted(combinations, key=len)
    return combinations

def add_custom_system(systems, name, mapping):
    systems[name] = mapping

if __name__ == "__main__":
    predefined_systems = {
        "Система 1": {char: i + 1 for i, char in enumerate(string.ascii_lowercase)},
        "Система 2": {char: (i % 9) + 1 for i, char in enumerate(string.ascii_lowercase)},
    }

    while True:
        print("\nДоступные системы:")
        for i, system in enumerate(predefined_systems.keys(), 1):
            print(f"{i}. {system}")
        print("0. Добавить новую систему")

        choice = input("Выберите систему (или 0 для добавления новой): ")
        if choice == "0":
            name = input("Введите название новой системы: ")
            print("Определите соответствие (например, a:1, b:2,...):")
            custom_mapping = {}
            while True:
                entry = input("Введите букву и значение (или 'готово' для завершения): ")
                if entry.lower() == 'готово':
                    break
                try:
                    char, value = entry.split(":")
                    custom_mapping[char.strip()] = int(value.strip())
                except ValueError:
                    print("Неверный формат. Используйте 'буква:значение'.")
            add_custom_system(predefined_systems, name, custom_mapping)
        else:
            try:
                system_name = list(predefined_systems.keys())[int(choice) - 1]
                mapping = predefined_systems[system_name]

                target_sum = int(input("Введите число от 1 до 99: "))
                combinations = generate_letter_combinations(target_sum, mapping)

                if not combinations:
                    print("Сочетания не найдены.")
                    continue

                print("Сортировать результаты: 1. По алфавиту 2. По длине")
                sort_choice = input("Выберите метод сортировки: ")
                sort_method = "alphabetical" if sort_choice == "1" else "length"

                sorted_combinations = sort_combinations(combinations, sort_method)
                print("\nРезультаты:")
                for combo in sorted_combinations:
                    print(combo)
            except (IndexError, ValueError):
                print("Неверный выбор. Попробуйте ещё раз.")
