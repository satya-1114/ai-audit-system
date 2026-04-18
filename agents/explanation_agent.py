def generate_explanation(row, behavior):
    avg = behavior['avg_amount']
    common_vendors = behavior['common_vendors']

    # Conditions
    high_amount = row['Amount'] > avg * 2
    unknown_vendor = row['Vendor'] not in common_vendors

    # SHORT + IMPACTFUL OUTPUT
    if high_amount and unknown_vendor:
        return "High amount and unfamiliar vendor detected."

    elif high_amount:
        return "Unusual transaction magnitude detected."

    elif unknown_vendor:
        return "Transaction with unfamiliar vendor."

    # Normal cases (variation)
    import random
    normal_responses = [
        "Transaction aligns with established behavioral patterns.",
        "No deviation from historical transaction behavior detected.",
        "Transaction consistent with prior activity trends.",
        "Behavior matches learned spending patterns and vendor interactions."
    ]

    return random.choice(normal_responses)