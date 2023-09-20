from flask import Flask, render_template, request

app = Flask(__name__)

class Concursos:
    def __init__(self, app):
        self.app = app
        self.register_routes()

    def register_routes(self):

        @self.app.route('/')
        def index():
            return render_template("index.html")

        @self.app.route('/cefet')
        def cefet():
            return render_template("cefet.html")

        @self.app.route('/pedro2')
        def pedro2():
            return render_template("pedro2.html")

        @self.app.route('/ifrj')
        def ifrj():
            return render_template("ifrj.html")

        @self.app.route('/fiocruz')
        def fiocruz():
            return render_template("fiocruz.html")

        @self.app.route('/ufrj')
        def ufrj():
            return render_template("ufrj.html")

        @self.app.route('/cmrj')
        def cmrj():
            return render_template("cmrj.html")

        @self.app.route('/cbnb')
        def cbnb():
            return render_template("cbnb.html")

        @self.app.route('/naval')
        def naval():
            return render_template("naval.html")
        

concursos = Concursos(app)

if __name__ == '__main__':
    app.run(debug=True)
