from flask import Flask
import random

app = Flask(__name__)


def comparison(func):
    def wrapper(number):
        if number == app.config['random_num']:
            return '''
                <h1 style="color:green">You found me</h1>  
                <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">
                '''
        elif number >= app.config['random_num']:
            return '''
               <h1 style="color:purple">Too high, try again!</h1> 
               <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">
               '''
        elif number <= app.config['random_num']:
            return '''
                <h1 style="color:red">Too low, try again</h1>
                <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">
                '''

    return wrapper


@app.route('/')
def headline():
    return '''
    <h1>Guess a number between 0 and 9</h1> 
    <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">
    '''


@app.route('/<int:number>')
@comparison
def user_choice(number):
    return str(number)


def get_random_num():
    return random.randint(0, 10)


app.config['random_num'] = get_random_num()

if __name__ == "__main__":
    app.run(debug=True, port=5002)
