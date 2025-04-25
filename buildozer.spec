[app]
# Application information
title = Parchisi Kingdoms: Royal Edition
package.name = parchisi_kingdoms
package.domain = org.example
version = 1.0

# Source configuration
source.dir = .
source.include_exts = py,png,jpg,kv,json,ttf,wav,ogg,mp3

# Application icon (ensure it exists or comment out the line)
icon.filename = assets/icon.png

# Requirements
requirements = python3,kivy,kivmob,pyrebase4

# Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# AdMob settings
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-8643407623577361~1203571307
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.1.0

# Display settings
orientation = portrait
fullscreen = 0

# Android settings
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# APK signing
android.release_keystore = AITNASSAR_Younes.keystore
android.release_keyalias = AITNASSAR_Younes
android.release_keystore_passwd = android
android.release_keyalias_passwd = android

# Other settings
android.entrypoint = org.kivy.android.PythonActivity
android.allow_backup = True
presplash.filename = assets/loading.png

[buildozer]
log_level = 2
warn_on_root = 1

android.icon = assets/icon.png
