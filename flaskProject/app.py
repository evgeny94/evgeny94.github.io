from flask import Flask, render_template, redirect, url_for, send_file

app = Flask(__name__)


@app.route('/main')
@app.route('/home page')
@app.route('/')
def index():
    return render_template('CV.html')


@app.route('/contactList')
def contact_list():
    return render_template('Contact List.html')


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


if __name__ == '__main__':
    app.run(debug=True)
