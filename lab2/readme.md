# lab 2

Собрать образ:
```
docker build . -t mtu-finder -f Dockerfile
```

Запустить:
```
docker run --rm mtu-finder <host>
```
Пример:
```
docker run --rm mtu-finder example.com
1500
```
