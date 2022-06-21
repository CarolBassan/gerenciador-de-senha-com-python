import sqlite3

MASTER_PASSWORD = "123456"

senha = input("Digite a senha: ")
if senha != MASTER_PASSWORD:
    print("Senha inválida! Encerrando...")
    exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL);
''')

def menu():
    print("****************************************")
    print("* i: Inserir nova senha                *")
    print("* l: Listar serviços salvos            *")
    print("* r: Recuperar senha                   *")
    print("* s: Sair                              *")
    print("****************************************")

def get_pasword(service):
    cursor.execute(f'''
       SELECT usarname, password FROM users 
       WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        print("Serviço não  (use 'l' para verificar os serviços).")
    else:
        for password in cursor.fetchall():
            print(user)

def insert_password(service, username, password):
    cursor.execute(f'''
    INSERT INTO users (service, username, password)
    VALUES ('{service}', '{username}', '{password}');
    ''')
    conn.commit()

def show_services():
    cursor.execute('''
    SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

while True:
    menu()
    op = input("O que deseja fazer? ")
    if op not in ['l', 'i', 'r', 's']:
        print("Opção inválida")
        continue

    if op == 's':
        break

    if op == 'i':
        service = input("Qual o serviço? ")
        username = input("Qual o usuário? ")
        password = input("Qual a senha? ")
        insert_password(service, username, password)

    if op == 'l':
        show_services()

    if op == 'r':
        service = input("Qual o serviço para o qual quer a senha? ")
        get_pasword(service)

conn.close()