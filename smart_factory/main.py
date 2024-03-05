import os
import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from home_window import HomeWindow
from main_window import MainWindow
from admin_window import AdminWindow

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_widget = QStackedWidget()

    home = HomeWindow(main_widget)
    main = MainWindow(main_widget)
    admin = AdminWindow(main_widget)

    main_widget.addWidget(home)
    main_widget.addWidget(main)
    main_widget.addWidget(admin)

    main_widget.setCurrentIndex(0)
    main_widget.show()

    sys.exit(app.exec_())
