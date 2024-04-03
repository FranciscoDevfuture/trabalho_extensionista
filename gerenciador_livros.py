class Aluno:
    def __init__(self, nome, rg, cpf, telefone, ru_escola):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.telefone = telefone
        self.ru_escola = ru_escola

    def __str__(self):
        return f"Nome: {self.nome}, RG: {self.rg}, CPF: {self.cpf}, Telefone: {self.telefone}, RU Escola: {self.ru_escola}"


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.alunos = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_livros_disponiveis(self):
        livros_disponiveis = [livro for livro in self.livros if livro['status'] == 'Disponível']
        return livros_disponiveis

    def listar_alunos(self):
        return self.alunos

    def salvar_info(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("### Lista de Alunos ###\n")
            for aluno in self.alunos:
                arquivo.write(str(aluno) + "\n\n")
            arquivo.write("### Lista de Livros Disponíveis ###\n")
            for livro in self.livros:
                arquivo.write(f"Título: {livro['titulo']}, Autor: {livro['autor']}\n")


def main():
    biblioteca = Biblioteca()
    print('#'*6,'Gerenciador de Biblioteca','#'*6)
    while True:
        print("\n### Menu ###")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Cadastrar livro")
        print("4. Listar livros disponíveis")
        print("5. Salvar informações")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do aluno: ")
            rg = input("Digite o RG do aluno: ")
            cpf = input("Digite o CPF do aluno: ")
            telefone = input("Digite o telefone do aluno: ")
            ru_escola = input("Digite o RU da escola do aluno: ")
            aluno = Aluno(nome, rg, cpf, telefone, ru_escola)
            biblioteca.cadastrar_aluno(aluno)
            print("Aluno cadastrado com sucesso!")

        elif opcao == '2':
            print("\nLista de Alunos:")
            for aluno in biblioteca.listar_alunos():
                print(aluno)

        elif opcao == '3':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            livro = {'titulo': titulo, 'autor': autor, 'status': 'Disponível'}
            biblioteca.cadastrar_livro(livro)
            print("Livro cadastrado com sucesso!")

        elif opcao == '4':
            print("\nLista de Livros Disponíveis:")
            for livro in biblioteca.listar_livros_disponiveis():
                print(f"Título: {livro['titulo']}, Autor: {livro['autor']}")

        elif opcao == '5':
            nome_arquivo = input("Digite o nome do arquivo para salvar as informações: ")
            biblioteca.salvar_info(nome_arquivo)
            print(f"Informações salvas no arquivo '{nome_arquivo}'")

        elif opcao == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
