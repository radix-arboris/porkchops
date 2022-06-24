from flask import Flask,render_template
app = Flask(__name__)

# https://platform.here.com/admin/apps/3G2h0Uupc8uqBPGPYy2s
@app.route('/map')
def map_func():
	return render_template('map.html')
if __name__ == '__main__':
    app.run(debug = True)   