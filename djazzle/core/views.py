from rest_framework import viewsets

from core.models import Track


class TrackViewSet(viewsets.ModelViewSet):
    model = Track
