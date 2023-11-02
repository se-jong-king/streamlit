import streamlit as st

from bot.components.faq import faq
from dotenv import load_dotenv
import os

from utils.streamlit import append_history, undo, stream_display
from bot.functions import functions

load_dotenv()


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. Upload a pdf, docx, or txt file📄\n"
            "3. Ask a question about the document💬\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=os.environ.get("OPENAI_API_KEY", None)
            or st.session_state.get("OPENAI_API_KEY", ""),
        )

        st.session_state["OPENAI_API_KEY"] = api_key_input

        # Role selection and Undo
        st.header("Chat")
        chat_role = st.selectbox("role", ["system", "assistant", "user", "function"], index=2)
        st.button("Undo", on_click=undo)

        # ChatCompletion parameters
        st.header("Parameters")
        chat_params = {
         "model": st.selectbox("model", ["gpt-3.5-turbo-0613", "gpt-3.5-turbo-16k-0613", "gpt-4-0613", "gpt-4-32k-0613"]),
         "n": st.number_input("n", min_value=1, value=1),
         "temperature": st.slider("temperature", min_value=0.0, max_value=2.0, value=1.0),
         "max_tokens": st.number_input("max_tokens", min_value=1, value=512),
         "top_p": st.slider("top_p", min_value=0.0, max_value=1.0, value=1.0),
         "presence_penalty": st.slider("presence_penalty", min_value=-2.0, max_value=2.0, value=0.0),
         "frequency_penalty": st.slider("frequency_penalty", min_value=-2.0, max_value=2.0, value=0.0),
         "stream": True,
         }



        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖KnowledgeGPT allows you to ask questions about your "
            "documents and get accurate answers with instant citations. "
        )
        st.markdown(
            "This tool is a work in progress. "
            "You can contribute to the project on [GitHub](https://github.com/mmz-001/knowledge_gpt) "  # noqa: E501
            "with your feedback and suggestions💡"
        )
        st.markdown("Made by [mmz_001](https://twitter.com/mm_sasmitha)")
        st.markdown("---")

        faq()