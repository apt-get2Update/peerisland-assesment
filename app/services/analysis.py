# services/analysis.py
import json
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def analyze_code_chunks(code_chunks, language, llm):
    """Analyze code chunks using LLM"""
    analysis_results = []
    overview_prompt = PromptTemplate(
        input_variables=["code", "language"],
        template="""
        Analyze the following {language} code and provide:
        1. A brief description of its purpose
        2. Key functions/methods with their signatures
        3. Any notable patterns or architecture

        Code:
        {code}

        Respond in JSON format with this structure:
        {{
            "description": "string",
            "methods": [
                {{
                    "name": "string",
                    "signature": "string",
                    "purpose": "string"
                }}
            ],
            "patterns": "string"
        }}
        """
    )
    chain = LLMChain(llm=llm, prompt=overview_prompt)
    for chunk in code_chunks:
        try:
            result = chain.run(code=chunk, language=language)
            analysis_results.append(json.loads(result))
        except Exception as e:
            print(f"Error analyzing chunk: {e}")
            continue
    return analysis_results

def generate_final_report(partial_analyses, language, llm):
    """Combine partial analyses into a final report"""
    combined_prompt = PromptTemplate(
        input_variables=["analyses", "language"],
        template="""
        Combine the following partial analyses of a {language} codebase into a comprehensive report.
        Provide a structured JSON output with:
        1. High-level project overview
        2. Key components/modules
        3. Complexity assessment
        4. Notable patterns and architecture
        
        Partial Analyses:
        {analyses}
        
        Respond in JSON format with this structure:
        {{
            "overview": "string",
            "keyComponents": [
                {{
                    "name": "string",
                    "description": "string",
                    "methods": [
                        {{
                            "signature": "string",
                            "description": "string"
                        }}
                    ]
                }}
            ],
            "complexity": {{
                "overall": "low/medium/high",
                "factors": ["string"]
            }},
            "architecture": "string"
        }}
        """
    )
    chain = LLMChain(llm=llm, prompt=combined_prompt)
    result = chain.run(analyses=json.dumps(partial_analyses), language=language)
    return json.loads(result)
