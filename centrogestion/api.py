from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from .models import CentroGestion
from .serializer import CentroGestionSerializer
from rest_framework.decorators import action


class CentroGestionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = CentroGestionSerializer
    queryset = CentroGestion.objects.all()

    def build_tree(self, nodes, parent_key=None):
        tree = []
        
        for index, node in enumerate(nodes):
            # Serializar los datos del nodo actual
            node_data = CentroGestionSerializer(node).data
            
            if parent_key is None:
                # Asignar key a los nodos raíz como "0", "1", "2", etc.
                current_key = str(index)
            else:
                # Formar el key basado en el parent_key y el index
                current_key = f"{parent_key}-{index}"
            
            node_data['key'] = current_key

            # Buscar hijos del nodo actual
            children = CentroGestion.objects.filter(parent=node, enable=1).order_by('id')  # Asegurar un orden consistente por ID
            if children.exists():
                # Generar el árbol para los hijos
                node_data['children'] = self.build_tree(children, current_key)

            tree.append(node_data)

        return tree

    @action(detail=False, methods=['get'], url_path='tree')
    def list_centro_gestion(self, request):
        # Obtener nodos raíz que están habilitados
        root_nodes = CentroGestion.objects.filter(parent__isnull=True, enable=1).order_by('id')
        
        # Llamar a build_tree pasando el queryset de nodos raíz
        tree = self.build_tree(root_nodes)

        return Response(tree)
    
        
    @action(detail=False, methods=['delete'], url_path='logical/delete/(?P<id>[^/.]+)')
    def logical_delete(self,request, id=None):
        try:
            mantenimiento = CentroGestion.objects.get(id=id)
            mantenimiento.enable = 0
            mantenimiento.save()
            return Response({'delete': 1})
        except CentroGestion.DoesNotExist:
            return Response({'error': 'Mantenimiento no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:  
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    

