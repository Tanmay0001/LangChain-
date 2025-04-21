import json
from langchain_core.prompts import PromptTemplate

# Define the prompt template as a string
template_str = """
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}
1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies:
   - Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length.
"""

# Create the prompt template object
prompt = PromptTemplate(input_variables=['paper_input', 'style_input', 'length_input'], template=template_str)

# Save the prompt as a JSON file manually
with open('template.json', 'w') as f:
    json.dump({
        'input_variables': prompt.input_variables,
        'template': prompt.template
    }, f, indent=4)
