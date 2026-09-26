const form = document.getElementById("chatForm");
const input = document.getElementById("messageInput");
const chatBox = document.getElementById("chatBox");
const sendButton = document.getElementById("sendButton");


// ============================================================
// Add Message
// ============================================================

function addMessage(text, type, source = "") {

    // Remove welcome screen
    const emptyState = document.querySelector(".empty-state");

    if (emptyState) {
        emptyState.remove();
    }


    const wrapper = document.createElement("div");

    wrapper.className = `message ${type}`;


    const content = document.createElement("div");

    content.className = "message-content";


    const bubble = document.createElement("div");

    bubble.className = "bubble";

    bubble.textContent = text;


    content.appendChild(bubble);


    if (source) {

        const sourceElement =
            document.createElement("div");

        sourceElement.className = "source";


        if (source.includes("Gemini")) {

            sourceElement.classList.add("gemini");

            sourceElement.textContent =
                "🤖 " + source;

        } else {

            sourceElement.classList.add("fallback");

            sourceElement.textContent =
                "💡 " + source;
        }


        content.appendChild(sourceElement);
    }


    wrapper.appendChild(content);

    chatBox.appendChild(wrapper);


    scrollToBottom();
}


// ============================================================
// Typing Indicator
// ============================================================

function showTyping() {

    const wrapper =
        document.createElement("div");

    wrapper.className =
        "message bot";

    wrapper.id =
        "typingMessage";


    wrapper.innerHTML = `
        <div class="message-content">
            <div class="bubble">
                <div class="typing">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </div>
    `;


    chatBox.appendChild(wrapper);

    scrollToBottom();
}


function removeTyping() {

    const typing =
        document.getElementById("typingMessage");

    if (typing) {
        typing.remove();
    }
}


// ============================================================
// Scroll
// ============================================================

function scrollToBottom() {

    chatBox.scrollTop =
        chatBox.scrollHeight;
}


// ============================================================
// Send Message
// ============================================================

async function sendMessage(message) {

    if (!message.trim()) {
        return;
    }


    addMessage(
        message,
        "user"
    );


    input.value = "";

    sendButton.disabled = true;

    input.disabled = true;


    showTyping();


    try {

        const response =
            await fetch("/api/chat", {

                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            });


        const data =
            await response.json();


        removeTyping();


        if (data.success) {

            addMessage(
                data.answer,
                "bot",
                `Source: ${data.source}`
            );

        } else {

            addMessage(
                data.error ||
                "Something went wrong.",
                "bot",
                "EduGenie"
            );
        }


    } catch (error) {

        removeTyping();


        addMessage(
            "I couldn't connect to the EduGenie server. Please try again.",
            "bot",
            "Connection fallback"
        );
    }


    sendButton.disabled = false;

    input.disabled = false;

    input.focus();
}


// ============================================================
// Form Submit
// ============================================================

form.addEventListener(
    "submit",
    function(event) {

        event.preventDefault();

        const message =
            input.value.trim();

        sendMessage(message);
    }
);


// ============================================================
// Quick Question Cards
// ============================================================

const quickCards =
    document.querySelectorAll(
        ".quick-card"
    );


quickCards.forEach(card => {

    card.addEventListener(
        "click",
        function() {

            const question =
                this.dataset.question;

            input.value = question;

            input.focus();

            sendMessage(question);
        }
    );
});


// ============================================================
// Enter Key
// ============================================================

input.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            form.dispatchEvent(
                new Event("submit")
            );
        }
    }
);