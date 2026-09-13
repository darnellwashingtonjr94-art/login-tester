import google.generativeai as genai

def analyze_threat_data(config, logs):
    api_key = config.get("ai_config", {}).get("gemini_api_key")
    genai.configure(api_key=api_key)
    
    model = genai.GenerativeModel(config["ai_config"]["model_version"])
    prompt = f"Analyze the following security logs and captured honeypot data for attack patterns, origins, and intent. Provide a structured threat report:\n\n{logs}"
    
    try:
        response = model.generate_content(prompt)
        print("Gemini Analysis Complete:")
        print(response.text)
        return response.text
    except Exception as e:
        print(f"AI Analysis Failed: {e}")
        return None
