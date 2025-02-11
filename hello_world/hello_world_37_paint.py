# In this example, we draw text in Russian Cylliric.

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

# 写了一些文本上下居中对齐的俄罗斯Cylliric语言的文字

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.text = "Лев Николаевич Толстой\nАнна Каренина"

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Drawing text')
        self.show()

    # 在绘画事件内完成绘画动作
    # QPainter是低级的绘画类。所有的绘画动作都在这个类的begin()和end()方法之间完成，绘画动作都封装在drawText()内部了
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        # 为文字绘画定义了笔和字体
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        # drawText()方法在窗口里绘制文本，rect()方法返回要更新的矩形区域
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())