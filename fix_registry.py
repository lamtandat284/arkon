content = open('/app/app/ai/registry.py', 'r').read()
content = content.replace(
    '    elif provider == ProviderType.OPENAI:\n        from app.ai.providers.openai_provider import OpenAIEmbedding\n        return OpenAIEmbedding\n    raise ValueError(f"Unsupported embedding provider: {provider}")',
    '    elif provider == ProviderType.OPENAI:\n        from app.ai.providers.openai_provider import OpenAIEmbedding\n        return OpenAIEmbedding\n    elif provider == ProviderType.OLLAMA:\n        from app.ai.providers.ollama_provider import OllamaEmbedding\n        return OllamaEmbedding\n    raise ValueError(f"Unsupported embedding provider: {provider}")'
).replace(
    '    elif provider == ProviderType.ANTHROPIC:\n        from app.ai.providers.anthropic_provider import AnthropicLLM\n        return AnthropicLLM\n    raise ValueError(f"Unsupported LLM provider: {provider}")',
    '    elif provider == ProviderType.ANTHROPIC:\n        from app.ai.providers.anthropic_provider import AnthropicLLM\n        return AnthropicLLM\n    elif provider == ProviderType.OLLAMA:\n        from app.ai.providers.ollama_provider import OllamaLLM\n        return OllamaLLM\n    raise ValueError(f"Unsupported LLM provider: {provider}")'
)
open('/app/app/ai/registry.py', 'w').write(content)
print('Done')
