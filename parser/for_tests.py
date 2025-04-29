import pandas as pd


def add_org_type_column(csv_path: str, org_type: str):
    df = pd.read_csv(csv_path)
    df["Тип организации"] = org_type
    df.to_csv(csv_path, index=False)
    print(f"Добавлена колонка 'Тип организации' со значением: {org_type}")


if __name__ == "__main__":
    add_org_type_column("yandex_reviews_main.csv", "Детская поликлиника")
