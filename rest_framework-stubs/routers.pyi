from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Mapping,
    NamedTuple,
    Optional,
    Tuple,
    Type,
    Union,
)

from django.utils.deprecation import RenameMethodsBase
from rest_framework import views
from rest_framework.renderers import BaseRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.schemas.views import SchemaView
from rest_framework.viewsets import ViewSetMixin

class Route(NamedTuple):
    url: str
    mapping: Dict[str, str]
    name: str
    detail: bool
    initkwargs: Dict[str, Any]

class DynamicRoute(NamedTuple):
    url: str
    name: str
    detail: bool
    initkwargs: Dict[str, Any]

def escape_curly_brackets(url_path: str) -> str: ...
def flatten(list_of_lists: Iterable[Iterable[Any]]) -> Iterable[Any]: ...

class RenameRouterMethods(RenameMethodsBase):
    renamed_methods: Iterable[Union[str, Callable[..., Any]]] = ...

class BaseRouter(metaclass=RenameRouterMethods):
    registry: List[Tuple[str, Type[ViewSetMixin], str]]
    def register(
        self, prefix: str, viewset: Type[ViewSetMixin], basename: Optional[str] = ..., base_name: Optional[str] = ...
    ) -> None: ...
    def get_default_basename(self, viewset: Type[ViewSetMixin]) -> str: ...
    # TODO: change return type
    def get_urls(self) -> Any: ...
    # TODO: change return type
    @property
    def urls(self) -> Any: ...

class SimpleRouter(BaseRouter):
    routes: List[Union[Route, DynamicRoute]] = ...
    trailing_slash: str
    def __init__(self, trailing_slash: bool = ...) -> None: ...
    def get_routes(self, viewset: Type[ViewSetMixin]) -> List[Route]: ...
    def _get_dynamic_route(self, route: DynamicRoute, action: Any) -> Route: ...
    def get_method_map(self, viewset: Type[ViewSetMixin], method_map: Mapping[str, str]) -> Dict[str, str]: ...
    def get_lookup_regex(self, viewset: Type[ViewSetMixin], lookup_prefix: str = ...) -> str: ...

class APIRootView(views.APIView):
    _ignore_model_permissions: bool = ...
    api_root_dict: Optional[Dict[str, str]] = ...
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...

class DefaultRouter(SimpleRouter):
    include_root_view: bool = ...
    include_format_suffixes: bool = ...
    root_view_name: str = ...
    default_schema_renderers = None
    APIRootView = APIRootView
    APISchemaView = SchemaView
    SchemaGenerator = SchemaGenerator

    root_renderers: List[Type[BaseRenderer]]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_api_root_view(self, api_urls: Optional[Any] = ...) -> Callable[..., Any]: ...
