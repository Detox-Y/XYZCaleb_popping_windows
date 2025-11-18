import pygame
import threading
import tkinter as tk
import random
import sys
import os

BG_COLOR = "#151541"   # 深蓝背景色
FG_COLOR = "#ed7638"   # 橙色文字


def resource_path(relative_path):
    """
    获取资源文件的绝对路径，兼容 pyinstaller 打包后的 _MEIPASS 目录
    """
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS  # 打包后的临时目录
    else:
        base_path = os.path.abspath(".")  # 直接运行 .py 时的当前目录
    return os.path.join(base_path, relative_path)


def play_bgm():
    pygame.mixer.init()
    # 注意：这里用的是 mp3（或 wav），不要再用 mp4
    music_file = resource_path("Architect.mp3")
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)  # -1 表示循环播放



class TipApp:
    def __init__(self):
        self.batch_windows = []
        self.single_window = None
        self.final_window = None
        self.root = None  # 统一根窗口

    def show_single_tip(self):

        self.root = tk.Tk()
        self.root.withdraw()

        self.single_window = tk.Toplevel(self.root)
        self.single_window.title('妹妹')
        self.single_window.configure(bg=BG_COLOR)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 350
        window_height = 120
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.single_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        tip = "不需要我？"
        tk.Label(
            self.single_window,
            text=tip,
            bg=BG_COLOR,
            fg=FG_COLOR,
            font=('GenRyuMin', 14),
            width=40,
            height=5,
            wraplength=320,
            justify='center'
        ).pack()

        self.single_window.bind('<space>', self.on_space_global)
        self.single_window.attributes('-topmost', True)
        self.single_window.protocol("WM_DELETE_WINDOW", self.start_batch_tips)

        self.root.mainloop()

    def create_batch_window(self, count):
        if count <= 0:
            self.root.after(500, self.show_final_big_tip)
            return

        window = tk.Toplevel(self.root)
        window.configure(bg=BG_COLOR)
        self.batch_windows.append(window)

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 350
        window_height = 120

        x = random.randrange(0, screen_width - window_width)
        y = random.randrange(0, screen_height - window_height)
        window.title('妹妹')
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        tips = [
            '好啊，那你需要什么？我都可以答应。',
            '你想要回临空，我们就回临空',
            '你想要回到从前，我们就回临空',
            '一座房子不够，那就给你建一座迷宫。',
            '我会在里面给你准备好的一切，把它变成世界上最漂亮的花园。',
            '有我陪你，以后别人就再也找不到你了。',
            '一上大学就跟出笼的小鸟似的，这么久没回来，家里东西也都不记得了吗？',
            '不许走，别留我一个人。',
            '总是听不到你说想见我，我可以把它当作你想我的证据。',
            '我的弱点还想知道吗？',
            '不需要我……好啊，那你需要什么？我都可以答应。',
            '还说不需要我？',
            '换留不需要，见识到你曾向我抱恨，把我想起的一切都下不下了吗？',
            '当年是不是你先牵住我的手，让我做你的哥哥的吗？',
            '现在你觉得自己长大了，就要松开这只手了吗？',
            '我一直想要和你在同一个边的世界，而不是只能看着你，想象你。',
            '我们是同两面的生，不管多么久，姻缘曲线。',
            '但在我出生的那一刻就注定了的，我从来没有抛弃。',
            '意识也好，躯体也罢，即便这些都不复存在，我的灵魂也仍然向你问候。',
            '说好了，生和死，都不再分开。',
            '我爱你。',
            '我一直记得是我先牵你的手',
            '知道长大了,看你啊,有你自己的小世界了.'
        ]

        tip = random.choice(tips)
        tk.Label(
            window,
            text=tip,
            bg=BG_COLOR,
            fg=FG_COLOR,
            font=('GenRyuMin', 14),
            width=40,
            height=3,
            wraplength=320,
            justify='center'
        ).pack()

        window.bind('<space>', self.on_space_global)
        window.attributes('-topmost', True)
        window.update()

        self.root.after(100, self.create_batch_window, count - 1)

    def show_final_big_tip(self):

        self.final_window = tk.Toplevel(self.root)
        self.final_window.title('妹妹')
        self.final_window.configure(bg=BG_COLOR)
        self.final_window.attributes('-topmost', True, '-alpha', 0.95)
        self.final_window.protocol("WM_DELETE_WINDOW", self.on_space_global)

        window_width = 600
        window_height = 250
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.final_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        final_tip = "说好了，生和死，都不再分开。"

        label = tk.Label(
            self.final_window,
            text=final_tip,
            bg=BG_COLOR,
            fg=FG_COLOR,
            font=('GenRyuMin', 25, 'bold'),
            padx=30,
            pady=30,
            wraplength=550,
            justify='center'
        )
        label.pack(expand=True, fill=tk.BOTH)

        self.final_window.update_idletasks()
        self.final_window.lift()

    def start_batch_tips(self):
        if self.single_window:
            self.single_window.destroy()
            self.single_window = None

        # 开始后台播放 BGM
        threading.Thread(target=play_bgm, daemon=True).start()
        self.create_batch_window(100)


    def on_space_global(self, event=None):

        if self.single_window:
            self.single_window.destroy()
        for window in self.batch_windows:
            try:
                window.destroy()
            except:
                pass
        if self.final_window:
            self.final_window.destroy()

        if self.root:
            self.root.quit()
        sys.exit()


if __name__ == '__main__':
    app = TipApp()
    app.show_single_tip()
