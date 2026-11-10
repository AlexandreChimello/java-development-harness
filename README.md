
## Sobre o projeto

A Java Development Harness é uma ferramenta criada para
automatizar a configuração e a validação de pequenos
projetos Java.

O objetivo é fornecer um ambiente de desenvolvimento
padronizado, reproduzível e preparado para trabalhar
com agentes de inteligência artificial.

## Funcionalidades implementadas

- Template Java 25 com Maven e JUnit 5.
- Geração automática de projetos Java.
- Validação dos nomes dos projetos.
- Testes automatizados do gerador com unittest.
- Integração contínua com GitHub Actions.

## Requisitos

- Java 25
- Apache Maven
- Python 3

## Como utilizar

Na raiz do repositório, executar:

    python scripts/create_project.py meu-projeto

O projeto será criado em:

    generated/meu-projeto/

Para executar os testes do projeto gerado:

    cd generated/meu-projeto
    mvn clean test

## Testes da harness

Para executar os testes automatizados do gerador:

    python -m unittest discover -s tests -v

Para executar os testes do template Java:

    cd templates/java-basic
    mvn clean test

## Próximas funcionalidades

- Ambiente isolado com Docker.
- Análise estática e verificações de qualidade.
- Integração com Claude Code.
- Melhorias na configuração dos projetos gerados.
- Documentação de arquitetura e decisões técnicas.
