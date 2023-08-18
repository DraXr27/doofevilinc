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
        flash("El nombre de la indicacion es obligatorio")

    if not form["indication_instruction"]:
        is_valid = False
        flash("La indicacion es obligatoria")

    return is_valid


def validate_category(form):
    is_valid = True
    if not form["category_name"]:
        is_valid = False
        flash("El nombre de la categoria es obligatorio")

    if not form["category_description"]:
        is_valid = False
        flash("La descripcion de la categoria es obligatoria")

    return is_valid


def validate_exam(form):
    is_valid = True
    if not form["exam_name"]:
        is_valid = False
        flash("El nombre del examen es obligatorio")

    if not form["exam_category"]:
        is_valid = False
        flash("La categoria del examen es obligatoria")

    if not form["exam_type"]:
        is_valid = False
        flash("El tipo de examen es obligatorio")

    if not form["exam_price"]:
        is_valid = False
        flash("El precio del examen es obligatorio")

    if not form["exam_indications"]:
        is_valid = False
        flash("Las indicaciones del examen son obligatorias")

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