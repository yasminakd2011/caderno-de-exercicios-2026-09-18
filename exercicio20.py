senha_secreta = "etec123"

senha = input("Digite a senha: ")

while senha != senha_secreta:
    print("Senha incorreta!")
    senha = input("Digite a senha novamente: ")

print("Acesso Permitido")