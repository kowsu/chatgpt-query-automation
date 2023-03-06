import openai
import docx
import os

openai.api_key = os.environ["OPENAI_API_KEY"]
engine = "davinci"
min_response_lines = 10
max_tokens = 150

def ask_gpt(prompt):
    prompt += "\n"
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5
    )
    answer = response.choices[0].text.strip()
    while len(answer.split("\n")) < min_response_lines:
        prompt = "In simple terms, " + prompt
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.5
        )
        answer = answer + "\n\n" + response.choices[0].text.strip()
    return answer

with open("questions.txt", "r") as f:
    questions = f.readlines()

doc = docx.Document()


for i in range(len(questions)):
    question = questions[i].strip()
    response = ask_gpt(question)
    doc.add_heading(f"{question}", level=1)
    doc.add_paragraph(f"{response}")
    if i < len(questions) - 1:
        doc.add_page_break()

doc.save("questions_and_answers.docx")

print('Done with recording by list questions and answers')
