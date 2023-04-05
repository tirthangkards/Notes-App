from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Notes, Feedback
import json

views=Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/notes', methods=['GET', 'POST'])
@login_required
def note():

    if request.method=='POST':
        note=request.form.get('note')

        if len(note) < 2:
            flash('Note is too short', category='error')
        else:
            new_note=Notes(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')
    return render_template('notes.html', user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note=json.loads(request.data)
    noteId=note['noteId']
    note=Notes.query.get(noteId)
    
    if note:
        if note.user_id==current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/feedback', methods=['GET', 'POST'])
def feedback():

    if request.method=='POST':
        feedback=request.form.get('feedback')

        if len(feedback) < 2:
            flash('Note is too short', category='error')
        else:
            new_feedback=Feedback(feedback_data=feedback, user_id=current_user.id)
            db.session.add(new_feedback)
            db.session.commit()
            flash('Feedback Submited. Thankyou for your response', category='success')
    return render_template('feedback.html', user=current_user)