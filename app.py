# app.py
import streamlit as st
from agents.blockchain_agent import record_debt
from agents.nft_agent import mint_nft

# Set page configuration
st.set_page_config(
    page_title="PayGuard",
    page_icon="💰",
    layout="centered"
)

# Title and description
st.title("PayGuard")
st.write("Generate proof of delayed salary")

# Input form
with st.form("debt_form"):
    employer = st.text_input("Employer Name")
    employee_email = st.text_input("Employee Email")
    amount = st.number_input("Amount Owed")
    submitted = st.form_submit_button("Generate Proof")

if submitted:
    with st.spinner("Creating proof..."):
        # Create debt details
        debt_details = {
            "employer": employer,
            "employee_email": employee_email,
            "amount": amount
        }
        
        # Call your agents
        tx_id = record_debt(debt_details)
        nft_id = mint_nft(tx_id, employee_email)
        
        # Show results
        st.success("Done!")
        st.write(f"Transaction ID: {tx_id}")
        st.write(f"NFT ID: {nft_id}")
