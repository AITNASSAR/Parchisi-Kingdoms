#!/usr/bin/env bash
set -e

echo "1️⃣ تحديث APT وتثبيت autotools و libtool..."
sudo apt-get update
sudo apt-get install -y autoconf automake libtool libltdl-dev

echo "2️⃣ تشغيل autoupdate لتحديث macros في configure.ac…"
if [ -f configure.ac ]; then
  autoupdate
else
  echo "⚠️ لا يوجد ملف configure.ac، سيتم التخطي"
fi

echo "3️⃣ مسح ذاكرة Buildozer المؤقتة…"
rm -rf .buildozer

echo "4️⃣ تنظيف البناء السابق…"
buildozer android clean || true

echo "✅ انتهى الإعداد. شغل الآن:"
echo "   buildozer --verbose android debug"
