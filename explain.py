def generate_explanation(recommendation_result, evidence):

    sources = []

    for item in evidence:
        sources.append(item["source"])


    unique_sources = list(set(sources))


    evidence_count = len(evidence)


    explanation = (
        f"The conclusion was generated using "
        f"{evidence_count} pieces of medical evidence "
        f"from trusted sources.\n\n"
        f"Sources considered:\n"
    )


    for source in unique_sources:
        explanation += f"- {source}\n"


    if recommendation_result["confidence"] == "High":

        explanation += (
            "\nConfidence is High because multiple "
            "sources contained supporting medical evidence."
        )


    elif recommendation_result["confidence"] == "Medium":

        explanation += (
            "\nConfidence is Medium because some evidence "
            "supports the conclusion but limitations exist."
        )


    else:

        explanation += (
            "\nConfidence is Low because available evidence "
            "was insufficient."
        )


    return explanation



if __name__ == "__main__":


    recommendation = {

        "recommendation":
        "Exercise may be beneficial for COPD patients.",

        "confidence":
        "High"
    }


    evidence = [

        {
            "source": "NCBI",
            "evidence":
            "Exercise improves quality of life."
        },

        {
            "source": "PMC",
            "evidence":
            "Pulmonary rehabilitation improves exercise tolerance."
        }

    ]


    result = generate_explanation(
        recommendation,
        evidence
    )


    print(result)