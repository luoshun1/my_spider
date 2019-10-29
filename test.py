import traceback

try:
    print("try")
    f = open("/temp/test.txt", "w")
    f.write("测试文件")
except Exception as e:
    print("except ****************")
    # print(repr(e))
    print(e)
    # traceback.print_exc()
else:
    print("else")
    f.close()

print("-"*40)