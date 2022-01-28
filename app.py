from flask import Flask, render_template
app = Flask(__name__)
from controllers.players_controller import players_blueprint

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

app.register_blueprint(players_blueprint)