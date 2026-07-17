def generate_recommendation(condition, question, evidence):

    # Combine all evidence
    evidence_text = " ".join(
        item["evidence"]
        for item in evidence
    ).lower()


    # Words that usually indicate positive/supporting evidence
    support_words = [
        "improve",
        "benefit",
        "recommended",
        "effective",
        "helps",
        "reduces",
        "increase",
        "better",
        "improves"
    ]


    # Words that indicate caution
    caution_words = [
        "risk",
        "avoid",
        "not recommended",
        "danger",
        "contraindicated",
        "consult"
    ]


    support_count = 0
    caution_count = 0


    # Count supporting and caution evidence
    for word in support_words:
        if word in evidence_text:
            support_count += 1


    for word in caution_words:
        if word in evidence_text:
            caution_count += 1



    # Decision making

    if support_count > caution_count:

        recommendation = (
            f"Based on the available medical evidence, "
            f"{condition} related guidance suggests that "
            f"the discussed approach may be beneficial. "
            f"The evidence indicates positive health effects "
            f"related to the user's question: {question}."
        )


        confidence = "High"


    elif caution_count > support_count:

        recommendation = (
            f"The available evidence suggests caution "
            f"regarding this topic for {condition}. "
            f"Further medical guidance may be required "
            f"before making decisions."
        )

        confidence = "Medium"


    else:

        recommendation = (
            f"Evidence was found for {condition}, but "
            f"the available information is not strong enough "
            f"to provide a clear recommendation."
        )

        confidence = "Low"



    return {
        "condition": condition,
        "question": question,
        "recommendation": recommendation,
        "confidence": confidence
    }



# Testing

if __name__ == "__main__":


    sample_evidence = [

        {
            "source": "NCBI",
            "evidence":
            "Exercise can improve physical performance "
            "and quality of life."
        },

        {
            "source": "WHO",
            "evidence":
            "Regular physical activity is recommended "
            "for better health outcomes."
        }

    ]


    result = generate_recommendation(
        "COPD",
        "Can I exercise?",
        sample_evidence
    )


    print("Recommendation:")
    print(result["recommendation"])

    print("\nConfidence:")
    print(result["confidence"])
