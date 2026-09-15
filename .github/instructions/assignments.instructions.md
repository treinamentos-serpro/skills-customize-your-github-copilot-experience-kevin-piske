---
description: "Instruções para usar sempre que criar ou editar arquivos markdown de assignment, garantindo consistência e clareza para os alunos."
applyTo: "assignments/**/*.md"
---

# Diretrizes de Estrutura para Markdowns de Tarefas

Todos os arquivos markdown de tarefas devem seguir estas diretrizes:

## 1. Uso do Template

- Os arquivos markdown de tarefas devem seguir a estrutura definida em [`templates/assignment-template.md`](../../templates/assignment-template.md).
- Cada atividade deve ser criada como um arquivo `README.md` dentro da sua pasta em `assignments/`.
- Não remova ou pule seções obrigatórias do template.

## 2. Estrutura obrigatória

Os cabeçalhos das seções devem usar a mesma estrutura do template, incluindo os emojis e a ordem correta:

```md
# 📘 Atividade: [Título da Atividade]

## 🎯 Objective

[breve descrição do objetivo]

## 📝 Tasks

### 🛠️ [Título da Tarefa]

#### Descrição
[descrição do que o aluno deve fazer]

#### Requisitos
O programa concluído deve:

- [requisito 1]
- [requisito 2]
- [requisito 3]
```

## 3. Regras de escrita

- Use títulos curtos, claros e específicos.
- Escreva o objetivo em 1 a 2 frases, com foco em aprendizagem prática.
- Em cada tarefa, descreva claramente a ação que o aluno deve executar.
- Nos requisitos, prefira itens objetivos, mensuráveis e alinhados com o aprendizado esperado.
- Mantenha o texto em português, com linguagem encorajadora e didática.
- Apenas adicione seções extras se a atividade realmente exigir isso.

## 4. Critério de qualidade

Uma tarefa está em conformidade quando:
- segue a estrutura do template,
- tem objetivo claro,
- contém tarefas bem definidas,
- usa requisitos mensuráveis,
- mantém linguagem consistente com o resto do projeto.