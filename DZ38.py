import requests
import json
from statistics import median
from datetime import datetime

responce = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = json.loads(responce.text)

posts_count = {}

for post in posts:
    try:
        posts_count[post["userId"]] += 1
    except KeyError:
        posts_count[post["userId"]] = 1

print("Количество постов пользователей: ")
print(posts_count)

top_posts = []
max_len = 0

for post in posts:
    total_len = len(post["title"]) + len(post["body"])

    if total_len > max_len:
        max_len = total_len

for post in posts:
    total_len = len(post["title"]) + len(post["body"])

    if total_len == max_len:
        top_posts.append({"id": post["id"], "userId": post["userId"], "total_length": total_len})

print("\nНаиболее длинные посты: ")
print(top_posts)

total_posts = len(posts)

body_len = []

for post in posts:
    body_len.append(len(post["body"]))

avg_body_len = round(sum(body_len) / len(body_len), 2)

top_user = sorted(posts_count.items(), key=lambda x: x[1], reverse=True)

active_user = top_user[0][0]

title_len = []

for post in posts:
    title_len.append(len(post["title"]))

median_len = median(title_len)

print("\nСтаитистика: ")
print("Всего постов: ", total_posts)
print("Средняя длина поста: ", avg_body_len)
print("Самый активный пользователь: ", active_user)
print("Медианная длина заголовка: ", median_len)

with open("report.json", "w") as f:
    json.dump({
        "generated_at": str(datetime.now()),
        "sourse": "https://jsonplaceholder.typicode.com/posts",

    "summary": {
    "total_posts": total_posts,
    "avg_body_len": avg_body_len,
    "most_active_user": active_user,
    "median_len_title": median_len
    },

    "per_user_post": posts_count,
    "top_post": top_posts

    }, f, indent = 4)


print("Отчет сохранен!")