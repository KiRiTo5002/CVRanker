def prompt(text, schema):
    return f""" You are and expert resume parser working for a company. you tast is to extract the structured information.
    Do not guess.
    If information is missing, return null or an empty list.
    Extract only information explicitly supported by the resume.
    Return only valid JSON.
    Follow the provided schema exactly.
    you have to extract the information from {text} based on {schema}."""
