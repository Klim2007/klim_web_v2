from flask import Flask, render_template, jsonify
from database import load_jobs_db
from database import load_id_db

app = Flask(__name__, static_folder='static')

@app.route("/")  #part of domain name
def hell():
  return render_template('home.html', jobs=load_jobs_db())

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_db()
  return jsonify(jobs)

@app.route("/job/<int:id>")
def show_job(id):
  job = load_id_db(id)
  if job is None:
    return jsonify({'error': 'Job not found'})
  else:
    return render_template('jobpage.html', job=job)

if __name__ == "__main__":
app.run(host='0.0.0.0',port=5001 ,debug=True)

