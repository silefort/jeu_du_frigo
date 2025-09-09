class FridgeGame:
    def __init__(self, max_attempts=20):
        self.max_attempts = max_attempts
        self.current_temp = 15  # Température initiale
        self.history = []  # Liste des coups : [{"input": X, "temp": Y}, ...]

    def play_turn(self, input_value):
        t = len(self.history)

        if t == 0:
            # Premier tour, température fixée à 15
            self.current_temp = 15
        else:
            prev_temp = self.current_temp
            temp_t_minus_5 = self.history[t - 5]["temp"] if t >= 5 else 0
            self.current_temp = prev_temp + ((input_value / 10) + 2 - temp_t_minus_5) / 3

        # Ajoute à l’historique
        self.history.append({"input": input_value, "temp": round(self.current_temp, 2)})

    def is_over(self):
        return len(self.history) >= self.max_attempts

    def is_won(self):
        # Victoire si à la fin des 20 tours la température est entre 0 et 4 inclus
        return (
            len(self.history) == self.max_attempts
            and 0 <= self.current_temp <= 4
        )

    # 🔹 Sérialiser pour la session Flask
    def to_dict(self):
        return {
            "max_attempts": self.max_attempts,
            "current_temp": self.current_temp,
            "history": self.history,
        }

    # 🔹 Recréer un objet à partir d’un dict
    @classmethod
    def from_dict(cls, data):
        game = cls(max_attempts=data["max_attempts"])
        game.current_temp = data["current_temp"]
        game.history = data["history"]
        return game
