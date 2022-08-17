import requests
from itertools import count
from typing import Iterable


SJ_BASE_URL = "https://api.superjob.ru/2.0/vacancies/"


def predict_sj_rub_salary(vacancy):
    if vacancy and vacancy.get("currency") == "rub":
        salary_from = vacancy.get("payment_from", None)
        salary_to = vacancy.get("payment_to", None)

        if salary_to and salary_from:
            return int((salary_to + salary_from) / 2)
        elif salary_from:
            return int((salary_from * 1.2))
        elif salary_to:
            return int(salary_to * 0.8)
    else:
        return None


def get_all_sj_vacancies(
        url: str,
        secret_key: str,
        search_request: str
        ) -> list:

    vacancies = []
    for page in count(0):
        headers = {'X-Api-App-Id': secret_key}
        payload = {
            "keyword": f"Программист {search_request}",
            "town": "4",
            "page": page
        }
        
        page_response = requests.get(url, params=payload, headers=headers)
        page_response.raise_for_status()

        page_data = page_response.json()

        vacancies.extend(page_data["objects"])
        if not page_data["more"]:
            return vacancies


def get_stats_on_sj_vacancies(
        secret_key: str,
        search_requests: Iterable
        ) -> dict:
    vacancy_stats = {}
    for search_request in search_requests:
        amount_of_salaries = 0
        vacancies_processed = 0
        try:
            vacancies = get_all_sj_vacancies(
                            SJ_BASE_URL,
                            secret_key,
                            search_request
                        )
        except requests.exceptions.HTTPError as error:
            print(f"Ошибка при получении данных: {error}")

        vacancies_found = len(vacancies)

        for vacancy in vacancies:
            predicted_salary = predict_sj_rub_salary(vacancy)

            if predicted_salary:
                amount_of_salaries = amount_of_salaries + predicted_salary
                vacancies_processed += 1

        if vacancies_processed != 0:
            average_salary = int(amount_of_salaries / vacancies_processed)
        else:
            average_salary = 0

        vacancy_stats[search_request] = {
            "vacancies_found": vacancies_found,
            "vacancies_processed": vacancies_processed,
            "average_salary": average_salary
        }
    return vacancy_stats
