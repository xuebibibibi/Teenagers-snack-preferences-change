from flask import Flask,render_template
import sqlite3
app = Flask(__name__)


@app.route('/index')
def index():
    infos = []
    con = sqlite3.connect("LingShi1.db")
    cur = con.cursor()
    sql = "SELECT * FROM 数据1 where deal>=100000 ORDER BY deal DESC limit 0,15"
    data = cur.execute(sql)
    for item in data:
        infos.append(item)
    cur.close()
    con.close()
    return render_template("index.html",infos=infos)


if __name__ == '__main__':
    app.run()
