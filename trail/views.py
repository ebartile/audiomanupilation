from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pydub import AudioSegment
import os
from pydub import AudioSegment
from pydub.effects import normalize
from .models import AudioSettings
import subprocess
from pydub.silence import detect_silence
import pyrubberband as pyrb
import soundfile as sf

@csrf_exempt
def upload_tracktwo_edit(request):
    if request.method == 'POST':

        # Extract audio properties using PyDub
        filename = request.POST.get('filename')
        path = os.path.join(settings.MEDIA_ROOT, filename)
        audio = AudioSegment.from_file(path)
        url = request.build_absolute_uri(settings.MEDIA_URL + filename)

        if request.POST.get('track-two-noise-separator-checkbox'):
            # Prepare edited audio file with new filename
            filename = os.path.splitext(filename)[0]
            cmd = ["python3", "-m", "spleeter", "separate", path, "-o", "media/", "-f", "{filename}_{instrument}.{codec}"]
            filename = filename + "_accompaniment.wav"
            try:
                subprocess.run(cmd, capture_output=True, text=True, check=True)
            except subprocess.CalledProcessError as e:
                print("Command returned non-zero exit status", e.returncode)
                print("Error output:\n", e.stderr)
            else:
                print("Command executed successfully.")

                path = os.path.join(settings.MEDIA_ROOT, filename)
                url = request.build_absolute_uri(settings.MEDIA_URL + filename)

        # Extract edited audio properties using PyDub
        audio = AudioSegment.from_file(path)

        if request.POST.get('slice-trim-two-checkbox'):
            # Slicing and trimming
            slice_start = float(request.POST.get('slice-start-track-two', 0))
            slice_end = float(request.POST.get('slice-end-track-two', audio.duration_seconds * 1000)) * 1000
            audio = audio[slice_start * 1000:slice_end]

            # Prepare edited audio file with new filename
            filename = os.path.splitext(filename)[0]
            if "edited_" in filename:
                filename = filename + '.wav'
            else:
                filename = "edited_" + filename + '.wav'
            path = os.path.join(settings.MEDIA_ROOT, filename)
            url = request.build_absolute_uri(settings.MEDIA_URL + filename)

            # Export the edited audio file
            audio.export(path, format='wav')

        # Extract edited audio properties using PyDub
        audio = AudioSegment.from_file(path)

        if request.POST.get('track-two-sample-rate-checkbox'):
            sample_rate = int(request.POST.get('track-two-sample-rate', 44100))
            channels = int(request.POST.get('track-two-channels', 1))

            # Prepare edited audio file with new filename
            filename = os.path.splitext(filename)[0]
            if "edited_" in filename:
                filename = filename + '.wav'
            else:
                filename = "edited_" + filename + '.wav'
            path = os.path.join(settings.MEDIA_ROOT, filename)
            url = request.build_absolute_uri(settings.MEDIA_URL + filename)

            audio = audio.set_frame_rate(sample_rate)
            audio = audio.set_channels(channels)

            # Export the edited audio file
            audio.export(path, format='wav')

        # Extract edited audio properties using PyDub
        audio = AudioSegment.from_file(path)

        if float(request.POST.get('track-two-tempo')) != 1.0:
            # Prepare edited audio file with new filename
            filename = os.path.splitext(filename)[0]
            if "edited_" in filename:
                filename = filename + '.wav'
            else:
                filename = "edited_" + filename + '.wav'
            path = os.path.join(settings.MEDIA_ROOT, filename)
            # Export the edited audio file
            audio.export(path, format='wav')

            data, samplerate = sf.read(path)

            # Apply time stretching to adjust the tempo without affecting pitch
            audio = pyrb.time_stretch(data, samplerate, float(request.POST.get('track-two-tempo')))
            url = request.build_absolute_uri(settings.MEDIA_URL + filename)

            # Export the edited audio file
            sf.write(path, audio, samplerate, format='wav')

        # Extract edited audio properties using PyDub
        audio = AudioSegment.from_file(path)

        if float(request.POST.get('track-two-pitch')) != 1.0:
            # Prepare edited audio file with new filename
            filename = os.path.splitext(filename)[0]
            if "edited_" in filename:
                filename = filename + '.wav'
            else:
                filename = "edited_" + filename + '.wav'
            path = os.path.join(settings.MEDIA_ROOT, filename)
            # Export the edited audio file
            audio.export(path, format='wav')

            data, samplerate = sf.read(path)

            # Apply time stretching to adjust the pitch without affecting tempo
            audio = pyrb.pitch_shift(data, samplerate, float(request.POST.get('track-two-pitch')))
            url = request.build_absolute_uri(settings.MEDIA_URL + filename)

            # Export the edited audio file
            sf.write(path, audio, samplerate, format='wav')

        # Extract edited audio properties using PyDub
        audio = AudioSegment.from_file(path)

        properties = {
            'name': filename,
            'sampleRate': audio.frame_rate,
            'numChannels': audio.channels,
            'numSamples': audio.frame_count(),
            'duration': int(audio.duration_seconds),
            'fileUrl': url
        }

        # Return edited audio properties as JSON response
        return JsonResponse({'success': True, 'data': properties})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

@csrf_exempt
def upload_trackone_edit(request):
    if request.method == 'POST':

        # Extract audio properties using PyDub
        filename = request.POST.get('filename')
        path = os.path.join(settings.MEDIA_ROOT, filename)
        audio = AudioSegment.from_file(path)
        url = request.build_absolute_uri(settings.MEDIA_URL + filename)

        if request.POST.get('track-one-noise-separator-checkbox'):
            # Prepare edited audio file with new filename
            filename = os.path.splitext(filename)[0]
            cmd = ["python3", "-m", "spleeter", "separate", path, "-o", "media/", "-f", "{filename}_{instrument}.{codec}"]
            filename = filename + "_vocals.wav"
            try:
                subprocess.run(cmd, capture_output=True, text=True, check=True)
            except subprocess.CalledProcessError as e:
                print("Command returned non-zero exit status", e.returncode)
                print("Error output:\n", e.stderr)
            else:
                print("Command executed successfully.")

                path = os.path.join(settings.MEDIA_ROOT, filename)
                url = request.build_absolute_uri(settings.MEDIA_URL + filename)

        # Extract edited audio properties using PyDub
        audio = AudioSegment.from_file(path)

        if request.POST.get('slice-trim-checkbox'):
            # Slicing and trimming
            slice_start = float(request.POST.get('slice-start-track-one', 0))
            slice_end = float(request.POST.get('slice-end-track-one', audio.duration_seconds * 1000)) * 1000
            audio = audio[slice_start * 1000:slice_end]

            # Prepare edited audio file with new filename
            filename = os.path.splitext(filename)[0]
            if "edited_" in filename:
                filename = filename + '.wav'
            else:
                filename = "edited_" + filename + '.wav'
            path = os.path.join(settings.MEDIA_ROOT, filename)
            url = request.build_absolute_uri(settings.MEDIA_URL + filename)

            # Export the edited audio file
            audio.export(path, format='wav')

        # Extract edited audio properties using PyDub
        audio = AudioSegment.from_file(path)

        if request.POST.get('track-sample-rate-checkbox'):
            sample_rate = int(request.POST.get('track-sample-rate', 44100))
            channels = int(request.POST.get('track-channels', 1))

            # Prepare edited audio file with new filename
            filename = os.path.splitext(filename)[0]
            if "edited_" in filename:
                filename = filename + '.wav'
            else:
                filename = "edited_" + filename + '.wav'
            path = os.path.join(settings.MEDIA_ROOT, filename)
            url = request.build_absolute_uri(settings.MEDIA_URL + filename)

            audio = audio.set_frame_rate(sample_rate)
            audio = audio.set_channels(channels)

            # Export the edited audio file
            audio.export(path, format='wav')

        # Extract edited audio properties using PyDub
        audio = AudioSegment.from_file(path)

        if float(request.POST.get('track-one-tempo')) != 1.0:
            # Prepare edited audio file with new filename
            filename = os.path.splitext(filename)[0]
            if "edited_" in filename:
                filename = filename + '.wav'
            else:
                filename = "edited_" + filename + '.wav'
            path = os.path.join(settings.MEDIA_ROOT, filename)
            # Export the edited audio file
            audio.export(path, format='wav')

            data, samplerate = sf.read(path)

            # Apply time stretching to adjust the tempo without affecting pitch
            audio = pyrb.time_stretch(data, samplerate, float(request.POST.get('track-one-tempo')))
            url = request.build_absolute_uri(settings.MEDIA_URL + filename)

            # Export the edited audio file
            sf.write(path, audio, samplerate, format='wav')

        # Extract edited audio properties using PyDub
        audio = AudioSegment.from_file(path)

        if float(request.POST.get('track-one-pitch')) != 1.0:
            # Prepare edited audio file with new filename
            filename = os.path.splitext(filename)[0]
            if "edited_" in filename:
                filename = filename + '.wav'
            else:
                filename = "edited_" + filename + '.wav'
            path = os.path.join(settings.MEDIA_ROOT, filename)
            # Export the edited audio file
            audio.export(path, format='wav')

            data, samplerate = sf.read(path)

            # Apply time stretching to adjust the pitch without affecting tempo
            audio = pyrb.pitch_shift(data, samplerate, float(request.POST.get('track-one-pitch')))
            url = request.build_absolute_uri(settings.MEDIA_URL + filename)

            # Export the edited audio file
            sf.write(path, audio, samplerate, format='wav')

        # Extract edited audio properties using PyDub
        audio = AudioSegment.from_file(path)

        properties = {
            'name': filename,
            'sampleRate': audio.frame_rate,
            'numChannels': audio.channels,
            'numSamples': audio.frame_count(),
            'duration': int(audio.duration_seconds),
            'fileUrl': url
        }

        # Return edited audio properties as JSON response
        return JsonResponse({'success': True, 'data': properties})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

@csrf_exempt
def upload_trackone(request):
    if request.method == 'POST' and request.FILES.get('file'):
        audio_file = request.FILES['file']

        # Generate a unique filename
        file_extension = os.path.splitext(audio_file.name)[1]
        filename = "trackone" + file_extension

        # Save the audio file to the media directory with the new filename
        path = os.path.join(settings.MEDIA_ROOT, filename)
        with open(path, 'wb') as f:
            for chunk in audio_file.chunks():
                f.write(chunk)

        audio = AudioSegment.from_file(os.path.join(settings.MEDIA_ROOT, filename))
        url = request.build_absolute_uri(settings.MEDIA_URL + filename)

        setting = AudioSettings.objects.first()

        if setting.silence_detection:
            # Detect silence segments
            silence_segments = detect_silence(audio, setting.min_silence_duration, setting.silence_threshold)

            # Print the detected silence segments
            for segment in silence_segments:
                start_time, end_time = segment
                audio = audio[:start_time] + audio[end_time:]
                print("Silence detected from {} ms to {} ms".format(segment[0], segment[1]))

            # Prepare edited audio file with new filename
            filename = os.path.splitext(filename)[0]
            filename = "edited_" + filename + '.wav'
            path = os.path.join(settings.MEDIA_ROOT, filename)
            url = request.build_absolute_uri(settings.MEDIA_URL + filename)

            # Export the edited audio file
            audio.export(path, format='wav')

        # Reverb the track
        if setting and setting.reverb_trackone:
            # Prepare edited audio file with new filename
            cmd = [
                "ffmpeg",
                "-y",
                "-i",
                os.path.join("media", filename),
                "-af",
                "aecho=0.8:0.9:1000|500:0.3|0.2",
                os.path.join("media", "edited_" + os.path.splitext(filename)[0] + '.wav')
            ]
            # Prepare edited audio file with new filename
            filename = os.path.splitext(filename)[0]
            filename = "edited_" + filename + '.wav'
            path = os.path.join(settings.MEDIA_ROOT, filename)
            url = request.build_absolute_uri(settings.MEDIA_URL + filename)
            try:
                subprocess.run(cmd, capture_output=True, text=True, check=True)
            except subprocess.CalledProcessError as e:
                print("Command returned non-zero exit status", e.returncode)
                print("Error output:\n", e.stderr)
            else:
                print("Command executed successfully.")
        # Extract edited audio properties using PyDub
        audio = AudioSegment.from_file(path)

        properties = {
            'name': filename,
            'sampleRate': audio.frame_rate,
            'numChannels': audio.channels,
            'numSamples': audio.frame_count(),
            'duration': int(audio.duration_seconds),
            'fileUrl': url
        }

        # Return edited audio properties as JSON response
        return JsonResponse({'success': True, 'data': properties})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

@csrf_exempt
def upload_tracktwo(request):
    if request.method == 'POST' and request.FILES.get('file'):
        audio_file = request.FILES['file']

        # Generate a unique filename
        file_extension = os.path.splitext(audio_file.name)[1]
        filename = "tracktwo" + file_extension

        # Save the audio file to the media directory with the new filename
        path = os.path.join(settings.MEDIA_ROOT, filename)
        with open(path, 'wb') as f:
            for chunk in audio_file.chunks():
                f.write(chunk)

        audio = AudioSegment.from_file(os.path.join(settings.MEDIA_ROOT, filename))
        url = request.build_absolute_uri(settings.MEDIA_URL + filename)

        setting = AudioSettings.objects.first()

        if setting.silence_detection:
            # Detect silence segments
            silence_segments = detect_silence(audio, setting.min_silence_duration, setting.silence_threshold)

            # Print the detected silence segments
            for segment in silence_segments:
                start_time, end_time = segment
                audio = audio[:start_time] + audio[end_time:]
                print("Silence detected from {} ms to {} ms".format(segment[0], segment[1]))

            # Prepare edited audio file with new filename
            filename = os.path.splitext(filename)[0]
            filename = "edited_" + filename + '.wav'
            path = os.path.join(settings.MEDIA_ROOT, filename)
            url = request.build_absolute_uri(settings.MEDIA_URL + filename)

            # Export the edited audio file
            audio.export(path, format='wav')

        # Reverb the track
        if setting and setting.reverb_tracktwo:
            # Prepare edited audio file with new filename
            cmd = [
                "ffmpeg",
                "-y",
                "-i",
                os.path.join("media", filename),
                "-af",
                "aecho=0.8:0.9:1000|500:0.3|0.2",
                os.path.join("media", "edited_" + os.path.splitext(filename)[0] + '.wav')
            ]
            # Prepare edited audio file with new filename
            filename = os.path.splitext(filename)[0]
            filename = "edited_" + filename + '.wav'
            path = os.path.join(settings.MEDIA_ROOT, filename)
            url = request.build_absolute_uri(settings.MEDIA_URL + filename)
            try:
                subprocess.run(cmd, capture_output=True, text=True, check=True)
            except subprocess.CalledProcessError as e:
                print("Command returned non-zero exit status", e.returncode)
                print("Error output:\n", e.stderr)
            else:
                print("Command executed successfully.")

        # Extract edited audio properties using PyDub
        audio = AudioSegment.from_file(path)

        properties = {
            'name': filename,
            'sampleRate': audio.frame_rate,
            'numChannels': audio.channels,
            'numSamples': audio.frame_count(),
            'duration': int(audio.duration_seconds),
            'fileUrl': url
        }

        # Return edited audio properties as JSON response
        return JsonResponse({'success': True, 'data': properties})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

@csrf_exempt
def finalize_track_edit(request):
    if request.method == 'POST':

        # Extract audio properties using PyDub
        trackone = request.POST.get('trackone')
        tracktwo = request.POST.get('tracktwo')
        trackone_path = os.path.join(settings.MEDIA_ROOT, trackone)
        tracktwo_path = os.path.join(settings.MEDIA_ROOT, tracktwo)
        trackone_audio = AudioSegment.from_file(trackone_path)
        tracktwo_audio = AudioSegment.from_file(tracktwo_path)
        filename = "final_audio." + request.POST.get("output-format")
        path = os.path.join(settings.MEDIA_ROOT, filename)

        setting = AudioSettings.objects.first()

        # Define the panning range (between -1.0 and 1.0)
        panning_value = float(request.POST.get('panoramic-range'))

        if request.POST.get('concatenation-format') == "overlay":
            if request.POST.get('concatenation-loop') == '1':
                # Calculate the number of repetitions required
                repetitions = int(tracktwo_audio.duration_seconds / trackone_audio.duration_seconds) + 1
                # Create the looped version of the shorter track
                trackone_audio = trackone_audio * repetitions
                # Overlay the section on top of the base audio

                if request.POST.get('track-volume-checkbox'):
                    trackone_audio = trackone_audio + request.POST.get('track-volume', 0)

                if request.POST.get('track-two-volume-checkbox'):
                    tracktwo_audio = tracktwo_audio + request.POST.get('track-two-volume', 0)

                # Normalize the track
                if setting and setting.normalize_trackone:
                    trackone_audio = normalize(trackone_audio, headroom=setting.normalize_trackone_headroom)

                # Normalize the track
                if setting and setting.normalize_tracktwo:
                    tracktwo_audio = normalize(tracktwo_audio, headroom=setting.normalize_tracktwo_headroom)

                combined_audio = tracktwo_audio.overlay(trackone_audio.fade_in(setting.fade_in_duration_trackone).fade_out(setting.fade_out_duration_trackone))

            elif request.POST.get('concatenation-loop') == '2':
                # Create a silent audio segment with the desired duration
                forward_silent_segment = AudioSegment.silent(duration=setting.fade_in_duration_tracktwo)
                back_silent_segment = AudioSegment.silent(duration=setting.fade_out_duration_tracktwo)

                trackone_audio = forward_silent_segment + trackone_audio + back_silent_segment

                # Calculate the number of repetitions required
                repetitions = int(trackone_audio.duration_seconds / tracktwo_audio.duration_seconds) + 1

                # Create the looped version of the shorter track
                tracktwo_audio = tracktwo_audio * repetitions

                if request.POST.get('track-volume-checkbox'):
                    trackone_audio = trackone_audio + request.POST.get('track-volume', 0)

                if request.POST.get('track-two-volume-checkbox'):
                    tracktwo_audio = tracktwo_audio + request.POST.get('track-two-volume', 0)

                # Normalize the track
                if setting and setting.normalize_trackone:
                    trackone_audio = normalize(trackone_audio, headroom=setting.normalize_trackone_headroom)

                # Normalize the track
                if setting and setting.normalize_tracktwo:
                    tracktwo_audio = normalize(tracktwo_audio, headroom=setting.normalize_tracktwo_headroom)

                # Overlay the section on top of the base audio
                combined_audio = trackone_audio.overlay(tracktwo_audio.fade_in(setting.fade_in_duration_tracktwo).fade_out(setting.fade_out_duration_tracktwo))

            else:
                if request.POST.get('track-volume-checkbox'):
                    trackone_audio = trackone_audio + request.POST.get('track-volume', 0)

                if request.POST.get('track-two-volume-checkbox'):
                    tracktwo_audio = tracktwo_audio + request.POST.get('track-two-volume', 0)

                # Normalize the track
                if setting and setting.normalize_trackone:
                    trackone_audio = normalize(trackone_audio, headroom=setting.normalize_trackone_headroom)

                # Normalize the track
                if setting and setting.normalize_tracktwo:
                    tracktwo_audio = normalize(tracktwo_audio, headroom=setting.normalize_tracktwo_headroom)

                combined_audio = trackone_audio.overlay(tracktwo_audio)

            # Apply the panning effect
            combined_audio = combined_audio.pan(panning_value)

            if request.POST.get('track-audio-filters-checkbox'):
                if request.POST.get('track-audio-filters-pass-checkbox') == "low-pass":                    
                    lowpass_cutoff = int(request.POST.get('track-low-pass', 0))
                    combined_audio = combined_audio.low_pass_filter(lowpass_cutoff)
                elif request.POST.get('track-audio-filters-pass-checkbox') == "high-pass":                                    
                    highpass_cutoff = int(request.POST.get('track-high-pass', 0))
                    combined_audio = combined_audio.high_pass_filter(highpass_cutoff)
                elif request.POST.get('track-audio-filters-pass-checkbox') == "band-pass":                                    
                    bandpass_lowcut = int(request.POST.get('track-band-pass-low', 0))
                    bandpass_highcut = int(request.POST.get('track-band-pass-high', 0))
                    combined_audio = combined_audio.low_pass_filter(bandpass_highcut).high_pass_filter(bandpass_lowcut)

            # Export the resulting audio to a file
            combined_audio = combined_audio.fade_in(setting.fade_in_duration_tracktwo).fade_out(setting.fade_out_duration_tracktwo)
            combined_audio.export(path, format=request.POST.get("output-format"))
        else:
            if request.POST.get('track-volume-checkbox'):
                trackone_audio = trackone_audio + request.POST.get('track-volume', 0)

            if request.POST.get('track-two-volume-checkbox'):
                tracktwo_audio = tracktwo_audio + request.POST.get('track-two-volume', 0)

            # Normalize the track
            if setting and setting.normalize_trackone:
                trackone_audio = normalize(trackone_audio, headroom=setting.normalize_trackone_headroom)

            # Normalize the track
            if setting and setting.normalize_tracktwo:
                tracktwo_audio = normalize(tracktwo_audio, headroom=setting.normalize_tracktwo_headroom)

            # Append the audio files
            if setting.crossfade:
                # Extract the overlapping portions for crossfading
                overlap1 = trackone_audio[-setting.crossfade_duration:]
                overlap2 = tracktwo_audio[:setting.crossfade_duration]

                # Apply crossfading by manipulating volume levels
                fade_in = overlap2.fade(to_gain=-120, start=0, duration=setting.crossfade_duration)
                fade_out = overlap1.fade(from_gain=-120, start=0, duration=setting.crossfade_duration)

                # Crossfade the audio segments
                appended_audio = trackone_audio[:-setting.crossfade_duration] + fade_out + fade_in + tracktwo_audio[setting.crossfade_duration:]
            else:
                appended_audio = trackone_audio + tracktwo_audio

            # Apply the panning effect
            appended_audio = appended_audio.pan(panning_value)

            if request.POST.get('track-audio-filters-checkbox'):
                if request.POST.get('track-audio-filters-pass-checkbox') == "low-pass":                    
                    lowpass_cutoff = int(request.POST.get('track-low-pass', 0))
                    appended_audio = appended_audio.low_pass_filter(lowpass_cutoff)
                elif request.POST.get('track-audio-filters-pass-checkbox') == "high-pass":                                    
                    highpass_cutoff = int(request.POST.get('track-high-pass', 0))
                    appended_audio = appended_audio.high_pass_filter(highpass_cutoff)
                elif request.POST.get('track-audio-filters-pass-checkbox') == "band-pass":                                    
                    bandpass_lowcut = int(request.POST.get('track-band-pass-low', 0))
                    bandpass_highcut = int(request.POST.get('track-band-pass-high', 0))
                    appended_audio = appended_audio.low_pass_filter(bandpass_highcut).high_pass_filter(bandpass_lowcut)

            # Export the appended audio to a new file
            appended_audio = appended_audio.fade_in(setting.fade_in_duration_tracktwo).fade_out(setting.fade_out_duration_tracktwo)
            appended_audio.export(path, format=request.POST.get("output-format"))        

        # Extract edited audio properties using PyDub
        audio = AudioSegment.from_file(path)
        url = request.build_absolute_uri(settings.MEDIA_URL + filename)

        properties = {
            'name': filename,
            'sampleRate': audio.frame_rate,
            'numChannels': audio.channels,
            'numSamples': audio.frame_count(),
            'duration': int(audio.duration_seconds),
            'fileUrl': url
        }

        # Return edited audio properties as JSON response
        return JsonResponse({'success': True, 'data': properties})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

def index(request):
    return render(request,'upload.html')

