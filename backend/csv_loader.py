import pandas as pd

def load_csv(file_path: str) -> pd.DataFrame:
    """
    Loads the insurance claims CSV file and returns a DataFrame.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"✅ Loaded CSV with shape: {df.shape}")
        return df
    except Exception as e:
        print(f"❌ Failed to load CSV: {e}")
        return pd.DataFrame()


def dataframe_to_chunks(df: pd.DataFrame) -> list:
    """
    Converts each row into a natural language description (semantic chunk).
    """
    chunks = []
    
    for _, row in df.iterrows():
        row_text = (
            f"Customer aged {row['age']} with policy #{row['policy_number']} in {row['policy_state']}, "
            f"filed a {row['incident_type']} on {row['incident_date']} (severity: {row['incident_severity']}) "
            f"in {row['incident_city']}. Total claim amount: ${row['total_claim_amount']}. "
            f"Property damage: {row['property_damage']}. Bodily injuries: {row['bodily_injuries']}. "
            f"Fraud reported: {row['fraud_reported']}."
        )
        chunks.append(row_text)
    
    print(f"✅ Converted {len(chunks)} rows to text chunks.")
    return chunks
