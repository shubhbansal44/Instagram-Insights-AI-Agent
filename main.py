from model import AI_MODEL  # Import the AI_MODEL class from the model module
import streamlit as st  # Streamlit is used for building the frontend

class AI_AGENT:
    """
    AI_AGENT serves as a bridge between the AI model backend and the Streamlit frontend.
    It handles user input, communicates with the AI model, and manages the chat interface.
    """

    def __init__(self):
        """
        Initializes the AI_AGENT with an instance of the AI_MODEL class.
        """
        self.model = AI_MODEL()

    def ask(self, prompt: str) -> str:
        """
        Sends a user prompt to the AI model and retrieves a response.

        Args:
            prompt (str): The user's input message.

        Returns:
            str: The AI model's response.
        """
        return self.model.ask_ai(prompt)

    def perform(self):
        """
        Entry point for the AI_AGENT to run the frontend application.
        """
        self.frontend()

    def frontend(self):
        """
        Defines the Streamlit frontend interface, managing user interactions, and chat history.
        """
        # Set the page configuration for the Streamlit app
        st.set_page_config(page_title="Instagram Insights ChatBot", layout="wide")

        # Page Title and Introduction
        st.title("Your Daily Instagram Insights")
        st.divider()

        # Sidebar for user settings or additional features
        with st.sidebar:
            st.header("Settings")
            # Input for the user's name
            name = st.text_input("Enter your name:", placeholder="Type your name here...")
            # Personalized greeting in the sidebar
            st.write(f"Hello, {name if name else 'Guest'}!")
            st.divider()

        # Main chat interface section
        st.subheader("Chat with Your Insights Assistant")
        st.divider()

        # Initialize the chat message history in Streamlit's session state
        if "messages" not in st.session_state:
            st.session_state.messages = []  # Create an empty message history

        # Display chat messages from the session state
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])  # Render the message content in Markdown

        # Input area for new user messages
        if user_input := st.chat_input("Type your message here..."):
            # Add the user's message to the chat history
            st.session_state.messages.append({"role": "user", "content": user_input})

            # Display the user's message in the chat
            with st.chat_message("user"):
                st.markdown(user_input)

            # Display a simulated response from the assistant with a loading spinner
            with st.chat_message("assistant"):
                with st.spinner("Generating response..."):
                    # Get the AI model's response
                    response = self.ask(user_input)
                st.markdown(response)

            # Add the assistant's response to the chat history
            st.session_state.messages.append({"role": "assistant", "content": response})


# Run the application if the script is executed directly
if __name__ == '__main__':
    agent = AI_AGENT()  # Instantiate the AI_AGENT
    agent.perform()  # Run the frontend
