- name: Setup Android SDK
  run: |
    # ایجاد دایرکتوری‌های موردنیاز
    mkdir -p $HOME/android-sdk/cmdline-tools

    # دانلود Android Command Line Tools
    wget https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip -O sdk-tools.zip

    # اکسترکت فایل زیپ
    unzip -q sdk-tools.zip -d $HOME/android-sdk/cmdline-tools

    # جابجایی برای داشتن ساختار صحیح
    mv $HOME/android-sdk/cmdline-tools/cmdline-tools $HOME/android-sdk/cmdline-tools/latest

    # اضافه کردن مسیر به PATH برای این step
    export PATH=$HOME/android-sdk/cmdline-tools/latest/bin:$PATH

    # ثبت PATH در محیط کلی GitHub Actions برای استفاده در مراحل بعدی
    echo "PATH=$HOME/android-sdk/cmdline-tools/latest/bin:$PATH" >> $GITHUB_ENV

    # تایید خودکار همه‌ی لایسنس‌های SDK
    yes | sdkmanager --licenses

    # نصب ابزارهای لازم برای build
    sdkmanager --sdk_root=$HOME/android-sdk \
      "platform-tools" \
      "platforms;android-31" \
      "build-tools;31.0.0" \
      "ndk;25.1.8937393"

