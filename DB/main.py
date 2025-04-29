import time
import pandas as pd
from supabase import create_client

# 🔐 Supabase ключи
url = "https://euglbxqhkxtnvcbwffjb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV1Z2xieHFoa3h0bnZjYndmZmpiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ5OTAxNTYsImV4cCI6MjA2MDU2NjE1Nn0.RV9w_dAKF-n1CvITnrHOycDYlcOXiQqJrJmjsd7ha_A"
supabase = create_client(url, key)

# 📂 Загружаем CSV
df = pd.read_csv("yandex_reviews_main_last_right_version.csv", sep=",", index_col=False)

last_url = None
clinic_id = None
source_id = None
batch = []

for index, row in df.iterrows():
    clinic_name = row["Название точки"]
    clinic_type = row["Тип организации"]
    url = row["Ссылка"]
    review_text = row["Отзыв"]
    rating = row["Оценка"]

    if pd.isna(rating):
        continue

    # 💥 Если началась новая клиника — вставляем предыдущий batch
    if url != last_url:
        if batch:
            supabase.table("reviews").insert(batch).execute()
            batch = []

        # 🔧 Вставляем новую клинику
        clinic = supabase.table("clinics").insert({
            "название": clinic_name,
            "тип_организации": clinic_type
        }).execute()
        clinic_id = clinic.data[0]["id"]

        # 🔗 Вставляем источник
        source = supabase.table("sources").insert({
            "url": url,
            "тип_источника": "yandex.map"
        }).execute()
        source_id = source.data[0]["id"]

        last_url = url

    # ⬇️ Добавляем отзыв в batch
    batch.append({
        "id_клиники": clinic_id,
        "id_источника": source_id,
        "текст_отзыва": review_text,
        "оценка": int(rating)
    })
# 🧹 После цикла — вставляем последний batch
if batch:
    supabase.table("reviews").insert(batch).execute()
