
import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine, text

load_dotenv()

url = URL.create(
    "postgresql+psycopg",
    username=os.environ["PGUSER"],
    password=os.environ["PGPASSWORD"],
    host=os.environ["PGHOST"],
    port=int(os.getenv("PGPORT", "5432")),
    database=os.environ["PGDATABASE"],
    query={
        "sslmode": os.getenv("PGSSLMODE", "require")
    },
)

engine = create_engine(
    url,
    connect_args={
        "options": "-c default_transaction_read_only=on"
    },
    pool_pre_ping=True,
)

try:
    with engine.connect() as connection:

        print("\nCONNECTED SUCCESSFULLY!")

        # Retrieve database constraints and relationships
        query = """
        SELECT
            tc.table_name,
            tc.constraint_type,
            tc.constraint_name,
            kcu.column_name,
            kcu.position_in_unique_constraint,
            kcu.referenced_table_name,
            kcu.referenced_column_name

        FROM information_schema.table_constraints tc

        LEFT JOIN information_schema.key_column_usage kcu
            ON tc.constraint_catalog = kcu.constraint_catalog
            AND tc.constraint_schema = kcu.constraint_schema
            AND tc.constraint_name = kcu.constraint_name
            AND tc.table_name = kcu.table_name

        WHERE tc.table_schema = 'public'
        AND tc.constraint_type IN (
            'PRIMARY KEY',
            'FOREIGN KEY',
            'UNIQUE'
        )

        ORDER BY
            tc.table_name,
            tc.constraint_type,
            kcu.ordinal_position;
        """

        relationships = pd.read_sql(
            text(query),
            connection
        )

        print("\nDATABASE KEYS AND RELATIONSHIPS:")

        print(relationships.to_string(index=False))

except Exception as error:
    print("An error occurred:")
    print(error)

finally:
    engine.dispose()
