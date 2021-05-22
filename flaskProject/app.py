from flask import Flask, render_template, redirect, url_for, send_file, request, session

app = Flask(__name__)
app.secret_key = '123'
users = {
    "Bret": {"name": "Leanne Graham", "email": "Sincere@april.biz", "id": "1"},
    "Antonette": {"name": "Ervin Howell", "email": "Shanna@melissa.tv", "id": "2"},
    "Samantha": {"name": "Clementine Bauch", "email": "Nathan@yesenia.net", "id": "3"},
    "Karianne": {"name": "Patricia Lebsack", "email": "Julianne.OConner@kory.org", "id": "4"},
    "Kamren": {"name": "Chelsey Dietrich", "email": "Lucio_Hettinger@annie.ca", "id": "5"}
}


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
                users[user_name] = {"name": request.form["name"], "id": request.form["id"], "email": request.form["email"]}
                session['user_name'] = user_name
                session['logged'] = True
        else:
            session['logged'] = False
    return render_template('assignment9.html', user_name=user_name, users=users)


@app.route('/logout', methods=['GET', 'POST', 'DELETE'])
def logout():
    session.clear()
    return redirect(url_for('assignment9'))


if __name__ == '__main__':
    app.run(debug=True)
