from rest_framework import viewsets

from djazzle.core.models import Track


class TrackViewSet(viewsets.ModelViewSet):
    model = Track
