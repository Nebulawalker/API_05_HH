import os
from dotenv import load_dotenv

from print_data import print_table_in_console
from hh_api import get_stats_on_hh_vacancies
from sj_api import get_stats_on_sj_vacancies


programming_languages = (
    "C#", "Objective-C", "Ruby", "Java", "C",
    "Typescript", "1С", "Go", "Swift",
    "C++", "PHP", "JavaScript", "Python"
)
python = ("Python", )


def main():
    load_dotenv()
    superjob_secret_key = os.getenv('SUPERJOB_SECRET_KEY')

    print_table_in_console(
        get_stats_on_hh_vacancies(programming_languages),
        "HeadHunter Moscow"
    )
    print_table_in_console(
        get_stats_on_sj_vacancies(
            superjob_secret_key,
            programming_languages
        ),
        "SuperJob Moscow"
    )


if __name__ == "__main__":
    main()
