#!/usr/bin/python3
import os

directory_path = "website/static/tournaments_images"

if os.path.exists(directory_path) and os.path.isdir(directory_path):
    print(f"The directory '{directory_path}' exists.")
else:
    print(f"The directory '{directory_path}' does not exist.")