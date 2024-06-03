import tkinter as tk
import time
import pyaudio
import wave

class Clock():
    def __init__(self) -> None:
        self.root = tk.Tk()                                       #メインウィンドウ取得
        self.label = tk.Label(text="デジタル時計",font = ('Helvetica', 58))
        self.label.pack()
        self.now = ""
        self.update_clock()                                       #時間取得
        self.root.mainloop()                                      #無限ループ
        
    def update_clock(self) -> None:
        self.now = time.strftime("%Y年%m月%d日 %H時%M分%S秒")
        self.label.configure(text=self.now)
        self.set_alarm(15,40)
        self.root.after(100, self.update_clock)                   #0.1秒ごとにこの関数を繰り返す

    def set_alarm(self, hour: int, minute: int) -> None:
        if("{}時{}分00秒".format(hour, minute) in self.now):
            self.alarm_sound()
            print("時間です.利息が付きます.")

    def alarm_sound(self) -> None:
        pass
        file = wave.open("cat1.wav", mode="rb")
        p = pyaudio.PyAudio()
        stream = p.open(
            format = p.get_format_from_width(file.getsampwidth()),
            channels = file.getnchannels(),
            rate = file.getframerate(),
            output = True
        )
        file.rewind()
        chunk = 1024
        data = file.readframes(chunk)
        while data:
            stream.write(data)
            data = file.readframes(chunk)
        stream.close()
        p.terminate()

app = Clock()