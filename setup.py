- name: Setup Android SDK
  run: |
    # دانلود Android Command Line Tools
    mkdir -p $HOME/android-sdk/cmdline-tools
    wget https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip -O sdk-tools.zip
    unzip -q sdk-tools.zip -d $HOME/android-sdk/cmdline-tools
    mv $HOME/android-sdk/cmdline-tools/cmdline-tools $HOME/android-sdk/cmdline-tools/latest

    # اضافه کردن PATH برای cmdline-tools
    echo "PATH=$HOME/android-sdk/cmdline-tools/latest/bin:$PATH" >> $GITHUB_ENV
    export PATH=$HOME/android-sdk/cmdline-tools/latest/bin:$PATH

    # تایید خودکار لایسنس‌های گوگل
    yes | sdkmanager --licenses

    # نصب platform-tools, build-tools و ndk موردنیاز
    sdkmanager --sdk_root=$HOME/android-sdk \
      "platform-tools" \
      "platforms;android-31" \
      "build-tools;31.0.0" \
      "ndk;25.1.8937393"

- name: Link SDK into Buildozer Path
  run: |
    mkdir -p ~/.buildozer/android/platform
    ln -sfn $HOME/android-sdk ~/.buildozer/android/platform/android-sdk
