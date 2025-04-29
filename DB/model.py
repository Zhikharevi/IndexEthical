from supabase import create_client

url = "https://euglbxqhkxtnvcbwffjb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV1Z2xieHFoa3h0bnZjYndmZmpiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ5OTAxNTYsImV4cCI6MjA2MDU2NjE1Nn0.RV9w_dAKF-n1CvITnrHOycDYlcOXiQqJrJmjsd7ha_A"
supabase = create_client(url, key)

model_data = {
    "название": "ai-forever/ruRoberta-large",
    "тип": "RoBERTa",
}

response = supabase.table("ai_models").insert(model_data).execute()

print(response)
