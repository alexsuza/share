from flask import Flask, render_template

from database import engine, text

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
  return render_template('home.html')


def load_items_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM items"))
    items = result.mappings().all()
  return items


@app.route('/market')
def market_page():
  items = load_items_from_db()
  return render_template('market.html', items=items)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
