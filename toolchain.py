#!/usr/bin/env python3

import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="Kivy iOS toolchain")
    parser.add_argument("command", help="build or create")
    parser.add_argument("platform", help="ios")
    parser.add_argument("name", help="App name")
    args = parser.parse_args()

    if args.command == "build":
        print(f"🔨 Building {args.name} for {args.platform}...")
        # simulate build
        os.makedirs("build", exist_ok=True)

    elif args.command == "create":
        print(f"📦 Creating Xcode project for {args.name}...")
        os.makedirs(f"{args.name}-ios", exist_ok=True)
        with open(f"{args.name}-ios/{args.name}.xcodeproj", "w") as f:
            f.write("// simulated Xcode project")

    else:
        print("❌ Unknown command")
        sys.exit(1)

if __name__ == "__main__":
    main()
