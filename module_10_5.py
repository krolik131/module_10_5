import multiprocessing
from time import time

def read_info(name):
    all_data = []
    with open(name, 'r') as file1:
        line = file1.readline()
        # С циклом for вычисления выполняются быстрее, чем с циклом while
        for line in file1:
            all_data.append(line)
            if not line:
                break

filesnames = [f'./file_{number}.txt' for number in range(1, 5)]

#Многопроцессное выполнение
# if __name__ == '__main__':
#     start_time = time()
#     # Применение функции read_info параллельно
#     pool = multiprocessing.Pool(processes=4)
#     pool.map(read_info, filesnames)
#     end_time = time()
#     print(end_time - start_time)

#Линейное выполнение
start_time = time()
for file in filesnames:
    read_info(file)
end_time = time()
print(end_time - start_time)



