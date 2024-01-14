# histoColorbar
    Erstellt ein Histogramm mit einer angehängten Farbskala (Colorbar) in einem Matplotlib-Achsenobjekt.

# Histogramm mit Farbskala in Matplotlib

Dieses Projekt beinhaltet die `histoColorbar`-Funktion, welche ein Histogramm mit einer angehängten Farbskala (Colorbar) in einem Matplotlib-Achsenobjekt erstellt. Die Funktion ist nützlich für die visuelle Datenanalyse und ermöglicht eine intuitive Darstellung der Datenverteilung.

## Funktionsbeschreibung

Die `histColorbar`-Funktion erstellt ein Histogramm der übergebenen Daten und fügt eine Farbskala hinzu, die der Datenverteilung entspricht. Die Farben des Histogramms korrespondieren mit den Farben der Farbskala. Diese Funktion ist besonders nützlich in der Datenvisualisierung und im wissenschaftlichen Kontext.

## Voraussetzungen

Um diese Funktion verwenden zu können, müssen Sie über eine Python-Umgebung mit installierten Paketen `matplotlib` und `numpy` verfügen.


## Verwendung

Um die histColorbar-Funktion zu verwenden, importieren Sie diese in Ihr Python-Skript oder Ihre Jupyter-Notebook-Umgebung. Hier ist ein einfaches Beispiel, wie die Funktion genutzt werden kann:

import matplotlib.pyplot as plt
import numpy as np
from histColorbar import histColorbar  # Angenommen, die Funktion befindet sich in der Datei histColorbar.py

```python
from histoColorbar import histoColorbar

# Daten für das Histogramm
data = np.random.normal(size=1000)

# Erstellen einer Matplotlib-Figur und eines Achsenobjekts
fig, ax = plt.subplots()

# Verwenden der histColorbar-Funktion
histoColorbar(ax, data)

# Anzeigen des Plots
plt.show()
```
## Installation über pip

```bash
pip install git+https://github.com/quojus/histoColorbar.git

```
