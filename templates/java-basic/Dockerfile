#Escolher imagem base que contém Java25 e Maven
FROM maven:3.10.0-eclipse-temurin-25-noble

#Define a pasta de trabalho dentro do container
WORKDIR /app

#Copia o pom.xml para o container
COPY pom.xml .

#Copia o checkstyle para análise estática
COPY checkstyle.xml .

#Copia as classes java e testes
COPY src ./src

#Comando padrao executado ao iniciar o container
CMD ["mvn", "--batch-mode", "clean", "test"]
