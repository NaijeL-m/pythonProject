# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import yadisk

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def ya_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_link_ya(self,adres_disk_file):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.ya_headers()
        params = {"path":adres_disk_file, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def upload(self, file_name):
        href = self.get_link_ya(adres_disk_file="test/"+file_name).get("href", "")
        print(href)
        response = requests.put(href, data=open(file_name, 'rb'))
        response.raise_for_status()
        return response.status_code
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file_on_computer = "test.txt"
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file_on_computer)
    #result = uploader.get_link_ya("test/net").get("href", "")
    print(result)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi!!!, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

t = requests.get(' https://superheroapi.com/api/2619421814940190/search/Thanos')
slovar= t.json()
print('Thanos',slovar['results'][0]['powerstats']['intelligence'])

def intellectus(list_hero):
    max=[0, ""]
    for hero in list_hero:
        x = requests.get(' https://superheroapi.com/api/2619421814940190/search/'+hero)
        intell=int(x.json()['results'][0]['powerstats']['intelligence'])
        if intell > max[0]:
            max[0] = intell
            max[1] = hero
    return max[1]

# Press the green button in the gutter to run the script.

s = ['Hulk','Captain America','Thanos']
print(intellectus(s))



hello=True