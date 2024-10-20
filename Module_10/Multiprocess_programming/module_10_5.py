import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while file.readline() != '':
            all_data.append(file.readline())


file_name = [f'./file {number}.txt' for number in range(1, 5)]

# start = datetime.now()
# for file in file_name:
#     read_info(file)
# end = datetime.now()
# print(f"Time taken without multiprocessing: {end - start}")


if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_name)
    end = datetime.now()
    print(f"Time taken with multiprocessing: {end - start}")