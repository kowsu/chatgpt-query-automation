# chatgpt-query-automation
Chat GPT Query automation with list of questions

**Required softwares:**
1) Python (https://www.python.org/downloads/)
2) Install python openapi package
      - Run <strong>pip install openapi</strong> in command prompt
3) Install python python-docx package
      - Run <strong>pip install python-docx</strong> in command prompt



**Steps to get OpenAI API Key**
1) Go to https://platform.openai.com/account/api-keys
2) Select API Keys on the left navigation menu; find the below screenshot for reference

![image](https://user-images.githubusercontent.com/10444449/223047522-08fe1cbe-65a5-4129-8fc6-b10d8694004e.png)

3) Click Create new secret Key and copy the Secret Key <strong>(If you don't copy the value you will never get it)</strong>
4) Set it in the environment variable with key as "OPENAI_API_KEY" and value is the copied one


**Please find the below image for reference**


![image](https://user-images.githubusercontent.com/10444449/223046925-489155f0-2883-4342-a59f-8853b6785713.png)



**Where are questions?**


You can add your questions in <strong>questions.txt</strong>

Please find the screenshot to follow the format.

![image](https://user-images.githubusercontent.com/10444449/223050587-fe8dd463-4adf-4600-9dff-2bd9299b4a69.png)

Input has to be in this format:

Chapter should contains "Chapter-" in the sentence

Sub Chapter should contains "Sub Chapter" in the sentence

Question should contains "Question" in the sentence and actual question should be embedded in "$"




**Run Python script to automate queries on Chat GPT**

C:\> py .\query.py


**If we see the below message, script execution completed**

###### Done with recording by list questions and answers


<strong>Now, you will be able to see the output in 'questions_and_answers.docx' file.</strong>

That's all.
