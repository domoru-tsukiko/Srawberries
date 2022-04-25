import os

from flask import Flask, render_template, json, redirect, request
from werkzeug.utils import secure_filename

from const import APP_KEY
from data import db_session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data.posts import Post
from data.topics import Topic
from data.accounts import Account
from forms.appendix import SearchForm
from forms.create_topic import CreateTopic
from forms.login import LoginForm
from forms.user import RegisterForm
from forms.create_post import CreatePost

app = Flask(__name__)
app.config['SECRET_KEY'] = APP_KEY
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/orange.db")
    app.run()


@app.route('/')
@app.route('/main', methods=['GET', 'POST'])
def str_main():
    db_sess = db_session.create_session()
    posts = list(db_sess.query(Post).all())
    posts.sort(key=lambda x: x.created_date, reverse=True)
    topics = db_sess.query(Topic)
    return render_template("main.html", posts=posts, topics=topics, title="Главная страница Orange forum")


@app.route('/topic')
def catalog():
    db_sess = db_session.create_session()
    topics = list(db_sess.query(Topic).all())
    topics.sort(key=lambda x: x.title)
    return render_template('catalog.html', topics=topics, title='Каталог тем Orange forum')


@app.route('/create-topic', methods=['GET', 'POST'])
def create_topic():
    form = CreateTopic()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        db_sess.add(Topic(title=form.title.data, description=form.description.data, is_moderated=False))
        db_sess.commit()
        return redirect('/')
    return render_template('create_topic.html', title='Добавление темы',
                           form=form)


@app.route('/topic/<int:id>')
def catalog_id(id):
    db_sess = db_session.create_session()
    topic = db_sess.query(Topic).filter(Topic.id == id).first()
    posts = list(db_sess.query(Post).filter(Post.topic_id == id).all())
    posts.sort(key=lambda x: x.created_date, reverse=True)
    return render_template('topic.html', topic=topic, posts=posts, len_post=len(posts), title=f'Тема: "{topic.title}"')


@app.route('/topic/<int:id>/create-post', methods=['GET', 'POST'])
def create_post(id):
    form = CreatePost()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        topic = db_sess.query(Topic).filter(Topic.id == id).first()
        news = Post(topic_id=id, topic=topic, author_id=current_user.id, title=form.title.data, text=form.text.data, count_likes=0,
                    count_comments=0, is_moderated=False)
        db_sess.add(news)
        db_sess.commit()
        return redirect('/')
    return render_template('create_post.html', title='Добавление поста',
                           form=form)


@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        text = request.form['search']
        text.strip()
        if text != '':
            db_sess = db_session.create_session()
            topics = db_sess.query(Topic).filter(Topic.title.like(f'%{text}%') | Topic.title.like(f'%{text.lower()}%') | Topic.title.like(f'%{text.upper()}%') | Topic.title.like(f'%{text.capitalize()}%')).all()
            posts = db_sess.query(Post).filter(Post.title.like(f'%{text}%') | Post.text.like(f'%{text}%') | Post.title.like(f'%{text.lower()}%') | Post.text.like(f'%{text.lower()}%') | Post.title.like(f'%{text.upper()}%') | Post.text.like(f'%{text.upper()}%') | Post.title.like(f'%{text.capitalize()}%') | Post.text.like(f'%{text.capitalize()}%')).all()
            topics.sort(key=lambda x: x.created_date, reverse=True)
            posts.sort(key=lambda x: x.created_date, reverse=True)
            return render_template('search.html', posts=posts, len_post=len(posts), topics=topics, len_topic=len(topics), title='Поиск по сайту Orange forum')
    posts = []
    topics = []
    return render_template('search.html', posts=posts, len_post=len(posts), topics=topics, len_topic=len(topics), title='Поиск по сайту Orange forum')


@app.route('/profile')
def profile():
    db_sess = db_session.create_session()
    posts = list(db_sess.query(Post).filter(Post.author_id == current_user.id).all())
    posts.sort(key=lambda x: x.created_date, reverse=True)
    statics = [f'Постов {len(posts)}', f'Лайков под постами {current_user.count_like()}', f'Комментариев под постами {current_user.count_comm()}', f'Оставленных комментариев {current_user.count_my_comm()}']
    return render_template('profile.html', user=current_user, user_id=current_user.id, posts=posts, len_post=len(posts), statics=statics, title='Профиль пользователя Orange forum')


@app.route('/profile/<int:id>')
def profile_id(id):
    if id == current_user.id:
        return redirect("/profile")
    db_sess = db_session.create_session()
    user = db_sess.query(Account).filter(Account.id == id).first()
    posts = list(db_sess.query(Post).filter(Post.author_id == user.id).all())
    posts.sort(key=lambda x: x.created_date, reverse=True)
    statics = [f'Постов {len(posts)}', f'Лайков под постами {user.count_like()}', f'Комментариев под постами {user.count_comm()}', f'Оставленных комментариев {user.count_my_comm()}']
    return render_template('profile.html', user=user, user_id=user.id, posts=posts, len_post=len(posts), statics=statics, title='Профиль пользователя Orange forum')


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(Account).filter(Account.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = Account(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data,
            is_moderator=False,
            is_email_true=False
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@login_manager.user_loader
def load_user(account_id):
    db_sess = db_session.create_session()
    return db_sess.query(Account).get(account_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(Account).filter(Account.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    main()
