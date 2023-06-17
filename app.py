from flask import Flask, render_template, jsonify
from database import load_jobs_db


app = Flask(__name__)





@app.route("/")  #part of domain name
def hell():
  return render_template('home.html', jobs=load_jobs_db())


@app.route("/api/JOBS")
def list_jobs():
  jobs = load_jobs_db()
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0',port=5000 ,debug=True)

#Start the app on port 5001
#if: __name__ == '__main__':
    #app.run(port=5001) 
