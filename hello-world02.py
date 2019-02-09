# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl

app = QApplication([])
view = QQuickView()
url = QUrl("view-of-hello-world02.qml")

view.setSource(url)
# Windowをリサイズした際の挙動を指定。以下の場合、QMLファイルのルートオブジェクトをビュー(ウィンドウ)のサイズに合わせてリサイズする
view.setResizeMode(QQuickView.SizeRootObjectToView)
view.show()
app.exec_()
