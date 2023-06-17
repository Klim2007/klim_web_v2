import sqlalchemy 
from sqlalchemy  import text, create_engine
import pymysql


con_data = 'mysql+pymysql://zhwyxi7bqny7js6mwq9w:pscale_pw_bUmDFBvvcdWuViLobx8DqW4Y8oTqhecFET6CBATyF8h@aws.connect.psdb.cloud:3306/klim_db2?charset=utf8mb4'

engine = create_engine(con_data, connect_args={"ssl": {
  "ca": "cacert.pem",
}})
"""
with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM jobs"))


fetch = []
for row in result.all():
  fetch.append(row._asdict())
print(fetch)

"""