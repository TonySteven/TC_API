from util.EncryptData import EncryptData

# 定义json路径
path = r"../json/response.txt"
file = open(path, 'r', encoding='utf-8')

file_result = open(r"../json/data.json", 'a')

# 秘钥
password = 'DJTDLRH3R7M9BINRL5O2E6O7MJM8LUXB'

# 需要加密的内容, file.read() 读取文件内容
data = file.read()
# 这里**的长度必须是16的倍数
eg = EncryptData(password)
res = eg.decrypt(str(data))

# 写入到file_result文件中的内容, file_result.write() 写入文件内容
file_result.write(res)
