[app]
title = Parchisi Kingdoms: Royal Edition
package.name = parchisi_kingdoms
package.domain = org.example
version = 1.0

source.dir = .
source.include_exts = py,png,jpg,kv,json,ttf,wav,ogg,mp3

icon.filename = assets/icon.png

requirements = python3,kivy,kivmob,pyrebase4

android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.1.0

orientation = portrait
fullscreen = 0

android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

android.release_keystore = AITNASSAR_Younes.keystore
android.release_keyalias = AITNASSAR_Younes
android.release_keystore_passwd = android
android.release_keyalias_passwd = android

presplash.filename = assets/loading.png

[buildozer]
log_level = 2
warn_on_root = 1

android.icon = assets/icon.png
