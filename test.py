from requests import get, post, delete

print(post('http://localhost:5000/news', json={}).json())

print(post('http://localhost:5000/api/news',
           json={'title': 'Заголовок'}).json())
#
# print(post('http://localhost:5000/api/news',
#            json={'title': 'Заголовок',
#                  'content': 'Текст новости',
#                  'user_id': 1,
#                  'is_private': False}).json())


