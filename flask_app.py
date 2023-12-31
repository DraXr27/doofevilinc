from flask import Flask, flash, redirect, render_template, request, url_for
from bson.objectid import ObjectId
from pymongo_get_database import get_database
from validators import validate_user, validate_login, validate_indication, encrypt_pass, decrypt_pass, generate_key
from check_signature import is_valid_signature
import git

app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = "7F~n)egL`C2_xu9m=8Qr3-J4>;QTY>n,$T3Ze/Bprr&&>xbFF#"

logged_user = {}

db = get_database()

users = db["users"]
categories = db["categories"]
products = db["products"]
indications = db["indications"]



#some bases, don't delete, but don't access lol
@app.route('/random_list', methods=['GET'])
def get_all_objects():
    #objects = db_objects.find()
    #return render_template("random_list.html", objects=objects)
    return render_template("user_register.html") #Delete after creating the method


@app.route('/random/<id>', methods=['GET'])
def get_one_object(id):
    #oid = ObjectId(id)
    #object = db_objects.find_one({'_id': oid})
    #return render_template("view.html", object=object)
    return redirect('/') #Delete after creating the method


@app.route('/test_list', methods=['GET'])
def get_all_test():
    #objects = db_objects.find()
    #return render_template("random_list.html", objects=objects)
    objects = [{'id':'0', 'codigo':'una wea random', 'nombre':'Instruccion1'},{'id':'0', 'codigo':'otra wea random', 'nombre':'Instruccion2'}]
    return render_template("list_base.html", indicationes=objects)





@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        x_hub_signature = request.headers.get('X-Hub-Signature')
        w_secret = 'doofenshmirtzsecretplan2077'
        if not is_valid_signature(x_hub_signature, request.data, w_secret):
            repo = git.Repo('https://github.com/DraXr27/doofevilinc')
            origin = repo.remotes.origin
            origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


@app.route('/', methods=['GET'])
def main():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    global logged_user
    if logged_user == {}:
        if request.method == 'POST':
            form = request.form
            if validate_login(form):
                userkey = generate_key()
                login_user = {
                    'username': form["user_username"],
                    'password': encrypt_pass(form["user_password"], userkey),
                    'key': userkey
                }
                userlist = users.find()
                try:
                    for user in userlist:
                        if user["username"] == login_user["username"]:
                            if decrypt_pass(user["password"], user["key"]) == decrypt_pass(login_user["password"], login_user["key"]):
                                logged_user = user
                                return redirect(url_for('main_page'))
                            else:
                                flash("La contraseña es incorrecta")
                                return redirect(url_for('login'))
                    flash("Usuario no encontrado")
                except StopIteration:
                    flash("No hay usuarios registrados")
                    return redirect(url_for('user_register'))
        return render_template("user_login.html")
    else:
        flash("Cierre sesion para continuar")
        return redirect(url_for('main_page'))



@app.route('/logout', methods=['GET', 'POST'])
def logout():
    global logged_user
    if logged_user:
        userlist = users.find()
        try:
            for user in userlist:
                if user["username"] == logged_user["username"] and decrypt_pass(user["password"], user["key"]) == decrypt_pass(logged_user["password"], logged_user["key"]):
                    logged_user = {}
                    return redirect(url_for('login'))

            flash("Datos de usuario invalidos. Inicie sesion de nuevo")
            logged_user = {}
            return redirect(url_for('login'))
        except StopIteration:
            flash("No hay usuarios registrados")
            return redirect(url_for('user_register'))
    else:
        flash("Inicie sesion para continuar")
        return redirect(url_for('login'))



@app.route('/register', methods=['GET', 'POST'])
def user_register():
    global logged_user
    if logged_user == {}:
        if request.method == 'POST':
            form = request.form
            if validate_user(form):
                userkey = generate_key()
                new_user = {
                    'name': form["user_name"],
                    'username': form["user_username"],
                    'password': encrypt_pass(form["user_password"], userkey),
                    'key': userkey
                }
                userlist = users.find()
                try:
                    for user in userlist:
                        if user["username"] == new_user["username"] or user["name"] == new_user["name"]:
                            flash("Ya se ha registrado a un usuario con ese Nombre o @")
                            return redirect('/register')

                    id = users.insert_one(new_user).inserted_id
                    if id:
                        flash("Usuario creado exitosamente")
                        return redirect(url_for('login'))
                    else:
                        flash("Ocurrio un error añadiendo el usuario")
                        return redirect('/register')

                except StopIteration:
                    id = users.insert_one(new_user).inserted_id
                    if id:
                        flash("Primer usuario creado exitosamente")
                        return redirect(url_for('login'))
                    else:
                        flash("Ocurrio un error añadiendo el usuario")
                        return redirect('/register')
        return render_template("user_register.html")
    else:
        flash("Cierre sesion para continuar")
        return redirect(url_for('main_page'))


@app.route('/main', methods=['GET'])
def main_page():
    global logged_user
    if logged_user:
        userlist = users.find()
        try:
            for user in userlist:
                if user["username"] == logged_user["username"] and decrypt_pass(user["password"], user["key"]) == decrypt_pass(logged_user["password"], logged_user["key"]):
                    return render_template("main_page.html", current_user=user)

            flash("Datos de usuario invalidos. Inicie sesion de nuevo")
            logged_user = {}
            return redirect(url_for('login'))
        except StopIteration:
            flash("No hay usuarios registrados")
            return redirect(url_for('user_register'))
    else:
        flash("Inicie sesion para continuar")
    return redirect(url_for('login'))


@app.route('/user_tab', methods=['GET'])
def user_tab():
    global logged_user
    if logged_user:
        userlist = users.find()
        try:
            for user in userlist:
                if user["username"] == logged_user["username"] and decrypt_pass(user["password"], user["key"]) == decrypt_pass(logged_user["password"], logged_user["key"]):
                    return render_template("user_tab.html", current_user=user)

            flash("Datos de usuario invalidos. Inicie sesion de nuevo")
            logged_user = {}
            return redirect(url_for('login'))
        except StopIteration:
            flash("No hay usuarios registrados")
            return redirect(url_for('user_register'))
    else:
        flash("Inicie sesion para continuar")
    return redirect(url_for('login'))


@app.route('/user_update', methods=['GET', 'POST'])
def user_update():
    global logged_user
    if logged_user:
        userlist = users.find()
        try:
            for user in userlist:
                if user["username"] == logged_user["username"] and decrypt_pass(user["password"], user["key"]) == decrypt_pass(logged_user["password"], logged_user["key"]):
                    if request.method == 'POST':
                        form = request.form
                        if validate_user(form):
                            new_user = {
                                'name': form["user_name"],
                                'username': form["user_username"],
                                'password': encrypt_pass(form["user_password"], user["key"]),
                                'key': user["key"]
                            }

                            users.replace_one({'_id': user["_id"]}, new_user)
                            logged_user = new_user
                            return redirect(url_for('user_tab'))


                    return render_template("user_update.html", old_user=user)

            flash("Datos de usuario invalidos. Inicie sesion de nuevo")
            logged_user = {}
            return redirect(url_for('login'))
        except StopIteration:
            flash("No hay usuarios registrados")
            return redirect(url_for('user_register'))
    else:
        flash("Inicie sesion para continuar")
    return redirect(url_for('login'))


@app.route('/user_delete', methods=['GET', 'POST'])
def user_delete():
    global logged_user
    if logged_user:
        userlist = users.find()
        try:
            for user in userlist:
                if user["username"] == logged_user["username"] and decrypt_pass(user["password"], user["key"]) == decrypt_pass(logged_user["password"], logged_user["key"]):
                    users.delete_one({'_id': user["_id"]})
                    logged_user = {}
                    flash("Usuario eliminado con exito")
                    return redirect(url_for('login'))

            flash("Datos de usuario invalidos. Inicie sesion de nuevo")
            logged_user = {}
            return redirect(url_for('login'))
        except StopIteration:
            flash("No hay usuarios registrados")
            return redirect(url_for('user_register'))
    else:
        flash("Inicie sesion para continuar")
    return redirect(url_for('login'))







@app.route('/indication_add', methods=['GET', 'POST'])
def indication_add():
    global logged_user
    if logged_user:
        userlist = users.find()
        try:
            for user in userlist:
                if user["username"] == logged_user["username"] and decrypt_pass(user["password"], user["key"]) == decrypt_pass(logged_user["password"], logged_user["key"]):


                    if request.method == 'POST':
                        form = request.form
                        if validate_indication(form):
                            new_indic = {
                                'name': form["indication_name"],
                                'instruction': form["indication_instruction"]
                            }

                            indicslist = indications.find()
                            try:
                                for indic in indicslist:
                                    if indic["indication_name"] == new_indic["indication_name"] or indic["indication_instruction"] == new_indic["indication_instruction"]:
                                        flash("Ya se ha registrado una indicacion con ese metodo o nombre")
                                        return redirect('/indications_list')

                                id = indications.insert_one(new_indic).inserted_id
                                if id:
                                    flash("Indicacion creada exitosamente")
                                    return redirect(url_for('indications_list'))
                                else:
                                    flash("Ocurrio un error creando la indicacion")
                                    return redirect('/indications_list')

                            except StopIteration:
                                id = indications.insert_one(new_indic).inserted_id
                                if id:
                                    flash("Primera indicacion creada exitosamente")
                                    return redirect(url_for('indications_list'))
                                else:
                                    flash("Ocurrio un error creando la indicacion")
                                    return redirect('/indications_list')

                    return render_template("indication_add.html", current_user=user)


            flash("Datos de usuario invalidos. Inicie sesion de nuevo")
            logged_user = {}
            return redirect(url_for('login'))
        except StopIteration:
            flash("No hay usuarios registrados")
            return redirect(url_for('user_register'))
    else:
        flash("Inicie sesion para continuar")
    return redirect(url_for('login'))


@app.route('/indications_list', methods=['GET'])
def indications_list():
    global logged_user
    if logged_user:
        userlist = users.find()
        try:
            for user in userlist:
                if user["username"] == logged_user["username"] and decrypt_pass(user["password"], user["key"]) == decrypt_pass(logged_user["password"], logged_user["key"]):


                    indicslist = indications.find()
                    return render_template("indications_list.html", indicationes=indicslist, current_user=user)



            flash("Datos de usuario invalidos. Inicie sesion de nuevo")
            logged_user = {}
            return redirect(url_for('login'))
        except StopIteration:
            flash("No hay usuarios registrados")
            return redirect(url_for('user_register'))
    else:
        flash("Inicie sesion para continuar")
    return redirect(url_for('login'))


@app.route('/<id>/indication_get', methods=['GET'])
def indication_get(id):
    global logged_user
    if logged_user:
        userlist = users.find()
        try:
            for user in userlist:
                if user["username"] == logged_user["username"] and decrypt_pass(user["password"], user["key"]) == decrypt_pass(logged_user["password"], logged_user["key"]):


                    indicslist = indications.find()
                    oid = ObjectId(id)
                    try:
                        for indic in indicslist:
                            if indic['_id'] == oid:
                                return render_template("indication_get.html", indication=indic, current_user=user)
                    except StopIteration:
                        flash("No hay indicaciones añadidas")
                        return redirect(url_for('indications_list'))


            flash("Datos de usuario invalidos. Inicie sesion de nuevo")
            logged_user = {}
            return redirect(url_for('login'))
        except StopIteration:
            flash("No hay usuarios registrados")
            return redirect(url_for('user_register'))
    else:
        flash("Inicie sesion para continuar")
    return redirect(url_for('login'))


@app.route('/<id>/indication_update', methods=['GET', 'POST'])
def indication_update(id):
    global logged_user
    if logged_user:
        userlist = users.find()
        try:
            for user in userlist:
                if user["username"] == logged_user["username"] and decrypt_pass(user["password"], user["key"]) == decrypt_pass(logged_user["password"], logged_user["key"]):


                    if request.method == 'POST':
                        form = request.form
                        if validate_indication(form):
                            new_indic = {
                                'name': form["indication_name"],
                                'instruction': form["indication_instruction"]
                            }

                            indicslist = indications.find()
                            oid = ObjectId(id)
                            try:
                                for indic in indicslist:
                                    if indic['_id'] == oid:
                                        indications.replace_one({'_id': indic["_id"]}, new_indic)
                                        flash("Indicacion reemplazada con exito")
                                        return redirect(url_for('indications_list'))
                            except StopIteration:
                                flash("No hay indicaciones añadidas")
                                return redirect(url_for('indications_list'))

                    indicslist = indications.find()
                    oid = ObjectId(id)
                    try:
                        for indic in indicslist:
                            if indic['_id'] == oid:
                                return render_template("indication_update.html", old_indication=indic, current_user=user)
                    except StopIteration:
                        flash("No hay indicaciones añadidas")
                        return redirect(url_for('indications_list'))


            flash("Datos de usuario invalidos. Inicie sesion de nuevo")
            logged_user = {}
            return redirect(url_for('login'))
        except StopIteration:
            flash("No hay usuarios registrados")
            return redirect(url_for('user_register'))
    else:
        flash("Inicie sesion para continuar")
    return redirect(url_for('login'))


@app.route('/<id>/indication_delete', methods=['GET', 'POST'])
def indication_delete(id):
    global logged_user
    if logged_user:
        userlist = users.find()
        try:
            for user in userlist:
                if user["username"] == logged_user["username"] and decrypt_pass(user["password"], user["key"]) == decrypt_pass(logged_user["password"], logged_user["key"]):


                        indicslist = indications.find()
                        oid = ObjectId(id)
                        try:
                            for indic in indicslist:
                                if indic['_id'] == oid:
                                    indications.delete_one({'_id': indic["_id"]})
                                    flash("Indicacion eliminada con exito")
                                    return redirect(url_for('indications_list'))
                        except StopIteration:
                            flash("No hay indicaciones añadidas")
                            return redirect(url_for('indications_list'))


            flash("Datos de usuario invalidos. Inicie sesion de nuevo")
            logged_user = {}
            return redirect(url_for('login'))
        except StopIteration:
            flash("No hay usuarios registrados")
            return redirect(url_for('user_register'))
    else:
        flash("Inicie sesion para continuar")
    return redirect(url_for('login'))






if __name__ == '__main__':
    app.run(debug=True)