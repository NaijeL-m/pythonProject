# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi!!!, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

x=requests.get(' https://superheroapi.com/api/2619421814940190/search/Hulk')
slovar= x.json()
print('Hulk',slovar['results'][0]['powerstats']['intelligence'])

k=requests.get(' https://superheroapi.com/api/2619421814940190/search/Captain America')
slovar= k.json()
print('Captain America',slovar['results'][0]['powerstats']['intelligence'])

t=requests.get(' https://superheroapi.com/api/2619421814940190/search/Thanos')
slovar= t.json()
print('Thanos',slovar['results'][0]['powerstats']['intelligence'])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
