# FastAPI-cервер для многопоточной загрузки  изображений

## Установка

### 1. Запускаем установку зависимостей: 
```python
    pip install -r reqirements.txt
```
### 2. Конфигурируем настройки uvicorn (по необходимости прокидываем кастомный ip:port):
```python
if __name__ == '__main__':
    uvicorn.run("routes:app", host="127.0.0.1", port=8000, reload=True)
```
### 3. Запускаем приложение:
```python
path/to/project/python/interpreter main.py
```
