import unittest

def verifica_senha(senha):
    if len(senha) < 8:
        return False

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True

    return tem_maiuscula and tem_minuscula and tem_numero

class TesteVerificaSenha(unittest.TestCase):

    def test_senha_segura(self):
        self.assertTrue(verifica_senha("Senha123"))

    def test_senha_curta(self):
        self.assertFalse(verifica_senha("123"))

    def test_senha_sem_maiuscula(self):
        self.assertFalse(verifica_senha("senha123"))

    def test_senha_sem_minuscula(self):
        self.assertFalse(verifica_senha("SENHA123"))

    def test_senha_sem_numero(self):
        self.assertFalse(verifica_senha("SenhaSemNumero"))

if __name__ == '__main__':
    unittest.main()

senha = input("Insira uma senha: ")

if verifica_senha(senha):
    print("Senha segura")
else:
    print("Senha não segura. Insira uma senha válida.")
