import requests

def get_weather(city):
    try:
        # Kullanıcıdan alınan şehir adını wttr.in servisine gönder
        response = requests.get(f'http://wttr.in/{city}?format=%C+%t')
        
        # İstek başarılıysa hava durumu bilgilerini al
        if response.status_code == 200:
            weather_data = response.text.strip()
            print(f'Weather info: {weather_data}')
        else:
            print('No info.')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    city = input('Enter city name for weather info: ')
    get_weather(city)
