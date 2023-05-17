from flask import Flask, render_template # type: ignore

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("checkerboard.html",row=8,col=8,color_one='red',color_two='black')
# this is the route that will be used to display the checkerboard

@app.route('/<int:x>')
def row(x):
    return render_template("checkerboard.html",row=x,col=8,color_one='red',color_two='black')
# this route will display the checkerboard with the number of rows specified by the user

@app.route('/<int:x>/<int:y>')
def row_col(x,y):
    return render_template("checkerboard.html",row=x,col=y,color_one='red',color_two='black')
# this route will display the checkerboard with the number of rows and columns specified by the user

@app.route('/<int:x>/<int:y>/<string:one>')
def row_col_one(x,y,one):
    return render_template("checkerboard.html",row=x,col=y,color_one=one,color_two='black')
# this route will display the checkerboard with the number of rows and columns specified by the user, and the color of the first square specified by the user

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def row_col_two(x,y,one,two):
    return render_template("checkerboard.html",row=x,col=y,color_one=one,color_two=two)
# this route will display the checkerboard with the number of rows and columns specified by the user, and the color of the first and second square specified by the user

if __name__=="__main__":
    app.run(debug=True, host="localhost", port=5002)