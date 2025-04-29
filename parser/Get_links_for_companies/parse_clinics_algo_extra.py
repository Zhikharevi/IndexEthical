from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


def get_links_on_stream_of_company(search_url, name_of_file, driver_path):
    options = Options()
    driver = webdriver.Chrome(service=Service(driver_path), options=options)
    wait = WebDriverWait(driver, 15)
    driver.maximize_window()

    try:
        driver.get(search_url)
        time.sleep(2)

        try:
            scroll_container = driver.find_element(By.CLASS_NAME, "scroll__container")
        except Exception as e:
            print("⚠️ Не удалось найти scroll__container:", e)
            scroll_container = None

        links = set()
        seen_titles = set()

        for i in range(150):  # максимальное число карточек, можно увеличить
            time.sleep(1)
            snippets = driver.find_elements(By.CLASS_NAME, "search-business-snippet-view__title")

            if i >= len(snippets):
                time.sleep(3)
                if i >= len(snippets):
                    print("✅ Все карточки обработаны.")
                    break

            snippet = snippets[i]

            try:
                title = snippet.text.strip()
                # if title in seen_titles:
                #     continue
                # seen_titles.add(title)

                driver.execute_script("arguments[0].scrollIntoView(true);", snippet)
                time.sleep(0.3)
                driver.execute_script("arguments[0].click();", snippet)

                # Переход внутрь карточки
                link_elem = wait.until(
                    EC.presence_of_element_located((By.CLASS_NAME, "card-title-view__title-link"))
                )
                href = link_elem.get_attribute("href") + "reviews"
                print(f"[{i + 1}] 🔗 {href}")
                links.add(href)

                driver.back()
                time.sleep(0.3)

            except Exception as e:
                print(f"⚠️ Ошибка при обработке карточки #{i + 1}: {e}")
                driver.back()
                time.sleep(2)

        driver.quit()

        os.makedirs("Links_for_diff_types_of_clinics", exist_ok=True)
        with open(os.path.join("Links_for_diff_types_of_clinics", name_of_file), "w", encoding="utf-8") as f:
            for link in sorted(links):
                f.write(link + "\n")

        print(f"\n✅ Сохранено {len(links)} ссылок в файл: {name_of_file}")

    except Exception as e:
        driver.quit()
        raise e


if __name__ == "__main__":
    get_links_on_stream_of_company(
        "https://yandex.ru/maps/213/moscow/search/детская%20городская%20больница",
        "moscow_children_hospital_links.txt",
        "/Users/akaki/PycharmProjects/omad_project/chromedriver"
    )
