from flask import Flask, request, session, render_template, redirect, url_for
from game import FridgeGame

app = Flask(__name__)
app.secret_key = "change_me"

def get_game():
    if "game" not in session:
        session["game"] = FridgeGame().to_dict()
    return FridgeGame.from_dict(session["game"])

def save_game(game):
    session["game"] = game.to_dict()

@app.route("/", methods=["GET", "POST"])
def index():
    game = get_game()
    message = None

    if request.method == "POST" and not game.is_over():
        try:
            input_value = int(request.form["input_value"])
        except ValueError:
            input_value = 0
        game.play_turn(input_value)
        save_game(game)

        if game.is_over():
            if game.is_won():
                message = f"Bravo, vous avez gagné ! Température finale : {game.current_temp}°C (entre 0 et 4)"
            else:
                message = f"Perdu... Température finale : {game.current_temp}°C"

    return render_template(
        "index.html",
        temp=game.current_temp,
        attempts_left=game.max_attempts - len(game.history),
        max_attempts=game.max_attempts,
        input_value=100,
        message=message,
        history=game.history  # ➝ on envoie l’historique au template
    )

@app.route("/reset")
def reset():
    session.pop("game", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
