
from flask_app.controllers import burgers # type: ignore

from flask_app import app # type: ignore

if __name__=="__main__":
    app.run(debug=True, port=5009)