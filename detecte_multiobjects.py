import cv2
from ultralytics import YOLO

# 1. Charger le modèle pré-entraîné (téléchargement automatique au 1er lancement)
model = YOLO("yolov8n.pt") 

# 2. Accéder à la caméra du laptop (0 est généralement l'ID par défaut)
cap = cv2.VideoCapture(0)

print("Appuyez sur 'q' pour quitter l'application.")

while cap.isOpened():
    # Lire une image de la caméra
    success, frame = cap.read()
    
    if success:
        # 3. Lancer la détection et le suivi (persist=True garde l'ID de l'objet)
        results = model.track(frame, persist=True, verbose=False)
        
        # 4. Dessiner les boîtes et les noms sur l'image
        annotated_frame = results[0].plot()
        
        # Afficher le résultat dans une fenêtre
        cv2.imshow("Suivi d'objets - Caméra Laptop", annotated_frame)
        
        # Quitter si on appuie sur la touche 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Libérer la caméra et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()
