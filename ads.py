from kivmob import KivMob

class AdsManager:
    def __init__(self, app):
        self.ads = KivMob("ca-app-pub-8643407623577361~1203571307")
        self.ads.new_banner("ca-app-pub-8643407623577361/5290171882", top_pos=False)
        self.ads.new_banner("ca-app-pub-8643407623577361/4868368624", top_pos=True)
        self.ads.new_interstitial("ca-app-pub-8643407623577361/1203571307")
        self.ads.new_rewarded("ca-app-pub-8643407623577361/7768075693")
        self.ads.new_native("ca-app-pub-8643407623577361/2017648460")
        self.ads.request_banner()
        self.ads.request_interstitial()
        self.ads.request_rewarded()
        self.ads.request_native()

    def show_banner(self): self.ads.show_banner()
    def show_interstitial(self): self.ads.show_interstitial()
    def show_rewarded(self): self.ads.show_rewarded()
    def show_native(self): self.ads.show_native()
