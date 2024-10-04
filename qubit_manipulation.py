import pennylane as qc

dev = qc.device("default.qubit", wires=3)
@qc.qnode(dev)
def circuit():

# STEP 1 to get PSI1
  qc.PauliX(wires = 0) 
  qc.PauliX(wires = 2)
# STEP 2 to get PSI2
  qc.Hadamard(wires = 1)
# STEP 3 to get PSI3
  qc.PauliX(wires = 1)
# STEP 4 to get PSI4
  qc.CNOT(wires = [0,2])

  return qc.state()

probability_amplitudes= circuit()
basis_states = ['|000>', '|001>', '|010>', '|011>', '|100>', '|101>', '|110>', '|111>']

for i in range(0 , 2**3):
    print( 'Probability amplitude for the basis state ' +  basis_states[i]  + ' is ' + str(probability_amplitudes[i]) )

print()
print("The circuit diagrgam for the qubit manipulation is -")  
print(qc.draw(circuit)())

 