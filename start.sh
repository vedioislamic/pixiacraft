echo "🔥 Starting backend..."
source venv/bin/activate

cd /workspace/pixiacraft

nohup uvicorn main:app --host 0.0.0.0 --port 7860 &

echo "🌐 Starting ngrok..."
ngrok config add-authtoken 30jU5V0H6Uku3vFQUxFAfUwgums_6nwttNKyscyowKpyf7hz4
nohup ngrok http 7860 > /dev/null &

sleep 5
curl http://127.0.0.1:4040/api/tunnels > tunnels.json
PUBLIC_URL=$(cat tunnels.json | grep -o 'https://[0-9a-z]*\.ngrok-free\.app')
echo "✅ Ngrok Public URL: $PUBLIC_URL"