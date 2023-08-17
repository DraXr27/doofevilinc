from flask import flash
from cryptography.fernet import Fernet

def validate_login(form):
    is_valid = True

    if not form["user_username"]:
        is_valid = False
        flash("El nombre de usuario es obligatorio")

    if not form["user_password"]:
        is_valid = False
        flash("La contraseña es obligatoria")

    return is_valid

def validate_user(form):
    is_valid = True
    if not form["user_name"]:
        is_valid = False
        flash("El nombre real del usuario es obligatorio")

    if not form["user_username"]:
        is_valid = False
        flash("El nombre de usuario es obligatorio")

    if not form["user_password"]:
        is_valid = False
        flash("La contraseña es obligatoria")

    return is_valid

def validate_indication(form):
    is_valid = True
    if not form["indication_name"]:
        is_valid = False
        flash("El nombre de la indicacion es obligatoria")

    if not form["indication_instruction"]:
        is_valid = False
        flash("La indicacion es obligatoria")

    return is_valid


def generate_key():
    key = Fernet.generate_key()
    return key


def encrypt_pass(passw, key):
    fernet = Fernet(key)
    encpass = fernet.encrypt(passw.encode())
    return encpass


def decrypt_pass(encpass, key):
    fernet = Fernet(key)
    passw = fernet.decrypt(encpass).decode()
    return passw