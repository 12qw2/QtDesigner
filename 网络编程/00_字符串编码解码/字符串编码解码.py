# 字符串编码解码
# 网络通信传递的数据格式：2进制传输 以字节为单位

# 编码
# str.encode()	编码：将字符串转化为字节码
# 解码
# bytes.decode()	解码：将字节码转化为字符串

# 将字符串 "中国123ABC" 编码成 "utf-8" 格式 的 字节序列 
bytes_arr = "中国123ABC".encode(encoding="utf-8")
print(bytes_arr)

# 将 字节序列 编码成 "utf-8" 格式 的 字符串 
aaa = b'\xe4\xbd\xa0\xe5\xa5\xbdabc123'
string = aaa.decode(encoding="utf-8")
print(string)