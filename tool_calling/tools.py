
import re

def keyword_overlap(cv, jd):

    cv_words = set(re.findall(r'\w+', cv.lower()))
    jd_words = set(re.findall(r'\w+', jd.lower()))

    common = cv_words.intersection(jd_words)

    important_keywords = [
        word for word in common
        if len(word) > 3
    ]

    return {
        "count": len(important_keywords),
        "matching_keywords": important_keywords
    }

from datetime import datetime

def date_helper(deadline):

    target_date = datetime.strptime(deadline, "%Y-%m-%d")

    today = datetime.today()

    remaining = target_date - today

    return {
        "deadline": deadline,
        "days_remaining": remaining.days
    }