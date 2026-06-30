class PromptBuilder:
    @staticmethod
    def build(context,question):
        return f"""
You are an expert assistant.
Answer ONLY using the supplied context.
If the answer isn't present or you don't know it,say you don't know.

Context
-------
{context}

Question
--------
{question}

Answer:
"""