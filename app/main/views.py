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

        return redirect(url_for('.profile',uname = user.username))

    return render_template('profile/update.html',form = form)

@main.route('/pitch/new',methods = ['GET','POST'])
@login_required
def new_pitches():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.txt.data
        category = pitch_form.carrtegory.data

        # updating pitch instance
        new_pitch = Pitch(title = title,content = pitch,category = category,user = current_user,likes = 0,dislikes = 0)

        # save pitch
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New Pitch'
    return render_template('new_pitch.html',title = title,pitch_form = pitch_form)


@main.route('/pitches/pickup_pitches')
def interview_pitches():

    pitches = Pitch.get_pitches('pickup-line')

    return render_template("pickup_line.html", pitches = pitches)

@main.route('/pitches/interview_pitches')
def interview_pitches():

    pitches = Pitch.get_pitches('interview')

    return render_template("interview_pitches.html", pitches = pitches)

@main.route('/pitches/product_pitches')
def product_pitches():

    pitches = Pitch.get_pitches('product')

    return render_template("product_pitches.html", pitches = pitches)

@main.route('/pitches/promotion_pitches')
def promotion_pitches():

    pitches = Pitch.get_pitches('promotion')

    return render_template("promotion_pitches.html", pitches = pitches)
