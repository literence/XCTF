#  XCTF 总结

## MISC

####  flag 提交的格式

带上单词`flag` 和 `{ }` 例如 `flag{th1s_!s_a_d4m0_4la9}` 



#### 找出 pdf 中图片隐藏的文字

选中图片 `ctrl+A` 复制即显示出文字

 

#### 如来十三掌

与佛论禅网站加上`佛曰：`解密成 `MzkuM3gvMUAwnzuvn3cgozMlMTuvqzAenJchMUAeqzWenzEmLJW9`

rot13 解密成 `ZmxhZ3tiZHNjamhia3ptbmZyZGhidmNraWpuZHNrdmJramRzYWJ9`

base64 解密成 `flag{bdscjhbkzmnfrdhbvckijndskvbkjdsab}`

##### 评价：

rot13即 **rotate by 13 places （反转13位）**题目中的'如来'与 rot 既不谐音也无含义上的相关，失去了通过CTF比赛学习以及密码学的目的，并且通过佛曰等文字联想到“与佛论禅”网站更是毫无学习价值，白白浪费时间，这种网站使用的密钥并不是在书籍论文中能查到的经典密钥，只有通过偷到对方密码本才能破解的密码失去了通过其学习计算机科学的作用。

注释：

ROT13算法：套用ROT13到一段文字上只需根据字母顺序取代字母表中13位之后的字母，超过Z则重新绕回26英文字母开头

BASE64：

```python
def base(string:str)->str:
    oldstr = ''
    newstr = []
    base = ''
    base64_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
                   'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                   'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
    #把原始字符串转换为二进制，用bin转换后是0b开头的，所以把b替换了，首位补0补齐8位
    for i in string:
        oldstr += '{:08}'.format(int(str(bin(ord(i))).replace('0b', '')))
    #把转换好的二进制按照6位一组分好，最后一组不足6位的后面补0
    for j in range(0, len(oldstr), 6):
        newstr.append('{:<06}'.format(oldstr[j:j + 6]))
    #在base_list中找到对应的字符，拼接
    for l in range(len(newstr)):
        base += base64_list[int(newstr[l], 2)]
    #判断base字符结尾补几个‘=’
    if len(string) % 3 == 1:
        base += '=='
    elif len(string) % 3 == 2:
        base += '='
    return  base
```







#### gif

下载文件夹中包含了 104 张黑白图片，转换为二进制数字，每八位分成一组转换成字符串



 #### 坚持60s

反编译 java 文件 找到 flag后把大括号中的内容 base64 解密



#### 掀桌子

两位16进制可以表示一个字节，将该字符串两两分组转换成字节，发现所有字节均大于128， ASCII码表示范围是0-127， 再转换成字符串。







