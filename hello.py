# Bloco 1 — saída direta
print("Hello, World!")

# Bloco 2 — variável
name = "Wagner"
print(name)

# Bloco 3 — função com type hints
def greet(name: str) -> str:
    return f"Olá, {name}!"

# Bloco 4 — ponto de entrada
if __name__ == "__main__":
    print(greet(name))