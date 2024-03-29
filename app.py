from flask import Flask, render_template, jsonify, request
from database import load_jobs_db
from database import load_id_db
from database import add_application_to_db

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

@app.route("/job/<int:id>/apply", methods = ['post'])
def apply_to_job(id):
  data = request.form
  job = load_id_db(id)
  add_application_to_db(id,data)
  
  return render_template('submitted_apps.html', application = data, job = job)

if __name__ == "__main__":
  app.run(host='0.0.0.0',port = 5000, debug = True)
else:
  print("port issue")