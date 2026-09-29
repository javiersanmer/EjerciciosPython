from flask import current_app, request, render_template
import sqlite3, os


def get_db_conn():
    return sqlite3.connect(current_app.config["DATABASE"])


def resultado():
    conn = get_db_conn()
    cur = conn.cursor()

    cur.execute("""
        SELECT q.id, q.texto, o.id, o.texto, o.es_correcta
        FROM questions q
        JOIN options o ON o.question_id = q.id
        ORDER BY q.id, o.id
    """)

    rows = cur.fetchall()
    conn.close()

    # Reorganizar por pregunta
    preguntas = {}

    for qid, qtext, oid, otext, es_corr in rows:
        preguntas.setdefault(qid, {
            "texto": qtext,
            "opciones": [],
            "correcta_id": None,
            "correcta_texto": None
        })

        preguntas[qid]["opciones"].append({
            "id": oid,
            "texto": otext
        })

        if es_corr:
            preguntas[qid]["correcta_id"] = oid
            preguntas[qid]["correcta_texto"] = otext

    detalles, aciertos = [], 0

    for qid, qdata in preguntas.items():
        elegido = request.form.get(f"q{qid}")
        elegido_id = int(elegido) if elegido and elegido.isdigit() else None

        elegido_texto = None

        for op in qdata["opciones"]:
            if op["id"] == elegido_id:
                elegido_texto = op["texto"]
                break

        ok = (elegido_id == qdata["correcta_id"])

        if ok:
            aciertos += 1

        detalles.append({
            "pregunta": qdata["texto"],
            "elegido_texto": elegido_texto,
            "correcta_texto": qdata["correcta_texto"],
            "acierto": ok
        })

    total = len(preguntas)

    return render_template(
        "resultado.html",
        aciertos=aciertos,
        total=total,
        detalles=detalles
    )