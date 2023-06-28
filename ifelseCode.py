year = input("Nhập năm: ")
if (int(year) % 4 == 0 and int(year) % 100 != 0) and (int(year) % 400 == 0 ):
     print("Năm " + year + " là năm nhuận")
else:
     print("Năm " + year + " là năm không nhuận")