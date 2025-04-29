from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_links_on_stream_of_company(link, name_of_file):

    options = Options()

    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)

    driver.get(link)

    time.sleep(2)

    try:
        scroll_container = driver.find_element(By.CLASS_NAME, "scroll__container")
        for _ in range(100):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_container)
            # time.sleep(1.5)
    except Exception as e:
        print("⚠️ Не удалось найти скролл-контейнер:", e)

    links = []

    for idx in range(1000):
        try:
            time.sleep(0.4)
            try:
                scroll_container = driver.find_element(By.CLASS_NAME, "scroll__container")
                for _ in range(100):
                    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_container)
                    # time.sleep(1.5)
            except Exception as e:
                print("⚠️ Не удалось найти скролл-контейнер:", e)
            time.sleep(0.4)
            snippets = driver.find_elements(By.CLASS_NAME, "search-business-snippet-view__title")

            if idx >= len(snippets):
                print("✅ Все карточки обработаны.")
                break

            snippet = snippets[idx]

            driver.execute_script("arguments[0].scrollIntoView(true);", snippet)
            time.sleep(0.07)
            driver.execute_script("arguments[0].click();", snippet)

            link_element = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "card-title-view__title-link"))
            )
            href = link_element.get_attribute("href")
            href = href + "reviews"
            print(f"[{idx+1}] 🔗 {href} ")
            links.append(href)

            driver.back()
            time.sleep(0.15)

        except Exception as e:
            print(f"⚠️ Ошибка при обработке {idx+1}: {e}")
            driver.back()
            time.sleep(3)
            continue

    driver.quit()

    with open(f"./Links_for_diff_types_of_clinics/{name_of_file}", "w", encoding="utf-8") as f:
        for link in list(set(links)):
            f.write(link + "\n")

    print(f"\n✅ Сохранено {len(links)} ссылок в файл '{name_of_file}'")
