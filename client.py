import poplib
# Configuration du client
pop3_server = 'localhost'
pop3_port = 110
username = 'username'
password = 'password'

# Se connecter au serveur POP3
pop3 = poplib.POP3(pop3_server, pop3_port)
pop3.user(username)
pop3.pass_(password)

# Récupérer la liste des e-mails
num_messages = len(pop3.list()[1])
print(f"Nombre d'e-mails : {num_messages}")

# Récupérer et afficher le contenu des e-mails
for i in range(1, num_messages + 1):
    response = pop3.retr(i)
    email_lines = response[1]
    email_content = b'\n'.join(email_lines).decode()
    print(f"--- Email {i} ---")
    print(email_content)
    print("-----------------")

# Fermer la connexion POP3
pop3.quit()