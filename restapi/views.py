from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from . import models, serializers


# ---------------------- Clinic CRUD ----------------------
class ClinicViewset(APIView):

    def get(self, request, id=None):
        if id:
            clinic = get_object_or_404(models.Clinic, id=id)
            serializer = serializers.ClinicSerializer(clinic)
            return Response({"status": "success", "data": serializer.data})
        clinics = models.Clinic.objects.all()
        serializer = serializers.ClinicSerializer(clinics, many=True)
        return Response({"status": "success", "data": serializer.data})

    def post(self, request):
        serializer = serializers.ClinicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=201)
        return Response({"status": "error", "errors": serializer.errors}, status=400)

    def patch(self, request, id=None):
        clinic = get_object_or_404(models.Clinic, id=id)
        serializer = serializers.ClinicSerializer(clinic, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "error", "errors": serializer.errors}, status=400)

    def delete(self, request, id=None):
        clinic = get_object_or_404(models.Clinic, id=id)
        clinic.delete()
        return Response({"status": "success", "data": "Clinic deleted"})


# ---------------------- Department CRUD ----------------------
class DepartmentViewset(APIView):

    def get(self, request, id=None):
        if id:
            dep = get_object_or_404(models.Department, id=id)
            serializer = serializers.DepartmentSerializer(dep)
            return Response({"status": "success", "data": serializer.data})
        deps = models.Department.objects.all()
        serializer = serializers.DepartmentSerializer(deps, many=True)
        return Response({"status": "success", "data": serializer.data})

    def post(self, request):
        serializer = serializers.DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=201)
        return Response({"status": "error", "errors": serializer.errors}, status=400)

    def patch(self, request, id=None):
        dep = get_object_or_404(models.Department, id=id)
        serializer = serializers.DepartmentSerializer(dep, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "error", "errors": serializer.errors}, status=400)

    def delete(self, request, id=None):
        dep = get_object_or_404(models.Department, id=id)
        dep.delete()
        return Response({"status": "success", "data": "Department deleted"})


# ---------------------- Equipments CRUD ----------------------
class EquipmentViewset(APIView):

    def get(self, request, id=None):
        if id:
            eq = get_object_or_404(models.Equipments, id=id)
            serializer = serializers.EquipmentsSerializer(eq)
            return Response({"status": "success", "data": serializer.data})
        eqs = models.Equipments.objects.all()
        serializer = serializers.EquipmentsSerializer(eqs, many=True)
        return Response({"status": "success", "data": serializer.data})

    def post(self, request):
        serializer = serializers.EquipmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=201)
        return Response({"status": "error", "errors": serializer.errors}, status=400)

    def patch(self, request, id=None):
        eq = get_object_or_404(models.Equipments, id=id)
        serializer = serializers.EquipmentsSerializer(eq, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "error", "errors": serializer.errors}, status=400)

    # def delete(self, request, id=None):
    #     eq = get_object_or_404(models.Equipments, id=id)
    #     eq.delete()
    #     return Response({"status": "success", "data": "Equipment deleted"})


# ---------------------- Equipment Details CRUD ----------------------
class EquipmentDetailsViewset(APIView):

    def get(self, request, id=None):
        if id:
            detail = get_object_or_404(models.EquipmentDetails, id=id)
            serializer = serializers.EquipmentDetailsSerializer(detail)
            return Response({"status": "success", "data": serializer.data})
        details = models.EquipmentDetails.objects.all()
        serializer = serializers.EquipmentDetailsSerializer(details, many=True)
        return Response({"status": "success", "data": serializer.data})

    def post(self, request):
        serializer = serializers.EquipmentDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=201)
        return Response({"status": "error", "errors": serializer.errors}, status=400)

    def patch(self, request, id=None):
        detail = get_object_or_404(models.EquipmentDetails, id=id)
        serializer = serializers.EquipmentDetailsSerializer(detail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "error", "errors": serializer.errors}, status=400)

    # def delete(self, request, id=None):
    #     detail = get_object_or_404(models.EquipmentDetails, id=id)
    #     detail.delete()
    #     return Response({"status": "success", "data": "Equipment detail deleted"})

class ParametersViewset(APIView):

    def get(self, request, id=None):
        if id:
            param = get_object_or_404(models.Parameters, id=id)
            serializer = serializers.ParametersSerializer(param)
            return Response({"status": "success", "data": serializer.data})

        params = models.Parameters.objects.all()
        serializer = serializers.ParametersSerializer(params, many=True)
        return Response({"status": "success", "data": serializer.data})

    def post(self, request):
        serializer = serializers.ParametersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"status": "error", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, id=None):
        param = get_object_or_404(models.Parameters, id=id)
        serializer = serializers.ParametersSerializer(param, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response(
            {"status": "error", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    # def delete(self, request, id=None):
    #     param = get_object_or_404(models.Parameters, id=id)
    #     param.delete()
    #     return Response(
    #         {"status": "success", "data": "Parameter deleted"},
    #         status=status.HTTP_200_OK
    #     )
