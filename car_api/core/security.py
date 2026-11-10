from pwdlib import PasswordHash

pwd_context = PasswordHash.recommended()


# Cria senha criptografada e devolve ela criptografada
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


# Verifica a senha criptografada e verifica se bate com a senha descriptografada
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
