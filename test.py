from data.posts import Post
from data.accounts import Account
from data.topics import Topic
from data import db_session


db_session.global_init("db/orange.db")
db_sess = db_session.create_session()

# account = Account(name='Тестовый', email='tect@email.ru', hashed_password='123456789', is_moderator=True,
#                   is_email_true=True)
# topic = Topic(title='Тест', description='Рецепт хороших пельменей очень прост. Кладёшь много-много мяса и мало-мало '
#                                         'теста', is_moderated=True)
acc = db_sess.query(Account).filter(Account.id == 1).first()
post = Post(topic_id=1, author_id=acc.id, author=acc, title='Первая запись', text='И она совершенно безинформативна!',
            count_likes=0, count_comments=0, is_moderated=True)

db_sess.add(post)
db_sess.commit()
