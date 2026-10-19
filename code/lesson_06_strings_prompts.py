
"""Lesson 1.6: Prompt Cleaner"""

raw_name = input("Enter your name: ")
raw_question = input("Enter your question: ")


clean_name = raw_name.strip().title()
clean_question = " ".join(raw_question.split()).capitalize()


short_question = clean_question[:150]
estimated_tokens = round(len(short_question) / 4)

mentions_python = "python" in clean_question.lower()

prompt = f"""You are a helpful Python tutor.
Answer in 3 short lines.
User: {clean_name}
Question: {short_question}"""

print("\nClean name:", clean_name)
print("Clean question:", clean_question)
print("Characters:", len(clean_question))
print("Estimated tokens:", estimated_tokens)
print("Mentions Python:", mentions_python)
print("\nAI Prompt:\n", prompt)
