import json, os
from firebase_handler import FirebaseHandler

class ScoreManager:
    def __init__(self):
        self.player_scores = [0,0,0,0]
        self.player_names  = ["","","",""]
        self._save_path = os.path.join(os.getcwd(), "savegame.json")
        self.firebase = FirebaseHandler()

    def update_score(self, idx, pts): self.player_scores[idx] += pts
    def set_player_name(self, idx, name): self.player_names[idx] = name

    def save_game_local(self):
        with open(self._save_path,"w",encoding="utf-8") as f:
            json.dump({"names":self.player_names,"scores":self.player_scores}, f, ensure_ascii=False, indent=2)

    def load_game_local(self):
        if not os.path.exists(self._save_path): return False
        data = json.load(open(self._save_path,"r",encoding="utf-8"))
        self.player_names, self.player_scores = data["names"], data["scores"]
        return True

    def save_game_remote(self, id_token):
        for n,s in zip(self.player_names,self.player_scores):
            if n: self.firebase.save_score(n,s,id_token)

    def load_top_scores_remote(self, id_token):
        return self.firebase.get_top_scores(id_token)
