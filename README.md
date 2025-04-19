<div align="center">

# FluentChat
![GitHub repo size](https://img.shields.io/github/repo-size/Meltide/FluentChat)
![GitHub Repo stars](https://img.shields.io/github/stars/Meltide/FluentChat?style=flat)
![GitHub branch status](https://img.shields.io/github/checks-status/Meltide/FluentChat/main)
![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Meltide/FluentChat)
![GitHub last commit](https://img.shields.io/github/last-commit/Meltide/FluentChat)
![GitHub Created At](https://img.shields.io/github/created-at/Meltide/FluentChat)
一个使用Python制作的伪AI

</div>

## 原理
使用`jieba`库对用户输入的文本进行分词，再判断关键词并进行回复。

## 使用方法
0. 确保你的Python版本为最新
1. 安装依赖
```bash
pip install -r requirements.txt
```
2. 启动程序
```bash
python main.py
```

## 打包为.exe文件
使用`pyinstaller`库来打包为.exe文件
1. 先安装`pyinstaller`库
```bash
pip install pyinstaller
```
2. 添加环境变量`C:\Users\你的用户名\AppData\Local\Programs\PythonXXX\Scripts`
3. 在项目目录下输入以下命令来打包
```bash
pyinstaller -F -w main.py
```