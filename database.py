from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://vx0sy0xno6y5poj9zi9m:pscale_pw_ETSRiaPx5YQyxlhXuvFbwPVmtH0smZZUIs8DRdOaHki@aws.connect.psdb.cloud/market"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from items"))
  print(result.all())
