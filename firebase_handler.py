from firebase_config import database, auth

class FirebaseHandler:
    def save_score(self, player_name, score, id_token):
        data = {"player": player_name, "score": score}
        return database.child("scores").push(data, id_token)

    def get_top_scores(self, id_token):
        all_scores = database.child("scores").get(id_token).val() or {}
        items = [{"player": v["player"], "score": v["score"]} for v in all_scores.values()]
        return sorted(items, key=lambda x: x["score"], reverse=True)
