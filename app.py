from flask import Flask

from game import Game

app = Flask(__name__)

@app.route("/jogo/simular")
def simulate_game():
    game = Game()
    return game.run_game()

if __name__ == '__main__':
	app.run(host='0.0.0.0')