from .models import CityModel,StateModel,CountryModel,StudentModel,EventModel,StudentParticipationModel
from .serializers import StudentSerializer,EventSerializer,CitySerializer,StateSerializer,CountrySerializer,StudentParticipationSerializer
from .paginations import StandardResultsSetPagination,DefaultPageNumberPagination
from .permissions import NewPermission
from .filters import StudentFilter,EventFilter,StudentParticipationFilter,StateFilter,CityFilter,CountryFilter

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = StudentModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StudentFilter
    pagination_class = StandardResultsSetPagination
    permission_classes = [NewPermission,]

    def get_queryset(self):
        pagination = self.request.query_params.get('pagination', None)
        queryset = super(StudentViewSet, self).get_queryset()
        queryset = queryset.filter(is_active=True)
        self.filterset_class = StudentFilter
        queryset = self.filter_queryset(queryset)
        if pagination is not None and pagination == "false":
            self.pagination_class = None
        return queryset

    @action(methods=['GET', 'POST'], detail=False)
    def country(self, request):
        if request.method == "GET":
            queryset = CountryModel.objects.filter(is_active=True)
            self.filterset_class = CountryFilter
            queryset = self.filter_queryset(queryset)
            return response.Ok(CountrySerializer(queryset.order_by("name"), many=True).data)
        else:
            return response.Ok(create_update_record(request, CountrySerializer, CountryModel))

    @action(methods=['GET', 'POST'], detail=False)
    def city(self, request):
        if request.method == "GET":
            queryset = CityModel.objects.filter(is_active=True)
            self.filterset_class = CityFilter
            queryset = self.filter_queryset(queryset)
            return response.Ok(CitySerializer(queryset.order_by("name"), many=True).data)
        else:
            return response.Ok(create_update_record(request, CitySerializer, CityModel))

    @action(methods=['GET', 'POST'], detail=False)
    def state(self, request):
        if request.method == "GET":
            queryset = StateModel.objects.filter(is_active=True)
            self.filterset_class = StateFilter
            queryset = self.filter_queryset(queryset)
            return response.Ok(StateSerializer(queryset.order_by("name"), many=True).data)
        else:
            return response.Ok(create_update_record(request, StateSerializer, StateModel))

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = EventModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EventFilter
    pagination_class = StandardResultsSetPagination
    permission_classes = [NewPermission, ]

    def get_queryset(self):
        pagination = self.request.query_params.get('pagination', None)
        queryset = super(EventViewSet, self).get_queryset()
        queryset = queryset.filter(is_active=True)
        self.filterset_class = EventFilter
        queryset = self.filter_queryset(queryset)
        if pagination is not None and pagination == "false":
            self.pagination_class = None
        return queryset

class StudentParticipationViewSet(viewsets.ModelViewSet):
    serializer_class = StudentParticipationSerializer
    queryset = StudentParticipationModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StudentParticipationFilter
    pagination_class = StandardResultsSetPagination
    permission_classes = [NewPermission, ]

    def get_queryset(self):
        pagination = self.request.query_params.get('pagination', None)
        queryset = super(StudentParticipationViewSet, self).get_queryset()
        queryset = queryset.filter(is_active=True)
        self.filterset_class = StudentParticipationFilter
        queryset = self.filter_queryset(queryset)
        if pagination is not None and pagination == "false":
            self.pagination_class = None
        return queryset







