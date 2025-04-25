[app]
title = Parchisi Kingdoms: Royal Edition
package.name = parchisi_kingdoms
package.domain = org.SKAW
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 1.0
requirements = python3,kivy,kivmob,pyrebase4
orientation = portrait
fullscreen = 0

android.permissions = INTERNET, ACCESS_NETWORK_STATE

android.gradle_dependencies = com.google.android.gms:play-services-ads:22.1.0

android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-8643407623577361~1203571307

android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
