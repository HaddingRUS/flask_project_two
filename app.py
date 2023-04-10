from flask import Flask, render_template, abort, request
import json
from data import days

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
    with open('data_base_teachers.json', 'r', encoding='utf-8') as f:
        all_teachers = json.load(f)
    for teacher in all_teachers:
        if teacher['id'] == id_t:
            id_teacher = teacher
            return render_template('profile.html', teacher=id_teacher, days=days)
    abort(404)


@app.route('/request/')
def requests():
    return render_template('request.html')


@app.route('/request_done/', methods=['POST'])
def requests_done():
    if request.method == 'POST':
        goal = request.form['goal']
        time = request.form['time']
        username = request.form['username']
        phone = request.form['user_phone']
        user_data = {'goal': goal, 'time': time, 'username': username,
                     'phone': phone}
        with open('request.json', 'a', encoding='utf-8') as f:
            json.dump(user_data, f)
        return render_template('request_done.html')


@app.route('/booking/<int:id_t>/<week>/<time>')
def bookings(id_t, week, time):
    with open('data_base_teachers.json', 'r', encoding='utf-8') as f:
        all_teachers = json.load(f)
    for teacher in all_teachers:
        if teacher['id'] == id_t:
            id_teacher = teacher
            return render_template('booking.html', week=week, time=time, name=id_teacher['name'], days=days, id_t=id_t)
    abort(404)


@app.route('/booking_done/', methods=['POST'])
def bookings_done():
    if request.method == 'POST':
        username = request.form['clientName']
        user_phone = request.form['clientPhone']
        client_weekday = request.form['clientWeekday']
        client_time = request.form['clientTime']
        client_teacher = request.form['clientTeacher']
        client_order = {'username': username, 'user_phone': user_phone,
                       'clientWeekday': client_weekday, 'clientTime': client_time,
                       'clientTeacher': client_teacher}
        with open('booking.json', 'a', encoding='utf-8') as f:
            json.dump(client_order, f)
        return render_template('booking_done.html',
                               username=username, date=days[client_weekday],
                               time=client_time, phone=user_phone)
    elif request.method == 'GET':
        return 'GET запрос'


@app.errorhandler(404)
def error_404(error):
    return 'Такой страницы не существует'


if __name__ == '__main__':
    app.run()
