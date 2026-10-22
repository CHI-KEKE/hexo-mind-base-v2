---
title: redis
date: 2026-09-05 11:56:05
categories: Docker
top_img: https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Random/Whale.png
cover : https://raw.githubusercontent.com/CHI-KEKE/pics/refs/heads/main/Random/Whale.png
tags:
    - Docker
toc:
toc_number:
comments :
---


{% tabs redis%}



<!-- tab 架構-->



![redis](https://pub-d7e550ef212547d888a6e01348459946.r2.dev/ethic/docker/redis-1-system.png)



```bash
docker run
   │
   ├─ -d
   │   └─ 背景執行
   │
   ├─ --name redis-open
   │   └─ Container 名稱叫 redis-open
   │
   ├─ -p 6379:6379
   │   └─ Host 6379 → Container 6379
   │
   ├─ redis:7
   │   └─ 使用 Redis 7 image
   │
   └─ redis-server --bind 0.0.0.0 --protected-mode no
       └─ Container 啟動後執行的程式
```



其中 **--bind 0.0.0.0** 很重要。它要求 Redis Server **接受 Container 所有網路介面的連線**，而不只限於 loopback



<!-- endtab -->


<!-- tab 啟動-->


```bash
docker ps


error during connect: Get "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/v1.46/containers/json": open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
```

我們在確認目前的 process 時發生了錯誤，意義是 Docker CLI 有安裝，但 Docker Desktop 的 Linux Engine 沒有啟動，所以 `The system cannot find the file specified.` 表示 docker 指令正在找 Docker Desktop 的 Linux Engine，但那個 named pipe 目前不存在。

因此要記得先打開 Windows 的 Docker Desktop，等到 Docker Desktop 顯示 Engine 已經啟動，例如介面顯示 Engine running



啟動完後，再回 PowerShell 執行 docker ps，正常會得到

```bash
CONTAINER ID   IMAGE   COMMAND   CREATED   STATUS   PORTS   NAMES
```


<!-- endtab -->


<!-- tab Redis 7 image 拉下來-->


```bash
docker pull redis:7


## 完成後再確認 image 已經存在

docker images redis

## 會看到類似

## REPOSITORY   TAG   IMAGE ID       CREATED       SIZE
## redis        7     xxxxxxxxxxxx   ...           ...

```




<!-- endtab -->


<!-- tab 啟動 Redis Container-->


我們建立一個叫 redis-open 的 Container、把電腦的 6379 對應到 Container 的 6379，然後啟動 Redis Server，讓它接受外部連線

```bash
docker run -d --name redis-open -p 6379:6379 redis:7 redis-server --bind 0.0.0.0 --protected-mode no


## 執行完後檢查

docker ps

## 應該會看到類似

## CONTAINER ID   IMAGE     COMMAND                  STATUS         PORTS                    NAMES
## xxxx           redis:7   "docker-entrypoint..."   Up ...         0.0.0.0:6379->6379/tcp   redis-open


```


```bash
我的 Windows
    │
    │ 6379
    │
    │ -p 6379:6379
    ▼
┌──────────────────────┐
│ redis-open Container │
│                      │
│ Redis Server :6379   │
└──────────────────────┘
```


<!-- endtab -->


<!-- tab Redis Container 裡自己 Ping 自己-->


```bash

## docker exec 的核心概念是在一個「已經正在執行」的 Container 裡，再執行一個新的指令
docker exec -it redis-open redis-cli PING


docker exec
│
├─ -it
│   └─ 讓你可以互動並看到終端輸出
│
├─ redis-open
│   └─ 指定「已經存在且正在執行」的 Container
│
└─ redis-cli PING
    └─ 要在這個 Container 裡執行的指令



┌────── redis-open Container ──────┐
│                                  │
│   redis-cli                      │
│       │                          │
│       │ PING localhost:6379      │
│       ▼                          │
│   redis-server                   │
│                                  │
└──────────────────────────────────┘
```




<!-- endtab -->


<!-- tab 從另一個 Container 經過 Windows Host 再打進 Redis-->



```bash
## 建立一個臨時 Container，在裡面執行 redis-cli，讓它去連我的 Windows Host 的 6379，送出 PING，執行完後把這個 Container 刪掉
docker run --rm redis:7 redis-cli -h host.docker.internal -p 6379 PING


臨時 redis-cli container
        │
        │ host.docker.internal:6379
        ▼
Windows Host
        │
        │ -p 6379:6379
        ▼
redis-open container
        │
        ▼
redis-server
```



<!-- endtab -->



{% endtabs %}
