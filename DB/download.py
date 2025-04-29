import pandas as pd
from supabase import create_client

# Подключение
url = "https://euglbxqhkxtnvcbwffjb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV1Z2xieHFoa3h0bnZjYndmZmpiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ5OTAxNTYsImV4cCI6MjA2MDU2NjE1Nn0.RV9w_dAKF-n1CvITnrHOycDYlcOXiQqJrJmjsd7ha_A"
supabase = create_client(url, key)

# Загружаем источники
sources = supabase.table("sources").select("*").execute().data
print(f"🔗 Загружено {len(sources)} источников")

rows = []

for i, source in enumerate(sources):
    source_id = source["id"]
    source_url = source["url"]

    # Получаем все отзывы по источнику
    all_reviews = []
    start = 0
    batch_size = 1000
    while True:
        batch = supabase.table("reviews")\
            .select("*")\
            .eq("id_источника", source_id)\
            .range(start, start + batch_size - 1)\
            .execute().data
        if not batch:
            break
        all_reviews.extend(batch)
        start += batch_size
    clinic_id = all_reviews[0]["id_клиники"]
    clinic_data = supabase.table("clinics").select("*").eq("id", clinic_id).execute().data
    if not clinic_data:
        continue
    clinic = clinic_data[0]
    for review in all_reviews:
        rows.append({
            "Название точки": clinic["название"],
            "Ссылка": source_url,
            "Отзыв": review["текст_отзыва"],
            "Оценка": review["оценка"],
            "Тип организации": clinic["тип_организации"]
        })

    print(f"✅ {i + 1}/{len(sources)}: {source_url} → {len(all_reviews)} отзывов")

# Сохраняем в CSV
df = pd.DataFrame(rows)
df.to_csv("отзывы_по_ссылкам.csv", sep=";", index=False)
print(f"\n🎉 Готово! Всего строк: {len(rows)}")
