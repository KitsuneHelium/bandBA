import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from PIL import Image
from threading import Thread

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BA 图片批量处理工具 (PNG/JPG)")
        self.root.geometry("600x600") # 稍微加高一点容纳新控件
        
        # 变量
        self.source_dir = tk.StringVar()
        self.target_dir = tk.StringVar()
        self.mode_var = tk.IntVar(value=1) # 1=缩放, 2=先缩后切, 3=缩放+填充, 4=自定义高度
        self.custom_height = tk.StringVar(value="480") # 新增：自定义高度变量，默认480

        # 检查 pngquant
        self.pngquant_path = self.find_pngquant()

        self.create_widgets()
        
        # 绑定模式变化事件，用于切换自定义高度输入框的状态
        self.mode_var.trace_add("write", self.on_mode_change)

    def find_pngquant(self):
        """找同目录下的 pngquant.exe"""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        exe_path = os.path.join(script_dir, "pngquant.exe")
        if os.path.exists(exe_path):
            return exe_path
        return None

    def create_widgets(self):
        # 1. 文件夹选择区域
        frame_top = tk.Frame(self.root, pady=10)
        frame_top.pack(fill=tk.X, padx=10)

        # 源文件夹
        tk.Label(frame_top, text="原图文件夹:", anchor="w").pack(fill=tk.X)
        frame_src = tk.Frame(frame_top)
        frame_src.pack(fill=tk.X, pady=2)
        tk.Entry(frame_src, textvariable=self.source_dir, width=50).pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(frame_src, text="选择...", command=self.select_source).pack(side=tk.LEFT, padx=5)

        # 目标文件夹
        tk.Label(frame_top, text="输出文件夹:", anchor="w").pack(fill=tk.X, pady=(10,0))
        frame_dst = tk.Frame(frame_top)
        frame_dst.pack(fill=tk.X, pady=2)
        tk.Entry(frame_dst, textvariable=self.target_dir, width=50).pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(frame_dst, text="选择...", command=self.select_target).pack(side=tk.LEFT, padx=5)

        # 2. 模式选择
        frame_mode = tk.LabelFrame(self.root, text="处理模式", padx=10, pady=10)
        frame_mode.pack(fill=tk.X, padx=10, pady=10)

        tk.Radiobutton(frame_mode, text="模式 0: 等比例缩放 (宽度336，高度自适应)", variable=self.mode_var, value=0).pack(anchor="w")
        tk.Radiobutton(frame_mode, text="模式 1: 等比例缩放 (高度480，宽度自适应)", variable=self.mode_var, value=1).pack(anchor="w")
        tk.Radiobutton(frame_mode, text="模式 2: 先缩后切 (高度480，居中裁剪宽度至336)", variable=self.mode_var, value=2).pack(anchor="w")
        tk.Radiobutton(frame_mode, text="模式 3: 缩放+填充 (宽度336，黑边填充高度至480)", variable=self.mode_var, value=3).pack(anchor="w")
        
        # 新增：模式4
        tk.Radiobutton(frame_mode, text="模式 4: 等比例缩放 (自定义高度，宽度自适应)", variable=self.mode_var, value=4).pack(anchor="w")
        
        # 新增：自定义高度输入区域
        frame_custom = tk.Frame(frame_mode)
        frame_custom.pack(anchor="w", pady=5)
        tk.Label(frame_custom, text="自定义高度:").pack(side=tk.LEFT)
        self.entry_custom_height = tk.Entry(frame_custom, textvariable=self.custom_height, width=10, state=tk.DISABLED) # 默认禁用
        self.entry_custom_height.pack(side=tk.LEFT, padx=5)
        tk.Label(frame_custom, text="像素").pack(side=tk.LEFT)

        # 3. 开始按钮
        self.btn_start = tk.Button(self.root, text="开始批量处理", command=self.start_process_thread, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), height=2)
        self.btn_start.pack(fill=tk.X, padx=20, pady=5)

        # 4. 日志区域
        tk.Label(self.root, text="处理日志:", anchor="w").pack(fill=tk.X, padx=10)
        self.log_text = scrolledtext.ScrolledText(self.root, height=12)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    def on_mode_change(self, *args):
        """当模式改变时，切换自定义高度输入框的启用状态"""
        mode = self.mode_var.get()
        if mode == 4:
            self.entry_custom_height.config(state=tk.NORMAL)
        else:
            self.entry_custom_height.config(state=tk.DISABLED)

    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)

    def select_source(self):
        path = filedialog.askdirectory()
        if path:
            self.source_dir.set(path)

    def select_target(self):
        path = filedialog.askdirectory()
        if path:
            self.target_dir.set(path)

    def start_process_thread(self):
        # 检查输入
        if not self.source_dir.get() or not self.target_dir.get():
            messagebox.showwarning("提示", "请先选择原图文件夹和输出文件夹！")
            return

        # 禁用按钮防止重复点击
        self.btn_start.config(state=tk.DISABLED, text="处理中...")
        self.log_text.delete(1.0, tk.END)

        # 开启新线程运行
        Thread(target=self.run_process).start()

    def process_image_core(self, img):
        """核心图像处理逻辑"""
        mode = self.mode_var.get()
        w, h = img.size
        if mode == 0:
            target_w = 336
            scale_ratio = target_w / w
            new_h = int(h * scale_ratio)
            new_w = target_w
            img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
            return img, f"缩放至 {new_w}x{new_h}"
        if mode == 1:
            # 模式 A: 等比例缩放 (高度固定480)
            target_h = 480
            scale_ratio = target_h / h
            new_w = int(w * scale_ratio)
            new_h = target_h
            img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
            return img, f"缩放至 {new_w}x{new_h}"
            
        elif mode == 2:
            # 模式 B: 先缩后切 (高度480，裁剪宽度336)
            target_h = 480
            target_w = 336
            
            # 1. 先缩放高度到480
            scale_ratio = target_h / h
            new_w = int(w * scale_ratio)
            img = img.resize((new_w, target_h), Image.Resampling.LANCZOS)
            
            # 2. 居中裁剪宽度
            left = (new_w - target_w) // 2
            left = max(0, left)
            right = left + target_w
            img = img.crop((left, 0, right, target_h))
            return img, f"缩放+裁剪至 336x480"
            
        elif mode == 3:
            # 模式 C: 缩放+填充 (宽度336，黑边填充高度480)
            target_w = 336
            target_h = 480
            
            # 1. 先按宽度336等比例缩放
            scale_ratio = target_w / w
            new_h = int(h * scale_ratio)
            img = img.resize((target_w, new_h), Image.Resampling.LANCZOS)
            
            # 2. 创建黑色背景画布 (336x480)
            bg_color = (0, 0, 0) # RGB黑色
            if img.mode in ('RGBA', 'LA'):
                # 如果原图有透明通道，创建带黑色背景的RGBA画布
                new_img = Image.new('RGBA', (target_w, target_h), (0, 0, 0, 255))
            else:
                new_img = Image.new('RGB', (target_w, target_h), bg_color)
                
            # 3. 计算居中位置并粘贴
            paste_y = (target_h - new_h) // 2
            new_img.paste(img, (0, paste_y))
            
            return new_img, f"缩放+黑边填充至 336x480"
            
        elif mode == 4:
            # 模式 D: 自定义高度，宽度自适应
            try:
                target_h = int(self.custom_height.get())
                if target_h <= 0:
                    raise ValueError("高度必须为正整数")
            except ValueError as e:
                raise Exception(f"自定义高度无效: {e}")
            
            scale_ratio = target_h / h
            new_w = int(w * scale_ratio)
            new_h = target_h
            img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
            return img, f"缩放至 {new_w}x{new_h} (自定义高度)"

    def run_process(self):
        src_dir = self.source_dir.get()
        dst_dir = self.target_dir.get()

        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        # 支持的扩展名
        valid_exts = ('.png', '.jpg', '.jpeg')
        files = [f for f in os.listdir(src_dir) if f.lower().endswith(valid_exts)]
        
        self.log(f"找到 {len(files)} 张图片\n")

        count_ok = 0
        for filename in files:
            src_path = os.path.join(src_dir, filename)
            dst_path = os.path.join(dst_dir, filename)
            
            # 判断文件类型
            is_png = filename.lower().endswith('.png')

            try:
                # 第一步：打开图片
                with Image.open(src_path) as img:
                    # 如果是JPG且有透明通道，先转RGB，防止报错
                    if not is_png and img.mode in ('RGBA', 'P'):
                        img = img.convert('RGB')
                    
                    # 第二步：处理 (缩放/裁剪/填充)
                    processed_img, action_msg = self.process_image_core(img)
                    
                    # 第三步：保存与压缩
                    if is_png:
                        # --- PNG 处理 ---
                        if not self.pngquant_path:
                            # 如果没有 pngquant，只用 Pillow 凑合压一下
                            processed_img.save(dst_path, format='PNG', optimize=True)
                            self.log(f"[PNG] {filename} ({action_msg})")
                        else:
                            # 有 pngquant，先用 temp 存，再压
                            temp_path = os.path.join(dst_dir, "_temp_gui.png")
                            processed_img.save(temp_path, format='PNG')
                            
                            # 调用 pngquant
                            subprocess.run(
                                [self.pngquant_path, "--quality", "20-40", "--speed", "1", "--strip", "--force", "--output", dst_path, temp_path],
                                check=True,
                                capture_output=True
                            )
                            os.remove(temp_path)
                            self.log(f"[PNG] {filename} ({action_msg})")
                    else:
                        # --- JPG 处理 ---
                        # Pillow 直接保存，quality=60 是兼顾体积和画质的好选择
                        if processed_img.mode == 'RGBA':
                            processed_img = processed_img.convert('RGB')
                        processed_img.save(dst_path, format='JPEG', quality=60, optimize=True)
                        self.log(f"[JPG] {filename} ({action_msg})")

                # 显示文件大小
                size_kb = os.path.getsize(dst_path) / 1024
                self.log(f"   完成 -> {size_kb:.1f} KB\n")
                count_ok += 1

            except Exception as e:
                self.log(f"❌ 错误 {filename}: {str(e)}\n")

        # 处理完恢复
        self.log(f"\n全部结束！成功处理 {count_ok}/{len(files)} 张。")
        self.btn_start.config(state=tk.NORMAL, text="开始批量处理")
        messagebox.showinfo("完成", f"处理完成！\n成功: {count_ok} 张")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()