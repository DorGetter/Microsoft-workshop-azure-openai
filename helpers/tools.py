def schedule_meeting(title: str, date_and_time: str, invitees: list['str']):
    """This function will schedule a new meeting"""
    return f"A new meeting '{title}' at: {date_and_time}, with invitees: {invitees} created sucessefully"


schedule_meeting_tool = {
    "type": "function",
    "function": {
        "name": "schedule_meeting",
        "description": "Schedules a new meeting with a specified title, date and time, and list of invitees.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "The title of the meeting."
                },
                "date_and_time": {
                    "type": "string",
                    "description": "The date and time of the meeting in a specified format."
                },
                "invitees": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "A list of invitees' names or email addresses."
                }
            },
            "required": ["title", "date_and_time", "invitees"],
        },
    }
}

schedule_system_message = """
You are a helpful assistant capable of scheduling meetings.
when a user asks to schedule a meeting make sure that the user specifies the following entities:
- **title**: Meeting title (string)
- **date_and_time**: Date and time (string)
- **invitees**: List of invitees' names (can be only one name)
Instructions:
When a user requests to schedule a meeting, ensure you have all the required entities needed to call the scheduling tool. 
If any information is missing, explicitly ask for the missing fields. if user provided only one name than dont ask him for more invitees.
"""

### -----------------------------------------------------------

def send_email(to: str, subject: str, body: str, cc: list = None):
    """Simulates sending an email by returning a string with all the provided parameters."""
    email_details = f"Email to: {to}\nSubject: {subject}\nBody: {body}"
    if cc:
        email_details += f"\nCC: {', '.join(cc)}"
    return "Email sent successfully!"


send_email(
    to="recipient@example.com",
    subject="Meeting Reminder",
    body="This is a reminder for our meeting tomorrow.",
    cc=["cc1@example.com", "cc2@example.com"],
)

send_email_tool = {
    "type": "function",
    "function": {
        "name": "send_email",
        "description": "When a user asks to send an email, ensure the following information is provided: 1. to: Recipient's email address (string) 2. subject: Email subject (string). If not specified, generate a suitable subject. 3. body: Email body content (string). Rephrase the user's input into a professional format if needed. cc: (Optional) List of email addresses to CC (array of strings)",
        "parameters": {
            "type": "object",
            "properties": {
                "to": {
                    "type": "string",
                    "description": "The recipient's email address."
                },
                "subject": {
                    "type": "string",
                    "description": "The subject of the email."
                },
                "body": {
                    "type": "string",
                    "description": "The body (content) of the email"
                },
                "cc": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "A list of email addresses to CC."
                }
            },
            "required": ["title", "date_and_time", "invitees"],
        },
    }
}

email_system_message = """
You are an assistant chatbot capable of sending emails.
When requested to send an email make sure that you have the 'to' field. If the 'to' parameter is missing ask specifically for it.
other fields you can generate yourself if needed. try avoid asking for information from the user unless the user didnt specify the 'to' and there is no body at all.
Do not confirm with the user if you been able to construct the email.

User Name: %s
"""

### -----------------------------------------------------------

def ask_database(conn, query):
    """Function to query SQLite database with a provided SQL query."""
    try:
        results = str(conn.execute(query).fetchall())
    except Exception as e:
        results = f"query failed with error: {e}"
    return results


ask_db_tool = {
    "type": "function",
    "function": {
        "name": "ask_database",
        "description": f"""
Use this function to query the Employees database.
The database contains the following schema:
Table: Employees
Columns: id, first_name, last_name, phone_number, email_address, role, rank, country
Possible values for columns:
- role: Manager, Developer, HR
- rank: senior, mid, junior
- country: IL, US, UK
The input should be a fully formed SQL query.""",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": f"""
SQL query extracting info to answer the user's question.
SQL should be written using this database schema:
Table: Employees
Columns: id, first_name, last_name, phone_number, email_address, role, rank, country
The query should be returned in plain text, not in JSON.
                                """,
                }
            },
            "required": ["query"],
        },
    }
}

sql_system_message = """
You are a helpful assistant capable of querying an SQLite database. The database contains information about employees with the following schema:

Table: Employees
Columns: id, first_name, last_name, phone_number, email_address, role, rank, country

Possible values for columns:
- role: Manager, Developer, HR
- rank: senior, mid, junior
- country: IL, US, UK

You can use the `ask_database` function to query the database. The input should be a fully formed SQL query.
"""


### -----------------------------------------------------------
func_tools = {
    "schedule_meeting_tool": schedule_meeting_tool,
    "send_email_tool": send_email_tool,
    "ask_db_tool": ask_db_tool
}

system_prompts = {
    "schedule_system_message": schedule_system_message,
    "email_system_message": email_system_message,
    "sql_system_message": sql_system_message
}

