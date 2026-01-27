from rest_framework import viewsets, permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import RiesgosOportunidades
from .serializer import RiesgosOportunidadesReadSerializer, RiesgosOportunidadesWriteSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from controles.models import Controles
from evaluacion.models import Evaluacion
from tratamiento.models import Tratamiento
from eficacia.models import Eficacia


class RiesgosOportunidadesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filterset_fields = ["tipo_riesgo", "enable", "id_cege","id_encabezado"]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    queryset = RiesgosOportunidades.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return RiesgosOportunidadesReadSerializer
        return RiesgosOportunidadesWriteSerializer

    @action(detail=False, methods=['delete'], url_path='logical/delete/(?P<id>[^/.]+)')
    def logical_delete(self,request, id=None):
        try:
            registro = RiesgosOportunidades.objects.get(id=id)
            registro.enable = 0
            registro.save()
            return Response({'delete': 1})
        except RiesgosOportunidades.DoesNotExist:
            return Response({'error': 'registro no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:  
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='duplicate')
    def duplicate_riesgo_oportunidad(self, request):
        """
        Duplica un riesgo/oportunidad con todas sus relaciones
        Parámetros requeridos:
        - id_riesgo_oportunidad: ID del riesgo/oportunidad a duplicar
        - id_encabezado_destino: ID del encabezado destino
        """
        try:
            id_riesgo_oportunidad = request.data.get('id_riesgo_oportunidad')
            id_encabezado_destino = request.data.get('id_encabezado_destino')
            
            if not id_riesgo_oportunidad or not id_encabezado_destino:
                return Response({
                    'error': 'Se requieren los parámetros: id_riesgo_oportunidad e id_encabezado_destino'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            # Obtener el riesgo/oportunidad original
            try:
                riesgo_original = RiesgosOportunidades.objects.get(id=id_riesgo_oportunidad, enable=1)
            except RiesgosOportunidades.DoesNotExist:
                return Response({
                    'error': 'Riesgo/oportunidad no encontrado'
                }, status=status.HTTP_404_NOT_FOUND)
            
            with transaction.atomic():
                # Crear el nuevo riesgo/oportunidad
                nuevo_riesgo = RiesgosOportunidades(
                    id_encabezado_id=id_encabezado_destino,
                    cod_riesgo='',  # Se generará automáticamente
                    tipo_riesgo=riesgo_original.tipo_riesgo,
                    id_proceso=riesgo_original.id_proceso,
                    id_tipo_riesgo=riesgo_original.id_tipo_riesgo,
                    id_sistema_gestion=riesgo_original.id_sistema_gestion,
                    id_efecto_consecuencia=riesgo_original.id_efecto_consecuencia,
                    descripcion=riesgo_original.descripcion,
                    objetivo_oportunidad=riesgo_original.objetivo_oportunidad,
                    id_partes_externas=riesgo_original.id_partes_externas,
                    id_amenaza_oportunidad=riesgo_original.id_amenaza_oportunidad,
                    id_fortaleza_debilidad=riesgo_original.id_fortaleza_debilidad,
                    enable=1,
                    id_cege=riesgo_original.id_cege,
                    id_fortaleza_oportunidad=riesgo_original.id_fortaleza_oportunidad,
                    controles_potenciadores=riesgo_original.controles_potenciadores,
                    id_padre=str(id_riesgo_oportunidad)  # ID del riesgo original que se está duplicando
                )
                nuevo_riesgo.save()
                
                # Generar código automáticamente de forma incremental
                tipo_riesgo = nuevo_riesgo.tipo_riesgo
                if tipo_riesgo.upper() == 'R':
                    prefijo = 'R'
                elif tipo_riesgo.upper() == 'O':
                    prefijo = 'O'
                else:
                    prefijo = tipo_riesgo.upper()
                
                # Buscar el último número usado para este prefijo en el encabezado destino
                riesgos_existentes = RiesgosOportunidades.objects.filter(
                    id_encabezado=id_encabezado_destino,
                    tipo_riesgo=tipo_riesgo,
                    enable=1,
                    cod_riesgo__startswith=f"{prefijo}-"
                ).values_list('cod_riesgo', flat=True)
                
                # Extraer números de los códigos existentes
                numeros_usados = []
                for codigo in riesgos_existentes:
                    try:
                        # Extraer el número después del guión
                        numero = int(codigo.split('-')[1])
                        numeros_usados.append(numero)
                    except (IndexError, ValueError):
                        continue
                
                # Encontrar el siguiente número disponible
                if numeros_usados:
                    siguiente_numero = max(numeros_usados) + 1
                else:
                    siguiente_numero = 1
                
                nuevo_riesgo.cod_riesgo = f"{prefijo}-{siguiente_numero}"
                nuevo_riesgo.save()
                
                # Duplicar controles
                controles_originales = riesgo_original.get_controles()
                for control in controles_originales:
                    nuevo_control = Controles(
                        id_riesgo_oportunidad=nuevo_riesgo,
                        nro_grado_aplicacion=control.nro_grado_aplicacion,
                        des_grado_aplicacion=control.des_grado_aplicacion,
                        nro_definicion_responsables=control.nro_definicion_responsables,
                        des_definicion_responsables=control.des_definicion_responsables,
                        nro_grado_evidencia=control.nro_grado_evidencia,
                        des_grado_evidencia=control.des_grado_evidencia,
                        nro_calculo_nivel_eficacia=control.nro_calculo_nivel_eficacia,
                        des_calculo_nivel_eficacia=control.des_calculo_nivel_eficacia,
                        efectividad_control=control.efectividad_control,
                        enable=1,
                        controles_existentes=control.controles_existentes,
                        probabilidad_oportunidad=control.probabilidad_oportunidad,
                        impacto_oportunidad=control.impacto_oportunidad,
                        nivel_oportunidad=control.nivel_oportunidad,
                        des_nivel_oportunidad=control.des_nivel_oportunidad,
                        des_probabilidad_oportunidad=control.des_probabilidad_oportunidad,
                        des_impacto_oportunidad=control.des_impacto_oportunidad
                    )
                    nuevo_control.save()
                
                # Duplicar evaluaciones
                evaluaciones_originales = riesgo_original.get_evaluaciones()
                for evaluacion in evaluaciones_originales:
                    nueva_evaluacion = Evaluacion(
                        nro_calculo_nivel_eficacia=evaluacion.nro_calculo_nivel_eficacia,
                        nro_probabilidad=evaluacion.nro_probabilidad,
                        nro_impacto=evaluacion.nro_impacto,
                        nro_calculo_nivel_riesgo=evaluacion.nro_calculo_nivel_riesgo,
                        des_calculo_nivel_riesgo=evaluacion.des_calculo_nivel_riesgo,
                        accion_tomar=evaluacion.accion_tomar,
                        id_tipo_riesgo=evaluacion.id_tipo_riesgo,
                        enable=1,
                        id_riesgo_oportunidad=nuevo_riesgo
                    )
                    nueva_evaluacion.save()
                
                # Duplicar tratamientos
                tratamientos_originales = riesgo_original.get_tratamientos()
                for tratamiento in tratamientos_originales:
                    nuevo_tratamiento = Tratamiento(
                        id_estrategia_tratamiento=tratamiento.id_estrategia_tratamiento,
                        actividades=tratamiento.actividades,
                        fecha_inicio=tratamiento.fecha_inicio,
                        fecha_fin=tratamiento.fecha_fin,
                        responsable=tratamiento.responsable,
                        recursos=tratamiento.recursos,
                        id_estado=tratamiento.id_estado,
                        observaciones=tratamiento.observaciones,
                        id_riesgo_oportunidad=nuevo_riesgo,
                        enable=1,
                        estado_cumplimiento=tratamiento.estado_cumplimiento
                    )
                    nuevo_tratamiento.save()
                
                # Duplicar eficacias
                eficacias_originales = riesgo_original.get_eficacias()
                for eficacia in eficacias_originales:
                    nueva_eficacia = Eficacia(
                        fecha_evaluacion=eficacia.fecha_evaluacion,
                        eficaz=eficacia.eficaz,
                        justificacion=eficacia.justificacion,
                        evidencia=eficacia.evidencia,
                        enable=1,
                        id_riesgo_oportunidad=nuevo_riesgo,
                        pregunta1=eficacia.pregunta1,
                        pregunta2=eficacia.pregunta2,
                        pregunta3=eficacia.pregunta3
                    )
                    nueva_eficacia.save()
                
                # Serializar el resultado
                serializer = RiesgosOportunidadesReadSerializer(nuevo_riesgo)
                
                return Response({
                    'message': 'Riesgo/oportunidad duplicado exitosamente',
                    'data': serializer.data,
                    'duplicados': {
                        'controles': len(controles_originales),
                        'evaluaciones': len(evaluaciones_originales),
                        'tratamientos': len(tratamientos_originales),
                        'eficacias': len(eficacias_originales)
                    }
                }, status=status.HTTP_201_CREATED)
                
        except Exception as e:
            return Response({
                'error': f'Error al duplicar: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)