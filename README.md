# pyssh

<p align="center">
  <img alt="Python version" src="https://img.shields.io/badge/python-3.7+-blue.svg">
</p>

* python连接ssh
* 运行脚本

## ssh连接参数 `config.json`配置：

* ssh登录参数保存与读取：

```python
import json

my_dict = {"host": "00.00.00.00","port": 22,"user": "root", "pw": "password"}
# 保存文件
tf = open("config.json", "w")
json.dump(my_dict,tf)
tf.close()
# 读取文件
tf = open("config.json", "r")
new_dict = json.load(tf)
print(new_dict)
```

* 直接新建 `config.json`文件，其样式如下：

```json
{
    "host": "00.00.00.00",
    "port": 22,
    "user": "root",
    "pw": "password"
}
```
