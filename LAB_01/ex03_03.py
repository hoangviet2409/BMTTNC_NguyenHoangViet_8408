def taotupletulist(lst):
    return tuple(lst)
inputlist = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, inputlist.split(',')))
mytuple = taotupletulist(numbers)
print("List: ", numbers)
print("Tuple từ List:", mytuple)