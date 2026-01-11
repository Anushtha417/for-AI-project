from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

context = """
Artificial Intelligence (AI) is the simulation of human intelligence
in machines that are programmed to think like humans and mimic their actions.
AI is widely used in healthcare, finance, robotics, and education.
"""

question = "Where is AI used?"

result = qa_pipeline(question=question, context=context)
print("Answer:", result["answer"])
print("Confidence Score:", result["score"])
