# Introdução à Banco de dados

## *Trilha de Banco de dados*

### Cenário de Dados 

#### O que são Bancos de dados

**Tudo hoje são dados**

**Diamante bruto** = esse são seus dados 
**Diamante perfeito** = seria o trabalho do cientista de dados já feito.

Formalmente:
Dados relacionados -> Database
|-> Fatos

**Cadastro**
Nome
Telefone
Email
Whatsapp

Podemos considerar uma coleção de palavras, que dentre elas há relacionamentos entre dados, constituindo então um banco de dados.

### O que são Banco de dados?

Contexto - representação do mundo real.
Coerência.
Propósito.

### Sistema de gerenciamento de banco de dados - SGBDs

**Definção** - Tipo de dados, estrutura e Constrains
**Construção** - Inserção de dados 
**Manipulação** - Recuperação e Relatórios
**Compartilhamento** - Simultaneidade e Acesso

Além disso... 
Acesso, Mal funcionamento, proteção e ciclo de vida de longo prazo 

**SGBDs - Exemplo**
Contexto: Universidade
Nome completo
Matricula
Endereco 
Campus
Curso
Telefone
Email
...

**Definição**
Estudantes
Cursos
Seção
Pré-requisitos
Report da grade

**Metadados**
Informações que fornecem uma descrição conscisa dos dados contidos no BD

**Manipulação**
Query
Updates

**Compartilhamento**
Por padrão o BD realiza o bloqueio e a liberação das tabelas


### Modelo Relacional 

Criando em 1970
Baseado na teoria de conjuntos
Álgebra relacional
Relações 
TAD para armazenamento
Transparência
 
 **Usuarios de BDs**
User convencional
Administrador do BD

**BD = Banco de dados**
Definição das tabelas e constrains para dados
Comandos traduzidos pelo processamento LDD
LDD - Linguagem de Definição de dados

**Modelo Realacional**
Tradução -> Mec. Execução -> Metadados e Schema

Características:
Altera e extrai informações
Duráveis
Transações = Agrupar para executar

**Sotage & Buffer**
Gerenciador de armazenamento
Gerenciador de Buffer

## Sistemas de Gerenciamento de Banco de Dados

**Abordagem de BD**
Suponha as aplicações 
		Cadastro
		Verificação de pagamento
		
		
Caracteristicas principais:
Abastração Auto-descrição
Isolamento Compartilhamento
Multiplas visões Transação multiuser

**Natureza Auto-descritiva**
Descrição da estrutura e constrains
DB schema

## Modelagem de Dados

**O que é modelagem?**
Representação, um modelo que vai servir de base para outros modelos 
Software Dados 
Computacional Conceitual

Possui foco na descricao e relacionamento dos elementos que compoe a representacao do contexto (mini-mundo)

Esquema
		Entidade-Relacionamento
		UML (UNified Modeling Language)





