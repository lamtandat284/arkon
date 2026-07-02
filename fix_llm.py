content = open('/app/app/ai/llm_catalog.py', 'r').read()
new_entry = '''
    # --- Ollama (Local) ---
    "ollama/llama3": LLMModelSpec(
        id="ollama/llama3",
        provider="ollama",
        model_id="llama3",
        context_window_tokens=128_000,
        max_output_tokens=8_000,
        supports_tools=True,
        supports_vision=False,
        label="Llama 3 (Local)",
        cost_per_1m_input_tokens=0.0,
        cost_per_1m_output_tokens=0.0,
        notes="Local Ollama model. Free, no API key required.",
    ),
'''
content = content.replace('    # --- OpenAI ---', new_entry + '    # --- OpenAI ---')
open('/app/app/ai/llm_catalog.py', 'w').write(content)
print('Done')
