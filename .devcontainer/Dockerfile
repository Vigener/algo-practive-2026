FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

# HPCを見据えてC/C++のコンパイラ(g++)とデバッガ(gdb)も標準搭載しておく
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    g++ \
    gdb \
    build-essential \
    git \
    curl \
    time \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# 競技プログラミング・HPC用Pythonライブラリ
RUN pip install --no-cache-dir \
    online-judge-tools \
    numpy \
    scipy \
    networkx \
    black