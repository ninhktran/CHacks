from flask import render_template, url_for, flash, redirect
from Website import app, db
from Website.forms import RegistrationFrom, UnSubscribeForm
from Website.models import Subscriber

@app.route("/", methods=['GET','POST'])
def home():
    form = RegistrationFrom()
    if form.validate_on_submit():
        print('form valid')

        area_string, topic_string = prepare_sub_data(form)
        subscriber = Subscriber(email=form.email.data,
                                area=area_string,
                                topic=topic_string)
        db.session.add(subscriber)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in.',
              'success')
        return redirect(url_for('home'))

    else:
        print('form not valid')


    return render_template("home.html", form=form)

@app.route("/unsub", methods=['GET', 'POST'])
def unsub():
    form = UnSubscribeForm()
    if form.validate_on_submit():
        if (user := db.session.query( email=form.email.data )):
            db.session.remove(user)
        else:
            print("that shouldn't have happened")
            raise Exception
    return render_template('unsub.html', form=form)




def prepare_sub_data(form):
    area_string = ','.join([
        'everett'*form.everett.data,
        'skagit_county'*form.skagit_county.data])
    topic_string = ','.join([
        'weather'*form.weather.data,
        'sports'*form.sports.data])
    return area_string, topic_string