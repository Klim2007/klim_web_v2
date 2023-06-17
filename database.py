import sqlalchemy
from sqlalchemy import text, create_engine
import pymysql
import os

con_data = os.environ['DB_connection_details']


engine = create_engine(con_data, connect_args={"ssl": {
  "ca": "cacert.pem",
}})

def load_jobs_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
  jobs = []
  for row in result.all():
    jobs.append(row._asdict())
  return jobs
"""
with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM jobs"))


fetch = []
for row in result.all():
  fetch.append(row._asdict())
print(fetch)

"""

