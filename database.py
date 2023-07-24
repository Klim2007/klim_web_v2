import sqlalchemy
from sqlalchemy import text, create_engine
import pymysql
import os
# Cnnection to DB with secret con details
con_data = os.environ['DB_connection_details']

engine = create_engine(con_data, connect_args={"ssl": {
  "ca": "cacert.pem",
}})


# List of jobs on front page
def load_jobs_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
  jobs = []
  for row in result.all():
    jobs.append(row._asdict())
  return jobs


def load_id_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),
                          {"val": id})
  row = result.fetchone()
  if row is None:
    return None
  else:
    column_names = result.keys(
    )  # Retrieve column names from the result object
    row_values = row  # Row values don't need to be retrieved separately
    data = dict(zip(column_names, row_values))
    return data


def add_application_to_db(id, data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO application (job_id, full_name, email, education, work_exp, resume_url, linked_inn_url) VALUES (:job_id, :full_name, :email, :education, :work_exp, :resume_url, :linked_inn_url)"
    )
    conn.execute(
      query, {
        'job_id': id,
        'full_name': data['full_name'],
        'email': data['email'],
        'education': data['education'],
        'work_exp': data['experiance'],
        'resume_url': data['resume'],
        'linked_inn_url': data['likedin_url']
      })
