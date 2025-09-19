# app.py
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="PayGuard",
    page_icon="💰",
    layout="centered"
)

# Title and description
st.title("🛡️ PayGuard")
st.markdown("""
### Autonomous Proof for Delayed Salaries
Generate tamper-proof, on-chain evidence when a salary payment is delayed.
""")

# Create a form for user input
with st.form("debt_details_form"):
    st.header("Enter Debt Details")
    
    # Input fields
    employer_name = st.text_input("Employer/Company Name *")
    employee_email = st.text_input("Employee Email Address *")
    employee_wallet = st.text_input("Employee Solana Wallet Address")
    amount_owed = st.number_input("Amount Owed (USD) *", min_value=0.0, step=0.01)
    due_date = st.date_input("Original Due Date *")
    description = st.text_area("Additional Details (optional)")
    
    # Submit button
    submitted = st.form_submit_button("🚀 Generate Proof of Debt")

# Process the form submission
if submitted:
    # Basic validation
    if not all([employer_name, employee_email, amount_owed, due_date]):
        st.error("Please fill in all required fields (*)")
    else:
        # Show loading spinner while processing
        with st.spinner("Generating immutable proof on Solana blockchain..."):
            # Simulate agent calls (will be replaced with real functions)
            # TODO: Replace with actual blockchain_agent.record_debt()
            tx_id = "Tx1234567890abcdef"  # Simulated transaction ID
            
            # TODO: Replace with actual nft_agent.mint_nft()
            nft_id = "NFT-9876543210"  # Simulated NFT ID
            
            # Display results
            st.success("✅ Proof of Debt successfully generated!")
            
            # Create two columns for results
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("🔗 Blockchain Proof")
                st.code(f"Transaction ID: {tx_id}")
                st.caption("Immutable record on Solana blockchain")
            
            with col2:
                st.subheader("🎨 Digital Asset")
                st.code(f"NFT ID: {nft_id}")
                st.caption("Verifiable Proof of Debt NFT")
            
            # Additional actions
            st.divider()
            st.subheader("Next Steps")
            
            # Communication options
            com_col1, com_col2 = st.columns(2)
            
            with com_col1:
                if st.button("📧 Generate Professional Email"):
                    st.info("Email generation will be implemented with Mistral AI")
            
            with com_col2:
                if st.button("🔊 Generate Voice Message"):
                    st.info("Voice generation will be implemented with ElevenLabs")
            
            # Documentation
            st.info("""
            **Your proof has been permanently recorded.**
            - Solana Transaction ID serves as timestamped evidence
            - NFT represents the debt as a digital asset
            - Use the communication tools above to notify the employer
            """)

# Footer
st.divider()
st.caption("""
Built with ❤️ for workers' rights | 
Solana ∙ Crossmint ∙ Mistral AI ∙ ElevenLabs ∙ Coral Protocol
""")
