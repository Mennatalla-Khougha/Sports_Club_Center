#!/usr/bin/python3
from flask_security.utils import hash_password
from website.user_table import user_datastore, app, db

def create_admin():
    """create the first admin"""
    with app.app_context():
        print("Creating admin user...")
        user = user_datastore.create_user(
            email="admin@admin.com",
            username='admin',
            password=hash_password('admin')
            # roles=['admin']
        )
        db.session.commit()
        print(f"Admin user created: {user.username}")

if __name__ == "__main__":
    create_admin()