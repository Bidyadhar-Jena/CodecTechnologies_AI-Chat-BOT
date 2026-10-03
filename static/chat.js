const form = document.querySelector('#chat-form');
const input = document.querySelector('#message-input');
const messages = document.querySelector('#messages');
const sendButton = document.querySelector('#send-button');

function addMessage(text, who) {
  const article = document.createElement('article');
  article.className = `message ${who}`;
  const label = document.createElement('span');
  label.className = 'speaker';
  label.textContent = who === 'user' ? 'You' : 'Assistant';
  const paragraph = document.createElement('p');
  paragraph.textContent = text; // textContent prevents HTML injection from chat messages.
  article.append(label, paragraph);
  messages.append(article);
  messages.scrollTop = messages.scrollHeight;
  return article;
}

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (!message) return;
  addMessage(message, 'user');
  input.value = '';
  input.focus();
  sendButton.disabled = true;
  const pending = addMessage('Thinking…', 'bot');
  try {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({message})
    });
    const data = await response.json();
    pending.remove();
    if (!response.ok) throw new Error(data.error || 'Request failed.');
    addMessage(data.reply, 'bot');
  } catch (error) {
    pending.remove();
    addMessage(error.message || 'Could not connect. Please try again.', 'bot');
  } finally {
    sendButton.disabled = false;
  }
});
