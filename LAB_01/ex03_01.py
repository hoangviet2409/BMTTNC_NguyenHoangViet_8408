def tinhtongsochan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num 
    return tong
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
tongchan = tinhtongsochan(numbers)
print("Tổng các số chẵn trong List là:", tongchan)