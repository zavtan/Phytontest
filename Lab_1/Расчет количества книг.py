# TODO Найдите количество книг, которое можно разместить на дискете
book_num_val = 50 * 25 * 100 * 4
disk_val = 1.44 * 1024 * 1024
count_book = int(disk_val / book_num_val)

print("Количество книг, помещающихся на дискету:", count_book)
