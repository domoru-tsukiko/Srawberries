from flask import Flask, render_template, json
from const import APP_KEY


app = Flask(__name__)
app.config['SECRET_KEY'] = APP_KEY


def main():
    app.run()


if __name__ == '__main__':
    main()
