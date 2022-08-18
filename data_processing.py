from terminaltables import SingleTable


def generate_table_for_console(vacancy_stats: dict, title: str) -> None:
    table_data = [
        ('Язык программирования',
         'Вакансий найдено',
         'Вакансий обработано',
         'Средняя зарплата')
    ]
    for language, stats in vacancy_stats.items():
        table_data.append(
            (language,
             stats['vacancies_found'],
             stats['vacancies_processed'],
             stats['average_salary']
             )
        )
    table_instance = SingleTable(table_data, title)
    return table_instance


def predict_rub_salary(
        salary_from: float | int,
        salary_to: float | int
        ) -> int | None:
    if salary_to and salary_from:
        return int((salary_to + salary_from) / 2)
    elif salary_from:
        return int((salary_from * 1.2))
    elif salary_to:
        return int(salary_to * 0.8)
    else:
        return None
