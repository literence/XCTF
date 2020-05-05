#辨认黑白

white = open("./gif/0.jpg", "rb").read()
black = open("./gif/1.jpg", "rb").read()

flag_dic = ""

for i in range(104):
    with open("./gif/%d.jpg"%i, "rb") as f:
        if f.read() == white:
            flag_dic += '0'
        else:
            flag_dic += '1'

flag = ""

# 二进制转成字符串
# 每八位分隔开
for i in range(len(flag_dic)//8):
    # 每八位转换成一个字符串
    flag += chr(int(flag_dic[i*8:(i+1)*8], 2))

print(flag)