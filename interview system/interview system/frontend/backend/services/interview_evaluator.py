def evaluate_answer(answer):

    if not answer.strip():

        return {
            "score": 0,
            "feedback":
            "Answer cannot be empty."
        }

    score = min(
        len(answer) // 5,
        100
    )

    if score > 80:

        feedback = \
        "Excellent answer."

    elif score > 50:

        feedback = \
        "Good answer."

    else:

        feedback = \
        "Needs improvement."

    return {

        "score": score,
        "feedback": feedback

    }