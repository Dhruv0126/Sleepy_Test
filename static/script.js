// 

document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("chat-form");
    const chatBox = document.getElementById("chat-box");
    const messageInput = document.getElementById("message");
  
    form.addEventListener("submit", function(e) {
      e.preventDefault();
      const userMessage = messageInput.value.trim();
      if (!userMessage) return;
  
      // Append user message
      appendMessage("user", userMessage);
      messageInput.value = '';
  
      // Send to Flask backend
      fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `message=${encodeURIComponent(userMessage)}`
      })
        .then(response => response.json())
        .then(data => {
          appendMessage("bot", data.response);
        })
        .catch(err => console.error(err));
    });
  
    function appendMessage(sender, message) {
      const msgDiv = document.createElement("div");
      msgDiv.classList.add("message");
      msgDiv.classList.add(sender === "bot" ? "bot-message" : "user-message");
      msgDiv.textContent = message;
      chatBox.appendChild(msgDiv);
      chatBox.scrollTop = chatBox.scrollHeight;
    }
  });
  