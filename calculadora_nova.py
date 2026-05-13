while True:
    entrada = input("\nDigite o primeiro número (ou 'sair' para encerrar): ")

    if entrada.lower() == "sair":
        print("Encerrando calculadora...")
        break

    try:
        num1 = float(entrada)
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao not in {"+", "-", "*", "/"}:
            raise ValueError("Operação inválida.")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2  # pode gerar ZeroDivisionError

    except ValueError as e:
        print("Erro:", e if str(e) else "Entrada não numérica.")
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida.")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Operação processada.")