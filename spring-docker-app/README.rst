=================
Simple java spring app
=================

How to run
==========
Run application with maven

``./mvnw package && java -jar target/gs-spring-boot-docker-0.1.0.jar``

Run it in docker

``docker build -t springio/gs-spring-boot-docker .``

``docker run -p 8080:8080 springio/gs-spring-boot-docker``

Dependencies:

Spring-boot

Spring-boot-web
  
