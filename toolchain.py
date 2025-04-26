#!/usr/bin/env python3

import os
import shutil
import argparse
from cookiecutter.main import cookiecutter

# -------- CLI ARGUMENTS --------
parser = argparse.ArgumentParser(description="🛠️ iOS Toolchain using Cookiecutter")
parser.add_argument("--name", required=True, help="📱 App name (used as folder name)")
parser.add_argument("--bundle-id", required=False, help="📦 App bundle identifier")
parser.add_argument("--template", required=True, help="📁 Path or URL to cookiecutter template")

args = parser.parse_args()

# -------- VALIDATION --------
output_dir = args.name

# احذف المجلد إذا كان موجودًا لتجنب الخطأ
if os.path.exists(output_dir):
    print(f"⚠️ المجلد '{output_dir}' موجود مسبقًا — سيتم حذفه لتجنب الخطأ")
    shutil.rmtree(output_dir)

# -------- COOKIECUTTER EXECUTION --------
extra_context = {"project_name": args.name}
if args.bundle_id:
    extra_context["bundle_id"] = args.bundle_id

print(f"🚀 إنشاء مشروع iOS: '{args.name}' باستخدام القالب '{args.template}'...")
cookiecutter(
    template=args.template,
    output_dir=".",
    no_input=True,
    extra_context=extra_context
)

print("✅ تم إنشاء مشروع iOS بنجاح.")
