FROM maven:3.6.3-openjdk-14-slim

EXPOSE 8888
COPY . /demo/
WORKDIR /demo/
RUN mvn package
ENTRYPOINT ["java", "-jar", "target/configserver-0.0.1-SNAPSHOT.jar"]