import json
from collections import Counter


def check_duplicates(json_filename="yandex_reviews_selenium.json"):
    with open(json_filename, "r", encoding="utf-8") as f:
        reviews = json.load(f)

    review_texts = [review[0] for review in reviews if review and review[0]]

    counts = Counter(review_texts)
    duplicates = {text: count for text, count in counts.items() if count > 1}

    if duplicates:
        print("Найдены дублирующиеся отзывы:")
        for text, count in duplicates.items():
            print(f"Отзыв: \"{text[:100]}...\" повторяется {count} раз.")
    else:
        print("Дубли не найдены.")

    unique_reviews = []
    seen = set()
    for review in reviews:
        review_text = review[0]
        if review_text not in seen:
            unique_reviews.append(review)
            seen.add(review_text)

    unique_filename = "yandex_reviews_selenium_unique.json"
    with open(unique_filename, "w", encoding="utf-8") as f:
        json.dump(unique_reviews, f, ensure_ascii=False, indent=2)

    print(f"\nСохранено {len(unique_reviews)} уникальных отзывов в файле {unique_filename}.")


if __name__ == "__main__":
    check_duplicates()
