from requests import get, post, delete

# print(get('http://localhost:8080/api/v2/news').json())
# print(get('http://localhost:8080/api/v2/news/4').json())
# print(get('http://localhost:8080/api/v2/news/q').json())


# print(post('http://localhost:8080/api/v2/news').json())
#
# print(post('http://localhost:8080/api/v2/news',
#            json={'title': 'Заголовок'}).json())
#
# print(post('http://localhost:8080/api/v2/news',
#            json={'title': 'Заголовок4',
#                  'content': 'Текст новости',
#                  'user_id': 1,
#                  'is_private': False}).json())

# print(delete('http://localhost:8080/api/news/999').json())
# # новости с id = 999 нет в базе
#
print(delete('http://localhost:8080/api/v2/news/5').json())