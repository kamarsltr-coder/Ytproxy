from flask import Flask, request, redirect
import yt_dlp

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ YouTube Proxy Aktif! Gunakan format: /stream?url=<link_youtube>"

@app.route('/stream')
def stream():
    url = request.args.get("url")
    if not url:
        return "❌ Parameter 'url' belum diisi", 400

    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'format': 'best',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            m3u8 = info.get("url")
            return redirect(m3u8, code=302)
    except Exception as e:
        return f"⚠️ Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
