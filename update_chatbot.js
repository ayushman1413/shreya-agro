const fs = require('fs');
const glob = require('glob'); // Not available by default. Better use child_process or recursive readdir.

const { join } = require('path');

function walk(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(function(file) {
        file = join(dir, file);
        const stat = fs.statSync(file);
        if (stat && stat.isDirectory()) { 
            results = results.concat(walk(file));
        } else { 
            if (file.endsWith('.html')) results.push(file);
        }
    });
    return results;
}

const files = walk('.');

const oldChatbotRegex = /<button class="chatbot-toggle" id="chatbotToggle".*?<\/div>[\s\n]*<\/div>/s;

const newChatbot = `<button class="chatbot-toggle" id="chatbotToggle" aria-label="Open chat">🤖</button>
<div class="chatbot-panel" id="chatbotPanel">
    <div class="chatbot-head">Shreya AI 🤖</div>
    <div class="chatbot-body" id="chatBody">
        <div class="chat-message bot">Hello! I'm Shreya's virtual assistant. How can I help you today?</div>
    </div>
    <div class="chatbot-footer">
        <input type="text" id="chatInput" placeholder="Type a message..." autocomplete="off">
        <button id="chatSendBtn">Send</button>
    </div>
</div>`;

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    if (content.match(oldChatbotRegex)) {
        content = content.replace(oldChatbotRegex, newChatbot);
        fs.writeFileSync(file, content);
        console.log('Updated ' + file);
    }
});
