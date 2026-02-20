from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Project, ContactMessage
from .serializers import ProjectSerializer, ContactMessageSerializer


@api_view(['GET'])
def project_list_api(request):
    projects = Project.objects.all().order_by('-created_date')
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def project_detail_api(request, slug):
    project = get_object_or_404(Project, slug=slug)
    serializer = ProjectSerializer(project)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def project_create_api(request):
    serializer = ProjectSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)

@api_view(['POST'])
def contact_create_api(request):
    serializer = ContactMessageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Contact message sent successfully"},
            status=201
        )

    return Response(serializer.errors, status=400)