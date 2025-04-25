from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from ads import AdsManager
from firebase_handler import FirebaseHandler
from score_manager import ScoreManager

class MenuScreen(Screen): pass
class GameScreen(Screen): pass

class LeaderboardScreen(Screen):
    def on_enter(self):
        id_token = App.get_running_app().user_token
        scores = FirebaseHandler().get_top_scores(id_token)
        grid = self.ids.scores_grid
        grid.clear_widgets()
        from kivy.uix.label import Label
        for e in scores:
            grid.add_widget(Label(text=f"{e['player']}: {e['score']}"))

class ParchisiApp(App):
    def build(self):
        self.user_token = None
        self.ads = AdsManager(self)
        self.ads.show_banner()
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(GameScreen(name="game"))
        sm.add_widget(LeaderboardScreen(name="leaderboard"))
        return sm

    def on_pause(self): return True
    def on_resume(self): self.ads.request_interstitial()

if __name__ == '__main__':
    ParchisiApp().run()
