[app]

# معلومات التطبيق
title = Parchisi Kingdoms: Royal Edition
package.name = parchisi_kingdoms
package.domain = org.example
version = 1.0

# مسار الملفات والمصادر
source.dir = .
source.include_exts = py,png,jpg,kv,json,ttf,wav,ogg,mp3

# الأيقونة (يمكنك تغييرها لاحقًا)
icon.filename = assets/icon.png

# المتطلبات
requirements = python3,kivy,kivmob,pyrebase4

# أكواد Java المطلوبة (AdMob)
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.1.0

# صلاحيات التطبيق
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# بيانات AdMob (تعديل المعرفات حسب حسابك)
android.meta_data = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-8643407623577361~1203571307

# الإعدادات المرئية
orientation = portrait
fullscreen = 0

# إصدار Android المستهدف
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# إعدادات التوقيع APK (تجريبية أو Production)
android.release_keystore = AITNASSAR_Younes.keystore
android.release_keyalias = AITNASSAR_Younes
android.release_keystore_passwd = android
android.release_keyalias_passwd = android

# اللغة والبيئة
android.entrypoint = org.kivy.android.PythonActivity
android.allow_backup = True

# مكتبات C و Java
android.use_android_native_api = False
android.add_src = 
android.add_jars = 

# إضافات متقدمة (اختياري)
# p4a.branch = master
# android.enable_legacy_android_support = 1

# اللغة الافتراضية
fullscreen = 0
presplash.filename = assets/loading.png

[buildozer]
log_level = 2
warn_on_root = 1
