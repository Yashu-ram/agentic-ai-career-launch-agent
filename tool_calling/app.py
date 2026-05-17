import ollama
from tools import keyword_overlap, date_helper
import time

start = time.time()


tools = [
    {
        "type": "function",
        "function": {
            "name": "keyword_overlap",
            "description": "Compare CV text and job description text for matching keywords",
            "parameters": {
                "type": "object",
                "properties": {
                    "cv": {
                        "type": "string",
                        "description": "CV or resume text"
                    },
                    "jd": {
                        "type": "string",
                        "description": "Job description text"
                    }
                },
                "required": ["cv", "jd"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "date_helper",
            "description": "Calculate remaining days until deadline",
            "parameters": {
                "type": "object",
                "properties": {
                    "deadline": {
                        "type": "string",
                        "description": "Date in YYYY-MM-DD format"
                    }
                },
                "required": ["deadline"]
            }
        }
    }
]

response = ollama.chat(
    model='qwen2.5:3b',
    messages=[
        {
            'role': 'user',
            'content': '''
How well does this CV match this job?

CV:
Python SQL Power BI Tableau Machine Learning

JD:
Looking for Python SQL Power BI skills
'''
        }
    ],
    tools=tools
)

tool_calls = response['message'].get('tool_calls')

print(tool_calls)

if tool_calls:

    tool_name = tool_calls[0]['function']['name']

    arguments = tool_calls[0]['function']['arguments']

    try:

        start = time.time()

        # TOOL 1
        if tool_name == "keyword_overlap":

            # VALIDATION
            if 'cv' not in arguments:
                raise ValueError("Missing 'cv' argument")

            if 'jd' not in arguments:
                raise ValueError("Missing 'jd' argument")

            result = keyword_overlap(
                arguments['cv'],
                arguments['jd']
            )

        # TOOL 2
        elif tool_name == "date_helper":

            # VALIDATION
            if 'deadline' not in arguments:
                raise ValueError("Missing 'deadline' argument")

            result = date_helper(
                arguments['deadline']
            )

        else:
            raise ValueError(f"Unknown tool: {tool_name}")

        end = time.time()

        trace = f"""
TOOL TRACE
-----------
Tool: {tool_name}
Arguments: {arguments}
Result: {result}
Time Taken: {end-start:.2f} sec
"""

        print(trace)

        with open("logs.txt", "a") as f:
            f.write(trace)

    except Exception as e:

        print(f"Tool execution failed: {str(e)}")

else:

    print(response['message']['content'])

try:

    if tool_name == "keyword_overlap":

        if 'cv' not in arguments or 'jd' not in arguments:
            raise ValueError("Missing cv or jd")

        result = keyword_overlap(
            arguments['cv'],
            arguments['jd']
        )

    elif tool_name == "date_helper":

        if 'deadline' not in arguments:
            raise ValueError("Missing deadline")

        result = date_helper(
            arguments['deadline']
        )

    print(result)

except Exception as e:
    print("Tool execution failed:", str(e))

end = time.time()

print(f"""
TOOL TRACE
-----------
Tool: {tool_name}
Arguments: {arguments}
Result: {result}
Time Taken: {end-start:.2f}s
""")