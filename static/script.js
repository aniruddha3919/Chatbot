document.getElementById('send-btn').addEventListener('click', async () => {
    const userInput = document.getElementById('user-input').value;
    if (!userInput) return;

    addMessage(userInput, 'user-message');
    document.getElementById('user-input').value = '';

    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    }).then(res => res.json());

    addMessage(response.response, 'bot-message');

    if (response.buttons) {
        addButtons(response.buttons);
    }
});

function addMessage(text, className) {
    const chat = document.getElementById('chat');
    const messageDiv = document.createElement('div');
    messageDiv.className = `chat-message ${className}`;
    messageDiv.textContent = text;
    chat.appendChild(messageDiv);
    chat.scrollTop = chat.scrollHeight;
}

function addButtons(buttons) {
    const chat = document.getElementById('chat');
    const buttonsDiv = document.createElement('div');
    buttonsDiv.className = 'buttons';

    buttons.forEach(button => {
        const btn = document.createElement('button');
        btn.className = 'button';
        btn.textContent = button.title;
        btn.addEventListener('click', () => {
            document.getElementById('user-input').value = button.title;
            document.getElementById('send-btn').click();
        });
        buttonsDiv.appendChild(btn);
    });

    chat.appendChild(buttonsDiv);
    chat.scrollTop = chat.scrollHeight;
}

document.getElementById('user-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        document.getElementById('send-btn').click();
    }
});
