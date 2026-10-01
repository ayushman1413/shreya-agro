import os, re

old_regex = re.compile(r'<button class="chatbot-toggle" id="chatbotToggle".*?</button>[\s\n]*<div class="chatbot-panel" id="chatbotPanel">[\s\n]*<div class="chatbot-head">Hi! 👋 How can we help you\?</div>[\s\n]*<div class="chatbot-body">.*?</div>[\s\n]*</div>', re.DOTALL)

new_chatbot = """<button class="chatbot-toggle" id="chatbotToggle" aria-label="Open chat">🤖</button>
<div class="chatbot-panel" id="chatbotPanel">
    <div class="chatbot-head">Shreya AI 🤖</div>
    <div class="chatbot-body" id="chatBody">
        <div class="chat-message bot">Hello! I'm Shreya's virtual assistant. How can I help you today?</div>
    </div>
    <div class="chatbot-footer">
        <input type="text" id="chatInput" placeholder="Type a message..." autocomplete="off">
        <button id="chatSendBtn">Send</button>
    </div>
</div>"""

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            if old_regex.search(content):
                content = old_regex.sub(new_chatbot, content)
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f'Updated {filepath}')
