import numpy as np
from numpy import pi
# importing Qiskit
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor
from qiskit.visualization import plot_histogram, plot_bloch_multivector


#### Se Carga la cuenta para poder realizar las simulaciones
#IBMQ.load_account()
###


# Librerías estandar de Qiskit
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from qiskit import *

#Librería para optimizar el circuito que se diseñe
from qiskit.compiler import transpile, assemble

#Librerias para el trabajo en el dispositivo real
from qiskit.tools.monitor import job_monitor
from qiskit import IBMQ

#Librerias para la visualización por medio de la esfera de Bloch y de histogramas
from qiskit.tools.visualization import plot_bloch_multivector
from qiskit.tools.visualization import plot_histogram
from qiskit.tools.visualization import plot_state_city

## Librerías para la visualización de Vectores y matrices
###Display usando markdown
import numpy as np
from IPython.display import display, Markdown, Latex
from array_to_latex import to_ltx
###Otros Display
from herramientas.tools import vector2latex
from herramientas.learn_quantum import format_state_vector
from herramientas.learn_quantum import print_short_state_vector
from herramientas.tools import unitary2latex
from herramientas.tools import unitary2latex2 #Funcion creada para poder visualizar la parte imaginaria

