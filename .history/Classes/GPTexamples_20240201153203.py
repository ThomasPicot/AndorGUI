import sys
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget

class ROIExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = pg.GraphicsLayoutWidget()
        self.setCentralWidget(self.central_widget)

        self.plot_item = self.central_widget.addPlot(title="Original Image")
        self.image_data = np.random.rand(100, 100)  # Example image data
        self.image_item = pg.ImageItem(self.image_data)
        self.plot_item.addItem(self.image_item)

        self.roi = pg.RectROI([20, 20], [30, 30], pen=(0, 9))  # Initial ROI position and size
        self.plot_item.addItem(self.roi)

        self.roi_plot_item = self.central_widget.addPlot(title="ROI Content")
        self.roi_plot_item.disableAutoRange('xy')  # Disable auto-scaling for ROI plot

        self.setCentralWidget(self.central_widget)

        # Connect signals
        self.roi.sigRegionChangeFinished.connect(self.roi_changed)

        # Add a normalization button
        self.normalization_button = QPushButton("Toggle Normalization")
        self.normalization_button.clicked.connect(self.toggle_roi_visibility)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.central_widget)
        layout.addWidget(self.normalization_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def roi_changed(self):
        roi_pos = self.roi.pos()
        roi_size = self.roi.size()

        # Extract the region within the ROI
        x, y, w, h = roi_pos[0], roi_pos[1], roi_size[0], roi_size[1]
        roi_data = self.image_data[int(y):int(y + h), int(x):int(x + w)]

        # Display the content of the ROI in a separate plot
        self.roi_plot_item.clear()
        self.roi_plot_item.plot(roi_data.flatten(), title="ROI Content")

    def toggle_roi_visibility(self):
        self.roi.setVisible(not self.roi.isVisible())


def main():
    app = QApplication(sys.argv)
    window = ROIExample()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
