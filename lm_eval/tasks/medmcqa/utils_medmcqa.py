# Copied from Master
def doc_to_text(doc) -> str:
    """
    Question: <question>
    Choices:
    A. <choice1>
    B. <choice2>
    C. <choice3>
    D. <choice4>
    Answer:
    """
    choices = [doc["opa"], doc["opb"], doc["opc"], doc["opd"]]
    option_choices = {
        "A": choices[0],
        "B": choices[1],
        "C": choices[2],
        "D": choices[3],
    }

    prompt = "Question: " + doc["question"] + "\nChoices:\n"
    for choice, option in option_choices.items():
        prompt += f"{choice.upper()}. {option}\n"
    prompt += "Answer:"
    return prompt

def doc_to_text_cot(doc) -> str:
    """ PROMPT
    The following is a multiple choice question about medical knowledge. 
    Solve it in a step-by-step fashion, starting by summarizing the available information. 
    Output a single option from the four options as the final answer: {doc["question"]}\nOptions:\n{options}\nAnswer:
    """
    """
    Question: <question>
    Choices:
    A. <choice1>
    B. <choice2>
    C. <choice3>
    D. <choice4>
    Answer:
    """
    choices = [doc["opa"], doc["opb"], doc["opc"], doc["opd"]]
    option_choices = {
        "A": choices[0],
        "B": choices[1],
        "C": choices[2],
        "D": choices[3],
    }

    prompt = f"The following is a multiple choice question about medical knowledge. Solve it in a step-by-step fashion, starting by summarizing the available information. Output a single option from the four options as the final answer: Question: {doc['question']}\nOptions:\n"
    for choice, option in option_choices.items():
        prompt += f"{choice.upper()}. {option}\n"
    prompt += "Answer:"
    return prompt
