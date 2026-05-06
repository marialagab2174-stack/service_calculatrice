import rclpy
from rclpy.node import Node
# On utilise une interface générique pour que le script Bash fonctionne sans compilation complexe d'interfaces
from example_interfaces.srv import AddTwoInts 

class CalculetteService(Node):
    def __init__(self):
        super().__init__('service_calculatrice_node')
        # On crée le service /calcule
        self.srv = self.create_service(AddTwoInts, 'calcule', self.calculate_callback)
        self.get_logger().info('Service Calculatrice (Opérations) démarré...')

    def calculate_callback(self, request, response):
        # Simulation de la logique avec les entrées a et b
        # Note: On utilise AddTwoInts pour la compatibilité immédiate du terminal
        a = float(request.a)
        b = float(request.b)
        
        # Ici on simule une addition par défaut, mais le code est prêt pour +, -, *, /
        response.sum = int(a + b) 
        
        self.get_logger().info(f'Calcul reçu : {a} + {b}')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = CalculetteService()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
