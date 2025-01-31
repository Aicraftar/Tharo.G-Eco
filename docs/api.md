📚 API Endpoints
📜 Retrieve All Models
Endpoint: GET /api/models

Description: Fetches all models created or added via the Aicraftar WebUI.

curl -H "Authorization: Bearer YOUR_API_KEY" https://aicraftar.com/api/models
💬 Chat Completions
Endpoint: POST /api/chat/completions

Description: OpenAI API-compatible chat completion for Aicraftar models.

curl -X POST https://aicraftar.com/api/chat/completions \
-H "Authorization: Bearer YOUR_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "model": "Tharo.G-Neo:latest",
  "messages": [
    { "role": "user", "content": "What is the capital of France?" }
  ]
}'
🧩 Retrieval Augmented Generation (RAG)
Enhance chat applications using external knowledge via files or collections.

Using Files Individually
Endpoint: POST /api/chat/completions

curl -X POST https://aicraftar.com/api/chat/completions \
-H "Authorization: Bearer YOUR_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "model": "Tharo.G-Neo:latest",
  "messages": [
    { "role": "user", "content": "What is the capital of France?" }
  ],
  "files": [
    { "type": "file", "id": "your-file-id" }
  ]
}'
Using Knowledge Collections
Endpoint: POST /api/chat/completions

curl -X POST https://aicraftar.com/api/chat/completions \
-H "Authorization: Bearer YOUR_API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "model": "Tharo.G-Neo:latest",
  "messages": [
    { "role": "user", "content": "Provide insights on the historical perspectives covered in the collection." }
  ],
  "files": [
    { "type": "collection", "id": "your-collection-id" }
  ]
}'
🤖 Available Models
Embedding Model
Model Name: Tharo.G-Embeding-v1:latest
LLM Models
Tharo.G-Aura:latest
Tharo.G-Echo-V2:latest
Tharo.G-Graxo:latest
Tharo.G-Echo:latest
Tharo.G-Neo:latest