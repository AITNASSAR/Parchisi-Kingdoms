#!/usr/bin/env python3
import argparse
import os
import shutil
from cookiecutter.main import cookiecutter

def create_ios_project(app_name, bundle_id):
    template_path = os.path.join(os.path.dirname(__file__), 'cookiecutter-ios-template')

    output_dir = os.path.abspath(f"ios/kivy-ios/{app_name}-ios")
    if os.path.exists(output_dir):
        print(f"⚠️ Directory '{output_dir}' already exists. Removing it...")
        shutil.rmtree(output_dir)

    print(f"🚀 Generating iOS Xcode project for {app_name}...")
    cookiecutter(
        template_path,
        no_input=True,
        extra_context={
            'project_name': app_name,
            'bundle_id': bundle_id
        },
        output_dir=os.path.abspath('ios/kivy-ios')
    )
    print(f"✅ iOS Xcode project created at {output_dir}")

def main():
    parser = argparse.ArgumentParser(description="Toolchain manager for iOS projects.")
    subparsers = parser.add_subparsers(dest='command')

    create_parser = subparsers.add_parser('create', help='Create a new iOS Xcode project.')
    create_parser.add_argument('--name', required=True, help='App project name')
    create_parser.add_argument('--bundle-id', required=True, help='Bundle identifier (e.g., com.example.myapp)')

    args = parser.parse_args()

    if args.command == 'create':
        create_ios_project(args.name, args.bundle_id)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
