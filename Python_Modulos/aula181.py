#  os.path.getsize e os.stat para dados dos arquivos
import os, math

def size_format(bytes_size: int, base: int = 1024) -> str:
    if bytes_size <= 0:
        return '0B'
    
    size_names = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'

    index_size_names = int(math.log(bytes_size, base))

    potency = base ** index_size_names

    final_size = round(bytes_size / potency, 2)

    size_names = size_names[index_size_names]    
    return f'{final_size} {size_names}'

# print(size_format(1000))
# print(size_format(10000))
# print(size_format(100000))
# print(size_format(1000000))
# print(size_format(10000000))
# print(size_format(100000000))
# print(size_format(1000000000))
# print(size_format(10000000000))
# print(size_format(100000000000))
# print(size_format(1000000000000))
# print(size_format(10000000000000))
# print(size_format(100000000000000))
# print(size_format(1000000000000000))
# print(size_format(10000000000000000))
# print(size_format(100000000000000000))
# print(size_format(1000000000000000000))

