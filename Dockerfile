# maintainer info
FROM python:3.12-slim
LABEL maintainer="hanjh@bigvalue.co.kr"

# copy requirements file
WORKDIR /app
COPY requirements.txt ./

# install python and dependences
RUN pip3 install --no-cache-dir -r ./requirements.txt

# copy app
COPY . ./

# start command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]