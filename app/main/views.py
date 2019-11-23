from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
import datetime

from ..models import User,Pitch,Comment
from .. import db
from .forms import UpdateProfile,PitchForm,CommentForm
# from .. import db,photos

# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = "Welcome to One Minute Perfect Pitch"

    # getting pitches by category
    pickup_pitches = Pitch.get_pitches("pickup-line")
    interview_pitches = Pitch.get_pitches("interview")
    product_pitches = Pitch.get_pitches("product")
    promotion_pitches = Pitch.get_pitches("promotion")

    return render_template('index.html',title = title,pickup = pickup_pitches,interview = interview_pitches,product = product_pitches,promotion = promotion_pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    pitches_count = Pitch.count_pitches(uname)

    if user is None:
        abort(404)

    return render_template('profile/profile.html',user = user,pitches = pitches_count)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
        
