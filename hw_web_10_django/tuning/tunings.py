import json
import requests
from bs4 import BeautifulSoup

from seed import load_authors_from_file, load_qoutes_from_file
from conects import connect_to_mongodb


if __name__ == '__main__':
    # Беремо з попереднього ДЗ
    # Завантаження даних з файлів у відповідні колекції MongoDB
    connect_to_mongodb()  # Підключення до  MongoDB з файлу connects
    load_authors_from_file('authors.json')
    load_qoutes_from_file('quotes.json')
