import requests


def get_age_from_agify_api(name):
    url = f"https://api.agify.io/?name={name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        age = data.get("age")
        count = data.get("count")
        if age and count:
            print(f"Для имени {name} возможный возраст: {age}, количество предсказаний: {count}")
        else:
            print("Данные не найдены")
    else:
        print("Произошла ошибка при запросе к API")

name=input("Введите имя: ")
get_age_from_agify_api(name)

