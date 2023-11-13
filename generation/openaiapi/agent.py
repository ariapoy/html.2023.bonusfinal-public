from openai import OpenAI

from collections import defaultdict

class Agent:
    def __init__(
        self,
        name,
        api_key,
        system_message=None,
        llm_config=None,
    ):
        self.name = name
        self.api_key = api_key

        self.llm_config = llm_config
        self._messages = defaultdict(list)
        self.client = OpenAI(api_key=self.api_key)

        # init agent
        if system_message is not None:
            self._system_message = [{"content": system_message, "role": "system"}]
            init_reply = self.generate_reply(self._system_message, sender='human')
            print(f'{self.name}: {init_reply}')

    def send(self, message, recipient, request_reply=0):
        self._append_message(message, "assistant", recipient)
        if recipient == 'human':
            print(f'{self.name}: {message}')
        else:
            recipient.receive(message, self, request_reply)

    def receive(self, message, sender, request_reply=0):
        self._process_received_message(message, sender)
        if request_reply == 0:
            return

        reply = self.generate_reply(messages=self._messages[sender], sender=sender)
        self.send(reply, sender)
        return reply

    def generate_reply(self, messages=None, sender=None):
        if messages is None:
            messages = self._messages[sender]


        reply = self.client.chat.completions.create(model=self.llm_config['model'],
        messages=messages)
        if not self.llm_config['model'] == reply.model:
            self.llm_config['model'] = reply.model

        reply = reply.choices[0].message.content
        return reply

    def _append_message(self, message, role, conversation_id):
        self._messages[conversation_id].append({'content': message, 'role': role})

    def _process_received_message(self, message, sender):
        self._append_message(message, "user", sender)

    def get_last_messages(self, recipient='human'):
        return self._messages[recipient][-1]['content']
