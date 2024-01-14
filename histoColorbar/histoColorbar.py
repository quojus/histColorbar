import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib import cm
from mpl_toolkits.axes_grid1 import make_axes_locatable

def histoColorbar(ax, data, binBreit=20, label=None, cmap=cm.viridis, breite_his_bar=(5, 2)):
    """
    Erstellt ein Histogramm mit einer angehängten Farbskala (Colorbar) in einem Matplotlib-Achsenobjekt.

    Argumente:
    ax (matplotlib.axes.Axes): Das Achsenobjekt, in dem das Histogramm und die Farbskala angezeigt werden sollen.
    data (Array-ähnlich): Die Daten, für die das Histogramm erstellt wird.
    binBreit (int, optional): Anzahl der Bins für das Histogramm. Standardwert ist 20.
    label (str, optional): Label für die Farbskala. Wenn None, wird kein Label angezeigt.
    cmap (str oder matplotlib.colors.Colormap, optional): Die zu verwendende Farbkarte. Kann ein String (Name der Farbkarte) oder ein Colormap-Objekt sein. Standardwert ist 'viridis'.
    breite_his_bar (tuple of (int, float), optional): Tuple, das die Breiten des Histogramms und der Farbskala in Prozent angibt. Standardwert ist (5, 2).

    Rückgabewert:
    matplotlib.colorbar.Colorbar: Das Colorbar-Objekt, das die Farbskala darstellt.
    """

    # Überprüfung des ax-Arguments
    if not isinstance(ax, plt.Axes):
        raise ValueError("ax muss ein Matplotlib Axes-Objekt sein")

    # Überprüfung des data-Arguments
    if not isinstance(data, (list, np.ndarray)):
        raise ValueError("data muss ein Array-ähnliches Objekt sein")

    # Überprüfung des binBreit-Arguments
    if not isinstance(binBreit, int):
        raise ValueError("binBreit muss ein Integer sein")

    # Überprüfung des label-Arguments
    if label is not None and not isinstance(label, str):
        raise ValueError("label muss ein String sein, falls angegeben")

    # Überprüfung des cmap-Arguments
    if not isinstance(cmap, (str, cm._colormaps)):
        raise ValueError("cmap muss ein String oder ein Matplotlib Colormap-Objekt sein")

    # Überprüfung des breite_his_bar-Arguments
    if not (isinstance(breite_his_bar, tuple) and len(breite_his_bar) == 2 and 
            all(isinstance(x, (int, float)) for x in breite_his_bar)):
        raise ValueError("breite_his_bar muss ein Tuple aus zwei Zahlen sein")

    # Berechnung des Histogramms aus den Daten
    hist_data, bin_edges = np.histogram(data, bins=binBreit, density=True)
    
    # Einstellen der Normalisierung für die Farbkarte
    norm = Normalize(vmin=data.min(), vmax=data.max())
    
    # Erhalten der Farbkarte, falls cmap ein String ist
    if isinstance(cmap, str):
        cmap = plt.get_cmap(cmap)
    
    # Zuordnung der Farben zu den Bins des Histogramms
    colors = cmap(norm(bin_edges[:-1]))
    
    # Aufteilung des Axes-Objekts für
    divider = make_axes_locatable(ax)

    # Erstellen der zusätzlichen Axes für Histogramm und Colorbar
    if len(breite_his_bar) == 2 and all(isinstance(x, (int, float)) for x in breite_his_bar):
        cax1 = divider.append_axes("right", size=f"{breite_his_bar[0]}%", pad=0.1)
        cax2 = divider.append_axes("right", size=f"{breite_his_bar[1]}%", pad=0)
    else:
        cax1 = divider.append_axes("right", size="5%", pad=0.1)
        cax2 = divider.append_axes("right", size="2%", pad=0)

    # Hinzufügen des Histogramms links neben der Farbskala
    ax1 = cax1
    ax1.barh(bin_edges[:-1], -hist_data, height=np.diff(bin_edges), color=colors, edgecolor='none', linewidth=0)
    verstz = ((data.min() - data.max()) / len(bin_edges)) * 0.5
    ax1.set_ylim(data.min() + verstz, data.max() + verstz)
    ax1.invert_xaxis()
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.invert_yaxis()

    # Umrandungen der Achse ax1 entfernen
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.axvline(0, color='black', linewidth=2)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['left'].set_visible(False)

    # Erstellen des Farbbalkens (Colorbar) und Anpassen der Breite
    norm = Normalize(vmin=data.min(), vmax=data.max())  # Erneutes Setzen der Normalisierung
    cb1 = plt.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), cax=cax2)  # Erstellen der Colorbar
    if label:
        cb1.set_label(label)  # Hinzufügen eines Labels, falls angegeben

    # Entfernen der Umrandung (Rahmen) der Colorbar
    cb1.outline.set_visible(False)

    return cb1

