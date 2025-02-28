import time  # Для задержек в работе программы
import serial.tools.list_ports  # Для поиска доступных COM-портов

# Список возможных скоростей передачи данных
speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200', '250000', '500000'] 

# Получаем список доступных COM-портов
ports = [p.device for p in serial.tools.list_ports.comports()] 

# Выбираем первый найденный порт (если портов нет, будет ошибка)
port_name = ports[0]  

# Устанавливаем максимальную скорость передачи (115200 бод)
port_speed = int(speeds[-1])  

# Таймаут для ожидания данных (10 секунд)
port_timeout = 10  

# Открываем соединение с устройством через COM-порт
ard = serial.Serial(port_name, port_speed, timeout=port_timeout)  
time.sleep(1)  # Ждём 1 секунду, чтобы устройство успело ответить
ard.flushInput()  # Очищаем входной буфер перед чтением данных

try:  
    # Читаем доступные данные из буфера (4 раза для надёжности)
    msg_bin = ard.read(ard.inWaiting())  
    msg_bin += ard.read(ard.inWaiting())  
    msg_bin += ard.read(ard.inWaiting())  
    msg_bin += ard.read(ard.inWaiting())  
    
    # Декодируем полученные байты в строку
    msg_str_ = msg_bin.decode()  
    
    # Выводим количество полученных байтов
    print(len(msg_bin))  
except Exception as e:  
    print('Error!')  # В случае ошибки выводим сообщение

# Закрываем соединение с устройством
ard.close()  
time.sleep(1)  # Делаем паузу перед завершением программы

# Выводим полученные данные на экран
print(msg_str_)
