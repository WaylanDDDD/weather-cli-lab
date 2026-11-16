import json
import argparse
from urllib.parse import urlencode
from urllib.request import urlopen


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


def parse_args():
    parser = argparse.ArgumentParser(
        description="Display current weather."
    )

    parser.add_argument(
        "--wind",
        action="store_true",
        help="Show wind speed",
    )
    parser.add_argument(
        "--humidity",
        action="store_true",
        help="Show relative humidity",
    )
    parser.add_argument(
        "--feels-like",
        action="store_true",
        help="Show apparent temperature",
    )
    parser.add_argument(
        "--city",
        default="Нижний Новгород",
        help="City name",
    )

    return parser.parse_args()


def get_location(city):
    params = {
        "name": city,
        "count": 1,
        "language": "ru",
    }

    url = (
        "https://geocoding-api.open-meteo.com/v1/search?"
        + urlencode(params)
    )

    with urlopen(url, timeout=10) as response:
        data = json.load(response)

    results = data.get("results") or []
    return results[0]


def format_weather(
    current,
    city_name,
    show_wind=False,
    show_humidity=False,
    show_feels_like=False,
):
    temperature = current["temperature_2m"]
    weather_code = current["weather_code"]

    condition = WEATHER_CODES.get(
        weather_code, "Неизвестные условия"
    )

    parts = [
        f"{city_name}: {temperature:+.0f}°C",
        condition,
    ]

    if show_feels_like:
        apparent = current["apparent_temperature"]
        parts.append(f"ощущается как {apparent:+.0f}°C")

    if show_humidity:
        humidity = current["relative_humidity_2m"]
        parts.append(f"влажность {humidity}%")

    if show_wind:
        wind = current["wind_speed_10m"]
        parts.append(f"ветер {wind:.0f} км/ч")

    return " · ".join(parts)


def main():
    args = parse_args()
    location = get_location(args.city)
    city_name = location["name"]
    country = location.get("country")

    if country:
        city_name = f"{city_name}, {country}"

    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current": (
            "temperature_2m,weather_code,"
            "wind_speed_10m,relative_humidity_2m,"
            "apparent_temperature"
        ),
        "timezone": "Europe/Moscow",
    }

    url = (
        "https://api.open-meteo.com/v1/forecast?"
        + urlencode(params)
    )

    with urlopen(url, timeout=10) as response:
        data = json.load(response)

    current = data["current"]
    print(
        format_weather(
            current,
            city_name=city_name,
            show_wind=args.wind,
            show_humidity=args.humidity,
            show_feels_like=args.feels_like,
        )
    )


if __name__ == "__main__":
    main()
