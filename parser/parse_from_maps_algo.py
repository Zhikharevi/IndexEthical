import time
import re
import csv
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def parse_yandex_reviews(url: str, driver_path: str, csv_filename: str, org_type: str) -> list:
    service = Service(driver_path)
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    try:
        driver.get(url)
        time.sleep(5)

        try:
            title_elem = driver.find_element(By.CSS_SELECTOR, "h1.orgpage-header-view__header")
            place_name = title_elem.text.strip()
        except Exception as e:
            print("Не удалось извлечь название:", e)
            place_name = "Неизвестное название"

        try:
            header_elem = driver.find_element(By.CSS_SELECTOR, "h2.card-section-header__title._wide")
            header_text = header_elem.text.strip()
            total_reviews = int(re.sub(r"\D", "", header_text))
        except Exception as e:
            print("Не удалось извлечь общее число отзывов:", e)
            total_reviews = 99999

        print(f"Название точки: {place_name}")
        print(f"Общее число отзывов (по счётчику): {total_reviews}")

        try:
            scroll_container = driver.find_element(By.CSS_SELECTOR, "div.scroll__container")
            print("Найден блок .scroll__container для прокрутки.")
        except Exception as e:
            print("Не нашли div.scroll__container, будем скроллить окно:", e)
            scroll_container = None

        collected_reviews = {}

        def collect_current_reviews():
            review_bodies = driver.find_elements(By.CSS_SELECTOR, "div.business-review-view__body")
            for rb in review_bodies:
                review_text = rb.text.strip()
                review_text = re.sub(r"\s+", " ", review_text)
                if not review_text:
                    continue
                try:
                    parent = rb.find_element(By.XPATH, "./ancestor::div[contains(@class, 'business-review-view')]")
                    rating_elem = parent.find_element(
                        By.CSS_SELECTOR,
                        "span[itemprop='reviewRating'] meta[itemprop='ratingValue']"
                    )
                    rating = rating_elem.get_attribute("content")
                except Exception:
                    rating = None
                collected_reviews[review_text] = rating

        collect_current_reviews()
        print(f"Начальное число собранных отзывов: {len(collected_reviews)}")

        pause = 1.0
        max_no_change = 5
        no_change_count = 0
        previous_count = len(collected_reviews)
        iteration = 0
        max_total_iterations = 200

        while len(collected_reviews) < total_reviews and iteration < max_total_iterations:
            iteration += 1
            more_buttons = driver.find_elements(By.XPATH, "//button[contains(., 'Показать ещё')]")
            if more_buttons:
                try:
                    more_buttons[0].click()
                    print(f"[Итерация {iteration}] Клик по кнопке 'Показать ещё'.")
                except Exception as e:
                    print(f"[Итерация {iteration}] Ошибка при клике на 'Показать ещё': {e}")
            else:
                if scroll_container:
                    driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", scroll_container)
                    print(f"[Итерация {iteration}] Прокрутили .scroll__container.")
                else:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    print(f"[Итерация {iteration}] Прокрутили окно.")

            time.sleep(pause)
            collect_current_reviews()
            current_count = len(collected_reviews)

            if current_count > previous_count:
                print(f"[Итерация {iteration}] Прирост: {current_count - previous_count} (всего: {current_count})")
                no_change_count = 0
                pause = 1.0
            else:
                no_change_count += 1
                print(f"[Итерация {iteration}] Нет прироста (осталось: {current_count}), no_change_count={no_change_count}")
                if no_change_count >= 3:
                    pause += 1.0
                    print(f"Увеличиваем паузу до {pause} сек.")

            previous_count = current_count
            if no_change_count >= max_no_change:
                print(f"Прекращаем, так как {no_change_count} итераций подряд без прироста.")
                break

        final_reviews = list(collected_reviews.items())
        print(f"Итого собрано: {len(final_reviews)} отзывов (из {total_reviews} по счётчику).")

        # === Запись в CSV ===
        write_mode = 'a' if os.path.exists(csv_filename) else 'w'
        with open(csv_filename, write_mode, newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if write_mode == 'w':
                writer.writerow(["Название точки", "Ссылка", "Отзыв", "Оценка", "Тип организации"])
            for review, rating in final_reviews:
                writer.writerow([place_name, url, review, rating, org_type])

        # === Альтернативно: JSON ===
        # with open("yandex_reviews_selenium.json", "w", encoding="utf-8") as f:
        #     json.dump(final_reviews, f, ensure_ascii=False, indent=2)

        return final_reviews

    finally:
        driver.quit()


def main():
    url = (
        "https://yandex.ru/maps/213/moscow/?ll=37.589017%2C55.767364&mode=poi"
        "&poi%5Bpoint%5D=37.588704%2C55.767410"
        "&poi%5Buri%5D=ymapsbm1%3A%2F%2Forg%3Foid%3D1110831851"
        "&tab=reviews&z=19.77"
    )
    driver_path = "/Users/akaki/PycharmProjects/omad_project/chromedriver"
    parse_yandex_reviews(url, driver_path)


if __name__ == "__main__":
    main()