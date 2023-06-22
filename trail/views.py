from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
import os,shutil
from pydub import AudioSegment
import sounddevice as sd
from scipy.io.wavfile import write,read
from django.contrib import messages
from .models import file
import os.path
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import os
from pydub.utils import make_chunks

def upload(request):
    if request.method == 'POST':
        context ={}
        doc = request.FILES
        uploaded_file = doc['d']
        name = uploaded_file.name
        if name.endswith(".mp3") or name.endswith('wav') or name.endswith('.mp4') or name.endswith('.m4a'):
            try:
                os.unlink(os.path.join(os.getcwd(),'media',"a.mp3"))
            except:
                print("No mp3 file in media directory")

            try:
                os.unlink('a.mp3')
            except:
                print("No mp3 file in media directory")
            try:
                os.unlink(os.path.join(os.getcwd(),'media',"combined.wav"))
            except:
                print("No file in media directory")

            fs = FileSystemStorage()
            nn = fs.save('a.mp3',uploaded_file)
            try:
                shutil.copy(os.path.join(os.getcwd(),'media',"a.mp3"), os.getcwd())
            except:
                print("Unable to copy")
            context['url'] = fs.url(nn)

            import subprocess

            cmd = ["python3", "-m", "spleeter", "separate", "a.mp3", "-o", "media/"]
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            except subprocess.CalledProcessError as e:
                print("Command returned non-zero exit status", e.returncode)
                print("Error output:\n", e.stderr)
            else:
                print("Command executed successfully.")
            
            return render(request,'show.html',context)
        else:
            print("Upload only .mp3 or .wav files")
    return render(request,'upload.html');


def combine(request):
    if request.method == 'POST':
        context = {}
        doc = request.FILES
        uploaded_file = doc['d']
        name = uploaded_file.name
        if name.endswith(".mp4") or name.endswith('wav') or name.endswith('.mp3'):
            try:
                os.unlink(os.path.join(os.getcwd(), 'media', "combined.wav"))
            except:
                print("No file in media directory")
            try:
                os.unlink(os.path.join(os.getcwd(), 'media', "sing.wav"))
            except:
                print("No file in media directory")

            fs = FileSystemStorage()
            nn = fs.save('sing.wav', uploaded_file)

            context['url'] = fs.url(nn)
            try:
                vocals = AudioSegment.from_file(os.path.join(os.getcwd(), "media", "a", "vocals.wav"))
                music = AudioSegment.from_file(os.path.join(os.getcwd(), "media", "sing.wav"))

                duration_music = len(music)
                duration_vocals = len(vocals)

                # Determine the longer audio and adjust the shorter one to match its duration
                if duration_music < duration_vocals:
                    repeat_times = int(duration_vocals / duration_music) + 1
                    music = music * repeat_times
                else:
                    repeat_times = int(duration_music / duration_vocals) + 1
                    vocals = vocals * repeat_times

                # Apply fade-in and fade-out effects to music and vocals
                fade_in_duration = 5000  # Fade-in duration in milliseconds
                fade_out_duration = 5000  # Fade-out duration in milliseconds

                music = music.fade_in(fade_in_duration).fade_out(fade_out_duration)
                vocals = vocals.fade_in(fade_in_duration).fade_out(fade_out_duration)

                # Adjust the volume of the music track
                music = music - 15  # Reduce the volume by 20 dB (adjust as needed)

                # Determine the length of the final combined audio
                combined_duration = max(len(music), len(vocals))

                # Adjust the vocal track to match the combined duration
                vocals = vocals[:combined_duration]

                # Combine the music and vocals
                combined = music.overlay(vocals)

                combined.export(os.path.join(os.getcwd(), "media", "combined.wav"), format='wav')

            except Exception as e:
                print("Problem in combining:", str(e))
            return render(request, 'combined.html', context)
        else:
            print("Upload only .mp3 or .wav files")
    return render(request, 'show.html')
