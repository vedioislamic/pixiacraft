#!/bin/bash
echo "🔥 Starting backend..."
source venv/bin/activate

# Run FastAPI app (update 'main:app' if your file is different)
nohup uvicorn main:app --host 0.0.0.0 --port 7860 &

# Start ngrok
echo "🌐 Starting ngrok..."
ngrok config add-authtoken 30jU5V0H6Uku3vFQUxFAfUwgums_6nwttNKyscyowKpyf7hz4
nohup ngrok http 7860 > /dev/null &

# Wait for ngrok to start and get public URL
sleep 5
curl http://127.0.0.1:4040/api/tunnels > tunnels.json
PUBLIC_URL=$(cat tunnels.json | grep -o 'https://[0-9a-z]*\.ngrok-free\.app')
echo "✅ Ngrok Public URL: $PUBLIC_URL"

# Optional: Send URL to your Firebase or backend
# curl -X POST -H "Content-Type: application/json" -d '{"url": "'"$PUBLIC_URL"'"}' https://your-backend.com/update-url