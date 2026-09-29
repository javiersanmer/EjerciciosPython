from flask import Flask
import os
import index
import resultado
from db_init import init_db

init_db()
app = Flask(__name__)
app.config["DATABASE"] = os.path.join("data", "quiz.db")

app.add_url_rule("/", view_func=index.index, methods=["GET"])
app.add_url_rule("/resultado", view_func=resultado.resultado, methods=["POST"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True) 