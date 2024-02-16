import sys
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget

class ROIExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = pg.GraphicsLayoutWidget()
        self.setCentralWidget(self.central_widget)

        self.plot_item = self.central_widget.addPlot(title="ROI Example")
        self.image_data = np.random.rand(100, 100)  # Example image data
        self.image_item = pg.ImageItem(self.image_data)
        self.plot_item.addItem(self.image_item)

        self.roi = None  # ROI is initially None
        self.normalization_button = QPushButton("Toggle Normalization")
        self.normalization_button.clicked.connect(self.toggle_normalization)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.central_widget)
        layout.addWidget(self.normalization_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def toggle_normalization(self):
        if self.roi is None:
            # Create ROI the first time the button is clicked
            self.roi = pg.RectROI([20, 20], [30, 30], pen=(0, 9))
            self.plot_item.addItem(self.roi)
            self.roi.sigRegionChangeFinished.connect(self.roi_changed)
        else:
            # Toggle ROI visibility
            self.roi.setVisible(not self.roi.isVisible())

    def roi_changed(self):
        roi_pos = self.roi.pos()
        roi_size = self.roi.size()

        # Extract the region within the ROI
        x, y, w, h = roi_pos[0], roi_pos[1], roi_size[0], roi_size[1]
        roi_data = self.image_data[int(y):int(y + h), int(x):int(x + w)]

        # Calculate the mean of all points within the ROI
        roi_mean = np.mean(roi_data)

        # Divide the entire image by the mean of the ROI
        normalized_image_data = self.image_data / roi_mean

        # Update the image item with the normalized data
        self.image_item.setImage(normalized_image_data)

def main():
    app = QApplication(sys.argv)
    window = ROIExample()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
