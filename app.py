from flask import Flask
app=Flask(__name__)

# use route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def welcome():
    return "Welcome to the home page."

@app.route("/contact")
def contactDetails():
    return "There is no contact details"

if(__name__ == "__main__"):
     app.run(debug = True)
     #app.run(debug=True , port = 8000)