import re

from datetime import datetime

from vectordb.main import retrieve_documents


# -----------------------------------
# TOOL 1
# -----------------------------------
def keyword_overlap(cv, jd):

    cv_words = set(
        re.findall(r'\w+', cv.lower())
    )

    jd_words = set(
        re.findall(r'\w+', jd.lower())
    )

    matched = cv_words.intersection(
        jd_words
    )

    important_matches = [

        word for word in matched

        if len(word) >= 2
    ]

    missing = jd_words - cv_words

    important_missing = [

        word for word in missing

        if len(word) >= 2
    ]

    match_percentage = round(

        (len(important_matches) / len(jd_words)) * 100,

        2
    )

    return {

        "match_percentage": match_percentage,

        "matched_skills": important_matches,

        "missing_skills": important_missing
    }


# -----------------------------------
# TOOL 2
# -----------------------------------

def date_helper(deadline):

    target_date = datetime.strptime(
        deadline,
        "%Y-%m-%d"
    )

    today = datetime.today()

    remaining = target_date - today

    return {

        "deadline": deadline,

        "days_remaining": remaining.days
    }


# -----------------------------------
# TOOL 3
# -----------------------------------

def search_documents(query):

    results = retrieve_documents(query)

    retrieved_docs = results["documents"][0]

    combined_docs = "\n".join(retrieved_docs)

    return combined_docs