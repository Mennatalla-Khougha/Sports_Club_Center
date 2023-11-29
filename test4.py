#!/usr/bin/python3
import os

file_name = '82da6470-5e43-4152-a8ce-a1e19d13a051.png'
directory = 'website/personal_images/'
new_path = os.path.join(directory, file_name)
print(new_path)