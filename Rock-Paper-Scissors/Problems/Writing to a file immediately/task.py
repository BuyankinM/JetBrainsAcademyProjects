long_list = list(range(1000000))
file_name = "my_file.txt"
opened_file = open(file_name, 'w')
for _item in long_list:
    command = "print(_item, file=opened_file, flush=True)"
opened_file.close()