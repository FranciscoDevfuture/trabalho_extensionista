print("*"*8+"Bem-vindos à Biblioteca Paulo Freire"+"*"*8)

class Aluno:
    def __init__(self, nome_completo, rg, cpf, ru):
        self.nome_completo = nome_completo
        self.rg = rg
        self.cpf = cpf
        self.ru = ru

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True
        self.aluno = None

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.alunos = []

    def cadastrar_aluno(self):
        nome_completo = input("Digite o nome completo do aluno: ")
        rg = input("Digite o RG do aluno: ")
        cpf = input("Digite o CPF do aluno: ")
        ru = input("Digite o RU do aluno: ")
        self.alunos.append(Aluno(nome_completo, rg, cpf, ru))
        print('Aluno Cadastrado com sucesso!')

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar_livro(self, titulo, ru):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                for aluno in self.alunos:
                    if aluno.ru == ru:
                        livro.disponivel = False
                        livro.aluno = aluno
                        return True
        return False

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and not livro.disponivel:
                livro.disponivel = True
                livro.aluno = None
                return True
        return False

    def listar_livros(self):
        for livro in self.livros:
            print(f'Título: {livro.titulo}, Autor: {livro.autor}, Disponível: {"Sim" if livro.disponivel else "Não"}, Aluno: {livro.aluno.nome_completo if livro.aluno else "Nenhum"}')

biblioteca = Biblioteca()
biblioteca.adicionar_livro(Livro('Lógica de programação', 'Rubens'))
biblioteca.adicionar_livro(Livro('Ferramentas de Matemática aplicada', 'Neto1'))

while True:
    print("\nEscolha uma opção:")
    print("1. Cadastrar aluno")
    print("2. Listar livros")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Sair")

    opcao = input("\nOpção selecionada: ")

    if opcao == "1":
        biblioteca.cadastrar_aluno()
    elif opcao == "2":
        biblioteca.listar_livros()
    elif opcao == "3":
        titulo = input("Digite o título do livro que deseja emprestar: ")
        ru = input("Digite o RU do aluno que está emprestando o livro: ")
        if biblioteca.emprestar_livro(titulo, ru):
            print("Livro emprestado com sucesso.")
        else:
            print("O livro não está disponível ou o aluno não está cadastrado.")
    elif opcao == "4":
        titulo = input("Digite o título do livro que deseja devolver: ")
        if biblioteca.devolver_livro(titulo):
            print("Livro devolvido com sucesso.")
        else:
            print("O livro não foi emprestado.")
    elif opcao == "5":
        break
    else:
        print("Opção inválida! Tente novamente.")
