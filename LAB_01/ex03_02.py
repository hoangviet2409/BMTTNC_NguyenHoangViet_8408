def daonguoclist(lst):
    return lst[::-1]
inputlist = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, inputlist.split(',')))
listdaonguoc = daonguoclist(numbers)
print("List sau khi đảo ngược:", listdaonguoc)
