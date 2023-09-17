from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('routes', __name__)

@bp.route('/')
@login_required
def profile():
    return render_template('profile.html')

@bp.route('/submit', methods=('GET', 'POST'))
@login_required
def submit():
    if request.method == 'POST':
        time  = request.form['time']
        
        db = get_db()
        db.execute(
            'INSERT INTO post (time, author_id)'
            ' VALUES (?, ?)',
            (time, g.user['id'])
        )
        db.commit()
        return redirect(url_for('routes.profile'))
    
    return render_template('profile.html')