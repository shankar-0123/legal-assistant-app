function sendMessage() {
  var userMessage = document.getElementById('user-input').value;
  if (userMessage.trim() === '') {
      return;
  }

  var chatBox = document.getElementById('chatBox');

  var userMessageDiv = document.createElement("div");
  userMessageDiv.classList.add("message");
  userMessageDiv.innerHTML = `<img src="user.jpg" alt="User" class="user-img"><span>${userMessage}</span>`;
  chatBox.appendChild(userMessageDiv);

  document.getElementById('user-input').value = '';

  fetch('/chat', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: 'user_message=' + encodeURIComponent(userMessage),
  })
  .then(response => response.json())
  .then(data => {
      var botResponse = data.bot_response;
      var botMessageDiv = document.createElement("div");
      botMessageDiv.classList.add("message-response");
      botMessageDiv.innerHTML = `<img src="chatbot.jpeg" alt="Chatbot" class="chatbot-img"><span>${botResponse}</span>`;
      chatBox.appendChild(botMessageDiv);
      scrollChatToBottom();
  });
}

function scrollChatToBottom() {
  var chatBox = document.getElementById('chatBox');
  chatBox.scrollTop = chatBox.scrollHeight;
}

document.getElementById('user-input').addEventListener('keyup', function (event) {
  if (event.key === 'Enter') {
      sendMessage();
  }
});
const changingText = document.getElementById('changingText');
const texts = ["Please be aware that while Nyaay Sahaayak aims to provide helpful information, it may not offer exhaustive or entirely accurate responses. Verify any critical information with a legal professional before making decisions based on Nyaay Sahaayak's advice.", "Exercise caution when sharing sensitive or personal information with Nyaay Sahaayak. While we strive to maintain confidentiality, avoid disclosing highly confidential details about legal matters that could compromise your privacy or security.", "Nyaay Sahaayak is not a substitute for professional legal advice. Its responses are intended for informational purposes only and should not be construed as legal counsel. Always consult with a qualified attorney for tailored legal assistance tailored to your specific circumstances."]; // Add as many texts as needed
let index = 0;

function changeText() {
    changingText.textContent = texts[index];
    index = (index + 1) % texts.length; 
}

setInterval(changeText, 7000); 

const changingHeading = document.getElementById('changingHeading');
const headings = ["Precision", "Confidentiality", "Disclaimer"]; 
let index1 = 0;

function changeHeading() {
    changingHeading.textContent = headings[index1];
    index1 = (index1 + 1) % headings.length; 
}

setInterval(changeHeading, 7000);
