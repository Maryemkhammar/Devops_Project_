from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def cv_form():
    if request.method == 'POST':
        # Récupération des données du formulaire
        data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'summary': request.form.get('summary'),
            'skills': request.form.get('skills').split(',')
        }
        return render_template('cv_preview.html', data=data)
    
    return render_template('cv_form.html')

if __name__ == '__main__':
    app.run(debug=True)
