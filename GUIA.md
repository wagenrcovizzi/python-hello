# Guia — Python Hello World

## Como executar

Abra o terminal na pasta do projeto e rode:

```
python hello.py
```

Resultado esperado:
Uma janela abre com o texto "Olá, Wagner!" e um botão OK. Clicar OK fecha a janela e encerra o script. Não há mais saída no terminal.

---

## Bloco a bloco

### Bloco 1 — `print()`

```python
print("Hello, World!")
```

`print()` é uma função built-in do Python — sempre disponível, sem necessidade de import. Ela recebe qualquer valor e escreve no stdout (o terminal). Aspas duplas e simples são equivalentes; a convenção é aspas duplas para strings literais.

---

### Bloco 2 — Variável

```python
name = "Wagner"
print(name)
```

Python usa **tipagem dinâmica**: você não declara o tipo, o interpretador o infere em tempo de execução. `name` é do tipo `str`. Não existe `var`, `let` ou `const` — atribuição direta com `=`.

Note que `print(name)` imprime o *valor* da variável, não a palavra "name".

---

### Bloco 3 — Função com type hints

```python
def greet(name: str) -> str:
    return f"Olá, {name}!"
```

**`def`** define uma função. A **indentação** (4 espaços, por convenção PEP 8) é sintaxe — não estilo. Errar a indentação é um erro de compilação em Python.

**`name: str` e `-> str`** são *type hints* (PEP 484, Python 3.5+). São opcionais e ignorados pelo interpretador em tempo de execução — existem para documentação, autocomplete em IDEs e verificação estática com ferramentas como `mypy`. Em projetos reais, type hints são convenção.

**`f"Olá, {name}!"`** é uma *f-string* (PEP 498, Python 3.6+). O prefixo `f` antes das aspas permite interpolar expressões Python diretamente dentro de `{}`. É a forma moderna de formatar strings — prefira sobre `%` e `.format()`.

---

### Bloco 4 — Ponto de entrada

```python
if __name__ == "__main__":
    print(greet(name))
```

Quando Python executa um arquivo diretamente (`python hello.py`), define a variável especial `__name__` como `"__main__"`.

Quando o mesmo arquivo é **importado** por outro script (`import hello`), `__name__` recebe o nome do módulo (`"hello"`), e o bloco não é executado.

Esse padrão protege código de execução de rodar involuntariamente ao importar. Você encontrará em todo projeto Python real — é a convenção universal para o ponto de entrada de um script.

**Para verificar:** crie um segundo arquivo `teste_import.py` com `import hello` e execute-o. Você verá que os `print()` dos blocos 1 e 2 *ainda rodam* (estão no nível do módulo), mas o `print(greet(name))` do bloco 4 não — porque `__name__` não é `"__main__"`.

---

## Próximo passo

Adicione entrada via linha de comando com `sys.argv`:

```python
import sys

# Bloco 5 — argumento de linha de comando
if __name__ == "__main__":
    nome = sys.argv[1] if len(sys.argv) > 1 else name
    print(greet(nome))
```

Execute com:
```
python hello.py Maria
```

`sys.argv` é a lista de argumentos passados ao script. `sys.argv[0]` é sempre o nome do arquivo; `sys.argv[1]` em diante são os argumentos do usuário. `sys` é um módulo da biblioteca padrão — disponível sem instalação, mas requer `import sys`.

Essa é a porta de entrada para qualquer script que precise receber input do usuário via terminal.

---

## v2 — Janela GUI

A partir de v2, `hello.py` usa `tkinter` para exibir o resultado em uma janela em vez do terminal.

```python
import tkinter as tk

def show_window(message: str) -> None:
    root = tk.Tk()
    root.title("Hello World")
    tk.Label(root, text=message, padx=20, pady=20).pack()
    tk.Button(root, text="OK", command=root.destroy).pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    show_window(greet(name))
```

### O que é `tkinter`

`tkinter` é a biblioteca GUI oficial da stdlib do Python — vem instalada junto com o interpretador, não requer `pip install`. É um wrapper sobre a biblioteca Tcl/Tk. Para projetos simples de desktop, é a opção zero-dependência.

### O modelo root → widgets → mainloop

Toda aplicação tkinter segue esta sequência obrigatória:

1. **`root = tk.Tk()`** — cria a janela raiz. Só pode existir uma por processo. Tudo que aparece na tela é filho desta janela.
2. **Widgets** — `Label`, `Button`, `Entry`, etc. são adicionados à janela. Cada widget recebe a janela pai como primeiro argumento (implícito em `.pack()`).
3. **`.pack()`** — gerenciador de layout. Posiciona o widget dentro do pai, por padrão empilhando verticalmente. `padx` e `pady` adicionam espaço interno.
4. **`root.mainloop()`** — inicia o loop de eventos. Bloqueia a execução do script e fica aguardando interações do usuário (cliques, teclas). O script só avança quando a janela é destruída.

### O que é um callback

```python
tk.Button(root, text="OK", command=root.destroy)
```

`command=root.destroy` passa a *referência* à função `destroy` — não a chama. O `()` está ausente intencionalmente. tkinter armazena essa referência e a chama automaticamente quando o botão é clicado.

Comparação:
- `command=root.destroy` → correto: passa a função
- `command=root.destroy()` → errado: chama a função imediatamente ao criar o botão

Esse padrão — passar uma função como argumento para ser chamada depois — chama-se **callback** e aparece em toda programação orientada a eventos (GUI, web, async).

### Por que `mainloop()` bloqueia

`mainloop()` é um loop infinito interno do tkinter:

```
enquanto janela existe:
    processa eventos pendentes (clique, tecla, resize...)
    atualiza a tela
```

O script fica parado nessa linha até que a janela seja destruída (`root.destroy()`). Código escrito após `mainloop()` só executa depois que a janela fecha — comportamento diferente de qualquer função normal.
