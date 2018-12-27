import dataking
from flask import Flask, url_for, redirect, jsonify, request, render_template
app = Flask(__name__)
from forms import *
from werkzeug.utils import secure_filename
import time

imgdir='static/imgdir'
qrdir='static/qrdir'

data = dataking.dataking(imgdir=imgdir, qrdir=qrdir)

data.load_data()
app.config['SECRET_KEY'] = 'any secret string'



@app.route('/')
def index():
    return 'Sup Nerds.  <a href="/list">List</a>'


@app.route('/list')
def list_all():
    item_list = data.get_all_item_data()
    # print(item_list)
    return render_template('list.j2', item_list=item_list)


@app.route('/<key>')
def item_detail(key):
    key = key[:8]
    # url_for_item(key)
    if data.exists(key):
        item_values = data.get_item(key)
        return render_template('item.j2', item_values=item_values)
    else:
        return 'Item Doesnt Exist'


@app.route('/add_item', methods=('GET', 'POST'))
def add_item():
    form = Add_Item()
    if form.validate_on_submit():
        filename = secure_filename(form.image.data.filename)
        form.image.data.save(imgdir + filename)
        return "woo"
    return render_template('add_item.j2', form=form)

@app.route('/get_server_time')
def get_server_time():
    print('called')
    localtime   = time.localtime()
    timeString  = time.strftime("%H:%M:%S", localtime)
    return jsonify(time=timeString)

@app.context_processor
def ultility_processor():
    def url_for_item(key):
        if key:
            key = key + "-"+data.get_item_name(key)
            # print(url_for('item_detail', key=key))
            return url_for('item_detail', key=key)
        return url_for('list_all')

    return dict(url_for_item=url_for_item)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
    
