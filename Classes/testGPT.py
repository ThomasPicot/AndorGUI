import pyqtgraph as pg
from PyQt5.QtGui import QTransform

# Créer un widget de tracé
plotWidget = pg.PlotWidget()

# Ajouter un tracé quelconque (pour illustrer)
plotWidget.plot([1, 2, 3, 4], [1, 2, 3, 4])

# Créer une transformation pour faire pivoter de 90 degrés dans le sens horaire
rotation = QTransform().rotate(90)

# Appliquer la transformation au widget de tracé
plotWidget.setTransform(rotation)

# Afficher le widget de tracé
plotWidget.show()
