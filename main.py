import json
from urllib.parse import urlencode
from urllib.request import urlopen


LATITUDE = 56.3269
LONGITUDE = 44.0059

WEATHER_CODES = {
    0: "Ясно",
    1: "Преимущественно ясно",
    2: "Переменная облачность",
    3: "Пасмурно",
    45: "Туман",
    48: "Туман с изморозью",
    51: "Морось",
    53: "Морось",
    55: "Сильная морось",
    61: "Небольшой дождь",
    63: "Дождь",
    65: "Сильный дождь",
    71: "Небольшой снег",
    73: "Снег",
    75: "Сильный снег",
    80: "Ливневый дождь",
    81: "Сильный ливень",
    82: "Очень сильный ливень",
    95: "Гроза",
    96: "Гроза с градом",
    99: "Сильная гроза с градом",
}


def main():
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current": "temperature_2m,weather_code",
        "timezone": "Europe/Moscow",
    }

    url = (
        "https://api.open-meteo.com/v1/forecast?"
        + urlencode(params)
    )

    with urlopen(url, timeout=10) as response:
        data = json.load(response)

    current = data["current"]
    temperature = current["temperature_2m"]
    weather_code = current["weather_code"]

    condition = WEATHER_CODES.get(
        weather_code, "Неизвестные условия"
    )

    print(f"Нижний Новгород: {temperature:+.0f}°C · {condition}")


if __name__ == "__main__":
    main()
