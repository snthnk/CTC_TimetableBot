import os
import openpyxl
import requests


def download_excel(date):
    url = f"https://cloud.mail.ru/public/c6kd/AESRAHGcn/{date}/1%20курс%20СПО.xlsx"
    response = requests.get(url)
    if response.status_code == 200:
        with open("schedule.xlsx", 'wb') as f:
            f.write(response.content)
        print(f"Файл schedule.xlsx успешно скачан.")
        return True
    else:
        url = f"https://cloud.mail.ru/public/c6kd/AESRAHGcn/{date}/1%20курс%20.xlsx"
        response = requests.get(url)
        if response.status_code == 200:
            with open("schedule.xlsx", 'wb') as f:
                f.write(response.content)
            print(f"Файл schedule.xlsx успешно скачан.")
            return True
        else:
            print(f"Ошибка при скачивании файла: {response.status_code}")
    return False


def find_schedule_for_group():
    group_name = "1ТМ-11п"
    excel_path = "schedule.xlsx"
    wb = openpyxl.load_workbook(excel_path)
    sheet = wb.active

    schedule = []
    for row in sheet.iter_rows(values_only=True):
        if group_name in row:
            schedule.append(row)

    if schedule:
        print(f"Расписание для группы {group_name}:")
        for lesson in schedule:
            print(lesson)
    else:
        print(f"Группа {group_name} не найдена в расписании.")

    os.remove(excel_path)



excel_url = "https://cloud.mail.ru/public/c6kd/AESRAHGcn/03.09/1%20курс%20НПО.xlsx"

