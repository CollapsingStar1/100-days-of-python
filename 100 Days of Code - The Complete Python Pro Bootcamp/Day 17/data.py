import html
import requests

API_URL = ("https://opentdb.com/api.php?amount=20&difficulty=hard&type=boolean")

response = requests.get(API_URL)
response.raise_for_status()
data = response.json()

question_data = []
for item in data["results"]:
    question_data.append({
        "text": html.unescape(item["question"]),
        "answer": item["correct_answer"]
    })
