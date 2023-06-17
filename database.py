import sqlalchemy as sqal
from sqlalchemy import text, create_engine
import pymysql


con_data = 'mysql+pymysql://9ex4c19d5d7uealyp9iw:pscale_pw_yACgHnRTveG8gppLq9QwyWDVGwpq2fxyUjuGhalgw8I@aws.connect.psdb.cloud:3306/klim_db2?charset=utf8mb4'

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