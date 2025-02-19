"""
SQL Utilities.
"""
import sqlite3


def connect_database(path: str) -> tuple:
    """
    ? Connects to a local sql database.

    Return the connection and the cursor.
    """
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    return connection, cursor


def close_database(connection) -> None:
    """
    ? Closes the connection to the database.
    """
    connection.commit()
    connection.close()


def create_table(cursor, name: str, columns: list) -> None:
    """
    ? Creates a table with the given columns in the database.
    ! name: str
        The name of the table.
    ! columns: list
        The columns to create in the table.
        (name, properties)
    """
    sql: str = ', '.join([f"{name} {props}" for name, props in columns])
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {name} ({sql});")


def insert_data(cursor, table: str, data: list, columns: list = []) -> None:
    """
    ? Insert the given data into a table in the database.
    ! table: str
        The name of the table to insert to.
    ! data: list
        The data to insert in the table.
    * columns: list = []
        The list of columns to insert to.
    """
    fields: str = ''
    if len(columns):
        fields = ', '.join(columns)
        fields = f"({fields})"
    placeholders: str = ', '.join(['?'] * len(data[0]))
    cursor.executemany(
        f"INSERT INTO {table} {fields} VALUES ({placeholders});", data)


def select_data(cursor, table: str, columns: list = [], where: str = '1=1') -> list:
    """
    ? Selects the data from a table in the database.
    ! table: str
        The name of the table to read to.
    * columns: list = []
        The list of columns to read to.
    * where: str = '1=1'
        The where clause of the query.
    """
    sql: str = ', '.join(columns) if len(columns) else '*'
    return list(cursor.execute(f"SELECT {sql} FROM {table} WHERE {where};"))
