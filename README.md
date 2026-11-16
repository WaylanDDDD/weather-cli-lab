# Weather CLI

A simple command-line utility for displaying current weather
conditions using the Open-Meteo API.

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

## Weather data

Weather information is provided by Open-Meteo.

- Temperature: Celsius
- Wind speed: km/h
- Humidity: percent
- Location: selected using Open-Meteo Geocoding API