from flask import Flask, render_template, redirect, url_for, send_file, request, session, jsonify
import mysql.connector
from assignment10.assignment10 import assignment10

app = Flask(__name__)
app.secret_key = '123'
users = {
    "Bret": {"name": "Leanne Graham", "email": "Sincere@april.biz", "id": "1"},
    "Antonette": {"name": "Ervin Howell", "email": "Shanna@melissa.tv", "id": "2"},
    "Samantha": {"name": "Clementine Bauch", "email": "Nathan@yesenia.net", "id": "3"},
    "Karianne": {"name": "Patricia Lebsack", "email": "Julianne.OConner@kory.org", "id": "4"},
    "Kamren": {"name": "Chelsey Dietrich", "email": "Lucio_Hettinger@annie.ca", "id": "5"}
}


# -------------------------------------------------------#
# --------------- Database Connection -------------------#
# -------------------------------------------------------#
def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost', user='root', passwd='root', database='assignment10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# -------------------------------------------------------#
# ----------------------- INSERT ------------------------#
# -------------------------------------------------------#

@app.route('/insert', methods=['POST'])
def assignment_insert():
    if request.method == 'POST':
        user_id = request.form['id']
        user_fullname = request.form['name']
        user_name = request.form['user_name']
        user_email = request.form['email']
        query = "INSERT INTO users VALUES('%s', '%s', '%s', '%s')" % (user_id, user_fullname, user_name, user_email)
        query_result = interact_db(query=query, query_type='commit')
        return redirect('/assignment10')


# -------------------------------------------------------#
# ----------------------- UPDATE ------------------------#
# -------------------------------------------------------#
@app.route('/update', methods=['POST', 'UPDATE'])
def assignment_update():
    if request.method == 'POST':
        user_id = request.form['id']
        if user_id != "":
            user_fullname = request.form['name']
            user_name = request.form['user_name']
            user_email = request.form['email']
            if user_fullname != "" and user_name != "" and user_email != "":
                query = "UPDATE users SET Name = '%s', UserName = '%s', Email = '%s' WHERE ID='%s'" % (
                    user_fullname, user_name, user_email, user_id)
                query_result = interact_db(query=query, query_type='commit')
                return redirect('/assignment10')
            elif user_fullname != "" and user_name != "":
                query = "UPDATE users SET Name = '%s', UserName = '%s' WHERE ID='%s'" % (
                    user_fullname, user_name, user_id)
                query_result = interact_db(query=query, query_type='commit')
                return redirect('/assignment10')
            elif user_fullname != "" and user_email != "":
                query = "UPDATE users SET Name = '%s', Email = '%s' WHERE ID='%s'" % (
                    user_fullname, user_email, user_id)
                query_result = interact_db(query=query, query_type='commit')
                return redirect('/assignment10')
            elif user_name != "" and user_email != "":
                query = "UPDATE users SET UserName = '%s', Email = '%s' WHERE ID='%s'" % (
                    user_name, user_email, user_id)
                query_result = interact_db(query=query, query_type='commit')
                return redirect('/assignment10')
            elif user_fullname != "" and user_name == "" and user_email == "":
                query = "UPDATE users SET UserName = '%s' WHERE ID='%s'" % (user_fullname, user_id)
                query_result = interact_db(query=query, query_type='commit')
                return redirect('/assignment10')
            elif user_name != "" and user_fullname == "" and user_email == "":
                query = "UPDATE users SET UserName = '%s' WHERE ID='%s'" % (user_name, user_id)
                query_result = interact_db(query=query, query_type='commit')
                return redirect('/assignment10')
            elif user_email != "" and user_name == "" and user_fullname == "":
                query = "UPDATE users SET Email = '%s' WHERE ID='%s'" % (user_email, user_id)
                query_result = interact_db(query=query, query_type='commit')
                return redirect('/assignment10')
    return redirect('/assignment10')


# -------------------------------------------------------#
# ----------------------- DELETE ------------------------#
# -------------------------------------------------------#

@app.route('/delete', methods=['POST'])
def assignment_delete():
    if request.method == 'POST':
        user_id = request.form['id']
        query = "DELETE FROM users WHERE ID='%s';" % user_id
        query_result = interact_db(query=query, query_type='commit')
        return redirect('/assignment10')


# -------------------------------------------------------#
# ----------------------- GET ---------------------------#
# -------------------------------------------------------#
@app.route('/assignment10', methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def assignment_get():
    query = "select * from users ORDER BY ID asc"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', template_folder='../assignment10/templates', users=query_result)
    return render_template('templates/assignment10.html', users=query_result)


@app.route('/main')
@app.route('/home page')
@app.route('/')
def index():
    return render_template('CV.html')


@app.route('/contactList')
def contact_list():
    return render_template('Contact List.html')


@app.route('/newUsersList')
def new_users_list():
    return render_template('new users list.html')


@app.route('/downloadCV')
def download_cv():
    return send_file('static/files/Evgeny Musatov-CV.docx')


@app.route('/assignment8')
def assignment8():
    user_name = {'firstname': "Evgeny", 'lastname': "Musatov"}
    hobbies = ['guitar', 'video games', 'tv series', 'nature', 'friends', 'travel']
    music = ('Rap', 'Trance', 'Hip-Hop', 'Classic Rock', 'Reggaeton')
    stranger_string = {'str': "Hello Stranger! I do not have any info about you."}
    return render_template('assignment8.html', user_name=user_name, hobbies=hobbies, music=music,
                           stranger_string=stranger_string)


@app.route('/assignment8withFriends')
def with_friends():
    user_name = {'firstname': "Evgeny", 'lastname': "Musatov"}
    hobbies = ['guitar', 'video games', 'tv series', 'nature', 'friends', 'travel']
    music = ('Rap', 'Trance', 'Hip-Hop', 'Classic Rock', 'Reggaeton')
    stranger_string = {'str': "Hello Stranger! I do not have any info about you."}
    return render_template('myFriendsBlock.html', user_name=user_name, hobbies=hobbies, music=music,
                           stranger_string=stranger_string)


@app.route('/assignment9', methods=['GET', 'POST', 'DELETE'])
def assignment9():
    cur_method = request.method
    if cur_method == 'GET':
        if request.args:
            if 'user_name' in request.args:
                user_name = request.args['user_name']
                if user_name != '' and user_name in users:
                    return render_template('assignment9.html', user_name=user_name, users=users, exists=True,
                                           search=True)
                elif user_name != '' and user_name not in users:
                    return render_template('assignment9.html', exists=False, search=True)
                else:
                    return render_template('assignment9.html', users=users, search=True)
            else:
                return render_template('assignment9.html', users=users, exists=False, search=True)
        else:
            return render_template('assignment9.html')
    elif cur_method == 'POST':
        if 'user_name' in request.form:
            user_name = request.form['user_name']
            if user_name != '' and user_name not in users:
                users[user_name] = {"name": request.form["name"], "id": request.form["id"],
                                    "email": request.form["email"]}
                session['user_name'] = user_name
                session['logged'] = True
        else:
            session['logged'] = False
    return render_template('assignment9.html', user_name=user_name, users=users)


@app.route('/logout', methods=['GET', 'POST', 'DELETE'])
def logout():
    session.clear()
    return redirect(url_for('assignment9'))


# -------------------------------------------------------#
# ------------------ Assignment 11 ----------------------#
# -------------------------------------------------------#

@app.route('/assignment11/users')
def users_list():
    query = "select * from users ORDER BY ID asc"
    query_result = interact_db(query=query, query_type='fetch')
    response = query_result
    response = jsonify(response)
    return response


@app.route('/assignment11/users/selected', defaults={'SOME_USER_ID': 0})
@app.route('/assignment11/users/selected/<int:SOME_USER_ID>')
def user_details(SOME_USER_ID):
    response = {}
    query = "select * from users where ID='%s';" % SOME_USER_ID
    query_result = interact_db(query=query, query_type='fetch')
    if len(query_result) != 0:
        response = query_result[0]
    else:
        response = "There is no such user. Try again..."

    response = jsonify(response)
    return response


# -------------------------------------------------------#
# ------------------- BluePrint 10 ----------------------#
# -------------------------------------------------------#
app.register_blueprint(assignment10)

if __name__ == '__main__':
    app.run(debug=True)
