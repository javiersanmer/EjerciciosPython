import sqlite3
import os

DB_PATH = "/app/data/quiz.db"

def init_db():
    os.makedirs("/app/data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Crear tabla preguntas
    cur.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL
        )
    """)

    # Crear tabla opciones
    cur.execute("""
        CREATE TABLE IF NOT EXISTS options (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER,
            texto TEXT NOT NULL,
            es_correcta INTEGER DEFAULT 0,
            FOREIGN KEY (question_id) REFERENCES questions(id)
        )
    """)

    # Limpiar datos anteriores
    cur.execute("DELETE FROM options")
    cur.execute("DELETE FROM questions")

    # =========================
    # PREGUNTAS DE PROGRAMACIÓN
    # =========================

    # 1
    cur.execute("INSERT INTO questions (texto) VALUES (?)",
                ("¿Qué es Python?",))
    q1 = cur.lastrowid

    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q1, "Un lenguaje de programación", 1))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q1, "Un sistema operativo", 0))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q1, "Un navegador web", 0))

    # 2
    cur.execute("INSERT INTO questions (texto) VALUES (?)",
                ("¿Qué es Flask?",))
    q2 = cur.lastrowid

    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q2, "Un framework web de Python", 1))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q2, "Una base de datos", 0))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q2, "Un editor de código", 0))

    # 3
    cur.execute("INSERT INTO questions (texto) VALUES (?)",
                ("¿Qué significa SQL?",))
    q3 = cur.lastrowid

    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q3, "Structured Query Language", 1))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q3, "Simple Query Logic", 0))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q3, "System Question Language", 0))

    # 4
    cur.execute("INSERT INTO questions (texto) VALUES (?)",
                ("¿Qué estructura de datos usa FIFO?",))
    q4 = cur.lastrowid

    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q4, "Cola (Queue)", 1))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q4, "Pila (Stack)", 0))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q4, "Árbol", 0))

    # 5
    cur.execute("INSERT INTO questions (texto) VALUES (?)",
                ("¿Qué hace un JOIN en SQL?",))
    q5 = cur.lastrowid

    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q5, "Combina tablas relacionadas", 1))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q5, "Elimina tablas", 0))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q5, "Ordena la base de datos", 0))

    # 6
    cur.execute("INSERT INTO questions (texto) VALUES (?)",
                ("¿Qué es una variable?",))
    q6 = cur.lastrowid

    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q6, "Un espacio de memoria para guardar datos", 1))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q6, "Un tipo de bucle", 0))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q6, "Un error del sistema", 0))

    # 7
    cur.execute("INSERT INTO questions (texto) VALUES (?)",
                ("¿Qué lenguaje se ejecuta en el navegador?",))
    q7 = cur.lastrowid

    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q7, "JavaScript", 1))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q7, "Python", 0))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q7, "C++", 0))

    # 8
    cur.execute("INSERT INTO questions (texto) VALUES (?)",
                ("¿Qué es un algoritmo?",))
    q8 = cur.lastrowid

    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q8, "Un lenguaje de programación", 0))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q8, "Un tipo de base de datos", 0))
    cur.execute("INSERT INTO options VALUES (NULL, ?, ?, ?)", (q8, "Un conjunto de pasos para resolver un problema", 1))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()