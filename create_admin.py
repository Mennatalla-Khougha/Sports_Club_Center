from flask_security.utils import hash_password

def create_admin():
    """create the first admin"""
    with app.app_context():
        admin_role = Role.query.filter_by(name='admin').first()
        if admin_role:
            user_datastore.create_user(
                email='menmen_1998@yahoo.com',
                password=hash_password('admin'),
                roles=[admin_role]
            )
            db.session.commit()