import subprocess
from tempfile import NamedTemporaryFile


def reverse_track(straight_mp3_stream, reversed_mp3_stream):
    with \
            NamedTemporaryFile('r+wb', suffix='.wav') as straight_wav_stream, \
            NamedTemporaryFile('r+wb', suffix='.wav') as reversed_wav_stream:

        mp3_to_wav(straight_mp3_stream, straight_wav_stream)
        reverse_wav(straight_wav_stream, reversed_wav_stream)
        wav_to_mp3(reversed_wav_stream, reversed_mp3_stream)


def reverse_wav(fin, fout):
    subprocess.check_call(['sox', '-V', fin.name, fout.name, 'reverse'])


def mp3_to_wav(fin, fout):
    p = subprocess.Popen(['ffmpeg', '-i', '-', '-f', 'wav', fout.name, '-y'],
                         stdin=subprocess.PIPE)
    p.communicate(fin.read())


def wav_to_mp3(fin, fout):
    subprocess.check_call(['ffmpeg', '-i', fin.name, '-b:a', '128k', fout.name, '-y'])
