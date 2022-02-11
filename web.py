#10/02/2022
#Illegal_Penguins
#MilEqDB/web.py

from flask import Flask, render_template, send_file, request, redirect, session

class web:

    """Serves the web side of the database."""

    #Creating a class-wide variable that can be used for routes
    app = Flask(__name__)

    def __init__(self):

        """Initialises the application."""

        #Running the app
        self.app.run(debug=True)

    #Main landing route, this will return the index.html file
    @app.route("/")
    def index():
        return render_template('index.html')


if __name__ == "__main__":
    web()
