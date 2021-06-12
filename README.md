# FastAPI-cервер для многопоточной загрузки  изображений

## Установка

### 0. Клонируем репозиторий
```
git clone https://github.com/MartIden/multithreading_upload_fastapi.git
```

### 1. Запускаем установку зависимостей: 
```python
pip install -r reqirements.txt
```
### 2. Конфигурируем настройки uvicorn (по необходимости прокидываем кастомный ip:port):
```python
if __name__ == '__main__':
    uvicorn.run("routes:app", host="127.0.0.1", port=8000, reload=True)
```
### 3. Указываем путь до корня проекта:
```python
ROOT = Path(HOME, "PycharmProjects/multithread_upload")
```
### 4. Запускаем приложение:
```python
path/to/project/python/interpreter main.py
```
### 5. Отправка запроса
Запрос отправляется по маршруту:
```python
/images
```
В корневой директории есть проект для Postman:
```python
Nlogic.postman_collection.json 
```
