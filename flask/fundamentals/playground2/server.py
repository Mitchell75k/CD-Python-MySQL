from flask import Flask , render_template # type: ignore
app = Flask(__name__)

@app.route('/play')
def lvl_1():
    return render_template("index.html",num=3,color="blue")


@app.route('/play/<int:num>')
def lvl_2(num):
    return render_template("index.html",num=num,color="blue")


@app.route('/play/<int:num>/<string:color>')
def lvl_3(num,color):
    return render_template("index.html", num=num, color=color)


if __name__=="__main__":   # IMPORTANT! This ensures this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8001)