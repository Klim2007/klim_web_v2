
from flask import Flask, render_template, jsonify
app = Flask(__name__)
JOBS = [
  {
  'id': 1,
  'title': 'Data analyst',
  'location': 'Astana',
  'salary': '900 000 tenge'
  },
    {
  'id': 2,
  'title': 'Data scientist',
  'location': 'Almaty',
  'salary': '1 000 000 tenge'
  },
      {
  'id': 3,
  'title': 'Sales manager',
  'location': 'Shumkent'
  
  }
]
@app.route("/")  #part of domain name
def hell():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/JOBS")
def list_jobs():
  return jsonify(JOBS)
  


if __name__ == "__main__":
  app.run(host = '0.0.0.0',debug=True)