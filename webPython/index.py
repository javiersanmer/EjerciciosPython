from flask import current_app, render_template
import sqlite3, os


def get_db_conn():
    return sqlite3.connect(current_app.config["DATABASE"])


def load_questions():
    conn = get_db_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, texto FROM questions ORDER BY id")
    rows = cur.fetchall()

    questions = []

    for qid, qtext in rows:
        cur.execute(
            "SELECT id, texto FROM options WHERE question_id = ? ORDER BY id",
            (qid,)
        )

        opts = [
            {"id": oid, "texto": otext}
            for (oid, otext) in cur.fetchall()
        ]

        questions.append({
            "id": qid,
            "texto": qtext,
            "opciones": opts
        })

    conn.close()
    return questions


def index():
    preguntas = load_questions()
    return render_template("index.html", preguntas=preguntas)