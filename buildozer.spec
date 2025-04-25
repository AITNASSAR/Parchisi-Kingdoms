[app]
# عنوان وحزمة التطبيق
title               = Parchisi Kingdoms: Royal Edition
package.name        = parchisi_kingdoms
package.domain      = org.example

# مجلّد المصدر والإصدار
source.dir          = .
source.include_exts = py,png,jpg,kv,json
version             = 1.0

# المتطلبات
requirements        = python3,kivy,kivmob,pyrebase4

# إعدادات Android
orientation         = portrait
fullscreen          = 0
android.permissions         = INTERNET, ACCESS_NETWORK_STATE
android.gradle_dependencies = com.google.android.gms:play-services-ads:22.1.0
android.meta_data           = com.google.android.gms.ads.APPLICATION_ID=ca-app-pub-8643407623577361~1203571307

# استهداف API و NDK
android.api                 = 31
android.minapi              = 21
android.ndk                  = 25b
android.accept_sdk_license  = True

[buildozer]
log_level    = 2
warn_on_root = 1
