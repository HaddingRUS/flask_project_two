from flask import Flask, render_template, abort
import json

app = Flask(__name__)
app.config.update(DEBUG=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/all')
def teachers():
    return render_template('all.html')


@app.route('/goals/<goal>')
def teach_goals(goal):
    return render_template('goal.html', goal=goal)


@app.route('/profiles/<int:id_t>')
def teach_profiles(id_t):
    id_teacher = {}
    with open('data_base_teachers.json', 'r', encoding='utf-8') as f:
        all_teachers = json.load(f)
    for teacher in all_teachers:
        if teacher['id'] == id_t:
            id_teacher = teacher
            return render_template('profile.html', teacher=id_teacher)
    abort(404)


@app.route('/request/')
def requests():
    return render_template('request.html')


@app.route('/request_done')
def requests_done():
    return render_template('request_done.html')


@app.route('/booking/<id_t>/<week>/<time>')
def bookings(id_t, week, time):
    return render_template('booking.html')


@app.route('/booking_done')
def bookings_done():
    return render_template('booking_done.html')


@app.errorhandler(404)
def error_404(error):
    return 'Такой страницы не существует'


if __name__ == '__main__':
    app.run()
