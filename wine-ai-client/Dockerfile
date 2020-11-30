FROM node:12.5.0-alpine

ENV LANG=C.UTF-8 TZ=Asia/Tokyo

WORKDIR /app

RUN apk update

COPY ./package*.json ./

RUN npm install

COPY ./ .

ENV HOST 0.0.0.0
EXPOSE 3000


# FROM命令で、元となるimageを指定(node)
# ENV命令で、環境変数を指定
# WORKDIR命令で、/app内へ移動
# RUN命令で、packageの更新
# COPY命令で、ホストマシンのpackage.jsonとpackage-lock.jsonをコンテナ内にコピー
# RUN命令で、コンテナ内で、npm installを実行し、moduleインストール
# COPY命令で、ホストマシンのファイルをすべてコンテナにコピー
# ENV HOSTでhostを指定
# EXPOSEで公開するport番号を指定しています