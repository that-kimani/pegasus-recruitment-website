
    const form = document.getElementById('chat-form');
    const input = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const userMessage = input.value.trim();
      if (!userMessage) return;

      appendMessage('You', userMessage);
      input.value = '';

      try {
        const response = await fetch('/api/guidance-bot', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message: userMessage }),
        });

        const data = await response.json();
        appendMessage('Assistant', data.reply || 'Sorry, no response received.');
      } catch (error) {
        appendMessage('Assistant', 'Error connecting to assistant.');
      }
    });

    function appendMessage(sender, text) {
      const messageDiv = document.createElement('div');
      messageDiv.classList.add('message');
      messageDiv.innerHTML = `<strong>${sender}:</strong> ${text}`;
      chatBox.appendChild(messageDiv);
      chatBox.scrollTop = chatBox.scrollHeight;
    }