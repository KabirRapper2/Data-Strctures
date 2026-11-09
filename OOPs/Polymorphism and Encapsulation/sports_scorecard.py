class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        # Fixed: Changed self.__runs to self.__score
        print(f"Cricket - Player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} smashes a six!")

    def get_score(self):
        return self.__score
    
    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be negative.")


class Football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        # Fixed: Changed "Cricket" to "Football" and self.__runs to self.__score
        print(f"Football - Player: {self.__player}, Score: {self.__score}")

    def play(self):
        # Fixed: Changed cricket terminology to football terminology
        print(f"{self.__player} scores a brilliant goal!")

    def get_score(self):
        return self.__score
    
    def set_score(self, new_score):
        if new_score >= 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            # Fixed: Typo in "negative"
            print("Score cannot be negative.")


# --- Execution Simulation ---

cricket = Cricket("Rohit", 265)
football = Football("Arjun", 1)

print("=== Sports Scoreboard ===\n")
for sport in (cricket, football):
    sport.info()
    sport.play()
    print()

print("--- Direct change attempt ---")
cricket.__score = 999
print(f"get_score() still shows: {cricket.get_score()}") 

print("\n--- Updating Scores ---")
cricket.set_score(347)
football.set_score(2)