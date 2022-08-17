from terminaltables import SingleTable


def print_table_in_console(vacancy_stats: dict, title: str) -> None:
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
    print(table_instance.table)
    print()
