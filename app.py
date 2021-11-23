from flask import Flask, render_template, request

from models import db, User, Coin, Paragraph
from handle_token import create_access_token, verify_token
from parsing import get_paragraphs

app = Flask(__name__, static_folder='templates/static')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///.db"

db.app = app
db.init_app(app)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", login=None)
    else:
        login_ = request.form["login"]
        pwd = request.form["password"]
        user = User.query.filter_by(login=login_, password=pwd).first()
        access_token = None
        if user is not None:
            access_token = create_access_token(login_, pwd)
            user.token = access_token
            db.session.add(user)
            db.session.commit()
        return render_template("login.html", token=access_token, login=login_)


@app.route("/protected", methods=["GET"])
def protected():
    encoded_jwt = request.args.get("token")
    check = verify_token(encoded_jwt)
    return render_template("token.html", check=check)


@app.route("/coin", methods=["GET", "POST"])
def coin():
    if request.method == "GET":
        return render_template("coin.html", paragraphs="")
    else:
        coin_name = request.form["coin"].lower()
        coin = Coin.query.filter_by(coin_name=coin_name).first()
        if not coin:
            coin = Coin(coin_name=coin_name)
            db.session.add(coin)
            db.session.flush()
            db.session.refresh(coin)
            paragraphs, summaries = get_paragraphs(coin_name)
            for i in range(len(paragraphs)):
                paragraph = Paragraph(coin_id=coin.id, text=paragraphs[i], summary=summaries[i])
                db.session.add(paragraph)
            db.session.commit()
            coin = Coin.query.filter_by(coin_name=coin_name).first()

        return render_template("coin.html", coin=coin_name, paragraphs=coin.paragraphs)


if __name__ == "__main__":
    app.debug = True
    db.create_all()
    app.run(host="0.0.0.0", port=5000)
