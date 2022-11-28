# ProjetoCompNuvem

### Autor: Bernardo Cunha Capoferri
### Curso: Engenharia da computação
### Ano: 2022
<br/>

## Descrição
Este é um program de **CLI** simples codado em **Python** para poder criar uma infraestrutura utilizando a linguagem *IaC* **Terraform** na *Amazon Web Service* (AWS). seu objetivo foi simplificar o processo de criação e apagar de instância, grupos de segurança e suas regras, Usuários e sistema de alta disponibilidade em duas regiões da AWS *us-east-1* e *us-east-2*  usando o **Terraform**.

<br/>

## Requerimentos

<br/>

### OS:
O programa foi codado e testado no sistema operacional **Ubuntu 22.04.1**, é recomendado que use um distribuição de Linux para trabalhar com este código.

<br/>

### Terraform:
É preciso que o programa de *Infrastructure as Code* (IaC) **Terraform** versão 1.3.5 ou acima esteja instalado em seu sistema. 

Para instalar siga o [tutorial](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) no site da HashiCorp

<br/>

### Python:
É recomendado que esteja instalada a versão 3.10.6 ou acima.

<br/>

## Configurando variáveis de ambiente no Linux
Para que o **Terraform** consiga realizar alterações na sua AWS é necessário que sejam inseridas suas
chaves de acesso que você obteve quando criou um usuário com permissões de gerar recursos. Existem duas opções para este programa, a primeira é colocar estas variáveis no seu ambiente local, rodando os seguintes comandos em seu terminal:  
```sh
$ export AWS_ACCESS_KEY_ID= <SUA_ACCESS_KEY>
$ export AWS_SECRET_ACCESS_KEY= <SUA_SECRET_ACCESS_KEY>
```
Leve em conta que neste caso as variáveis são definidas apenas na sessão atual, ou seja para toda nova instância de terminal estes comandos deverão ser rodados. A opção mais permanente consiste em colocar estes dois comandos no arquivo `.bashrc` e em seguida rodar o seguinte comando para atualizar o terminal aberto:
```sh
$ source ~/.bashrc
```
<br>

## Como Rodar o código
Primeiramente clone o repositório para seu sistema local.  
```sh
$ git clone git@github.com:bert799/ProjetoCompNuvem.git # Clone com SSH (recomendado)
$ git clone https://github.com/bert799/ProjetoCompNuvem # Clone com HTTPS
```
Com o terminal aberto entre na pasta `python/`  
Rode a aplicação com o seguinte comando:
```sh
$ python3 projeto.py
```
Pronto! Agora é só seguir os menus para construir sua infraestrutura.  

## Manual do usuário

Se encontra neste [site](), também contém um tutorial do **Terraform**