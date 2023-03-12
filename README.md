# Невизначеність та групування інформації
#### Викладач: Івохін Є.В.
#### Студент: Півень Д.М.

Необхідно реалізувати довільний проект, що складается з сукупності сервісів (мінімум з 2 web-дoдатків). Для реалізації використати підхід на основі контейнеризації за допомогою платформи Docker в середовищах ОС Linux/Windows/MacOS 
з подальшою Kubernetes-кластеризацією на базі застосунку minikube (однонодовий кластер).
Розробити засоби розгортання та обслуговування наявні образи сервісів. 
Подати звіт за розробленими проектами з описом та архівом розроблених програмних засобів або посиланням на git-cховище файлів проекту.
Для уникнення можливих накладок у тематиці проектів прошу надсилати у класрум/пошту Назву проекта та Посилання на нього (якщо реалізуеться Інтернет-проект).

docker build -t logic ./sa-logic
docker build -t web ./sa-webapp
docker build -t front ./sa-frontend

docker run -d --name logic -p 5000:5000 logic 
docker run -d --name web -p 8080:8080 web 
docker run -d --name front -p 8081:80 front 

docker network create backend
docker network connect backend logic
docker network connect backend web
docker network connect backend front