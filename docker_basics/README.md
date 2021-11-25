# Dojo Básico de Docker

Este projeto contém o estado inicial do dojo básico de Docker.

O estado inicial está na branch _main_, enquanto a resolução padrão está na branch _solution_

## Requisitos

- O projeto foi criado usando o Python 3.7.2, porém o estado inicial funciona em qualquer versão do Python 3

- Antes de iniciar é legal você instalar os pacotes que o projeto usa com o comando ```pip install -r .\requirements.txt```

## Como começar

No estado inicial do Dojo você consegue verificar se tudo está OK para começar usando o comando ```flask run```

Ele vai subir a aplicação no seu computador. Se tudo estiver OK, ao acessar no seu navegador o endereço ```http://localhost:8042/guia/quote``` você deverá ver a mensagem ```NÃO ENTRE EM PÂNICO```

## O desafio

O projeto é composto basicamente por uma API feita utilizando Flask, que quando chamada retorna uma citação ~aleatória do Guia do Mochileiro das Galáxias (por enquanto a única citação é a "NÃO ENTRE EM PÂNICO", hehe).

### O problema

Para subir essa aplicação em um novo computador, como vimos nos Requisitos deste Dojo, você precisaria ter instalado no computador o Phython e os pacotes necessários para o projeto. Como é um projeto pequeno, isso não seria muito trabalhoso. Mas em projetos maiores essa "configuração de ambiente" pode se tornar uma grande dor de cabeça.

> **"Ué... mas na minha máquina funciona..."**
>
> *Uma pessoa qualquer com problemas de ambiente*

Um dos caminhos para resolver essa dor de cabeça é scrpitar todo o processo de configuração de ambiente (sdds Powershell), mas atualmente existem soluções ainda mais simples para este tipo de problema.

### A missão

Para resolver esse problema, sua missão é fazer a nossa API rodar dentro de um Contêiner ao invés de simplesmente rodar diretamente no seu computador.

> **"Se na sua máquina funciona, então entrega sua máquina!"**
>
> *Uma pessoa provocativa, que proavelmente conhece Docker*

A ferramenta de conteinerização sugerida aqui é o **Docker**.

Você saberá que chegou na solução final quando rodar o comando ```docker run -p 5000:8042 guia_do_mochileiro_api``` e acessar o endereço ```http://127.0.0.1:8042/guia/quote``` no seu navegador, vendo como output a mensagem ```NÃO ENTRE EM PÂNICO```.

*Boa sorte! E não esqueça de levar sua toalha!*

*[Lula](https://twitter.com/lulacode)*