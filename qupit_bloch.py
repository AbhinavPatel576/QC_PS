import pennylane as qc
import numpy as np
import qutip

dev=qc.device("default.qubit" , wires=1)

@qc.qnode(dev)
def circuit():
    qc.RY(np.pi*(3/4) , wires=0 )
    return qc.state()
psi = circuit()

fig= qutip.Bloch()
psi_obj= qutip.Qobj(psi)
fig.add_states(psi_obj)
fig.show()

