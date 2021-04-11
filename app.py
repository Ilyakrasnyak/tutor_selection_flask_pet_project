from flask import Flask, render_template, redirect, request, url_for

from core.teacher import Teacher
from core.booking_form import BookingForm
from core.request_form import RequestForm
from core.data_handler import DataHandler

app = Flask(__name__)
app.secret_key = 'my-super-secret-phrase-I-dont-tell-this-to-nobody'


@app.route('/')
def render_main():
    return render_template('index.html')


@app.route('/all')
def render_all():
    return render_template('all.html')


@app.route('/goals/<goal>')
def render_goal(goal):
    return render_template('goal.html ')


@app.route('/profiles/<int:teacher_id>/')
def render_profile(teacher_id):
    teacher = Teacher(teacher_id)
    return render_template('profile.html', teacher=teacher.data, free_time=teacher.free_time)


@app.route('/request/')
def render_request():
    form = RequestForm()
    if request.method == "POST" and form.validate_on_submit():
        return redirect(url_for('render_request_done'))
    return render_template('request.html', form=form)


@app.route('/request_done/', methods=["GET", "POST"])
def render_request_done():
    form = RequestForm()
    form_data = form.data
    db = DataHandler('request.json')
    db.append(form_data)
    return render_template('request_done.html', form_data=form_data)


@app.route('/booking/<int:teacher_id>/<weekday>/<time>/', methods=["GET", "POST"])
def render_booking(teacher_id, weekday, time):
    form = BookingForm(teacher_id=teacher_id, weekday=weekday, time=time)
    teacher = Teacher(teacher_id)
    if request.method == "POST" and form.validate_on_submit():
        return redirect(url_for('render_booking_done'))
    return render_template('booking.html', form=form, teacher=teacher)


@app.route('/booking_done/', methods=["GET", "POST"])
def render_booking_done():
    form = BookingForm()
    form_data = form.data
    db = DataHandler('booking.json')
    db.append(form_data)
    return render_template('booking_done.html', form_data=form_data)


if __name__ == '__main__':
    app.run()
