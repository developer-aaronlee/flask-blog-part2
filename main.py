import requests

blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_post = blog_response.json()
# print(all_post)

for x in all_post:
    print(x["title"])
    print(x["subtitle"])