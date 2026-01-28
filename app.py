from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    email = request.form['email']
    skills = request.form['skills']
    education = request.form['education']
    experience = request.form['experience']
    role = request.form['role']

    resume_text = f"""
    Name: {name}
    Email: {email}

    Target Role:
    {role}

    Skills:
    {skills}

    Education:
    {education}

    Experience:
    {experience}

    Career Objective:
    Motivated candidate applying for the role of {role}, 
    with strong skills in {skills}.
    """

    return render_template('result.html', resume=resume_text)

if __name__ == '__main__':
    app.run(debug=True)
