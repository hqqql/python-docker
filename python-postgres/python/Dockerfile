FROM python:3
WORKDIR /usr/src/app
# 添加依赖声明文件
COPY requirements.txt ./
# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]