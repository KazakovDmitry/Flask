from flask import Flask, render_template, request, make_response, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '9628a7bef98e08396c7cdf440381b789ad090db6f81715fa66d4f7b785961425'


@app.route('/')
def index():
    if 'username' in session:
        # return f'Привет, {session["username"]}'
        return render_template('logout_form.html')
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        return redirect(url_for('index'))
    return render_template('login_form.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
