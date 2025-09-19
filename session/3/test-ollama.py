#!/usr/bin/env python3
"""
Simple Ollama Connection Test
Tests if Ollama is running and accessible on the local network
"""

import requests
import json
import sys

# Default Ollama API endpoint
OLLAMA_BASE_URL = "http://localhost:11434"

def test_ollama_connection():
    """Test if Ollama is running and accessible"""
    print("🔍 Testing Ollama connection...")

    try:
        # Test basic connection
        response = requests.get(f"{OLLAMA_BASE_URL}/api/version", timeout=5)

        if response.status_code == 200:
            print("✅ Ollama is running!")
            version_info = response.json()
            print(f"📋 Version: {version_info.get('version', 'Unknown')}")
            return True
        else:
            print(f"❌ Ollama responded with status code: {response.status_code}")
            return False

    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Ollama. Is it running on localhost:11434?")
        return False
    except requests.exceptions.Timeout:
        print("❌ Connection timeout. Ollama might be slow to respond.")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def list_available_models():
    """List available models in Ollama"""
    print("\n🤖 Checking available models...")

    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=10)

        if response.status_code == 200:
            models = response.json()
            if models.get('models'):
                print("📚 Available models:")
                for model in models['models']:
                    print(f"   • {model['name']}")
                return models['models']
            else:
                print("⚠️  No models found. You may need to pull a model first.")
                print("   Try: ollama pull llama3.1:8b")
                return []
        else:
            print(f"❌ Failed to get models: {response.status_code}")
            return []

    except Exception as e:
        print(f"❌ Error getting models: {e}")
        return []

def test_simple_generation(model_name="llama3.1:8b"):
    """Test story generation"""
    print(f"\n🎯 Testing story generation with {model_name}...")

    try:
        payload = {
            "model": model_name,
            "prompt": "Tell me a short story about a brave knight and a dragon in 2-3 paragraphs.",
            "stream": False
        }

        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json=payload,
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()
            generated_text = result.get('response', '').strip()
            print(f"✅ Generation successful!")
            print(f"🗨️  Response: {generated_text}")
            return True
        else:
            print(f"❌ Generation failed: {response.status_code}")
            return False

    except Exception as e:
        print(f"❌ Error during generation: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Ollama Connection Test Starting...")
    print("=" * 50)

    # Test connection
    if not test_ollama_connection():
        print("\n💡 Make sure Ollama is installed and running:")
        print("   • Install: https://ollama.ai/")
        print("   • Start: ollama serve")
        sys.exit(1)

    # List models
    models = list_available_models()

    # Test generation if models are available
    if models:
        test_simple_generation()
    else:
        print("\n⚠️  Skipping generation test - no models available")
        print("   To install a model: ollama pull llama2")

    print("\n" + "=" * 50)
    print("🎉 Ollama test completed!")

if __name__ == "__main__":
    main()