
# Ù…Ø¹Ù„ÙˆÙ…Ø§Øª Ø§Ù„ØªØ·Ø¨ÙŠÙ‚
title = Parchisi Kingdoms: Royal Edition
package.name = parchisi_kingdoms
package.domain = org.example
version = 1.0

# Ù…Ø³Ø§Ø± Ø§Ù„Ù…ØµØ§Ø¯Ø±
source.dir = .
source.include_exts = py,png,jpg,kv,json,ttf,wav,ogg,mp3

# Ø£ÙŠÙ‚ÙˆÙ†Ø© Ø§Ù„ØªØ·Ø¨ÙŠÙ‚ (ØªØ£ÙƒØ¯ Ù…Ù† ÙˆØ¬ÙˆØ¯Ù‡Ø§ Ø£Ùˆ Ø¹Ù„Ù‘Ù‚ Ø§Ù„Ø³Ø·Ø±)
icon.filename = assets/icon.png

# Ø§Ù„Ù…ØªØ·Ù„Ø¨Ø§Øª
requirements = python3,kivy,kivmob,pyrebase4

# ØµÙ„Ø§Ø­ÙŠØ§Øª Ø§Ù„ÙˆØµÙˆÙ„
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# AdMob
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-8643407623577361~1203571307
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.1.0

# Ø¥Ø¹Ø¯Ø§Ø¯Ø§Øª Ø§Ù„Ø¹Ø±Ø¶
orientation = portrait
fullscreen = 0

# Ø¥ØµØ¯Ø§Ø± Android
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# ØªÙˆÙ‚ÙŠØ¹ APK
android.release_keystore = AITNASSAR_Younes.keystore
android.release_keyalias = AITNASSAR_Younes
android.release_keystore_passwd = android
android.release_keyalias_passwd = android

# Ø£Ø®Ø±Ù‰
android.entrypoint = org.kivy.android.PythonActivity
android.allow_backup = True
presplash.filename = assets/loading.png

[buildozer]
log_level = 2
warn_on_root = 1

android.icon = assets/icon.png
