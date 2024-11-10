import aiohttp
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_API_TOKEN")

async def get_gemini_response(query):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": query
                    }
                ]
            }
        ]
    }

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={GEMINI_API_KEY}"

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            result = await response.json()

            if response.status == 200:
                if "candidates" in result:

                    generated_text = result["candidates"][0]["content"]["parts"][0]["text"].strip()
                    return generated_text
                else:

                    error_message = f"Respuesta inesperada: {result}"
                    return error_message
            else:

                error_message = result.get("error", {}).get("message", "Error desconocido en la API de Google Gemini")
                return f"Error HTTP: {response.status}, Mensaje: {error_message}"

import asyncio

query = "Explain how AI works"

async def main():
    response = await get_gemini_response(query)
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
