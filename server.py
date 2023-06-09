from flask import Flask, render_template, request, redirect, session # added request and redirect
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form
# show route
@app.route('/')
def index(): 
    return render_template("index.html")

# action route
@app.route('/process', methods=['POST'])
def process_form():
    session['form_data'] = request.form
    return redirect('/result')

# show route
@app.route('/result')
def show_results():
    return render_template('result.html')


@app.route('/reset')
def resetSurvey():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
