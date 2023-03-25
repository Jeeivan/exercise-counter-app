from flask import Flask, render_template
from replit import db

app = Flask(__name__)

if 'number' not in db:
  db['number'] = 0

# db = {'number': 0}

### HTML & CSS ### Static
# my_home_page = '''
#  <link rel='stylesheet' href='./static/counter_styles.css'>
#<span>{{ number }}</span>
#<div>
# <form action='/decrement'>
#   <button>-</button>
# </form>

# <form action='/increment'>
#   <button>+</button>
# </form>
#</div>
# '''

@app.route('/')
def home():
  # return show(home_page, number=db['number'])
  return render_template('index.html', number=db['number'])

@app.route('/increment')
def increment():
  db['number'] += 1
  print(db)
  return render_template('index.html', number=db['number'])

@app.route('/decrement')
def decrement():
  db['number'] -= 1
  
  print(db)
  return render_template('index.html', number=db['number'])

app.run(host='0.0.0.0', port=81)