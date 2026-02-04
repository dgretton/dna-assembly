from pyhamilton import HamiltonInterface, initialize

with HamiltonInterface() as ham_int:
    initialize(ham_int, init_always=True)
    print("Initialization complete!")
