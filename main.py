from flask import Flask, render_template, json
from const import APP_KEY
from data import db_session
# from flask_login import LoginManager, login_user

from forms.login import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = APP_KEY
# login_manager = LoginManager()
# login_manager.init_app(app)


def main():
    # db_session.global_init("db/orange.db")
    app.run()


@app.route('/')
@app.route('/main')
def str_main():
    return render_template('main.html', title='Главная')


# @login_manager.user_loader
# def load_user(account_id):
#     db_sess = db_session.create_session()
#     return db_sess.query(Account).get(account_id)
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         db_sess = db_session.create_session()
#         user = db_sess.query(Account).filter(Account.email == form.email.data).first()
#         if user and user.check_password(form.password.data):
#             login_user(user, remember=form.remember_me.data)
#             return redirect("/")
#         return render_template('login.html',
#                                message="Неправильный логин или пароль",
#                                form=form)
#     return render_template('login.html', title='Авторизация', form=form)
#
#
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect("/")


if __name__ == '__main__':
    main()
