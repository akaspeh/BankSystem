FROM python:3.11.1
# Устанавливаем рабочий каталог внутри контейнера
WORKDIR /BackEnd

# Копируем зависимости
COPY BackEnd/requirements.txt ./

# Устанавливаем зависимости
RUN pip install  -r requirements.txt
RUN pip install flask_cors

# Копируем все файлы приложения
COPY BackEnd/ .

# Команда для запуска приложения
CMD ["python", "./main.py"]
