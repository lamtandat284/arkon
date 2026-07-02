"""Ollama local provider for LLM and Embedding."""
from typing import Optional
from app.ai.providers.base import EmbeddingProvider, LLMProvider, ProviderConfig
import httpx

class OllamaEmbedding(EmbeddingProvider):
    def __init__(self, config: ProviderConfig):
        super().__init__(config)
        self.base_url = config.base_url or "http://localhost:11434"

    async def embed(self, text: str) -> list[float]:
        async with httpx.AsyncClient() as client:
            r = await client.post(f"{self.base_url}/api/embeddings",
                json={"model": self.config.model_id, "prompt": text}, timeout=60)
            r.raise_for_status()
            return r.json()["embedding"]

    async def embed_batch(self, texts: list[str], concurrency: int = 5) -> list[list[float]]:
        results = []
        for text in texts:
            results.append(await self.embed(text))
        return results

    async def test_connection(self) -> tuple[bool, str]:
        try:
            await self.embed("test")
            return True, "Ollama embedding OK"
        except Exception as e:
            return False, str(e)

class OllamaLLM(LLMProvider):
    def __init__(self, config: ProviderConfig):
        super().__init__(config)
        self.base_url = config.base_url or "http://localhost:11434"

    async def generate(self, prompt: str, system: Optional[str] = None,
                       max_tokens: Optional[int] = None, temperature: float = 0.7) -> str:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        async with httpx.AsyncClient() as client:
            r = await client.post(f"{self.base_url}/api/chat",
                json={"model": self.config.model_id, "messages": messages, "stream": False},
                timeout=120)
            r.raise_for_status()
            return r.json()["message"]["content"]

    async def test_connection(self) -> tuple[bool, str]:
        try:
            await self.generate("ping")
            return True, "Ollama LLM OK"
        except Exception as e:
            return False, str(e)
