from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    prelim = float(request.form['prelim'])
    midterm = float(request.form['midterm'])
    final = float(request.form['final'])
    quizzes = float(request.form['quizzes'])
    recitation = float(request.form['recitation'])
    projects = float(request.form['projects'])

    # Ensure weights add up to 1. Adjust as necessary
    total_grade = (
        (prelim * 0.2) +   # 20% weight
        (midterm * 0.3) +  # 30% weight
        (final * 0.4) +    # 40% weight
        (quizzes * 0.05) +  # 5% weight
        (recitation * 0.025) + # 2.5% weight
        (projects * 0.025)  # 2.5% weight
    )

    # Cap the final grade to a maximum of 100
    total_grade = min(total_grade, 100)

    return render_template('index.html', result=total_grade)

if __name__ == '__main__':
    app.run(debug=True)
