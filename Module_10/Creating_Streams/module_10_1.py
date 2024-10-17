from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count: int, file_name: str):
    with open(file_name, 'a', encoding='utf-8') as file:
        [file.write(f'Какое-то слово № {number}\n') for number in range(1, word_count + 1)]
        sleep(0.1)
    print(f'Завершилась запись в файл {file_name}.')

time_start = datetime.now()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

time_end = datetime.now()

print(f'Работа потоков {time_end - time_start}.')

fst = Thread(target=write_words(10, "example5.txt"))
scd = Thread(target=write_words(30, "example6.txt"))
thd = Thread(target=write_words(200, "example7.txt"))
frt = Thread(target=write_words(100, "example8.txt"))

time_start = datetime.now()

fst.start()
scd.start()
thd.start()
frt.start()

fst.join()
scd.join()
thd.join()
frt.join()

time_end = datetime.now()

print(f'Работа потоков {time_end - time_start}.')