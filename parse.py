from transformers import pipeline

# Load the question-answering model
question_answering = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Your text content
text = """
vrishank is smart and confident but his friends are stupid
"""

# Ask a question about the text
question = "7+7"
result = question_answering(question=question, context=text)

# Print the answer
print(result["answer"])
