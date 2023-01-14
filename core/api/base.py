from rest_framework import generics
from rest_framework.response import Response


class BaseGenericAPIView(generics.GenericAPIView):
    response_serializer_class = None

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = generics.get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

    def get_serializer(self, *args, **kwargs):
        serializer = super(BaseGenericAPIView, self).get_serializer(*args, **kwargs)
        result = serializer.data
        if self.pagination_class is not None:
            result = super(BaseGenericAPIView, self).get_paginated_response(result)
        response_serializer = self.response_serializer_class(data={
            "code": 0,
            "message": "success",
            "result": result
        })
        response_serializer.is_valid()
        return response_serializer

    def get_paginated_response(self, data):
        return Response(data=data)
