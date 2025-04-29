import parse_from_maps_algo
import os
from selenium.common.exceptions import WebDriverException
import time


def read_links(filename: str) -> list:
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]


def main():
    driver_path = "/Users/akaki/PycharmProjects/omad_project/chromedriver"
    org_type = "Стоматология"

    links_file_path = os.path.join(
        "Get_links_for_companies", "Links_for_diff_types_of_clinics", "moscow_dental_clinic_links.txt"
    )
    links = read_links(links_file_path)

    for idx, url in enumerate(links, 1):
        print(f"\nОбработка клиники {idx}/{len(links)}")
        print(f"Ссылка: {url}")

        try:
            path_to_save_csv = "yandex_reviews_main_57k_last_right_version.csv"
            reviews = parse_from_maps_algo.parse_yandex_reviews(url, driver_path, path_to_save_csv, org_type)
            print(f"Собрано {len(reviews)} отзывов.")
        except WebDriverException as e:
            print(f"Ошибка Selenium: {e}")
        except Exception as e:
            print(f"Общая ошибка: {e}")

        print(f"Завершена обработка {idx}/{len(links)}\n")
        time.sleep(1)

    print("Все клиники обработаны!")


if __name__ == "__main__":
    main()
