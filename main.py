import os
from dotenv import load_dotenv

from data_processing import generate_table_for_console
from hh_api import get_stats_on_hh_vacancies
from sj_api import get_stats_on_sj_vacancies


PROGRAMMING_LANGUAGES = (
    "C#", "Objective-C", "Ruby", "Java", "C",
    "Typescript", "1С", "Go", "Swift",
    "C++", "PHP", "JavaScript", "Python"
)


def main():
    load_dotenv()
    superjob_secret_key = os.getenv('SUPERJOB_SECRET_KEY')

    vacancies_stats_hh = get_stats_on_hh_vacancies(PROGRAMMING_LANGUAGES)
    hh_table = generate_table_for_console(
        vacancies_stats_hh,
        "HeadHunter Moscow")
    print(hh_table.table)

    vacancies_stats_sj = get_stats_on_sj_vacancies(
        superjob_secret_key,
        PROGRAMMING_LANGUAGES)
    sj_table = generate_table_for_console(
        vacancies_stats_sj,
        "SuperJob Moscow")
    print(sj_table.table)


if __name__ == "__main__":
    main()
