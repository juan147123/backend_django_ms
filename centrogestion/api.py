from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from .models import CentroGestion
from .serializer import CentroGestionSerializer
from rest_framework.decorators import action


class CentroGestionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CentroGestionSerializer
    queryset = CentroGestion.objects.all()

    def build_tree(self, node, parent_key='0', order=0):
        node_data = CentroGestionSerializer(node).data
        if node.parent is None:
            current_key = f"{parent_key}" if parent_key else str(node.id)
            node_data['order'] = f"{parent_key}" 
        else:
            current_key = f"{parent_key}-{node.id}" if parent_key else str(node.id)
            node_data['order'] = f"{parent_key}-{order}" 

        node_data['key'] = current_key

        
        children = CentroGestion.objects.filter(parent=node)
        if children.exists():
            # Generar el árbol para los hijos, pasando el índice como el número de orden
            node_data['children'] = [
                self.build_tree(child, current_key, index) for index, child in enumerate(children)
            ]
        
        return node_data

    @action(detail=False, methods=['get'], url_path='tree')
    def list_centro_gestion(self, request):
        root_nodes = CentroGestion.objects.filter(parent__isnull=True)
        tree = [self.build_tree(node) for node in root_nodes]
        return Response(tree)

