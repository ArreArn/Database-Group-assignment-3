import os
from typing import Any, List, Tuple, Optional

import psycopg2 as pg
from dotenv import load_dotenv
from psycopg2 import OperationalError, Error


class Database:
    def __init__(self) -> None:

        Database.load_configuration()

        self.dbname = os.getenv("DB_NAME")
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.host = os.getenv("HOST")
        self.port = os.getenv("PORT")

        self.connection: Optional[pg.extensions.connection] = None

    @staticmethod
    def load_configuration():
        load_dotenv("config.env")

    def connect(self) -> None:
        try:
            self.connection = pg.connect(
                dbname = self.dbname,
                user = self.user,
                password = self.password,
                host = self.host,
                port = self.port
            )
        except OperationalError as e:
            raise RuntimeError(f"Error connecting to the database: {e}")

    def close(self) -> None:
        if self.connection:
            try:
                self.connection.close()
            except Error as e:
                raise RuntimeError(f"Error closing the connection: {e}")

    def execute_query(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> None:
        if not self.connection:
            raise RuntimeError("Connection is not established.")
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
        except Error as e:
            self.close()
            raise RuntimeError(f"Error executing query: {e}")

    def fetch_results(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> List[Tuple[Any, ...]]:
        if not self.connection:
            raise RuntimeError("Connection is not established.")
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                results = cursor.fetchall()
                return results
        except Error as e:
            self.close()
            raise RuntimeError(f"Error fetching results: {e}")

