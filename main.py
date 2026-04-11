import sys
import os
import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# ======================== 【配置与路径管理】 ========================
CONFIG_PATH = os.path.join(os.path.expanduser("~"), ".vge_editor_config.json")

def load_config():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    return {"last_file": None, "common_root": r"C:\Users\Helium\Mi Band Projects\VelaGameEngine\VGE-BA\bandBA\src\common"}

def save_config(config):
    try:
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(config, f, ensure_ascii=False, indent=2)
    except:
        pass

CONFIG = load_config()
GAME_COMMON_ROOT = CONFIG.get("common_root", r"C:\Users\Helium\Mi Band Projects\VelaGameEngine\VGE-BA\bandBA\src\common")
RESOURCE_CONTAINERS = {
    "bg": {
        "game_path": "/common/gaming/bg/",
        "local_path": os.path.join(GAME_COMMON_ROOT, "gaming", "bg")
    },
    "chara": {
        "game_path": "/common/chara/",
        "local_path": os.path.join(GAME_COMMON_ROOT, "chara")
    }
}

def game_path_to_local(game_path):
    if game_path.startswith("/common/"):
        rel_path = game_path.replace("/common/", "").replace("/", os.sep)
        return os.path.join(GAME_COMMON_ROOT, rel_path)
    return game_path

def local_path_to_game(local_path):
    rel_path = os.path.relpath(local_path, GAME_COMMON_ROOT).replace(os.sep, "/")
    return f"/common/{rel_path}"

# ======================== 【深色主题样式表】 ========================
DARK_STYLE = """
QMainWindow {
    background-color: #1e1e1e;
    color: #d4d4d4;
}
QWidget {
    background-color: #1e1e1e;
    color: #d4d4d4;
    font-family: "微软雅黑", "Segoe UI", sans-serif;
    font-size: 9pt;
}
QGroupBox {
    border: 1px solid #3c3c3c;
    border-radius: 4px;
    margin-top: 8px;
    padding-top: 8px;
    font-weight: bold;
    color: #d4d4d4;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 8px;
    padding: 0 4px;
}
QTextEdit {
    background-color: #252526;
    color: #d4d4d4;
    border: 1px solid #3c3c3c;
    border-radius: 3px;
    font-family: "Consolas", "Courier New", monospace;
    font-size: 9pt;
}
QPushButton {
    background-color: #3c3c3c;
    color: #d4d4d4;
    border: 1px solid #555;
    border-radius: 3px;
    padding: 4px 10px;
    min-height: 20px;
}
QPushButton:hover {
    background-color: #4c4c4c;
    border: 1px solid #666;
}
QPushButton:pressed {
    background-color: #2c2c2c;
}
QComboBox {
    background-color: #252526;
    color: #d4d4d4;
    border: 1px solid #3c3c3c;
    border-radius: 3px;
    padding: 3px 5px;
    min-width: 80px;
}
QComboBox::drop-down {
    border: none;
    width: 20px;
}
QComboBox::down-arrow {
    image: none;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 4px solid #d4d4d4;
    width: 0;
    height: 0;
    margin-right: 5px;
}
QComboBox QAbstractItemView {
    background-color: #252526;
    color: #d4d4d4;
    border: 1px solid #3c3c3c;
    selection-background-color: #007acc;
}
QGraphicsView {
    background-color: #1e1e1e;
    border: 1px solid #3c3c3c;
}
QMenu {
    background-color: #252526;
    color: #d4d4d4;
    border: 1px solid #3c3c3c;
}
QMenu::item {
    padding: 5px 25px 5px 15px;
}
QMenu::item:selected {
    background-color: #007acc;
}
QScrollBar:vertical {
    background-color: #1e1e1e;
    width: 14px;
    margin: 0px;
    border: none;
}
QScrollBar::handle:vertical {
    background-color: #4c4c4c;
    min-height: 30px;
    border-radius: 7px;
    margin: 2px;
}
QScrollBar::handle:vertical:hover {
    background-color: #5c5c5c;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}
QScrollBar:horizontal {
    background-color: #1e1e1e;
    height: 14px;
    margin: 0px;
    border: none;
}
QScrollBar::handle:horizontal {
    background-color: #4c4c4c;
    min-width: 30px;
    border-radius: 7px;
    margin: 2px;
}
QScrollBar::handle:horizontal:hover {
    background-color: #5c5c5c;
}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0px;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}
QDialog {
    background-color: #1e1e1e;
}
QListWidget {
    background-color: #252526;
    color: #d4d4d4;
    border: 1px solid #3c3c3c;
}
QListWidget::item {
    padding: 5px;
    border-radius: 3px;
}
QListWidget::item:selected {
    background-color: #007acc;
}
QInputDialog {
    background-color: #1e1e1e;
}
QLineEdit {
    background-color: #252526;
    color: #d4d4d4;
    border: 1px solid #3c3c3c;
    border-radius: 3px;
    padding: 3px;
}
QMessageBox {
    background-color: #1e1e1e;
}
QMessageBox QPushButton {
    min-width: 70px;
}
QToolBar {
    background-color: #252526;
    border: none;
    spacing: 3px;
}
QToolBar QToolButton {
    background-color: transparent;
    border: none;
    padding: 4px 8px;
    border-radius: 3px;
}
QToolBar QToolButton:hover {
    background-color: #3c3c3c;
}
QMenuBar {
    background-color: #252526;
    color: #d4d4d4;
    border: none;
}
QMenuBar::item {
    padding: 5px 10px;
    background: transparent;
}
QMenuBar::item:selected {
    background-color: #3c3c3c;
}
"""

# ======================== 【关于对话框】 ========================
class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("关于 VGE剧本编辑器")
        self.setFixedSize(450, 350)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        
        title_label = QLabel("VGE剧本编辑器")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #007acc; padding: 8px;")
        layout.addWidget(title_label)
        
        version_label = QLabel("版本：2.1.2 吸附优化版")
        version_label.setAlignment(Qt.AlignCenter)
        version_label.setStyleSheet("font-size: 12px; color: #888;")
        layout.addWidget(version_label)
        
        info_text = QTextEdit()
        info_text.setReadOnly(True)
        info_text.setHtml("""
        <div style="text-align: center; padding: 8px;">
            <h4 style="color: #007acc;">🎮 功能特性</h4>
            <p>✅ 可视化流程图编辑</p>
            <p>✅ 节点智能吸附对齐</p>
            <p>✅ 选中节点下方追加</p>
            <p>✅ JSON代码实时同步</p>
            <p>✅ 图片资源容器管理</p>
            <p>✅ 子文件夹图片选择</p>
            <p>✅ 自动保存与恢复</p>
            <p>✅ 自定义工作目录</p>
            <p>✅ 代码自动定位</p>
            <p>✅ 游戏实时渲染预览</p>
            <p>✅ 撤销/重做功能</p>
            <p>✅ 深色护眼模式</p>
            <br>
            <p style="color: #888; font-size: 10px;">基于 PyQt5 开发</p>
        </div>
        """)
        layout.addWidget(info_text)
        
        btn_layout = QHBoxLayout()
        btn_close = QPushButton("关闭")
        btn_close.clicked.connect(self.accept)
        btn_layout.addStretch()
        btn_layout.addWidget(btn_close)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

# ======================== 【图片选择弹窗】 ========================
class ImagePickerDialog(QDialog):
    def __init__(self, container_type, parent=None):
        super().__init__(parent)
        self.container_type = container_type
        self.container = RESOURCE_CONTAINERS[container_type]
        self.selected_path = None
        self.root_dir = self.container["local_path"]
        self.current_folder = self.root_dir
        self.folders = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(f"选择{self.container_type}图片")
        self.setFixedSize(700, 550)
        layout = QVBoxLayout(self)
        
        folder_layout = QHBoxLayout()
        folder_layout.addWidget(QLabel("选择文件夹："))
        self.folder_combo = QComboBox()
        folder_layout.addWidget(self.folder_combo, 1)
        layout.addLayout(folder_layout)
        
        self.list_widget = QListWidget()
        self.list_widget.setViewMode(QListWidget.IconMode)
        self.list_widget.setIconSize(QSize(120, 120))
        self.list_widget.setResizeMode(QListWidget.Adjust)
        self.list_widget.setSpacing(8)
        self.list_widget.itemDoubleClicked.connect(self.on_select)
        layout.addWidget(self.list_widget)
        
        btn_layout = QHBoxLayout()
        self.btn_confirm = QPushButton("确认选择")
        self.btn_confirm.clicked.connect(self.on_select)
        self.btn_cancel = QPushButton("取消")
        self.btn_cancel.clicked.connect(self.reject)
        btn_layout.addWidget(self.btn_confirm)
        btn_layout.addWidget(self.btn_cancel)
        layout.addLayout(btn_layout)
        
        self.scan_and_load_folders()
        self.folder_combo.currentIndexChanged.connect(self.on_folder_changed)

    def scan_and_load_folders(self):
        self.folders = []
        self.folders.append(("根目录", self.root_dir))
        if os.path.exists(self.root_dir):
            for item in os.listdir(self.root_dir):
                item_path = os.path.join(self.root_dir, item)
                if os.path.isdir(item_path):
                    self.folders.append((item, item_path))
        self.folder_combo.blockSignals(True)
        self.folder_combo.clear()
        for name, path in self.folders:
            self.folder_combo.addItem(name, path)
        self.folder_combo.blockSignals(False)
        self.load_images()

    def on_folder_changed(self, index):
        folder_path = self.folder_combo.itemData(index)
        if folder_path and os.path.exists(folder_path):
            self.current_folder = folder_path
            self.load_images()

    def load_images(self):
        local_dir = self.current_folder
        if not os.path.exists(local_dir):
            os.makedirs(local_dir)
            QMessageBox.warning(self, "提示", f"文件夹已创建：{local_dir}\n请放入图片后重新打开！")
            return
        self.list_widget.clear()
        img_exts = (".png", ".jpg", ".jpeg", ".bmp")
        for file in os.listdir(local_dir):
            if file.lower().endswith(img_exts):
                img_path = os.path.join(local_dir, file)
                item = QListWidgetItem()
                item.setText(file)
                pixmap = QPixmap(img_path).scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                item.setIcon(QIcon(pixmap))
                item.setData(Qt.UserRole, img_path)
                self.list_widget.addItem(item)

    def on_select(self):
        item = self.list_widget.currentItem()
        if not item:
            QMessageBox.warning(self, "警告", "请选择一张图片！")
            return
        self.selected_path = item.data(Qt.UserRole)
        self.accept()

# ======================== 【图形节点类】 ========================
class GraphicsNode(QGraphicsItem):
    def __init__(self, node_type="label", parent=None, label_name=None, cmd_index=None):
        super().__init__(parent)
        self.node_type = node_type
        self.label_name = label_name
        self.cmd_index = cmd_index
        self.width = 140
        self.height = 50
        self.data = {}
        self.code_line = -1

        if node_type == "label":
            self.color = QColor(30, 144, 255)
            self.title = label_name or "new_label"
        else:
            self.color = self._get_cmd_color()
            self.title = self._get_cmd_title()

        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.setZValue(1)

    def _get_cmd_color(self):
        cmd_type = self.data.get("type", "")
        color_map = {
            "bg": QColor(255, 165, 0),
            "chara": QColor(144, 238, 144),
            "text": QColor(255, 100, 100),
            "ani": QColor(255, 215, 0),
            "bg_ani": QColor(255, 215, 0),
            "wait": QColor(169, 169, 169),
            "goto": QColor(138, 43, 226),
            "select": QColor(0, 191, 255),
            "end": QColor(255, 0, 0),
            "warp": QColor(128, 0, 128)
        }
        return color_map.get(cmd_type, QColor(128, 128, 128))

    def _get_cmd_title(self):
        cmd_type = self.data.get("type", "")
        params = self.data.get("params", {})
        if cmd_type == "text":
            speaker = params.get("speaker", "无")
            content = params.get("content", "")
            return f"【{speaker}】{content[:10]}..." if content else f"【{speaker}】空文本"
        elif cmd_type == "bg":
            path = params.get("path", "")
            return f"bg: {path.split('/')[-1]}"
        elif cmd_type == "chara":
            path = params.get("path", "")
            return f"chara: {path.split('/')[-1]}"
        elif cmd_type in ["ani", "bg_ani"]:
            name = params.get("name", "")
            return f"{cmd_type}: {name}"
        elif cmd_type == "wait":
            return "wait"
        elif cmd_type == "goto":
            target = params.get("label", "")
            return f"goto: {target}"
        elif cmd_type == "select":
            return f"选项({len(params.get('options', []))})"
        elif cmd_type == "end":
            return "end"
        elif cmd_type == "warp":
            return f"warp: {params.get('path', 'unknown')}"
        return "未知指令"

    def boundingRect(self):
        return QRectF(0, 0, self.width, self.height)

    def paint(self, painter, option, widget):
        painter.setBrush(self.color)
        painter.setPen(Qt.red if self.isSelected() else Qt.black)
        painter.drawRoundedRect(0, 0, self.width, self.height, 8, 8)
        painter.setPen(Qt.white)
        painter.setFont(QFont("微软雅黑", 8, QFont.Bold))
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self.title)

    def itemChange(self, change, value):
        if self.scene() is None:
            return super().itemChange(change, value)
            
        if change == QGraphicsItem.ItemPositionChange and self.node_type == "command":
            new_pos = value
            new_pos.setX(200)
            # 保持60px间隔对齐，不强制跳转到Label顶端
            aligned_y = round(new_pos.y() / 60) * 60
            new_pos.setY(aligned_y)

            # 避免同Label的节点重叠
            for item in self.scene().items():
                if isinstance(item, GraphicsNode) and item != self and item.node_type == "command":
                    if item.pos().y() == new_pos.y() and item.label_name == self.label_name:
                        new_pos.setY(new_pos.y() + 60)
            return new_pos
        return super().itemChange(change, value)

    def mouseReleaseEvent(self, event):
        if self.scene() is not None and self.node_type == "command":
            # ✅ 修复：仅更新Label归属，不强制修改位置
            main_window = None
            for widget in QApplication.topLevelWidgets():
                if isinstance(widget, StoryEditor):
                    main_window = widget
                    break
            if main_window:
                target_label_node = main_window.get_label_by_y(self.pos().y())
                if target_label_node:
                    self.label_name = target_label_node.label_name
            self.scene().changed.emit([])
        super().mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event):
        if self.node_type == "command":
            self._edit_command()
        elif self.node_type == "label":
            self._edit_label()
        self.update()
        event.accept()

    def _edit_command(self):
        cmd_type = self.data.get("type", "")
        params = self.data.get("params", {})
        if cmd_type == "text":
            speaker, ok1 = QInputDialog.getText(None, "编辑对话", "说话人:", text=params.get("speaker", ""))
            content, ok2 = QInputDialog.getMultiLineText(None, "编辑对话", "对话内容:", text=params.get("content", ""))
            if ok1 and ok2:
                self.data["params"]["speaker"] = speaker
                self.data["params"]["content"] = content
        elif cmd_type == "bg":
            path, ok = QInputDialog.getText(None, "编辑背景", "图片路径:", text=params.get("path", ""))
            if ok:
                self.data["params"]["path"] = path
        elif cmd_type == "chara":
            path, ok = QInputDialog.getText(None, "编辑立绘", "图片路径:", text=params.get("path", ""))
            if ok:
                self.data["params"]["path"] = path
        elif cmd_type in ["ani", "bg_ani"]:
            name, ok = QInputDialog.getText(None, f"编辑{cmd_type}", "动画名:", text=params.get("name", ""))
            if ok:
                self.data["params"]["name"] = name
        elif cmd_type == "goto":
            target, ok = QInputDialog.getText(None, "编辑跳转", "目标Label:", text=params.get("label", ""))
            if ok:
                self.data["params"]["label"] = target
        elif cmd_type == "select":
            options = params.get("options", [])
            options_str = "\n".join([f"{opt['text']} -> {opt['targetLabel']}" for opt in options])
            new_options_str, ok = QInputDialog.getMultiLineText(None, "编辑选项", "格式：选项文本 -> 目标Label\n每行一个选项", text=options_str)
            if ok and new_options_str:
                new_options = []
                for line in new_options_str.strip().split("\n"):
                    if "->" in line:
                        text, target = line.split("->", 1)
                        new_options.append({"text": text.strip(), "targetLabel": target.strip()})
                self.data["params"]["options"] = new_options
        elif cmd_type == "warp":
            target, ok = QInputDialog.getText(None, "编辑warp", "目标path:", text=params.get("path", ""))
            if ok:
                self.data["params"]["path"] = target
        self.title = self._get_cmd_title()
        self.color = self._get_cmd_color()

    def _edit_label(self):
        old_name = self.title
        new_name, ok = QInputDialog.getText(None, "编辑Label", "Label名称:", text=self.title)
        if not ok or not new_name or new_name == old_name:
            return

        self.title = new_name
        self.label_name = new_name

        main_window = None
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, StoryEditor):
                main_window = widget
                break
        if not main_window:
            return

        if old_name in main_window.script_data["labels"]:
            cmds = main_window.script_data["labels"].pop(old_name)
            main_window.script_data["labels"][new_name] = cmds

        for label_cmds in main_window.script_data["labels"].values():
            for cmd in label_cmds:
                if cmd["type"] == "goto" and cmd["params"].get("label") == old_name:
                    cmd["params"]["label"] = new_name
                if cmd["type"] == "select":
                    for opt in cmd["params"]["options"]:
                        if opt.get("targetLabel") == old_name:
                            opt["targetLabel"] = new_name
                if cmd["type"] == "warp" and cmd["params"].get("path") == old_name:
                    cmd["params"]["path"] = new_name

        main_window.refresh_json_view()
        main_window.refresh_flowchart_from_json()

# ======================== 【连线类】 ========================
class GraphicsConnection(QGraphicsLineItem):
    def __init__(self, start_node, end_node, parent=None):
        super().__init__(parent)
        self.start_node = start_node
        self.end_node = end_node
        self.setPen(QPen(QColor(255,140,0), 2, Qt.SolidLine))
        self.setZValue(0)
        self.update_line()

    def update_line(self):
        s = self.start_node.pos() + QPointF(self.start_node.width/2, self.start_node.height/2)
        e = self.end_node.pos() + QPointF(self.end_node.width/2, self.end_node.height/2)
        self.setLine(QLineF(s, e))

# ======================== 【实时渲染预览器】 ========================
class PreviewRenderer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(280, 400)
        self.bg_path = game_path_to_local("/common/main_page_img/bg.png")
        self.chara_path = game_path_to_local("/common/empty.png")
        self.speaker = ""
        self.content = "选中节点预览"
        self.ani = ""
        self.bg_ani = ""
        self.select_options = []
        self.selected_option = -1
        self.show_ani_indicator = False

    def update_preview(self, bg, chara, speaker, content, ani="", bg_ani="", select_options=[], show_ani_indicator=False):
        self.bg_path = game_path_to_local(bg)
        self.chara_path = game_path_to_local(chara)
        self.speaker = speaker
        self.content = content
        self.ani = ani
        self.bg_ani = bg_ani
        self.select_options = select_options
        self.selected_option = -1
        self.show_ani_indicator = show_ani_indicator
        self.update()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(0,0,280,400, QColor(40,40,40))

        bg_pix = QPixmap(self.bg_path)
        if not bg_pix.isNull():
            painter.drawPixmap(0,0,280,400, bg_pix.scaled(280,400, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation))
        else:
            painter.fillRect(0,0,280,400, QColor(50,50,50))

        chara_pix = QPixmap(self.chara_path)
        if not chara_pix.isNull():
            scaled_chara = chara_pix.scaled(280, 330, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            x = (280 - scaled_chara.width()) // 2
            y = 70 + (330 - scaled_chara.height()) // 2
            painter.drawPixmap(x, y, scaled_chara)

        painter.setBrush(QColor(0,0,0,200))
        painter.drawRect(0, 320, 280, 80)
        painter.setPen(Qt.white)
        painter.setFont(QFont("微软雅黑", 10))
        if self.speaker:
            painter.drawText(15, 335, f"【{self.speaker}】")
        painter.drawText(15, 355, 250, 40, Qt.TextWordWrap, self.content)

        if self.show_ani_indicator and (self.ani or self.bg_ani):
            painter.setPen(QColor(255,210,0))
            painter.setFont(QFont("微软雅黑", 8))
            painter.drawText(5, 15, f"人物动画：{self.ani}  背景动画：{self.bg_ani}")

        if self.select_options:
            option_height = 25
            start_y = 250
            for i, opt in enumerate(self.select_options):
                btn_rect = QRect(15, start_y + i*(option_height+5), 250, option_height)
                painter.setBrush(QColor(0,128,255) if i == self.selected_option else QColor(100,100,100))
                painter.drawRoundedRect(btn_rect, 4,4)
                painter.setPen(Qt.white)
                painter.setFont(QFont("微软雅黑", 9))
                painter.drawText(btn_rect, Qt.AlignCenter, opt["text"])

    def mousePressEvent(self, event):
        if not self.select_options:
            return
        option_height = 25
        start_y = 250
        for i, opt in enumerate(self.select_options):
            btn_rect = QRect(15, start_y + i*(option_height+5), 250, option_height)
            if btn_rect.contains(event.pos()):
                self.selected_option = i
                self.update()
                break

# ======================== 【主编辑器】 ========================
class StoryEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VGE剧本编辑器 - 专业拓展版")
        screen = QApplication.primaryScreen().availableGeometry()
        window_width = min(screen.width() * 0.9, 1400)
        window_height = min(screen.height() * 0.9, 850)
        self.setGeometry(
            (screen.width() - window_width) // 2,
            (screen.height() - window_height) // 2,
            window_width,
            window_height
        )
        
        self.script_data = {
            "version": "1.0",
            "defaultLabel": "start",
            "labels": {"start": []}
        }
        self.current_label = "start"
        self.preview_current_cmd_index = 0
        self.undo_stack = []
        self.redo_stack = []
        self.current_file = CONFIG.get("last_file")
        self.auto_save_timer = QTimer(self)
        self.auto_save_timer.timeout.connect(self.auto_save)
        self.auto_save_timer.start(30000)
        self.init_ui()
        self.bind_events()
        self.load_last_file()
        self.save_state()

    # 根据Y坐标找到对应Label
    def get_label_by_y(self, y_pos):
        label_nodes = []
        for item in self.scene.items():
            if isinstance(item, GraphicsNode) and item.node_type == "label":
                label_nodes.append( (item.pos().y(), item) )
        if not label_nodes:
            return None
        label_nodes.sort(key=lambda x: x[0])
        target_label = None
        for i in range(len(label_nodes)):
            label_y, label_node = label_nodes[i]
            next_label_y = label_nodes[i+1][0] if i+1 < len(label_nodes) else float('inf')
            if label_y <= y_pos < next_label_y:
                target_label = label_node
                break
        if not target_label:
            target_label = label_nodes[0][1]
        return target_label

    # 获取当前选中的节点
    def get_selected_node(self):
        items = self.scene.selectedItems()
        if len(items) == 1 and isinstance(items[0], GraphicsNode) and items[0].node_type == "command":
            return items[0]
        return None

    def init_ui(self):
        menubar = self.menuBar()
        
        file_menu = menubar.addMenu("文件(&F)")
        new_action = QAction("新建(&N)", self)
        new_action.setShortcut(QKeySequence.New)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)
        
        open_action = QAction("打开(&O)...", self)
        open_action.setShortcut(QKeySequence.Open)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        save_action = QAction("保存(&S)", self)
        save_action.setShortcut(QKeySequence.Save)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        save_as_action = QAction("另存为(&A)...", self)
        save_as_action.setShortcut(QKeySequence("Ctrl+Shift+S"))
        save_as_action.triggered.connect(self.save_file_as)
        file_menu.addAction(save_as_action)
        
        set_common_root_action = QAction("设置工作目录(&W)...", self)
        set_common_root_action.triggered.connect(self.set_common_root)
        file_menu.addAction(set_common_root_action)
        
        file_menu.addSeparator()
        export_action = QAction("导出游戏剧本(&E)...", self)
        export_action.triggered.connect(self.export_json)
        file_menu.addAction(export_action)
        file_menu.addSeparator()
        exit_action = QAction("退出(&X)", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        edit_menu = menubar.addMenu("编辑(&E)")
        self.undo_action = QAction("撤销(&U)", self)
        self.undo_action.setShortcut(QKeySequence.Undo)
        self.undo_action.triggered.connect(self.undo)
        self.undo_action.setEnabled(False)
        edit_menu.addAction(self.undo_action)
        
        self.redo_action = QAction("重做(&R)", self)
        self.redo_action.setShortcut(QKeySequence.Redo)
        self.redo_action.triggered.connect(self.redo)
        self.redo_action.setEnabled(False)
        edit_menu.addAction(self.redo_action)
        
        view_menu = menubar.addMenu("视图(&V)")
        refresh_action = QAction("刷新流程图(&F)", self)
        refresh_action.setShortcut(QKeySequence("F5"))
        refresh_action.triggered.connect(self.refresh_flowchart_from_json)
        view_menu.addAction(refresh_action)
        
        help_menu = menubar.addMenu("帮助(&H)")
        about_action = QAction("关于(&A)...", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
        toolbar = QToolBar("主工具栏")
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)
        toolbar.addSeparator()
        toolbar.addAction(self.undo_action)
        toolbar.addAction(self.redo_action)
        toolbar.addSeparator()
        toolbar.addAction(refresh_action)
        toolbar.addSeparator()
        
        self.btn_prev_step = QAction("⏮️ 上一步", self)
        self.btn_prev_step.triggered.connect(self.simulate_prev_click)
        toolbar.addAction(self.btn_prev_step)
        
        self.btn_reset_preview = QAction("🔄 重置预览", self)
        self.btn_reset_preview.triggered.connect(self.reset_preview)
        toolbar.addAction(self.btn_reset_preview)
        
        self.btn_next_step = QAction("⏭️ 下一步", self)
        self.btn_next_step.triggered.connect(self.simulate_click)
        toolbar.addAction(self.btn_next_step)
        toolbar.addSeparator()
        
        self.label_preview_combo = QComboBox()
        self.label_preview_combo.setFixedWidth(120)
        toolbar.addWidget(QLabel("预览Label："))
        toolbar.addWidget(self.label_preview_combo)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(6,6,6,6)
        main_layout.setSpacing(6)

        left_group = QGroupBox("流程图分支编辑器")
        left_layout = QVBoxLayout(left_group)
        left_layout.setContentsMargins(6,6,6,6)
        self.scene = QGraphicsScene()
        self.graphics_view = QGraphicsView(self.scene)
        self.graphics_view.setDragMode(QGraphicsView.ScrollHandDrag)
        self.graphics_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.graphics_view.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.graphics_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.graphics_view.setRenderHint(QPainter.Antialiasing)
        left_layout.addWidget(self.graphics_view)
        main_layout.addWidget(left_group, 2)

        mid_group = QGroupBox("完整剧本JSON代码区")
        mid_layout = QVBoxLayout(mid_group)
        mid_layout.setContentsMargins(6,6,6,6)
        self.json_edit = QTextEdit()
        self.json_edit.setFont(QFont("Consolas", 10))
        self.json_edit.textChanged.connect(self.on_code_changed)
        mid_layout.addWidget(self.json_edit)
        self.btn_refresh_flow = QPushButton("🔄 刷新流程图（从代码生成）")
        self.btn_refresh_flow.clicked.connect(self.refresh_flowchart_from_json)
        mid_layout.addWidget(self.btn_refresh_flow)
        main_layout.addWidget(mid_group, 3)

        right_layout = QVBoxLayout()
        right_layout.setSpacing(6)
        
        preview_group = QGroupBox("游戏实时渲染预览")
        preview_layout = QVBoxLayout(preview_group)
        preview_layout.setContentsMargins(6,6,6,6)
        self.preview = PreviewRenderer()
        preview_layout.addWidget(self.preview, alignment=Qt.AlignCenter)
        right_layout.addWidget(preview_group, 2)

        cmd_group = QGroupBox("快捷指令插入")
        cmd_layout = QVBoxLayout(cmd_group)
        cmd_layout.setContentsMargins(6,6,6,6)
        cmd_layout.setSpacing(4)
        btn_config = [
            ("Label节点", "label", '{"type":"label","params":{"name":"new_label"}}'),
            ("背景bg", "bg", '{"type":"bg","params":{"path":"/common/gaming/bg/default.png"}}'),
            ("立绘chara", "chara", '{"type":"chara","params":{"path":"/common/empty.png"}}'),
            ("对话text", "text", '{"type":"text","params":{"speaker":"真寻","content":"输入对话"}}'),
            ("人物动画ani", "ani", '{"type":"ani","params":{"name":"shakex"}}'),
            ("背景动画bg_ani", "bg_ani", '{"type":"bg_ani","params":{"name":"shakex"}}'),
            ("选项select", "select", '{"type":"select","params":{"options":[{"text":"选项1","targetLabel":"label1"}]}}'),
            ("等待wait", "wait", '{"type":"wait"}'),
            ("跳转goto", "goto", '{"type":"goto","params":{"label":"target"}}'),
            ("warp", "warp", '{"type":"warp","params":{"path":"targetPath"}}'),
            ("结束end", "end", '{"type":"end"}')
        ]
        for name, cmd_type, cmd_str in btn_config:
            btn = QPushButton(name)
            btn.setFixedHeight(24)
            btn.clicked.connect(lambda checked, t=cmd_type, s=cmd_str: self.insert_command(t, s))
            cmd_layout.addWidget(btn)
        self.btn_export = QPushButton("📤 导出游戏剧本")
        self.btn_export.clicked.connect(self.export_json)
        cmd_layout.addWidget(self.btn_export)
        right_layout.addWidget(cmd_group, 1)

        main_layout.addLayout(right_layout, 2)

        self.refresh_json_view()
        self.refresh_flowchart_from_json()

    def bind_events(self):
        self.graphics_view.customContextMenuRequested.connect(self.show_right_menu)
        self.scene.selectionChanged.connect(self.on_node_selected)
        self.scene.changed.connect(self.on_scene_changed)

    def load_last_file(self):
        if self.current_file and os.path.exists(self.current_file):
            try:
                with open(self.current_file, "r", encoding="utf-8") as f:
                    self.script_data = json.load(f)
                self.refresh_json_view()
                self.refresh_flowchart_from_json()
                self.save_state()
                self.setWindowTitle(f"VGE剧本编辑器 - {os.path.basename(self.current_file)}")
            except Exception as e:
                QMessageBox.warning(self, "警告", f"加载上次文件失败：{str(e)}")
                self.current_file = None

    def auto_save(self):
        if self.current_file:
            try:
                with open(self.current_file, "w", encoding="utf-8") as f:
                    json.dump(self.script_data, f, ensure_ascii=False, indent=2)
            except:
                pass

    def set_common_root(self):
        global GAME_COMMON_ROOT, RESOURCE_CONTAINERS
        path = QFileDialog.getExistingDirectory(self, "选择/common目录", GAME_COMMON_ROOT)
        if path:
            GAME_COMMON_ROOT = path
            RESOURCE_CONTAINERS = {
                "bg": {
                    "game_path": "/common/gaming/bg/",
                    "local_path": os.path.join(GAME_COMMON_ROOT, "gaming", "bg")
                },
                "chara": {
                    "game_path": "/common/chara/",
                    "local_path": os.path.join(GAME_COMMON_ROOT, "chara")
                }
            }
            CONFIG["common_root"] = path
            save_config(CONFIG)
            QMessageBox.information(self, "成功", "工作目录已更新，重启软件后生效")

    def save_state(self):
        state = json.dumps(self.script_data, ensure_ascii=False)
        self.undo_stack.append(state)
        self.redo_stack.clear()
        self.update_undo_redo_actions()
        if len(self.undo_stack) > 50:
            self.undo_stack.pop(0)

    def undo(self):
        if len(self.undo_stack) <= 1:
            return
        current_state = json.dumps(self.script_data, ensure_ascii=False)
        self.redo_stack.append(current_state)
        prev_state = self.undo_stack[-2]
        self.undo_stack.pop()
        self.script_data = json.loads(prev_state)
        self.refresh_json_view()
        self.refresh_flowchart_from_json()
        self.update_undo_redo_actions()

    def redo(self):
        if not self.redo_stack:
            return
        current_state = json.dumps(self.script_data, ensure_ascii=False)
        self.undo_stack.append(current_state)
        next_state = self.redo_stack.pop()
        self.script_data = json.loads(next_state)
        self.refresh_json_view()
        self.refresh_flowchart_from_json()
        self.update_undo_redo_actions()

    def update_undo_redo_actions(self):
        self.undo_action.setEnabled(len(self.undo_stack) > 1)
        self.redo_action.setEnabled(len(self.redo_stack) > 0)

    def new_file(self):
        if self.undo_stack and len(self.undo_stack) > 1:
            reply = QMessageBox.question(
                self, "新建", "是否保存当前文件？",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
            )
            if reply == QMessageBox.Yes:
                self.save_file()
            elif reply == QMessageBox.Cancel:
                return
        
        self.script_data = {
            "version": "1.0",
            "defaultLabel": "start",
            "labels": {"start": []}
        }
        self.current_file = None
        self.undo_stack.clear()
        self.redo_stack.clear()
        self.refresh_json_view()
        self.refresh_flowchart_from_json()
        self.save_state()
        self.setWindowTitle("VGE剧本编辑器 - 专业拓展版")

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "打开剧本", "", "JSON文件 (*.json);;所有文件 (*.*)"
        )
        if not path:
            return
        
        try:
            with open(path, "r", encoding="utf-8") as f:
                self.script_data = json.load(f)
            self.current_file = path
            CONFIG["last_file"] = path
            save_config(CONFIG)
            self.undo_stack.clear()
            self.redo_stack.clear()
            self.refresh_json_view()
            self.refresh_flowchart_from_json()
            self.save_state()
            self.setWindowTitle(f"VGE剧本编辑器 - {os.path.basename(path)}")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"打开文件失败：{str(e)}")

    def save_file(self):
        if not self.current_file:
            self.save_file_as()
            return
        
        try:
            with open(self.current_file, "w", encoding="utf-8") as f:
                json.dump(self.script_data, f, ensure_ascii=False, indent=2)
            CONFIG["last_file"] = self.current_file
            save_config(CONFIG)
            self.save_state()
        except Exception as e:
            QMessageBox.critical(self, "错误", f"保存文件失败：{str(e)}")

    def save_file_as(self):
        path, _ = QFileDialog.getSaveFileName(
            self, "另存为", "", "JSON文件 (*.json);;所有文件 (*.*)"
        )
        if not path:
            return
        
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.script_data, f, ensure_ascii=False, indent=2)
            self.current_file = path
            CONFIG["last_file"] = path
            save_config(CONFIG)
            self.save_state()
            self.setWindowTitle(f"VGE剧本编辑器 - {os.path.basename(path)}")
        except Exception as e:
            QMessageBox.critical(self, "错误", f"保存文件失败：{str(e)}")

    def show_about(self):
        dialog = AboutDialog(self)
        dialog.exec_()

    def show_right_menu(self, pos):
        menu = QMenu()
        scene_pos = self.graphics_view.mapToScene(pos)
        menu.addAction("➕ 添加Label节点", lambda: self.add_label_node(scene_pos))
        menu.addAction("➕ 添加text指令", lambda: self.add_cmd_node(scene_pos, "text"))
        menu.addAction("➕ 添加bg指令", lambda: self.add_cmd_node(scene_pos, "bg"))
        menu.addAction("➕ 添加chara指令", lambda: self.add_cmd_node(scene_pos, "chara"))
        menu.addAction("➕ 添加select选项", lambda: self.add_cmd_node(scene_pos, "select"))
        menu.addAction("➕ 添加warp指令", lambda: self.add_cmd_node(scene_pos, "warp"))
        menu.addAction("➕ --添加wait指令--", lambda: self.add_cmd_node(scene_pos, "wait"))

        selected = self.scene.selectedItems()
        if len(selected) == 1 and isinstance(selected[0], GraphicsNode) and selected[0].node_type == "command":
            node = selected[0]
            cmd_type = node.data.get("type")
            if cmd_type == "bg":
                menu.addAction("🖼️ 选择背景图片", lambda: self.pick_image(node, "bg"))
            elif cmd_type == "chara":
                menu.addAction("👤 选择立绘图片", lambda: self.pick_image(node, "chara"))

        if len(selected) == 2 and all(isinstance(x, GraphicsNode) for x in selected):
            if all(x.node_type == "label" for x in selected):
                menu.addAction("🔗 连接Label（生成goto）", lambda: self.connect_nodes(selected[0], selected[1]))
        if len(selected) == 1:
            menu.addAction("🗑️ 删除选中", self.delete_selected_item)
        menu.exec_(self.graphics_view.viewport().mapToGlobal(pos))

    def pick_image(self, node, container_type):
        dialog = ImagePickerDialog(container_type, self)
        if dialog.exec_() and dialog.selected_path:
            game_path = local_path_to_game(dialog.selected_path)
            node.data["params"]["path"] = game_path
            node.title = node._get_cmd_title()
            self.on_scene_changed([])
            self.update_preview_from_node(node)
            node.update()

    def add_label_node(self, pos):
        label_name = f"label_{len(self.script_data['labels'])}"
        node = GraphicsNode(node_type="label", label_name=label_name)
        node.setPos(pos)
        self.scene.addItem(node)
        self.script_data["labels"][label_name] = []
        self.refresh_json_view()
        self.refresh_flowchart_from_json()
        self.save_state()

    # ✅ 修复：新增节点优先在选中节点下方追加
    def add_cmd_node(self, pos, cmd_type):
        cmd_map = {
            "text": {"type":"text","params":{"speaker":"真寻","content":"新对话"}},
            "bg": {"type":"bg","params":{"path":"/common/gaming/bg/default.png"}},
            "chara": {"type":"chara","params":{"path":"/common/empty.png"}},
            "select": {"type":"select","params":{"options":[{"text":"选项1","targetLabel":"label1"}]}},
            "warp": {"type":"warp","params":{"path":"targetPath"}},
            "wait": {"type":"wait"}
        }
        cmd = cmd_map.get(cmd_type, {})

        # 优先判断是否有选中的节点
        selected_node = self.get_selected_node()
        if selected_node:
            # 用选中节点的Label
            label_name = selected_node.label_name
            # 插入到选中节点的下一个位置
            insert_index = selected_node.cmd_index + 1
            # 位置放在选中节点的下方
            new_y = selected_node.pos().y() + 60
        else:
            # 无选中节点时，按点击位置找Label
            target_label_node = self.get_label_by_y(pos.y())
            if not target_label_node:
                QMessageBox.warning(self, "警告", "请先创建Label节点！")
                return
            label_name = target_label_node.label_name
            insert_index = 0
            new_y = pos.y()

        # 创建节点
        node = GraphicsNode(node_type="command", label_name=label_name, cmd_index=insert_index)
        node.data = cmd
        node.title = node._get_cmd_title()
        node.setPos(200, new_y)
        self.scene.addItem(node)

        # 插入到对应位置
        self.script_data["labels"][label_name].insert(insert_index, cmd)
        self.refresh_json_view()
        self.scroll_to_node(node)
        self.save_state()

    def connect_nodes(self, n1, n2):
        if n1.node_type != "label" or n2.node_type != "label":
            QMessageBox.warning(self, "警告", "只能连接Label节点！")
            return
        conn = GraphicsConnection(n1, n2)
        self.scene.addItem(conn)
        goto_cmd = {"type":"goto","params":{"label":n2.label_name}}
        self.script_data["labels"][n1.label_name].append(goto_cmd)
        self.refresh_json_view()
        self.refresh_flowchart_from_json()
        self.save_state()

    def delete_selected_item(self):
        for item in self.scene.selectedItems():
            if isinstance(item, GraphicsNode) and item.node_type == "command":
                if item.label_name and item.cmd_index is not None:
                    del self.script_data["labels"][item.label_name][item.cmd_index]
            elif isinstance(item, GraphicsNode) and item.node_type == "label":
                del self.script_data["labels"][item.label_name]
            self.scene.removeItem(item)
        self.refresh_json_view()
        self.refresh_flowchart_from_json()
        self.save_state()

    def scroll_to_node(self, node):
        if node.node_type != "command" or node.label_name is None or node.cmd_index is None:
            return
        json_text = self.json_edit.toPlainText()
        lines = json_text.splitlines()
        label_line = -1
        cmd_line = -1
        for i, line in enumerate(lines):
            if f'"{node.label_name}":' in line:
                label_line = i
                break
        if label_line != -1:
            brace_count = 0
            for i in range(label_line, len(lines)):
                if '[' in lines[i]:
                    brace_count += 1
                if ']' in lines[i]:
                    brace_count -= 1
                if '{' in lines[i] and brace_count == 2:
                    if node.cmd_index == 0:
                        cmd_line = i
                        break
                    node.cmd_index -= 1
        if cmd_line != -1:
            cursor = self.json_edit.textCursor()
            cursor.setPosition(len("\n".join(lines[:cmd_line])) + 1)
            self.json_edit.setTextCursor(cursor)
            self.json_edit.ensureCursorVisible()

    def refresh_json_view(self):
        self.json_edit.blockSignals(True)
        self.json_edit.setPlainText(json.dumps(self.script_data, ensure_ascii=False, indent=2))
        self.json_edit.blockSignals(False)

    def refresh_flowchart_from_json(self):
        self.scene.clear()
        y_pos = 40
        label_spacing = 110
        cmd_spacing = 60
        max_y = 0

        for label_name, cmds in self.script_data["labels"].items():
            label_node = GraphicsNode(node_type="label", label_name=label_name)
            label_node.setPos(40, y_pos)
            self.scene.addItem(label_node)
            cmd_y = y_pos
            for idx, cmd in enumerate(cmds):
                if cmd["type"] == "label":
                    continue
                cmd_node = GraphicsNode(node_type="command", label_name=label_name, cmd_index=idx)
                cmd_node.data = cmd
                cmd_node.title = cmd_node._get_cmd_title()
                cmd_node.color = cmd_node._get_cmd_color()
                cmd_node.setPos(200, cmd_y)
                self.scene.addItem(cmd_node)
                cmd_y += cmd_spacing
            y_pos += label_spacing + len(cmds)*cmd_spacing
            max_y = max(max_y, y_pos)

        self.scene.setSceneRect(0, 0, 1000, max_y + 80)
        
        self.label_preview_combo.blockSignals(True)
        self.label_preview_combo.clear()
        self.label_preview_combo.addItems(self.script_data["labels"].keys())
        self.label_preview_combo.blockSignals(False)

    def on_code_changed(self):
        try:
            data = json.loads(self.json_edit.toPlainText())
            self.script_data = data
            self.update_preview_from_code()
        except:
            pass

    def on_scene_changed(self, regions):
        label_cmd_map = {}
        for item in self.scene.items():
            if isinstance(item, GraphicsNode) and item.node_type == "command":
                if item.label_name not in label_cmd_map:
                    label_cmd_map[item.label_name] = []
                label_cmd_map[item.label_name].append(item)
        for label_name, nodes in label_cmd_map.items():
            nodes.sort(key=lambda n: n.pos().y())
            new_cmds = []
            for node in nodes:
                new_cmds.append(node.data)
                node.cmd_index = len(new_cmds)-1
            self.script_data["labels"][label_name] = new_cmds
        self.refresh_json_view()
        self.save_state()

    def reset_preview(self):
        self.preview.update_preview(
            "/common/main_page_img/bg.png",
            "/common/empty.png",
            "",
            "预览已重置",
            "",
            "",
            [],
            False
        )
        self.preview_current_cmd_index = 0

    def simulate_click(self):
        label_name = self.label_preview_combo.currentText() or self.current_label
        cmds = self.script_data["labels"].get(label_name, [])
        if not cmds:
            self.reset_preview()
            return

        if self.preview.select_options and self.preview.selected_option >= 0:
            target_label = self.preview.select_options[self.preview.selected_option]["targetLabel"]
            self.label_preview_combo.setCurrentText(target_label)
            self.preview_current_cmd_index = 0
            return

        while self.preview_current_cmd_index < len(cmds):
            cmd = cmds[self.preview_current_cmd_index]
            self.update_preview_to_step(label_name, self.preview_current_cmd_index)
            self.preview_current_cmd_index += 1
            if cmd["type"] in ["wait", "select", "end", "warp"]:
                break
        if self.preview_current_cmd_index >= len(cmds):
            self.preview_current_cmd_index = 0

    def simulate_prev_click(self):
        if self.preview_current_cmd_index > 0:
            self.preview_current_cmd_index -= 1
            self.update_preview_to_step(self.label_preview_combo.currentText() or self.current_label, self.preview_current_cmd_index)
        else:
            self.reset_preview()

    def change_preview_label(self, label_name):
        self.preview_current_cmd_index = 0
        self.update_preview_to_step(label_name, 0)

    def update_preview_to_step(self, label_name, step):
        cmds = self.script_data["labels"].get(label_name, [])
        if not cmds:
            self.reset_preview()
            return

        bg = "/common/main_page_img/bg.png"
        chara = "/common/empty.png"
        speaker = ""
        content = ""
        ani = ""
        bg_ani = ""
        select_options = []
        show_ani_indicator = False

        for i in range(step + 1):
            if i >= len(cmds):
                break
            cmd = cmds[i]
            if cmd["type"] == "bg":
                bg = cmd["params"]["path"]
            elif cmd["type"] == "chara":
                chara = cmd["params"]["path"]
            elif cmd["type"] == "text":
                speaker = cmd["params"]["speaker"]
                content = cmd["params"]["content"]
            elif cmd["type"] == "ani":
                ani = cmd["params"]["name"]
            elif cmd["type"] == "bg_ani":
                bg_ani = cmd["params"]["name"]
            elif cmd["type"] == "select":
                select_options = cmd["params"]["options"]
            elif cmd["type"] == "wait":
                if i > 0:
                    prev_cmd = cmds[i-1]
                    if prev_cmd["type"] in ["ani", "bg_ani"]:
                        show_ani_indicator = True
            elif cmd["type"] == "warp":
                target = cmd["params"]["path"]
                if target in self.script_data["labels"]:
                    self.label_preview_combo.setCurrentText(target)
                    self.preview_current_cmd_index = 0
                    return

        self.preview.update_preview(bg, chara, speaker, content, ani, bg_ani, select_options, show_ani_indicator)

    def on_node_selected(self):
        items = self.scene.selectedItems()
        if not items or len(items) != 1:
            return
        node = items[0]
        if not isinstance(node, GraphicsNode):
            return
        self.update_preview_from_node(node)
        self.scroll_to_node(node)

    def update_preview_from_node(self, node):
        if node.node_type != "command" or "type" not in node.data:
            return
        cmd = node.data
        bg, chara, speaker, content, ani, bg_ani, select_options = "/common/bg.png", "/common/empty.png", "", "", "", "", []
        if cmd["type"] == "bg": bg = cmd["params"]["path"]
        if cmd["type"] == "chara": chara = cmd["params"]["path"]
        if cmd["type"] == "text":
            speaker = cmd["params"]["speaker"]
            content = cmd["params"]["content"]
        if cmd["type"] == "ani": ani = cmd["params"]["name"]
        if cmd["type"] == "bg_ani": bg_ani = cmd["params"]["name"]
        if cmd["type"] == "select": select_options = cmd["params"]["options"]
        self.preview.update_preview(bg, chara, speaker, content, ani, bg_ani, select_options, False)

    def update_preview_from_code(self):
        try:
            cmds = self.script_data["labels"][self.current_label]
            if cmds:
                self.update_preview_from_node(GraphicsNode("command", label_name=self.current_label, cmd_index=0, data=cmds[-1]))
        except:
            pass

    def insert_command(self, cmd_type, cmd_str):
        cmd = json.loads(cmd_str)
        # 优先在选中节点下方插入
        selected_node = self.get_selected_node()
        if selected_node:
            label_name = selected_node.label_name
            insert_index = selected_node.cmd_index + 1
            self.script_data["labels"][label_name].insert(insert_index, cmd)
        else:
            # 无选中节点时，插入到当前默认Label的末尾
            self.script_data["labels"][self.current_label].append(cmd)
        self.refresh_json_view()
        self.refresh_flowchart_from_json()
        self.save_state()

    def export_json(self):
        path, _ = QFileDialog.getSaveFileName(
            self, 
            "导出剧本", 
            "gamedata1.txt", 
            "剧本文件 (*.txt);;JSON文件 (*.json);;所有文件 (*.*)"
        )
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.script_data, f, ensure_ascii=False, indent=2)
            QMessageBox.information(self, "成功", f"剧本导出完成！\n文件：{path}\n直接放入游戏即可运行！")
        except Exception as e:
            QMessageBox.critical(self, "失败", str(e))

    def closeEvent(self, event):
        if self.undo_stack and len(self.undo_stack) > 1:
            reply = QMessageBox.question(
                self, "退出", "是否保存当前文件？",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
            )
            if reply == QMessageBox.Yes:
                self.save_file()
                event.accept()
            elif reply == QMessageBox.No:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

# ======================== 启动程序 ========================
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(DARK_STYLE)
    window = StoryEditor()
    window.show()
    sys.exit(app.exec_())