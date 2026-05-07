from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    choice = None
    error = None
    clothes_input = ''

    if request.method == 'POST':
        clothes_input = request.form.get('clothes', '')
        clothes = [line.strip() for line in clothes_input.split('\n') if line.strip()]
        if clothes:
            choice = random.choice(clothes)
        else:
            error = 'Please enter at least one clothing item to choose from.'

    return render_template('index.html', choice=choice, error=error, clothes_input=clothes_input)

if __name__ == '__main__':
    app.run(debug=True)