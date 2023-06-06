import sqlalchemy as sql
from sqlalchemy import text, create_engine

con_data = "mysql+pymysql://p6fgraiptf4aso926w60:pscale_pw_mr7L5Fxd1iZfIrfkkUuaBLsSSrP96RppuZUa45XQxXu@aws.connect.psdb.cloud/klim_db?charset=utf8mb4"
connect_args = {
    "ssl": {
        "ca": "/etc/ssl/cert.pem"
    }
}

engine = create_engine(con_data, args=connect_args)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    fetch = []
    for row in result:
        fetch.append(row)

print(fetch)
