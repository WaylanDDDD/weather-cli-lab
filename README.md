# Weather CLI

A lightweight CLI for getting current weather forecasts from Open-Meteo.

## Usage

Run with the default city:

    python3 main.py

Choose a city:

    python3 main.py --city Moscow

Select additional weather parameters:

    python3 main.py --wind --humidity --feels-like

Combine options:

    python3 main.py --city Kazan --wind --humidity

Display available options:

    python3 main.py --help

## Command-line options

| Option | Description | Default |
| --- | --- | --- |
| `--city CITY` | City to retrieve weather for | Нижний Новгород |
| `--wind` | Show wind speed | Disabled |
| `--humidity` | Show relative humidity | Disabled |
| `--feels-like` | Show apparent temperature | Disabled |

For city names containing spaces, enclose the value in quotes:

    python3 main.py --city "Nizhny Novgorod"


## Weather data

Weather information is provided by Open-Meteo.

- Temperature: Celsius
- Wind speed: km/h
- Humidity: percent
- Location: selected using Open-Meteo Geocoding API
