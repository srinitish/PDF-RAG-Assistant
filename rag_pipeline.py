from groq import Groq

class RAGPipeline:

    def __init__(self,retriver):
        self.retriver = retriver
        self.client = Groq(
            api_key="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"
        )

    def ask(self,question):
        docs = self.retriver.retrieve(question)

        context = "\n".join(docs)

        prompt = f"""
        Ansewer the question using the context below.

        context:
        {context}

        Question: 
        {question}
        """

        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages = [
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        return response.choices[0].message.content