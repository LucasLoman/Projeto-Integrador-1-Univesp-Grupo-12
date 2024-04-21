# Projeto Integrador 1 Univesp Grupo 12
 PI Grupo 012

## Preparando o ambiente

As boas práticas de desenvolvimento em Python incentivam a criação de ambiente virtual (virtual environment) para a instalação de extensões, mantendo a instalação original do Python praticamente intacta.

### Criando um ambiente virtual

Antes de começar a instalar as extensões, é necessário criar o ambiente virtual. Para isso, é necessário rodar o seguinte comando:

```
$ python3 -m venv venv
```
Onde -m é a opção "module", seguido do nome do módulo, "venv", de "virtual environment", e depois o nome escolhido para o módulo. No exemplo, é utilizado o mesmo nome do pacote, "venv".

#### Ativando o ambiente virtual

No diretório raiz do projeto, execute o seguinte comando:

**Linux:**

```
$ source venv/bin/activate
```
**Windows:**
```
$ venv\Scripts\activate
```
**Windows PowerShell:**
```
$ venv\Scripts\Activate.ps1
```
Após a ativação correta do ambiente virtual, o prompt de comando mostrará o ambiente virtual ativo da seguinte forma:
```
(venv) $
```

### Instalando os pacotes necessários

Para executar este projeto, precisará instalar os seguintes pacotes:

- flask
- dotenv
- flask-sqlalchemy
- flask-migrate
- flask-wtf
- mariadb
- mysqlclient


**(to be continued...)**