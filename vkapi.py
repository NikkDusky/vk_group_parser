import requests
import csv

def take_posts():

    token = "VK_APP_TOKEN" #token of vk_app, u can create app vk.com/dev!!!!!!!
    version = "5.103"
    domain = 'disps' #VK GROUP ID OR USE "owner_id" in params instead "domain" if ID like id93530463567458702
    count = 10
    offset = 0
    all_posts = []

    while offset < 100:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                }
                                )

        data = response.json()['response']['items']
        offset += 10
        all_posts.extend(data)
    return all_posts

def file_writer(data):

    with open('test.csv', 'w', encoding='utf-8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes', 'body', 'url'))
        for post in data:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass
            try:
                a_pen.writerow((post['likes']['count'], post['text'], img_url))
            except:
                pass


all_posts = take_posts()
file_writer(all_posts)

print("End")



#source https://www.youtube.com/watch?v=UjMZ7lTYvyI