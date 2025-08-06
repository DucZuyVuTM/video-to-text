import whisper
import moviepy.editor as mp  # Version 1.0.3

import curses
from CLI import options, select_language

def extract_audio(video_path, audio_path):
    clip = mp.VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)

def transcribe_audio(audio_path, language="ru"):
    model = whisper.load_model("medium")  # Hoặc "small", "large" nếu cần
    result = model.transcribe(audio_path, language=language)
    return result["text"]

def main():
    lang = curses.wrapper(select_language)

    if lang == "Other":
        lang = input("Enter your language code (e.g. en, fr, es, etc.)")

    if lang == "Exit":
        print("Exited\n")
        return

    video_path = "./input_video.mp4"  # Đổi thành đường dẫn video của bạn
    audio_path = "./output_audio.wav"
    
    print("🔄 Đang trích xuất âm thanh từ video...")
    extract_audio(video_path, audio_path)
    
    print("📝 Đang nhận diện giọng nói...")
    transcript = transcribe_audio(audio_path)
    
    with open("output_text.txt", "w", encoding="utf-8") as f:
        f.write(transcript)

    print("📜 Văn bản đã được nhận!")

if __name__ == "__main__":
    main()
