FROM tensorflow/tensorflow

USER root

LABEL version="0.1.0"

ENV DEBIAN_FRONTEND=noninteractive

# サーバー変更
RUN sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list

# インストール関連
RUN apt update && apt install -y \
		neovim \
		python3-pip
RUN pip install pandas \
		matplotlib \
		tqdm \
		gensim \
		sklearn \
		hydra-core

# 作業用ディレクトリの作成
RUN mkdir Workspace

# aliasの設定
RUN echo "alias python='python3'" >> /root/.bashrc
RUN echo "alias vi='nvim'" >> /root/.bashrc
RUN echo "alias pip='pip3'" >> /root/.bashrc

# プロンプトの変更
RUN echo 'export PS1="\e[0;32m> \e[0;35m[docker] \e[0;34m\\w \e[m\]$ "' >> /root/.bashrc

# ホームディレクトリをWorkspaceに変更
WORKDIR /Workspace

CMD bash

