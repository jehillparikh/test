from sqlalchemy import create_engine, inspect

from sqlalchemy import Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
import os
database_url = "postgresql://userdatabase_740c_user:VswYN2reYmzvjgZ5QMkNugBPxYvzTe08@dpg-cvn3uaemcj7s73c3a8vg-a.singapore-postgres.render.com/userdatabase_740c"
engine = create_engine(database_url)


def clear_database(database_url):
    """
    Drops all tables from the database, effectively clearing it.

    Args:
        database_url (str): SQLAlchemy DB URL.
    """
    engine = create_engine(database_url)
    metadata = MetaData(bind=engine)
    
    # Reflect the tables in the database
    metadata.reflect()

    # Drop all tables
    metadata.drop_all(engine)
    print("✅ All tables have been cleared from the database.")


import pandas as pd
from sqlalchemy import create_engine

import pandas as pd
from sqlalchemy import create_engine

def import_excel_to_db(excel_path, table_name, db_url):
    """
    Reads data from an Excel file and writes it to a PostgreSQL database.

    Args:
        excel_path (str): Path to the Excel file.
        table_name (str): Name of the destination table in the database.
        db_url (str): SQLAlchemy-compatible database URL.
    """
    # Read Excel into DataFrame
    df = pd.read_excel(excel_path)

    # Create SQLAlchemy engine
    engine = create_engine(db_url)

    # Use engine.connect() context to avoid AttributeError
    with engine.begin() as connection:
        df.to_sql(table_name, con=connection, index=False, if_exists='replace')

    print(f"✅ Data from {excel_path} written to '{table_name}' table.")




def drop_table(database_url, table_name):
    engine = create_engine(database_url)
    metadata = MetaData(bind=engine)
    table = Table(table_name, metadata, autoload_with=engine)
    table.drop(engine)
    print(f"Table '{table_name}' dropped.")

# Database URL from Render
database_url = "postgresql://userdatabase_740c_user:VswYN2reYmzvjgZ5QMkNugBPxYvzTe08@dpg-cvn3uaemcj7s73c3a8vg-a.singapore-postgres.render.com/userdatabase_740c"

def check_db_tables(db_url):
    try:
        # Create a database engine
        engine = create_engine(db_url)
        conn = engine.connect()
        
        # Get PostgreSQL version
        version = conn.execute("SELECT version();").fetchone()
        print(f"✅ Successfully connected to the database!")
        print(f"PostgreSQL version: {version[0]}")
        
        # Fetch all table names
        inspector = inspect(engine)
        tables = inspector.get_table_names()

        if tables:
            print("\n📌 Tables in the database:")
            for table in tables:
                print(f"  - {table}")
        else:
            print("\n⚠️ No tables found in the database.")

        # Close connection
        conn.close()

    except Exception as e:
        print(f"❌ Failed to connect to the database!")
        print(f"Error: {e}")

from sqlalchemy import create_engine, text

# Database URL from Render

def list_users(db_url):
    try:
        # Create a database engine
        engine = create_engine(db_url)
        with engine.connect() as connection:
            # Execute the query to fetch all users
            result = connection.execute(text("SELECT * FROM profile where first_name = 'Deepak'"))
            rows = result.fetchall()

            if rows:
                print("📌 Users in the database:")
                for row in rows:
                    # Convert each row to a dictionary and print
                    print(dict(row))
            else:
                print("⚠️ No users found in the database.")
    except Exception as e:
        print("❌ Failed to retrieve users from the database!")
        print(f"Error: {e}")


def list_funds(db_url):
    try:
        # Create a database engine
        engine = create_engine(db_url)
        with engine.connect() as connection:
            # Execute the query to fetch all users
            result = connection.execute(text("SELECT * FROM mf_factsheet"))
            rows = result.fetchall()

            if rows:
                print("📌 Users in the database:")
                for row in rows:
                    # Convert each row to a dictionary and print
                    print(dict(row))
            else:
                print("⚠️ No users found in the database.")
    except Exception as e:
        print("❌ Failed to retrieve users from the database!")
        print(f"Error: {e}")



if __name__ == "__main__":
   #list_users(database_url)


    #check_db_tables(database_url)
    clear_database(database_url)
    #list_funds(database_url)


    #directory='/Users/njp60/Documents/mutualfunddata/data/factsheets/test/'

    #factsheets = os.path.join(directory, 'factsheet_testdata.xlsx')

    #nav=os.path.join(directory, 'nav_testdata.xlsx')
    #portfolio=os.path.join(directory, 'portfolio_testdata.xlsx')
    #returns=os.path.join(directory, 'returns_testdata.xlsx')

    #import_excel_to_db(factsheets, 'mf_factsheet', database_url)
    #import_excel_to_db(nav, 'mf_nav', database_url)
    #import_excel_to_db(portfolio, 'mf_portfolio', database_url)
    #import_excel_to_db(returns, 'mf_returns', database_url) 


