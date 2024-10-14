import streamlit as st

# Fonction pour générer des réponses
def generate_response(user_input):
    # Logique simple de réponse
    if "bonjour" in user_input.lower():
        return "Bonjour! Comment puis-je vous aider aujourd'hui?"
    elif "comment ça va" in user_input.lower():
        return "Je vais bien, merci! Et vous?"
    else:
        return "Je suis un chatbot et je n'ai pas encore appris cette réponse."

# Configuration de l'interface
st.title("Chatbot avec Streamlit")
st.write("Bienvenue sur l'interface de chatbot. Posez-moi des questions !")

# Stockage des échanges de chat
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Formulaire d'entrée utilisateur
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Vous :", key="input")
    submit_button = st.form_submit_button(label='Envoyer')

# Lorsque l'utilisateur soumet une question
if submit_button and user_input:
    response = generate_response(user_input)
    # Ajouter l'entrée utilisateur et la réponse à l'historique
    st.session_state.chat_history.append(("Vous", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Affichage de l'historique des échanges
for sender, message in st.session_state.chat_history:
    if sender == "Vous":
        st.write(f"**{sender}:** {message}")
    else:
        st.write(f"*{sender}:* {message}")

