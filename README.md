# EXPA03 — Sistema de Gestão de Notas

**Disciplina:** Programação e Sistemas de Informação (PSI) — Módulo 3
**Exercício Prático:** 03
**Código:** `1I-PSI-M3-14785-EXPA03`
**Turma:** 1.º I — N.º 14785
**Ano Letivo:** 2025/2026

Programa em Python que integra `while`, `for`, funções e um menu interativo para gerir uma lista de notas escolares. Estruturado em três níveis de complexidade progressiva.

---

## Ficheiros

| Ficheiro | Descrição |
|---|---|
| `Exercicio Pratico 03 - Modulo 3 - Ficha Pratica de Sintese.py` | Programa completo |
| `README.md` | Este ficheiro |

---

## Funcionalidades

| Opção | Ação |
|---|---|
| 1 | Adicionar nota (validação: 0 a 20) |
| 2 | Listar todas as notas |
| 3 | Calcular e mostrar média |
| 4 | Mostrar notas positivas (>= 10) |
| 0 | Sair com animação de contagem decrescente |

---

## Funções Implementadas

### Nível Básico

**`validar_nota()`** — Solicita uma nota ao utilizador em ciclo `while` até obter um valor válido entre 0 e 20. Inclui tratamento de exceção `ValueError` para entradas não numéricas.

```python
def validar_nota():
    while True:
        try:
            nota = float(input("Insira a nota (0-20): "))
            if 0 <= nota <= 20:
                return nota
            print("Erro: Nota deve estar entre 0 e 20.")
        except ValueError:
            print("Erro: Insira apenas valores numericos.")
```

**`listar_notas_simples(lista)`** — Percorre a lista com `for` e mostra as notas numeradas. Devolve `False` se a lista estiver vazia.

**`contar_pares(lista)`** — Conta quantas notas são valores pares usando `for` e `%`.

---

### Nível Intermédio

**`calcular_soma(lista)`** — Acumulador manual com `for` — não usa a função `sum()`.

```python
def calcular_soma(lista):
    soma = 0
    for nota in lista:
        soma += nota
    return soma
```

**`gerar_tabuada_media(lista)`** — Calcula a média e mostra a sua tabuada de 1 a 10 com `for`.

**`contar_positivos_manual(lista)`** — Conta as notas iguais ou superiores a 10 sem usar funções embutidas.

---

### Nível Avançado

**`entrada_multipla_notas(lista)`** — Permite inserir várias notas em sequência; input vazio termina a entrada.

**`calcular_fatorial_adaptado(lista)`** — Produtório de todas as notas não nulas, adaptação do conceito de fatorial.

**`menu_principal(lista)`** — Ciclo `while True` com estrutura `if / elif` para cada opção; termina com a opção `0`.

---

## Estrutura Geral do Programa

```
Inicialização
|
+-- Cabeçalho académico
|
+-- menu_principal(notas)
    |
    +-- opção 1 --> validar_nota() --> lista.append()
    |
    +-- opção 2 --> listar_notas_simples() --> contar_pares()
    |
    +-- opção 3 --> calcular_soma() / len() --> média
    |               gerar_tabuada_media()
    |
    +-- opção 4 --> contar_positivos_manual()
    |               for nota in lista: if nota >= 10
    |
    +-- opção 0 --> animação de saída (for range(3,0,-1)) --> break
```

---

## Conceitos Abordados

| Conceito | Aplicação |
|---|---|
| `while True` | Menu repetitivo com `break` controlado |
| `while` com condição | Validação de input até valor correto |
| `for` em lista | Percorrer, contar, acumular |
| `try / except ValueError` | Tratamento de entrada não numérica |
| Funções | Modularização — cada função com responsabilidade única |
| Lista (`list`) | Estrutura de dados mutável para acumular notas |
| `:.2f` | Formatação de decimais em f-strings |
| `range(3, 0, -1)` | Contagem decrescente |

---

## Como Executar

```bash
git clone https://github.com/a14785-oficina/sistema-gestao-notas.git
cd sistema-gestao-notas
python3 "Exercicio Pratico 03 - Modulo 3 - Ficha Pratica de Sintese.py"
```

---

## Navegação — Módulo 3

| Posição | Repositório |
|---|---|
| Anterior | [EXPA02 — Ciclos While e For](https://github.com/a14785-oficina/ciclos-while-e-for) |
| Seguinte | [EXPA04 — Sistema de Gestão de Stock](https://github.com/a14785-oficina/sistema-gestao-stock) |
| Portfólio | [oficina-jpc](https://github.com/a14785-oficina/oficina-jpc) |

---

*PSI — Módulo 3 — Programação Estruturada — OFICINA — 2025/2026*
