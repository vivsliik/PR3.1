# Используем официальный образ Python 3.10
FROM python:3.10

# Устанавливаем зависимости
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Копируем Python-скрипт внутрь контейнера
COPY Mal3.1.py /app/Mal3.1.py

# Запускаем скрипт при старте контейнера
CMD ["python", "Mal3.1.py"]
