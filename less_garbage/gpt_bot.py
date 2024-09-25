from openai import OpenAI
client = OpenAI()

class GPTBot:
    def __init__(self, role="") -> None:
        self.history = []
        self.role = role

    def ask(self, prompt):
        # add the meta prompt
        messages = [{"role": "system", "content": self.role}] if self.role else []
        
        # add the history to the prompt
        for (role, content) in self.history:
            messages.append({"role": role, "content": content})
        
        # add the actual prompt
        messages.append({"role": "user", "content": prompt})

        print(messages)

        # send to GPT API
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        response = completion.choices[0].message.content

        self.update_history(prompt, response)

        return response
    
    # add the given prompt and response to the history of this bot
    def update_history(self, prompt, response):
        self.history.append(("user", prompt))
        self.history.append(("assistant", response))