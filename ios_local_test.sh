#!/bin/bash

set -e

echo "🔧 تهيئة البيئة الافتراضية..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install cython sh pbxproj cookiecutter

echo "📥 نسخ kivy-ios..."
git clone https://github.com/kivy/kivy-ios.git ios/kivy-ios
cd ios/kivy-ios

echo "🛠️ بناء toolchain..."
./toolchain.py build python3 kivy

echo "📦 إنشاء مشروع Xcode..."
./toolchain.py create ios myapp

echo "🔍 التحقق من myapp.xcodeproj..."
if [ ! -d "myapp-ios/myapp.xcodeproj" ]; then
    echo "❌ خطأ: لم يتم إنشاء Xcode project"
    exit 1
fi

echo "✅ تم التحقق بنجاح! يمكنك الآن الدفع إلى GitHub 🚀"
