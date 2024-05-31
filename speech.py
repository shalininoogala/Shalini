import whisper
 
def load_whisper_model(model_name='base'):
    model = whisper.load_model(model_name)
    return model
 
def transcribe_audio(model, audio_path):
    result = model.transcribe(audio_path)
    return result['text']
 
def main(audio_path, model_name='base'):
    model = load_whisper_model(model_name)
    transcription = transcribe_audio(model, audio_path)
    print(transcription)
 
if __name__ == "__main__":
    audio_file_path ='https://content.libsyn.com/p/c/6/4/c645e2d2b61f34bd/PodcastReturns.mp3?c_id=4336104&cs_id=4336104&response-content-type=audio%2Fmpeg&Expires=1717129077&Signature=FUYFD7Lq71pteJhkVS2QVqlsJqqpfgq2k0uGnbkYWEyptj06EUl2-O4fJ2BNLlAjUjAYGB7sltDLACHt7uP7FnR5sB4GnfhxoxCCZqJsZFRHZEB1pi3iLOQ4svGi4JNJrIZJskNgmobjStE6CHyPP4wS3DUYAQ809cAXv01H~YZO6rUn6tckNndujQASJJh6WmU9nT5AjM2TAyNz0BVdaITAqMk6i8lxBCWFE3fu-O7SAFwG6fZFB83w9blOkZwEcXqt5EalmGMLugMfqX8Bl11kRXzZZgp5NKHWJmK15zwPOiQ06IGWUXKcYrIIRcNuWdkomARzs9nIsPuho-U7-A__&Key-Pair-Id=K1YS7LZGUP96OI'

    main(audio_file_path)
    