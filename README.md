# Parchisi Kingdoms: Royal Edition

🎮 **Parchisi Kingdoms** هو تطبيق لعبة لوحية تم تطويره باستخدام [Kivy](https://kivy.org/) و[Buildozer](https://github.com/kivy/buildozer) ويتم توليد ملف APK تلقائيًا باستخدام GitHub Actions.

---

## 📦 مميزات التطبيق

- 🎲 لعبة Parchisi متعددة اللاعبين
- 📊 نظام نقاط ولوحة متصدرين
- ☁️ تكامل مع Firebase لتخزين النقاط
- 💰 إعلانات AdMob (Banner, Interstitial, Rewarded)
- 🤖 دعم اللاعبين الآليين (AI)

---

## ⚙️ متطلبات البناء اليدوي

```bash
pip install buildozer cython
sudo apt install zip unzip openjdk-17-jdk libltdl-dev autoconf automake libtool
buildozer android debug
```

---

## 🚀 البناء التلقائي باستخدام GitHub Actions

### 📁 المسار: `.github/workflows/build_apk.yml`

عند رفع أي تغييرات إلى الفرع `main`، سيتم:

1. تثبيت Java 17 و Python 3.10
2. تحميل Android SDK و NDK
3. تثبيت Buildozer والمتطلبات
4. تنفيذ الأمر `buildozer android debug`
5. رفع ملف APK داخل قسم **Artifacts**

---

## 📥 تحميل الـ APK

بعد تنفيذ الـ Workflow، يمكنك تحميل ملف APK النهائي من:

**GitHub → Actions → آخر عملية تشغيل → Artifacts → `parchisi-kingdoms-apk.zip`**

---

## 🛡️ تنويه

لرفع التطبيق إلى متجر Google Play، يجب توقيع ملف APK باستخدام keystore خاص بك.

---

## 👨‍💻 المطور

- الاسم: *اAITNASSAR Younes
- البريد الإلكتروني: *Aitnassaryounes09@gmail.com*

---

## MIT License

Copyright (c) 2025 AITNASSAR Younes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

MIT © 2025
