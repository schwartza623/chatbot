import streamlit as st
import openai

# App title
st.title("Cold Call AI Sales Assistant")

openai_api_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")
if not openai_api_key:
    st.stop()
openai.api_key = openai_api_key


# Define the prompt template for GPT
prompt_template = (
        "You are an AI assistant for a commercial real estate agent specializing in multifamily buildings "
        "in Bed-Stuy and Bushwick, Brooklyn. Based on the ongoing cold call transcript below, suggest what "
        "the agent should say next.\n\n"
        "The suggestions should be focused on:\n"
        "- Overcoming objections\n"
        "- Proposing a complimentary property valuation or proposal\n"
        "- Asking the right follow-up questions to gauge interest\n"
        "- Highlighting value of Marcus & Millichap’s platform\n\n"
        f"Transcript:\n{user_input}\n\nResponse Suggestions:"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant for a real estate agent cold calling."},
                {"role": "user", "content": prompt_template}
            ]
        )

        if response.get('choices'):
            suggestions = response['choices'][0]['message']['content']
            st.subheader("🧠 Suggested Responses:")
            st.write(suggestions)
        else:
            st.warning("No suggestions were returned. Please try again.")

    except Exception as e:
        st.error(f"Error: {str(e)}")

elif not api_key:
    st.info("Please enter your OpenAI API Key to begin.")
elif not user_input.strip():
    st.info("Start by entering a portion of your call transcript.")
