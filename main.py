#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Halaman Konten Berjalan
@app.route('/')
def index():
    return render_template('index.html')


#Keterampilan Dinamis
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    return render_template('index.html', button_python=button_python,
                           button_discord=button_discord)

@app.route('/feedback', methods=['POST'])
def get_feedback():
    
    email = request.form.get('email')
    feedback = request.form.get('text')
    
    with open('feedback_log', 'a') as f:
        f.write(email + '\n' + feedback + '\n\n')

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
