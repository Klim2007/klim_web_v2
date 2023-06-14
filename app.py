from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)


def lod_jobs_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
  jobs = []
  for row in result.all():
    jobs.append(row._asdict())
  return jobs


@app.route("/")  #part of domain name
def hell():
  return render_template('home.html', jobs=lod_jobs_db())


@app.route("/api/JOBS")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

 # Start the app on port 5001
#if: __name__ == '__main__':
    #app.run(port=5001) 
