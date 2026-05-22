import ollama
import json
import time

from tool_calling.tools import (
    keyword_overlap,
    date_helper,
    search_documents
)

# -----------------------------------
# TOOL DEFINITIONS
# -----------------------------------

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
    },

    {
        "type": "function",
        "function": {
            "name": "search_documents",
            "description": "Search career PDF documents for relevant information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query"
                    }
                },
                "required": ["query"]
            }
        }
    }
]


# -----------------------------------
# AGENT LOOP
# -----------------------------------

def agent_loop(user_question, max_turns=5):

    messages = [

        {
            "role": "system",
            "content": """
You are a career assistant AI agent.

You can use these tools:

1. keyword_overlap
2. date_helper
3. search_documents

Rules:
- Think step by step
- Use tools only if needed
After observing tool results:

- If the user question is already answered,
immediately provide:

FINAL ANSWER: <answer>

- Do NOT ask unrelated follow-up questions

- Do NOT continue reasoning unnecessarily

- Only use another tool if absolutely required
to answer the original user question
- NEVER stop without FINAL ANSWER

- You MUST either:
    1. call a tool
    OR
    2. respond with:
       FINAL ANSWER: <answer>

- Never respond casually
- Avoid unnecessary tool usage
"""
        },

        {
            "role": "user",
            "content": user_question
        }
    ]

    # -----------------------------------
    # FINAL ANSWER SAFETY
    # -----------------------------------

    final_answer_attempts = 0

    # -----------------------------------
    # REACT LOOP
    # -----------------------------------

    for turn in range(max_turns):

        print(f"\n{'='*50}")
        print(f"TURN {turn + 1}")
        print(f"{'='*50}")

        start = time.time()

        # -----------------------------------
        # CALL OLLAMA
        # -----------------------------------

        response = ollama.chat(

            model='qwen2.5:3b',

            messages=messages,

            tools=tools
        )

        message = response['message']

        content = message.get('content', '')

        print("\nMODEL RESPONSE:\n")
        print(content)

        # -----------------------------------
        # STOP CONDITION
        # -----------------------------------

        if "FINAL ANSWER" in content:

            print("\nAGENT STOPPED\n")

            print(content)

            break

        # -----------------------------------
        # TOOL CALLS
        # -----------------------------------

        tool_calls = message.get('tool_calls')

        if tool_calls:

            tool_call = tool_calls[0]

            tool_name = tool_call['function']['name']

            arguments = tool_call['function']['arguments']

            print("\nTOOL SELECTED:\n")
            print(tool_name)

            print("\nARGUMENTS:\n")
            print(arguments)

            try:

                # -----------------------------------
                # TOOL 1
                # -----------------------------------

                if tool_name == "keyword_overlap":

                    if 'cv' not in arguments:
                        raise ValueError("Missing 'cv'")

                    if 'jd' not in arguments:
                        raise ValueError("Missing 'jd'")

                    result = keyword_overlap(
                        arguments['cv'],
                        arguments['jd']
                    )

                # -----------------------------------
                # TOOL 2
                # -----------------------------------

                elif tool_name == "date_helper":

                    if 'deadline' not in arguments:
                        raise ValueError("Missing 'deadline'")

                    result = date_helper(
                        arguments['deadline']
                    )

                # -----------------------------------
                # TOOL 3
                # -----------------------------------

                elif tool_name == "search_documents":

                    if 'query' not in arguments:
                        raise ValueError("Missing 'query'")

                    result = search_documents(
                        arguments['query']
                    )

                else:

                    raise ValueError(
                        f"Unknown tool: {tool_name}"
                    )

                # -----------------------------------
                # TOOL RESULT
                # -----------------------------------

                print("\nTOOL RESULT:\n")
                print(result)

                # -----------------------------------
                # TRACE LOGGING
                # -----------------------------------

                end = time.time()

                trace = {

                    "turn": turn + 1,

                    "tool": tool_name,

                    "arguments": arguments,

                    "result": str(result),

                    "time_taken_sec": round(end - start, 2)
                }

                print("\nTRACE LOG:\n")

                print(
                    json.dumps(
                        trace,
                        indent=2
                    )
                )

                # -----------------------------------
                # SAVE LOGS
                # -----------------------------------

                with open("logs.txt", "a") as f:

                    f.write(
                        json.dumps(trace) + "\n"
                    )

                # -----------------------------------
                # OBSERVATION STEP
                # -----------------------------------

                messages.append({

                    "role": "assistant",

                    "content": content
                })

                messages.append({

                    "role": "tool",

                    "content": f"""
Observation:

Tool Used:
{tool_name}

Tool Result:
{result}

Now decide:
- use another tool
OR
- provide FINAL ANSWER
"""
                })

            except Exception as e:

                print(
                    f"\nTool execution failed: {str(e)}"
                )

                break

        # -----------------------------------
        # NO TOOL USED
        # -----------------------------------

        else:

            print("\nNO TOOL USED\n")

            final_answer_attempts += 1

            messages.append({

                "role": "assistant",

                "content": f"""
You did not call a tool.

Now provide FINAL ANSWER only.

Previous response:
{content}
"""
            })

            # -----------------------------------
            # SAFETY STOP
            # -----------------------------------

            if final_answer_attempts >= 2:

                print("\nFORCED FINAL RESPONSE:\n")

                print(content)

                break

            continue


# -----------------------------------
# TEST QUESTION
# -----------------------------------

agent_loop(
    """
Compare this CV with the JD
and tell how many days remain until 2026-06-01.

CV:
Python SQL Tableau Machine Learning

JD:
Looking for Python SQL Power BI skills
"""
)