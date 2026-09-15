# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objective

Crie uma API REST simples com FastAPI para praticar rotas, modelos de dados, validação e respostas JSON em Python.

## 📝 Tasks

### 🛠️ Configurar a aplicação FastAPI

#### Descrição
Inicialize uma aplicação FastAPI e crie um endpoint raiz para confirmar que a API está funcionando corretamente.

#### Requisitos
O programa concluído deve:

- Importar e inicializar o objeto `FastAPI`.
- Definir uma rota inicial, como `/`, que retorne uma mensagem de boas-vindas.
- Garantir que a aplicação possa ser executada com `uvicorn`.
- Exibir uma resposta JSON simples para o cliente.

### 🛠️ Modelar dados e criar endpoints de leitura

#### Descrição
Defina modelos de dados com Pydantic e crie endpoints para listar todos os itens e consultar um item específico.

#### Requisitos
O programa concluído deve:

- Criar um modelo `Item` com campos como `id`, `name`, `description`, `price` e `in_stock`.
- Armazenar uma lista de itens em memória.
- Criar um endpoint `GET /items` para retornar todos os itens.
- Criar um endpoint `GET /items/{item_id}` para retornar um item específico.
- Validar que os dados enviados respeitam o esquema definido.

### 🛠️ Adicionar criação e atualização de recursos

#### Descrição
Implemente operações para criar e atualizar itens usando requisições HTTP com JSON.

#### Requisitos
O programa concluído deve:

- Criar um endpoint `POST /items` para adicionar um novo item.
- Criar um endpoint `PUT /items/{item_id}` para atualizar um item existente.
- Retornar o item criado ou atualizado em JSON.
- Usar códigos de status apropriados, como `201` para criação.

### 🛠️ Melhorar a API com validação e respostas padronizadas

#### Descrição
Finalize a API adicionando boas práticas de resposta, tratamento de erros e visibilidade do comportamento esperado.

#### Requisitos
O programa concluído deve:

- Usar `response_model` para padronizar as respostas.
- Retornar `404` quando um item solicitado não existir.
- Demonstrar mensagens de erro claras para entradas inválidas.
- Organizar a API de forma legível e fácil de expandir.
