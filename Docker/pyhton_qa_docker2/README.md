# pyhton_qa_docker2

docker - инструмент для доставки приложений в виде контейнеров.

```
docker volumes docker run --rm -p 80:80 -v $(pwd):/app {IMAGE}

docker run -d -p {system_port:container_port}
-d для запуска в режиме detached
-p прокидывание портов в систему
```

docker-compose - инструмент для организации работы многоконтейнерного приложения

```
docker-compose build - создать много контейнерный образ
docker-compose up - запустить имеющийся образ
docker-compose images - посмотреть имеющиеся образы
docker-compose rm - удалить остановленные контейнеры
```

## Устройство docker 

 https://habr.com/ru/post/253877/ - Понимая docker
 
 https://dker.ru/docs/docker-engine/docker-overview/ - Введение в docker
 