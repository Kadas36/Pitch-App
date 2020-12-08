from flask import render_template, url_for, flash, redirect, request, abort
from . import main
from flask_login import login_required, current_user
from .forms import PitchForm, CommentForm
from ..models import User, Category, Pitch, Comment
from ..import db

@main.route('/')
def index():
   return render_template('index.html')

@main.route('/pitch/new', methods=["GET", "POST"])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(title = form.title.data, body = form.body.data)
        db.session.add(pitch)
        db.session.commit()
        flash('Your pitch has been created')
        return redirect(url_for('main.new_pitch'))
    title = "Create a Pitch"
    pitches = Pitch.query.all()

    return render_template('pitch.html', title=title, form=form, pitch_list=pitches)

@main.route('/comment/new', methods = ["GET", "POST"])
@login_required
def new_comment():
    Commentform = CommentForm()
    if Commentform.validate_on_submit():
        comment = Comment(comment=Commentform.comment.data)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been posted')
        return redirect(url_for('main.new_comment'))
    title = "Comment"    
    comments = Comment.query.all()
    return render_template('form.html', title=title, form=Commentform, comment_list=comments)