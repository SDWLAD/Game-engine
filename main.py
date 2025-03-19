from PyQt6.QtWidgets import QApplication, QWidget
import sys

def main():
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("PyQt6 Template")
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
