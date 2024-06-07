# 使用官方的Python镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 将requirements.txt复制到容器中
COPY requirements.txt .

# 安装依赖项
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件到容器中
COPY . .

# 暴露Django默认的8000端口
EXPOSE 8000

# 运行Django开发服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
