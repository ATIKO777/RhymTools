# Используем официальный базовый образ Python
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false
RUN poetry lock --no-update
RUN poetry install --only main
RUN poetry update

# Открываем порт, который будет использоваться приложением
EXPOSE 5000

# Определяем команду запуска приложения
CMD ["python", "app.py"]
