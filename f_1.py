import requests
from f_2 import http_correct_or_error

statu_1 = requests.get("https://movie.douban.com/top250")
statu_num_1 = statu_1.status_code
print(str(statu_num_1) + ':' + http_correct_or_error(statu_num_1))

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
                  "Safari/537.36 Edg/119.0.0.0"}

statu_2 = requests.get("https://movie.douban.com/top250", headers=header)
statu_num_2 = statu_2.status_code
print(str(statu_num_2) + ':' + http_correct_or_error(statu_num_2))
