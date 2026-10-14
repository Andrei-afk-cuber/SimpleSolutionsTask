from sqlmodel import create_engine

from .config import DBConfig

sql_url = (f"postgresql+psycopg2://{DBConfig.user}:{DBConfig.password}"
           f"@{DBConfig.host}:{DBConfig.port}/{DBConfig.database}")


engine = create_engine(sql_url, echo=True)