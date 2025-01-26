
def assign_credit_score_with_non_financial(df):
    """
    Assigns a credit score (0-100) based on financial and non-financial data.
    """
    # Financial Features (normalized)
    df['payment_history_score_norm'] = df['payment_history_score'] / 10  # Assuming max is 10
    df['debt_to_income_score'] = (1 - df['debt_to_income_ratio']).clip(0, 1)  # Invert and cap
    df['savings_to_contribution_score'] = df['savings_to_contribution_ratio'].clip(0, 1)  # Cap at 1
    df['loan_history_score'] = (df['loan_history'] / df['loan_history'].max()).clip(0, 1)

    # Non-Financial Features (normalized)
    df['years_in_sacco_score'] = (df['years_in_sacco'] / df['years_in_sacco'].max()).clip(0, 1)
    df['dependents_score'] = (1 - df['dependents'] / df['dependents'].max()).clip(0, 1)  # Lower dependents = better score
    df['group_membership_score'] = df['group_membership'].apply(lambda x: 1 if x != 'Unknown' else 0)  # 1 for known groups
    df['location_score'] = df['location'].apply(lambda x: 1 if x != 'Unknown' else 0)  # 1 for known locations

    # Financial and Non-Financial Weights
    financial_weight = 0.7
    non_financial_weight = 0.3

    # Financial Score (weighted sum)
    financial_score = (
        df['payment_history_score_norm'] * 0.4 +
        df['debt_to_income_score'] * 0.3 +
        df['savings_to_contribution_score'] * 0.2 +
        df['loan_history_score'] * 0.1
    )

    # Non-Financial Score (weighted sum)
    non_financial_score = (
        df['years_in_sacco_score'] * 0.4 +
        df['dependents_score'] * 0.3 +
        df['group_membership_score'] * 0.2 +
        df['location_score'] * 0.1
    )

    # Combined Credit Score (scaled to 0-100)
    df['credit_score'] = (financial_score * financial_weight + non_financial_score * non_financial_weight) * 100

    # Round the score for clarity
    df['credit_score'] = df['credit_score'].round(2)

    return df