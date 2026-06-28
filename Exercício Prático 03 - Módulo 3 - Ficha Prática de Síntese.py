import time
import os

# Limpar consola (compatível com Windows e sistemas Unix)
os.system("cls" if os.name == "nt" else "clear")


# ============================================================
# NÍVEL BÁSICO - Fundamentos de Controlo de Fluxo
# ============================================================
# Conceitos: while para validação, for para iteração sequencial

def validar_nota():
    """B1: Validação com while
    Solicita até obter nota válida (0-20).
    Equivalente à contagem controlada B1 original."""
    while True:
        try:
            nota = float(input("Insira a nota (0-20): "))
            if 0 <= nota <= 20:
                return nota
            print("Erro: Nota deve estar entre 0 e 20.")
        except ValueError:
            print("Erro: Insira apenas valores numéricos.")


def listar_notas_simples(lista):
    """B2/B3: Listagem com for
    Mostra todas as notas numeradas.
    Retorna True se existirem notas, False caso contrário."""
    if not lista:
        print("Não existem notas registadas.")
        return False

    print("\n--- Listagem de Notas ---")
    for i in range(len(lista)):
        print(f"  Nota {i + 1}: {lista[i]}")
    return True


def contar_pares(lista):
    """B4: Contagem condicional (adaptado)
    Conta valores pares na lista usando for."""
    contador = 0
    for nota in lista:
        if nota % 2 == 0:
            contador += 1
    return contador


# ============================================================
# NÍVEL INTERMÉDIO - Processamento e Cálculos
# ============================================================
# Conceitos: Acumuladores e contadores (I1, I2, I3)

def calcular_soma(lista):
    """I1: Acumulador manual
    Calcula somatório usando ciclo for (não usar sum())."""
    soma = 0
    for nota in lista:
        soma += nota
    return soma


def gerar_tabuada_media(lista):
    """I2: Tabuada adaptada
    Mostra multiplicação da média por 1 a 10."""
    if not lista:
        return

    media = calcular_soma(lista) / len(lista)
    print(f"\n--- Tabuada da Média ({media:.2f}) ---")

    for i in range(1, 11):
        resultado = media * i
        print(f"  {media:.2f} x {i} = {resultado:.2f}")


def contar_positivos_manual(lista):
    """I3: Contador Condicional manual
    Conta notas >= 10 usando for."""
    contador = 0
    for nota in lista:
        if nota >= 10:
            contador += 1
    return contador


# ============================================================
# NÍVEL AVANÇADO - Sistema Integrado
# ============================================================
# Conceitos: Menu repetitivo, soma personalizada, fatorial adaptado

def entrada_multipla_notas(lista):
    """A1: Soma Personalizada
    Permite inserir várias notas de uma vez."""
    print("\n--- Entrada Múltipla ---")
    print("(Deixe vazio e pressione Enter para terminar)")

    while True:
        entrada = input("Nova nota: ").strip()
        if entrada == "":
            print("Entrada terminada.")
            break

        try:
            valor = float(entrada)
            if 0 <= valor <= 20:
                lista.append(valor)
                print(f"  ✓ Registada: {valor}")
            else:
                print(f"  ✗ Fora do intervalo (0-20)")
        except ValueError:
            print("  ✗ Valor inválido")


def calcular_fatorial_adaptado(lista):
    """A3: Fatorial adaptado para produtório
    Multiplica todas as notas (excluindo zeros)."""
    if not lista:
        return 0

    produto = 1
    for nota in lista:
        if nota != 0:
            produto *= nota
    return produto


def menu_principal(lista):
    """A2: Menu Repetitivo Profissional
    Estrutura while True com opções 1-4+0 conforme enunciado."""

    while True:
        # Apresentação do menu
        print("\n" + "="*55)
        print(":           SISTEMA DE GESTÃO DE NOTAS                :")
        print("="*55)
        print(": 1 - Adicionar nota                                  :")
        print(": 2 - Listar notas                                    :")
        print(": 3 - Calcular média                                  :")
        print(": 4 - Mostrar notas positivas (≥10)                   :")
        print(": 0 - Sair                                            :")
        print("="*55)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            # Validação individual
            nova = validar_nota()
            lista.append(nova)
            print(f"Nota {nova} adicionada.")

        elif opcao == "2":
            # Listagem simples
            if listar_notas_simples(lista):
                # Extra: informação sobre pares
                pares = contar_pares(lista)
                print(f"Notas pares: {pares}")

        elif opcao == "3":
            # Cálculo de média com 2 casas decimais
            if len(lista) == 0:
                print("Sem notas para calcular.")
            else:
                soma = calcular_soma(lista)
                media = soma / len(lista)
                print(f"\nSoma: {soma}")
                print(f"Quantidade: {len(lista)}")
                print(f"Média: {media:.2f}")

                # Demonstração extra (I2)
                gerar_tabuada_media(lista)

        elif opcao == "4":
            # Notas positivas usando for (I3)
            positivas = contar_positivos_manual(lista)
            print(f"\nTotal de notas positivas: {positivas}")

            if positivas > 0:
                print("Valores:")
                for nota in lista:
                    if nota >= 10:
                        print(f"  → {nota}")

        elif opcao == "0":
            # Animação de saída
            print("\nA encerrar...")
            for i in range(3, 0, -1):
                print(f"{i}...")
                time.sleep(0.3)
            print("Programa terminado.")
            break

        else:
            print("Opção inválida. Use 0-4.")

        input("\nPressione Enter para continuar...")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

if __name__ == "__main__":
    # Inicialização
    notas = []

    # Cabeçalho académico
    print("""
    ╔══════════════════════════════════════════╗
    ║  FICHA PRÁTICA DE SÍNTESE - PROGRAMAÇÃO  ║
    ║  10º Ano - Ensino Profissional            ║
    ╚══════════════════════════════════════════╝
    """)

    # Iniciar sistema
    menu_principal(notas)


# ============================================================
# PERGUNTAS DE REFLEXÃO
# ============================================================
"""
Q1: Quando usaste while e porquê?
R: Usámos 'while' em três situações principais:
   - No menu principal (menu_principal): while True mantém o programa 
     ativo até o utilizador escolher 0. Necessário porque não sabemos 
     quantas operações serão realizadas.
   - Na validação de notas (validar_nota): while repete até obter 
     valor válido (0-20). Garante integridade dos dados.
   - Na entrada múltipla (entrada_multipla_notas): while continua 
     até utilizador indicar fim (input vazio).

Q2: Quando usaste for e porquê?
R: Usámos 'for' quando o número de iterações é conhecido:
   - Para percorrer a lista de notas (listar_notas_simples, 
     calcular_soma, contar_positivos_manual). O for é mais seguro 
     que while para listas pois evita erros de índice.
   - Para contagens fixas (range) na animação de saída e na tabuada.
   - Preferimos for em vez de while para processamento de coleções 
     pois é mais legível e menos propenso a loops infinitos.

Q3: Que dificuldades encontraste?
R: [Resposta pessoal do aluno]
   Sugestões de reflexão:
   - Diferença entre variáveis locais (dentro de funções) e o 
     passo de listas por referência.
   - Necessidade de validar inputs para evitar erros de execução.
   - Organização do código em funções para melhor manutenção.
   - Cálculo manual da média vs uso de funções embutidas como sum().
"""
