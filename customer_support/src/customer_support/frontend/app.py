import streamlit as st 
import httpx 

def layout():
    st.markdown("# Support bot")
    st.markdown("Support bot will help with refund, warranty and shipping")

    if user_query := st.text_input("Ask support bot"):
        response = httpx.get(
            "http://127.0.0.1:8000/customer_support", params={"question": user_query}
        )

        st.markdown("## YOU:")
        st.markdown(user_query)
        
        st.markdown("## BOT:")
        st.markdown(response.text)




if __name__ == "__main__":
    layout()