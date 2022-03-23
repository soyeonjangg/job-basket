import pandas as pd
import en_core_web_sm

nlp = en_core_web_sm.load()


def extract_skills(resume_text):
    nlp_text = nlp(resume_text)
    noun_chunks = nlp_text.noun_chunks

    # removing stop words and implementing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]

    # reading the csv file
    data = pd.read_csv("skills.csv")

    # extract values
    skills = list(data.columns.values)

    skill_set = []

    # check for one-grams (example: python)
    for token in tokens:
        if token.lower() in skills:
            skill_set.append(token)

    # check for bi-grams and tri-grams (example: machine learning)
    for token in noun_chunks:
        token = token.text.lower().strip()
        if token in skills:
            skill_set.append(token)

    return [i.capitalize() for i in set([i.lower() for i in skill_set])]


# open text file in read mode
text_file = open("resume.txt", "r")

# read whole file to a string
f = text_file.read()

print('Skills', extract_skills(f))
# close file
text_file.close()
