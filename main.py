import os
from dotenv import load_dotenv

from print_data import generate_table_for_console
from hh_api import get_stats_on_hh_vacancies
from sj_api import get_stats_on_sj_vacancies


programming_languages = (
    "C#", "Objective-C", "Ruby", "Java", "C",
    "Typescript", "1С", "Go", "Swift",
    "C++", "PHP", "JavaScript", "Python"
)


def main():
    load_dotenv()
    superjob_secret_key = os.getenv('SUPERJOB_SECRET_KEY')

    vacancies_stats_hh = get_stats_on_hh_vacancies(programming_languages)
    hh_table = generate_table_for_console(
        vacancies_stats_hh,
        "HeadHunter Moscow")
    print(hh_table)

    vacancies_stats_sj = get_stats_on_sj_vacancies(
        superjob_secret_key,
        programming_languages)
    sj_table = generate_table_for_console(
        vacancies_stats_sj,
        "SuperJob Moscow")
    print(sj_table)


if __name__ == "__main__":
    main()
