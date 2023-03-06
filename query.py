import openai
import docx

openai.api_key = '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'
engine = "davinci"

def ask_gpt(prompt):
    prompt += "\n"
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5
    )
    answer = response.choices[0].text.strip()
    while len(answer.split("\n")) < 10:
        prompt = "In simple terms, " + prompt
        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=150,
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
    doc.add_heading(f"Question {i+1}", level=5)
    doc.add_paragraph(f"Q: {question}")
    doc.add_paragraph(f"A: {response}")
    if i < len(questions) - 1:
        doc.add_page_break()

doc.save("questions_and_answers.docx")

print('Done with recording by list questions and answers')