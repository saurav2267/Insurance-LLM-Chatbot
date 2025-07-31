# backend/plotter.py

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

def generate_chart(query: str, df: pd.DataFrame):
    """
    Detects intent and generates a Matplotlib chart based on the user's query.
    Basic logic: if 'by' is used, we group and plot.
    """
    query = query.lower()

    if "claim amount" in query and "by" in query:
        # Example: 'Show total claim amount by incident type'
        if "incident type" in query:
            group_col = "incident_type"
        elif "incident city" in query:
            group_col = "incident_city"
        elif "policy state" in query:
            group_col = "policy_state"
        else:
            return "I understood you want a chart, but couldn't find the right column."

        fig, ax = plt.subplots()
        df.groupby(group_col)["total_claim_amount"].sum().sort_values().plot(kind="barh", ax=ax)
        ax.set_xlabel("Total Claim Amount")
        ax.set_title(f"Total Claim Amount by {group_col.replace('_', ' ').title()}")
        st.pyplot(fig)
        return None

    return "I couldn’t generate a chart from that query. Try saying 'chart of total claim by city' or similar."
