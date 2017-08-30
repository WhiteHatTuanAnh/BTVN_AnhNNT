# a
d = { "apples": 15, "bananas": 35, "grapes": 12 }
print(d["bananas"] )
print("hiện value của key banana")
print()

# b
d["oranges"] = 20
print(len(d))
print("số key có trong dictionary")
print()

# c
print("grapes" in d)
print("check xem key "grapes" co trong dictionary khong?")
print()

# d
print("print(d["pears"]) sẽ lỗi do không có key này")
print()

# e
print(d.get("pears", 0))
print("tìm key "pears" trong d và trả về =0 nếu không có trong d")
print()

# f
fruits = list(d.keys())
fruits.sort()
print(fruits)
print( "fruits là sort các key của d")
print()

# g
del d["apples"]
print("apples" in d)
print ("Trả về giá trị False do key "apples" đã bị xóa")