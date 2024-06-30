import pandas as pd
from termcolor import colored

def get_table_names(conn):
    """Return a list of table names."""
    table_names = []
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    for table in tables.fetchall():
        table_names.append(table[0])
    return table_names

def get_column_names(conn, table_name):
    """Return a list of column names."""
    column_names = []
    columns = conn.execute(f"PRAGMA table_info('{table_name}');").fetchall()
    for col in columns:
        column_names.append(col[1])
    return column_names

def get_database_info(conn):
    """Return a list of dicts containing the table name and columns for each table in the database."""
    table_dicts = []
    for table_name in get_table_names(conn):
        columns_names = get_column_names(conn, table_name)
        table_dicts.append({"table_name": table_name, "column_names": columns_names})
    return table_dicts

def show_table_as_dataframe(conn, table_name):
    """Display the contents of a table as a DataFrame."""
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql_query(query, conn)
    return df


def get_database_schemas(conn):
    database_schema_dict = get_database_info(conn)
    database_schema_string = "\n".join(
        [
            f"Table: {table['table_name']}\nColumns: {', '.join(table['column_names'])}" for table in
            database_schema_dict
        ]
    )
    # Possible values for columns
    role_values = ["Manager", "Developer", "HR"]
    rank_values = ["senior", "mid", "junior"]
    country_values = ["IL", "US", "UK"]
    return database_schema_dict, database_schema_string, role_values, rank_values, country_values


def append_to_history(role: str, content: str, memory: list[dict], tool_id=None, function_name=None):
    if role == "system":
        memory.append({"role": "system", "content":content})
    if role == "user":
        memory.append({"role": "user", "content":content})
    if role == "assistant":
        memory.append({"role": "assistant", "content":content})
    if role == "tool":
        memory.append({"role": "tool", "tool_call_id": tool_id,  "name": function_name, "content": content})
    return memory


def create_chat_response(client, tools, memory, tool_choice="auto"):
    return client.chat.completions.create(
    model = "gpt-4-32k",
    temperature = 0,
    n=1,
    tools=tools,
    tool_choice=tool_choice,
    messages = memory
    )


def pretty_print(response):
    if response.choices[0].message.content:
        msg = f"""{response.choices[0].message.role}: {response.choices[0].message.content}"""
        if response.choices[0].message.role == "assistant":
            print(colored(msg, 'red'))
        if response.choices[0].message.role == "user":
            print(colored(msg, 'green'))
        if response.choices[0].message.role == "tool":
            print(colored(msg, 'blue'))
