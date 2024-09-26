import cx_Oracle


class Oracle():
    
    def __init__(self, account, password) -> None:
        
        self.account = account
        self.password = password
        
        
    # def connect_to_account(self):
        
    #     return cx_Oracle.connect(f"{self.account}/{self.password}")
    
    
    def get_table_schema(self, table_name):
        cursor = cx_Oracle.connect(f"{self.account}/{self.password}").cursor()
        cursor.execute(f"""
            SELECT column_name, data_type
            FROM all_tab_columns
            WHERE table_name = '{table_name.upper()}'
            ORDER BY column_id
        """)
        columns = cursor.fetchall()
        cursor.close()
        
        schema = f"Table: {table_name}\nColumns:\n"
        for column in columns:
            schema += f"- {column[0]} ({column[1]})\n"
        return schema
    
    
    def execute_query(self, sql_query):
        connection = cx_Oracle.connect(self.account, self.password)
        try:
            cursor = connection.cursor()
            cursor.execute(sql_query)
            if sql_query.strip().upper().startswith("SELECT"):
                query_result = cursor.fetchall()
                print("\nQuery Result:")
                for row in query_result:
                    print(row)
                return query_result
            else:
                connection.commit()
                print("\nQuery executed successfully.")
                return None
        except cx_Oracle.Error as error:
            print(f"Error executing SQL: {error}")
            return None
        finally:
            if connection:
                connection.close()
        