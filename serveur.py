from poplib import POP3Server
# Classe de gestion du serveur POP3
class MyPOP3Server(POP3Server):
    def handle_AUTH(self, args):
        self.send_response('OK', b'Authentication succeeded')

# Configuration du serveur
host = 'localhost'
port = 110

# Démarrer le serveur POP3
server = MyPOP3Server((host, port))
print(f"Serveur POP3 démarré sur {host}:{port}")

# Lancer la boucle d'écoute du serveur
server.serve_forever()