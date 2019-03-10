FROM openjdk:8-jdk-alpine
VOLUME /tmp
EXPOSE 8080
EXPOSE 5000
ARG DEPENDENCY=build/libs/gs-accessing-data-mysql-0.1.0
COPY ${DEPENDENCY}/BOOT-INF/lib /app/lib
COPY ${DEPENDENCY}/META-INF /app/META-INF
COPY ${DEPENDENCY}/BOOT-INF/classes /app
ENTRYPOINT ["java","-cp","app:app/lib/*","cup.Application"]