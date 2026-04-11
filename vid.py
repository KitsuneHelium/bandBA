import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
import ffmpeg

class WebmToTransparentPngGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WebM转透明PNG｜480高+24帧")
        self.root.geometry("600x350")
        self.root.resizable(False, False)

        # 路径变量
        self.input_path = tk.StringVar(value="请拖拽WebM视频到此处")
        self.output_dir = tk.StringVar(value="未选择导出文件夹")

        # 固定参数
        self.TARGET_HEIGHT = 480
        self.TARGET_FPS = 24

        self.setup_ui()

    def setup_ui(self):
        # 标题
        ttk.Label(self.root, text="WebM 转 透明PNG序列", font=("微软雅黑", 16, "bold")).pack(pady=10)

        # 拖拽区域
        ttk.Label(self.root, text="📥 拖拽WebM文件到下方", font=("微软雅黑", 11)).pack(pady=5)
        drop_frame = tk.Frame(self.root, bg="#E8F4FD", width=550, height=90, relief=tk.GROOVE, bd=2)
        drop_frame.pack(padx=20, fill=tk.X)
        drop_label = tk.Label(drop_frame, textvariable=self.input_path, bg="#E8F4FD", font=("微软雅黑", 10))
        drop_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # 绑定拖拽
        drop_frame.drop_target_register(DND_FILES)
        drop_frame.dnd_bind('<<Drop>>', self.on_file_drop)

        # 导出文件夹
        ttk.Button(self.root, text="📂 选择PNG导出文件夹", command=self.select_output_dir).pack(pady=12)
        ttk.Label(self.root, textvariable=self.output_dir, font=("微软雅黑", 9), foreground="#555").pack()

        # 转换按钮
        self.convert_btn = ttk.Button(self.root, text="▶ 开始转换", command=self.start_convert, width=20)
        self.convert_btn.pack(pady=15)

        # 状态
        self.status_var = tk.StringVar(value="待机中...")
        ttk.Label(self.root, textvariable=self.status_var, font=("微软雅黑", 10), foreground="#2E8B57").pack()

    def on_file_drop(self, event):
        file_path = event.data.strip("{}")
        if file_path.lower().endswith(".webm"):
            self.input_path.set(file_path)
            self.status_var.set("✅ 已加载透明WebM文件")
        else:
            messagebox.showerror("格式错误", "仅支持 .webm 格式！")

    def select_output_dir(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_dir.set(folder)
            self.status_var.set("✅ 已选择导出文件夹")

    def start_convert(self):
        video = self.input_path.get()
        out_dir = self.output_dir.get()

        # 校验
        if not os.path.isfile(video) or not video.endswith(".webm"):
            messagebox.showerror("错误", "请拖拽有效WebM！")
            return
        if not os.path.isdir(out_dir):
            messagebox.showerror("错误", "请选择导出文件夹！")
            return

        self.convert_btn.config(state=tk.DISABLED)
        self.status_var.set("🔄 处理中（保留透明背景）...")
        self.root.update()

        try:
            # 核心命令：保留透明通道 + 缩放 + 24帧 + 高清PNG
            output_pattern = os.path.join(out_dir, "frame_%05d.png")
            (
                ffmpeg
                .input(video)
                .filter('fps', fps=self.TARGET_FPS)          # 60帧→24帧
                .filter('scale', w=-1, h=self.TARGET_HEIGHT) # 高480宽自适应
                .output(output_pattern, vcodec='png', pix_fmt='rgba') # 保留透明通道
                .overwrite_output()
                .run(capture_stdout=True, capture_stderr=True)
            )

            self.status_var.set("✅ 转换完成！透明PNG已导出")
            messagebox.showinfo("成功", f"全部完成！\n✅ 保留透明背景\n✅ 480px高度\n✅ 24帧\n导出路径：{out_dir}")

        except ffmpeg.Error as e:
            self.status_var.set("❌ 转换失败")
            messagebox.showerror("错误", f"FFmpeg报错：{e.stderr.decode()}")
        finally:
            self.convert_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    WebmToTransparentPngGUI(root)
    root.mainloop()