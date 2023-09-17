from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('routes', __name__)

@bp.route('/', methods=['GET', 'POST'])
@login_required
def profile():
    db = get_db()
    history = db.execute(
        'SELECT h.id, stime, author_id, username'
        ' FROM history h JOIN user u ON h.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    return render_template('profile.html', history = history)

@bp.route('/submit', methods=['POST'])
@login_required
def submit():
    stime = request.form['stime']
    print(stime)

    print('hi')
        
    db = get_db()
    db.execute(
        'INSERT INTO history (stime, author_id)'
        ' VALUES (?, ?)',
        (stime, g.user['id'])
    )
    db.commit()

    return redirect(url_for('routes.profile'))