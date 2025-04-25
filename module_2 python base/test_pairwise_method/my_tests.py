import itertools
from typing import Dict, List, Any


class TrueMinimalPairwise:
    def __init__(self, parameters: Dict[str, List[Any]]):
        self.parameters = parameters
        self.param_names = list(parameters.keys())
        self.all_pairs = self.generate_all_pairs()
        self.test_cases = []

    def generate_all_pairs(self) -> set:
        pairs = set()
        for i, p1 in enumerate(self.param_names):
            for p2 in self.param_names[i + 1:]:
                for v1 in self.parameters[p1]:
                    for v2 in self.parameters[p2]:
                        pairs.add((p1, v1, p2, v2))
        return pairs

    def generate(self) -> List[Dict[str, Any]]:
        all_combinations = list(itertools.product(
            *[self.parameters[param] for param in self.param_names]
        ))
        uncovered_pairs = set(self.all_pairs)

        while uncovered_pairs:
            best_case = None
            best_coverage = set()

            for combination in all_combinations:
                test_case = dict(zip(self.param_names, combination))
                covered = set()

                for i, p1 in enumerate(self.param_names):
                    for p2 in self.param_names[i + 1:]:
                        pair = (p1, test_case[p1], p2, test_case[p2])
                        if pair in uncovered_pairs:
                            covered.add(pair)

                if len(covered) > len(best_coverage):
                    best_coverage = covered
                    best_case = test_case

            if best_case:
                self.test_cases.append(best_case)
                for i, p1 in enumerate(self.param_names):
                    for p2 in self.param_names[i + 1:]:
                        pair = (p1, best_case[p1], p2, best_case[p2])
                        uncovered_pairs.discard(pair)
            else:
                break  # safety

        return self.test_cases

    def format_test_cases(self) -> str:
        output = f"Всего тестов: {len(self.test_cases)}\n\n"
        for idx, case in enumerate(self.test_cases, 1):
            output += f"Тест #{idx}:\n"
            for param in self.param_names:  # Строго по порядку
                output += f"  {param}: {case[param]}\n"
            output += "\n"
        return output

    def validate_coverage(self) -> bool:
        generated_pairs = set()
        for test_case in self.test_cases:
            for i, p1 in enumerate(self.param_names):
                for p2 in self.param_names[i + 1:]:
                    pair = (p1, test_case[p1], p2, test_case[p2])
                    generated_pairs.add(pair)

        # Выводим общее количество всех пар
        print(f"\nПроверка покрытия всех пар ({len(self.all_pairs)} пар):")

        missing = self.all_pairs - generated_pairs
        if missing:
            print("\n❌ Не покрытые пары:")
            for pair in sorted(missing):
                print(pair)
            return False
        else:
            print("✅ Все пары покрыты один раз!")
            return True


if __name__ == "__main__":
    parameters = {
        "Размер пиццы": ["Маленькая", "Средняя", "Большая"],
        "Тип корки": ["Тонкая", "Пышная"],
        "Соус": ["Томатный", "Сливочный"],
        "Дополнительные ингредиенты": ["Пепперони", "Грибы", "Оливки", "Ветчина"]
    }

    generator = TrueMinimalPairwise(parameters)
    test_cases = generator.generate()
    print(generator.format_test_cases())

    generator.validate_coverage()