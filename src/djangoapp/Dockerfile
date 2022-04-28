# python:3.8.2の公式 image をベースの image として設定
FROM python:3.8.2

# 作業ディレクトリの設定
WORKDIR /code/djangoapp

# 必要ファイルの配置
ADD ./src/djangoapp/requirements.txt /code/djangoapp

# 環境アップデート
RUN apt-get update && \
    apt-get -y install locales vim less && \
    pip3 install -r /code/djangoapp/requirements.txt

ENV PYTHONUNBUFFERED    1
ENV LANG C.UTF-8
ENV LANGUAGE en_US
