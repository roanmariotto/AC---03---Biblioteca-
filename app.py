from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from validacoes import validar_titulo, validar_categoria

app = Flask(__name__)
app.secret_key = "biblioteca123"

# ---- Banco de Dados ----


def conectar_banco():
    conn = sqlite3.connect("biblioteca.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS livros (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        categoria TEXT NOT NULL,
                        disponivel INTEGER DEFAULT 1
                    )''')
    return conn

# ---- Rotas ----

@app.route("/")
def index():
    return redirect(url_for("listar"))

@app.route("/listar")
def listar():
    conn = conectar_banco()
    cursor = conn.execute("SELECT * FROM livros ORDER BY titulo")
    livros = cursor.fetchall()
    conn.close()
    return render_template("listar.html", livros=livros)

@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        autor = request.form["autor"].strip()
        categoria = request.form["categoria"].strip()

        erros = []
        if not validar_titulo(titulo):
            erros.append("Título é obrigatório!")
        if not validar_categoria(categoria):
            erros.append("Categoria inválida!")

        if erros:
            for e in erros:
                flash(e, "error")
            return redirect(url_for("editar", id=id))

        conn.execute("UPDATE livros SET titulo = ?, autor = ?, categoria = ?, disponive l= ? WHERE id = ?",
                     (titulo.title(), autor.title(), categoria.title(), disponivel, id))
        conn.commit()
        conn.close()

        flash("Livro atualizado com sucesso!", "success")
        return redirect(url_for("listar"))

    conn.close()
    return render_template("editar.html", livro=livro)

@app.route("/deletar/<int:id>", methods=["POST"])
def deletar(id):
    conn = conectar_banco()
    conn.execute("DELETE FROM livros WHERE id=?", (id,))
    conn.commit()
    conn.close()
    flash("Livro excluído com sucesso!", "success")
    return redirect(url_for("listar"))

if __name__ == "main": 
    app.run(debug = True) 

