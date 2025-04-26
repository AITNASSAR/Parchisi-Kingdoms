#!/usr/bin/env python3
import os
import sys
import argparse
from os.path import join, exists
import sh
from sh import git, python3, pip3

# Paths
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
BUILD_DIR = join(ROOT_DIR, "build")
DIST_DIR = join(ROOT_DIR, "dist")
APP_DIR = join(ROOT_DIR, "apps")

# Create necessary directories
os.makedirs(BUILD_DIR, exist_ok=True)
os.makedirs(DIST_DIR, exist_ok=True)
os.makedirs(APP_DIR, exist_ok=True)

# Simple logging
def info(msg):
    print(f"[INFO] {msg}")

def error(msg):
    print(f"[ERROR] {msg}")
    sys.exit(1)

def run_cmd(cmd, cwd=None):
    info(f"Running command: {cmd}")
    os.system(cmd)

def build(package):
    """Build a package."""
    info(f"Building {package}")
    run_cmd(f"python3 -m toolchain build {package}")

def create(platform, app_name):
    """Create an Xcode project for a Kivy app."""
    if platform != "ios":
        error("Only 'ios' platform is supported.")

    app_path = join(APP_DIR, f"{app_name}-ios")
    if not exists(app_path):
        info(f"Creating new app directory: {app_path}")
        run_cmd(f"cookiecutter templates/app --no-input app_name={app_name}")

    project_path = join(app_path, f"{app_name}.xcodeproj")
    if not exists(project_path):
        info(f"Generating Xcode project for {app_name}")
        run_cmd(f"python3 -m toolchain create {app_name}")

    if exists(project_path):
        info(f"✅ Xcode project created at {project_path}")
    else:
        error("Failed to create Xcode project.")

def clean():
    """Clean build artifacts."""
    info("Cleaning build and dist directories")
    run_cmd(f"rm -rf {BUILD_DIR}/* {DIST_DIR}/*")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["build", "create", "clean"])
    parser.add_argument("args", nargs="*")
    args = parser.parse_args()

    if args.command == "build":
        if not args.args:
            error("Please specify at least one package to build.")
        for package in args.args:
            build(package)

    elif args.command == "create":
        if len(args.args) != 2:
            error("Usage: toolchain.py create ios appname")
        platform, app_name = args.args
        create(platform,
