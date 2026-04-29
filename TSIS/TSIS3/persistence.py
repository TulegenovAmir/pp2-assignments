import json
import os

# файлы где хранятся настройки и таблица рекордов
SETTINGS_FILE = 'settings.json'
LEADERBOARD_FILE = 'leaderboard.json'


# загрузка настроек игры
def load_settings():

    # значения по умолчанию
    default = {
        "sound": True,
        "car_color": "red",
        "difficulty": "normal"
    }

    # если файл существует
    if os.path.exists(SETTINGS_FILE):

        try:
            with open(SETTINGS_FILE, 'r') as f:
                return json.load(f)

        except (json.JSONDecodeError, IOError):
            # если файл сломан → используем default
            pass

    # если файла нет или он сломан — создаём новый
    save_settings(default)
    return default


# сохранение настроек
def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=4)


# загрузка таблицы рекордов
def load_leaderboard():

    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, 'r') as f:
            return json.load(f)

    # если файла нет — пустой список
    return []


# сохранение результата игрока
def save_score(name, score, distance):

    # читаем старую таблицу
    board = load_leaderboard()

    # добавляем новый результат
    board.append({
        "name": name,
        "score": score,
        "distance": distance
    })

    # сортируем по очкам (лучшие сверху)
    board = sorted(board, key=lambda x: x['score'], reverse=True)

    # оставляем только топ 10
    board = board[:10]

    # сохраняем обратно в файл
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(board, f, indent=4)

        # сразу записываем в файл
        f.flush()