# from functions.get_files_info import get_files_info
from functions.write_file import write_file

# print(f"Result for current directory:\n{get_files_info('calculator', '.')}\n")
# print(f"Result for 'pkg' directory:\n{get_files_info('calculator', 'pkg')}\n")
# print(f"Result for '/bin' directory:\n{get_files_info('calculator', '/bin')}\n")
# print(f"Result for '../' directory:\n{get_files_info('calculator', '../')}\n")

print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))