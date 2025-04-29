import pandas as pd
from supabase import create_client
from datetime import datetime

# 🔐 Подключение
url = "https://euglbxqhkxtnvcbwffjb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV1Z2xieHFoa3h0bnZjYndmZmpiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ5OTAxNTYsImV4cCI6MjA2MDU2NjE1Nn0.RV9w_dAKF-n1CvITnrHOycDYlcOXiQqJrJmjsd7ha_A"
supabase = create_client(url, key)

# 📥 Загружаем CSV
df = pd.read_csv("companies_ethics_indexes_ai-forever_ruRoberta-large.csv")

# 📥 Загружаем все клиники из БД
clinics = supabase.table("clinics").select("*").execute().data

# Сопоставляем название клиники -> id
clinic_name_to_id = {clinic["название"]: clinic["id"] for clinic in clinics}

# Укажи ID модели!
model_id = 3  # <-- сюда подставь ID твоей модели из таблицы ai_models

# 📤 Заливаем
for index, row in df.iterrows():
    clinic_name = row["company"]
    clinic_id = clinic_name_to_id.get(clinic_name)

    if clinic_id is None:
        print(f"❗ Клиника '{clinic_name}' не найдена в базе, пропускаем")
        continue

    result_json = {
        "avg_p_positive": row["avg_p_positive"],
        "avg_norm_diff": row["avg_norm_diff"],
        "avg_weighted_score": row["avg_weighted_score"],
        "avg_pos_over_non_neu": row["avg_pos_over_non_neu"],
        "n_reviews": int(row["n_reviews"])
    }

    # Вставляем
    supabase.table("ai_results").insert({
        "id_модели": model_id,
        "id_клиники": clinic_id,
        "результат": result_json,
        "дата_анализа": datetime.utcnow().isoformat()
    }).execute()

print("✅ Все результаты успешно загружены!")