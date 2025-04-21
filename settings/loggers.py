import logging
import datetime
from pytz import timezone # Для работы нужно установить библиотеку pytz

class MoscowTimeFormatter(logging.Formatter): # Наследуемся от стандартного форматера логгера
    
    def formatTime(self, record, datefmt=None): # Далее мы ПЕРЕОПРЕДЕЛЯЕМ метод formatTime, который будет форматировать время в соответствии с нашим МСК временем. 
        record_time = datetime.datetime.fromtimestamp(record.created, tz=timezone('Europe/Moscow')) # Переводим время из timestamp в datetime объект с учетом МСК временной зоны.
        if datefmt: # Нужни ли как то форматировать время по особенному?
            return record_time.strftime(datefmt) #Вывод в формате, который задали.
        return record_time.isoformat() # Вывод в стандартном формате

app_logger = logging.getLogger('my_app')
app_logger.setLevel(logging.INFO)
app_file_logger = logging.FileHandler('logs/app.log', encoding='utf-8')
app_file_logger.setFormatter(
    MoscowTimeFormatter(
        fmt = "%(asctime)s - %(module)s\n[%(levelname)s] %(funcName)s:\n %(lineno)d - %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S",
        )
)
app_logger.addHandler(app_file_logger)