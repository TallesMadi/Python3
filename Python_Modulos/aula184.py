# json.dump e json.load com arquivos
import json
import os

ARCHIVE_NAME = 'aula184.json'
ARCHIVE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ARCHIVE_NAME
    )
)

dict_movie = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(ARCHIVE_PATH, 'w', encoding='utf-8') as archive:
    json.dump(dict_movie, archive, ensure_ascii=False, indent=2)

with open(ARCHIVE_PATH, 'r', encoding='utf-8') as archive:
    json_movie = json.load(archive)

print(json_movie)