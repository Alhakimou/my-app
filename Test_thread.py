import threading
import time

def tache1():
    for i in range(5):
        print("Run Task 1:", i)
        time.sleep(5)

def tache2():
    for i in range(5):
        print("Executer Tâche 2:", i)
        time.sleep(5)
def tache3():
    for i in range(5):
        print("Run Task 3:", i)
        time.sleep(5)

# Création des threads
thread1 = threading.Thread(target=tache1)
thread2 = threading.Thread(target=tache2)
thread3 = threading.Thread(target=tache3)

# Démarrage des threads
thread1.start()
thread2.start()
thread3.start()
# Attendre que les threads finissent
thread1.join()
thread2.join()
thread3.join()

print("Toutes les tâches sont terminées.")
