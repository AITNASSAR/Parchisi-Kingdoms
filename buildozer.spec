[app]
title = Parchisi Kingdoms: Royal Edition
package.name = parchisi_kingdoms
package.domain = org.example
source.include_exts = py,png,jpg,kv,json
source.include_patterns = assets/*, *.py
requirements = python3,kivy,kivmob,pyrebase4
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.1.0
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-8643407623577361~1203571307
orientation = portrait
[buildozer]
log_level = 2
warn_on_root = 1
target = android
