# Parchisi Kingdoms: Royal Edition

A mobile board game built with Kivy and packaged for Android using Buildozer. Includes Firebase integration and AdMob ads.

## 📱 Features

- Beautiful Kivy UI (KV Language)
- Firebase leaderboard support
- AdMob integration (Banner, Interstitial, Rewarded)
- Score tracking and saving
- AI player logic

---

## 🧰 Requirements

Install Python packages:

```bash
pip install -r requirements.txt
```

Install Buildozer (for Android build):

```bash
pip install buildozer
sudo apt install -y openjdk-8-jdk unzip zip
```

---

## 🚀 Run Locally (Desktop)

```bash
python main.py
```

---

## 📦 Build for Android

1. Make sure `buildozer.spec` is configured (already included).
2. Then run:

```bash
buildozer android debug
```

To install on connected device:

```bash
buildozer android deploy run
```

---

## ☁️ CI/CD (GitHub Actions)

This project includes a GitHub Actions workflow that builds your APK automatically on push to the `main` branch.

---

## 📄 License

MIT License © 2025
