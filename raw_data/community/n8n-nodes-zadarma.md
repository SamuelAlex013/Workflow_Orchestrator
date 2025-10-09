# Zadarma Audio Downloader

Автоматическое скачивание аудиозаписей звонков из Zadarma API.

## Установка

```bash
git clone <repository>
cd <project-directory>
pip install -r requirements.txt
```

## Настройка

Создайте `.env` файл:
```bash
API_KEY=your_zadarma_api_key
API_SECRET=your_zadarma_api_secret
SANDBOX_MODE=false
DAYS_BACK=1
```

## Запуск

```python
python3 run.py
```

## Функции

- Получение списка записанных звонков за указанный период
- Автоматическое скачивание аудиофайлов
- Настраиваемый формат имен файлов
- Retry механизм для неуспешных загрузок
- Статистика скачивания

## API

### ZadarmaDownloader

```python
from src.downloader import ZadarmaDownloader

downloader = ZadarmaDownloader()
downloader.download_all_records()
```

### ZadarmaAPI

```python
from src.zadarma.api import ZadarmaAPI

api = ZadarmaAPI(key="your_key", secret="your_secret")
response = api.call('/v1/statistics/pbx/', {
    'start': '2024-01-01 00:00:00',
    'end': '2024-01-02 00:00:00'
})
```

## Переменные окружения

- `API_KEY` - Zadarma API ключ
- `API_SECRET` - Zadarma API секрет  
- `SANDBOX_MODE` - Режим sandbox (true/false)
- `DAYS_BACK` - Дней назад для поиска (по умолчанию: 1)
- `DOWNLOAD_FOLDER` - Папка для сохранения (по умолчанию: downloads)
- `FILENAME_TEMPLATE` - Шаблон имен файлов

## Лицензия

MIT License - см. [LICENSE](LICENSE) файл.