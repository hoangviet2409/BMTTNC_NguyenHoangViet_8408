def demsolanxuathien(lst):
    countdict = {}
    for item in lst:
        if item in countdict:
            countdict[item] += 1
        else:
            countdict[item] = 1
    return countdict
input_string = input("Nhập danh sách các từ, cách nhau bằng dấu cách:")
wordlist = input_string.split()
solanxuathien = demsolanxuathien(wordlist)
print("Số lần xuất hiện của các phần tử: ", solanxuathien)
