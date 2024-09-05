from cache import *


def read_trace_file(file_path):
    # count = 0
    obj = Cache(4096, 4, 4)
    with open(file_path, "r") as file:
        for line in file:
            address = str(line.strip().split(" ")[1])
            obj.mem_access(address)

    print(obj.hit_rate(), " ", obj.miss_rate())
