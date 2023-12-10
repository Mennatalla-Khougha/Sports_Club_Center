#!/usr/bin/python3
""" Starts a Flash Web Application """
from os import getenv
import uuid
from models import storage
from models.player import Player
from models.sport import Sport
from models.tournament import Tournament
from models.record import Record
from flask import Flask, render_template, abort, request, redirect, url_for, flash
from flask_security import login_required, current_user, login_user, LoginForm
from datetime import datetime
from website.user_table import user_datastore, app, db, Role
from flask_security.utils import hash_password, verify_password
from datetime import datetime
from console import ConsoleCommand
# from website.web_flasks.form import ExtendedLoginForm

# app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/', strict_slashes=False)
def home_page():
    """ routes the home page """
    return render_template('index.html')

@app.route('/players', strict_slashes=False)
def players():
    """ routes the players page """
    sports = storage.all(Sport).values()
    sports = sorted(sports, key=lambda k: k.name)

    players = storage.all(Player).values()
    players = sorted(players, key=lambda k: (k.first_name, k.last_name))
    ages = [player.age(datetime.now()) for player in players]

    return render_template('players.html',
                           sports=sports, players=players, ages=ages, size=len(ages))

@app.route('/players/<player_id>', strict_slashes=False)
def player_page(player_id):
    """ routes the player_page page """
    player = storage.get(Player, player_id)
    if not player:
        abort(404)
    stats = player.stats()
    records = sorted(player.records, key=lambda k: (-k.score, k.matches_played))
    age = player.age(datetime.now())
    return render_template('player_page.html',
                           player=player,
                           stats=stats,
                           records=records,
                           age=age)


@app.route('/sports', strict_slashes=False)
def sports():
    """ routes the sports page """
    return render_template('sports.html')


@app.route('/sports/karate', strict_slashes=False)
def karate():
    """ routes the karate page """
    return render_template('karate.html')


@app.route('/sports/squash', strict_slashes=False)
def squash():
    """ routes the squash page """
    return render_template('squash.html')

@app.route('/sports/track_field', strict_slashes=False)
def track_field():
    """ routes the track_field page """
    return render_template('track_field.html')

@app.route('/schedules', strict_slashes=False)
def schedules():
    """ routes the schedules page """
    return render_template('schedules.html')

# @app.route('/register', methods=['POST','GET'],strict_slashes=False)
# def register():
#     """routes the register page"""
#     if request.method == 'POST':
#         user_role = Role.query.filter_by(name='user').first()
#         roles = []
#         if user_role:
#             roles.append(user_role)
#         if current_user.is_authenticated and current_user.has_role('admin'):
#             role_name = request.form.get('roles')
#             role = Role.query.filter_by(name=role_name).first()
#             if role:
#                 roles.append(role)
#         user_datastore.create_user(
#             email=request.form.get('email'),
#             password=hash_password(request.form.get('password')),
#             confirmed_at=datetime.utcnow(),
#             roles=roles
#         )
#         db.session.commit()
        
#         return redirect(url_for('profile'))

#     return render_template('register.html')

@app.route('/log_in',methods=['POST','GET'], strict_slashes=False)
def login():
    """Handle login and redirect to profile page"""
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = user_datastore.find_user(email=email)
        if user and verify_password(password, user.password):
            login_user(user)
            return redirect(url_for('profile'))
        else:
            flash('Invalid email or password')
    return render_template('login.html', form=form)
        

@app.route('/profile', strict_slashes=False)
def profile():
    """routes the profile page"""
    console_commands = ['create', 'show', 'destroy', 'update', 'all', 'count', 'append', 'help']  # Add all your console commands here
    return render_template('profile.html', console_commands=console_commands)

@app.route('/admin/create', methods=['POST', 'GET'], strict_slashes=False)
def admin_create():
    classes = {
        'Player': ['first_name', 'last_name', 'gender', 'birth_day', 'weight', 'height', 'address', 'phone_number'],
        'Tournament': ['name', 'date', 'age_range', 'description', 'win_value'],
        'Sport': ['name']
        }
    if request.method == 'POST':
        class_name = request.form.get('class_name')
        attributes = request.form.get('attributes')
        console = ConsoleCommand()
        console.do_create(f"{class_name} {attributes}")
        return render_template('create.html', classes=classes)
    return render_template('create.html')

@app.route('/admin/show', methods=['POST', 'GET'])
def admin_show():
    if request.method == 'POST':
        class_name = request.form.get('class_name')
        attributes = request.form.get('attributes')
        console = ConsoleCommand()
        console.do_create(f"{class_name} {attributes}")
        return render_template('create.html', message="Instance created successfully")
    return render_template('create.html')

@app.route('/admin/destroy', methods=['POST', 'GET'])
def admin_destroy():
    if request.method == 'POST':
        class_name = request.form.get('class_name')
        attributes = request.form.get('attributes')
        console = ConsoleCommand()
        console.do_create(f"{class_name} {attributes}")
        return render_template('create.html', message="Instance created successfully")
    return render_template('create.html')

@app.route('/admin/update', methods=['POST', 'GET'])
def admin_update():
    if request.method == 'POST':
        class_name = request.form.get('class_name')
        attributes = request.form.get('attributes')
        console = ConsoleCommand()
        console.do_create(f"{class_name} {attributes}")
        return render_template('create.html', message="Instance created successfully")
    return render_template('create.html')

@app.route('/admin/all', methods=['POST', 'GET'])
def admin_all():
    if request.method == 'POST':
        class_name = request.form.get('class_name')
        attributes = request.form.get('attributes')
        console = ConsoleCommand()
        console.do_create(f"{class_name} {attributes}")
        return render_template('create.html', message="Instance created successfully")
    return render_template('create.html')

@app.route('/admin/count', methods=['POST', 'GET'])
def admin_count():
    if request.method == 'POST':
        class_name = request.form.get('class_name')
        attributes = request.form.get('attributes')
        console = ConsoleCommand()
        console.do_create(f"{class_name} {attributes}")
        return render_template('create.html', message="Instance created successfully")
    return render_template('create.html')

@app.route('/admin/append', methods=['POST', 'GET'])
def admin_append():
    if request.method == 'POST':
        class_name = request.form.get('class_name')
        attributes = request.form.get('attributes')
        console = ConsoleCommand()
        console.do_create(f"{class_name} {attributes}")
        return render_template('create.html', message="Instance created successfully")
    return render_template('create.html')

@app.route('/admin/help', methods=['POST', 'GET'])
def admin_help():
    if request.method == 'POST':
        classes = {
            'Player': ['first_name', 'last_name', 'gender', 'birth_day', 'weight', 'height', 'address', 'phone_number'],
            'Tournament': ['name', 'date', 'age_range', 'description', 'win_value'],
            'Sport': ['name']
            }
        # class_name = request.form.get('class_name')
        # attributes = request.form.get('attributes')
        # console = ConsoleCommand()
        # console.do_create(f"{class_name} {attributes}")
        return render_template('create.html', classes=classes)
    return render_template('create.html')

@app.route('/tournaments', strict_slashes=False)
def tournaments():
    """ routes the tournaments page """
    sports = storage.all(Sport).values()
    sports = sorted(sports, key=lambda k: k.name)
    return render_template('tournaments.html', sports=sports)


@app.route('/tournaments/<tournament_id>', strict_slashes=False)
def tournament_page(tournament_id):
    """ routes the tournament_page page """
    tournament = storage.get(Tournament, tournament_id)
    if not tournament:
        abort(404)
    date = datetime.strptime(tournament.date, '%Y-%m-%d %H:%M')
    held = date < datetime.now()
    records = sorted(tournament.records, key=lambda k: (-k.score, k.matches_played))
    return render_template('tournament_page.html',
                           tournament=tournament,
                           records=records,
                           held=held)

if __name__ == "__main__":
    """ Main Function """
    host = getenv('API_HOST', '0.0.0.0')
    port = getenv('API_PORT', 5000)
    app.run(host=host, port=port)