FROM python:3.12.1

# Устанавливаем рабочий каталог внутри контейнера
WORKDIR /BackEnd/

# Копируем зависимости
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения
COPY ../../../Desktop .

# Команда для запуска приложения
CMD ["python", "main.py"]
