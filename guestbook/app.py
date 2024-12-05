from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

entries = []

@app.route('/')
def index():
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['GET','POST'])
def add_entry():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')

        if name and message:
            entries.append({'name':name, 'message':message})
            return redirect(url_for('index'))
    return render_template('add_entry.html')

if __name__ == '__main__':
    app.run(debug=True)