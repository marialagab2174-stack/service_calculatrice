# Challenge 2: Service Calculatrice (ROS 2)

Ce package implémente un serveur de calcul simple via les **Services ROS 2** pour une communication synchrone (requête-réponse).

## 📋 Spécifications
- **Nom du Service** : `/calcule`
- **Interface** : `example_interfaces/srv/AddTwoInts`
- **Fonction** : Additionne deux entiers.

## 🛠 Compilation
```bash
cd ~/ros2_ws
colcon build --packages-select service_calculatrice
source install/setup.bash
```

## 🚀 Utilisation
Lancer le serveur :
```bash
ros2 run service_calculatrice calculette
```

Appeler le service :
```bash
ros2 service call /calcule example_interfaces/srv/AddTwoInts "{a: 15, b: 5}"
```
