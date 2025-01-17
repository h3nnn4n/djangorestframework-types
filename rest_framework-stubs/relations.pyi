from collections import OrderedDict
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    TypeVar,
    Union,
)

from django.db.models import Manager, Model, QuerySet
from rest_framework.fields import Field, Option
from rest_framework.request import Request

def method_overridden(method_name: str, klass: type, instance: Model) -> bool: ...

class ObjectValueError(ValueError): ...
class ObjectTypeError(TypeError): ...

class Hyperlink(str):
    def __new__(cls, url: str, obj: Any) -> Hyperlink: ...
    def __getnewargs__(self) -> None: ...  # type: ignore [override]
    @property
    def name(self) -> str: ...
    is_hyperlink: bool = ...

class PKOnlyObject:
    pk: Any = ...
    def __init__(self, pk: Any) -> None: ...

MANY_RELATION_KWARGS: Sequence[str]

_MT = TypeVar("_MT", bound=Model)

class RelatedField(Field[Any, Any, Any, Any]):
    queryset: Optional[Union[QuerySet[Any], Manager[Any]]] = ...
    html_cutoff: Optional[int] = ...
    html_cutoff_text: Optional[str] = ...
    def __init__(
        self,
        many: bool = ...,
        allow_empty: bool = ...,
        queryset: Optional[Union[QuerySet[Any], Manager[Any]]] = ...,
        html_cutoff: Optional[int] = ...,
        html_cutoff_text: str = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: Any = ...,
        initial: Any = ...,
        source: Union[Callable[..., Any], str] = ...,
        label: Optional[str] = ...,
        help_text: str = ...,
        allow_null: bool = ...,
        validators: Optional[Sequence[Callable[..., Any]]] = ...,
        error_messages: Optional[Dict[str, str]] = ...,
        style: Optional[Dict[str, str]] = ...,
    ): ...
    # mypy doesn't accept the typing below, although its accurate to what this class is doing, hence the ignore
    def __new__(cls, *args: Any, **kwargs: Any) -> Union[RelatedField, ManyRelatedField]: ...  # type: ignore
    @classmethod
    def many_init(cls, *args: Any, **kwargs: Any) -> ManyRelatedField: ...
    def get_queryset(self) -> QuerySet[Any]: ...
    def use_pk_only_optimization(self) -> bool: ...
    def get_choices(self, cutoff: Optional[int] = ...) -> OrderedDict[Any, Any]: ...
    @property
    def choices(self) -> OrderedDict[Any, Any]: ...
    @property
    def grouped_choices(self) -> OrderedDict[Any, Any]: ...
    def iter_options(self) -> Iterable[Option]: ...
    def get_attribute(self, instance: Any) -> Optional[Any]: ...
    def display_value(self, instance: Any) -> str: ...

class StringRelatedField(RelatedField): ...

class PrimaryKeyRelatedField(RelatedField):
    pk_field: Optional[str] = ...
    def __init__(
        self,
        many: bool = ...,
        allow_empty: bool = ...,
        queryset: Optional[Union[QuerySet[_MT], Manager[_MT]]] = ...,
        html_cutoff: Optional[int] = ...,
        html_cutoff_text: str = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: Any = ...,
        initial: Any = ...,
        source: Union[Callable[..., Any], str] = ...,
        label: Optional[str] = ...,
        help_text: str = ...,
        allow_null: bool = ...,
        validators: Optional[Sequence[Callable[..., Any]]] = ...,
        error_messages: Optional[Dict[str, str]] = ...,
        style: Optional[Dict[str, str]] = ...,
        pk_field: Optional[Union[str, Field[Any, Any, Any, Any]]] = ...,
    ): ...

class HyperlinkedRelatedField(RelatedField):
    reverse: Callable[..., Any] = ...
    lookup_field: str = ...
    lookup_url_kwarg: str = ...
    format: Optional[str] = ...
    view_name: Optional[str] = ...
    def __init__(
        self,
        many: bool = ...,
        allow_empty: bool = ...,
        queryset: Optional[Union[QuerySet[_MT], Manager[_MT]]] = ...,
        html_cutoff: Optional[int] = ...,
        html_cutoff_text: str = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: Any = ...,
        initial: Any = ...,
        source: Union[Callable[..., Any], str] = ...,
        label: Optional[str] = ...,
        help_text: str = ...,
        allow_null: bool = ...,
        validators: Optional[Sequence[Callable[..., Any]]] = ...,
        error_messages: Optional[Dict[str, str]] = ...,
        style: Optional[Dict[str, str]] = ...,
        view_name: Optional[str] = ...,
        lookup_field: Optional[str] = ...,
        lookup_url_kwarg: Optional[str] = ...,
        format: Optional[str] = ...,
    ): ...
    def get_object(self, view_name: str, *view_args: Any, **view_kwargs: Any) -> Any: ...
    def get_url(self, obj: Model, view_name: str, request: Request, format: str) -> Optional[str]: ...

class HyperlinkedIdentityField(HyperlinkedRelatedField): ...

class SlugRelatedField(RelatedField):
    slug_field: Optional[str] = ...
    def __init__(
        self,
        many: bool = ...,
        allow_empty: bool = ...,
        queryset: Optional[Union[QuerySet[_MT], Manager[_MT]]] = ...,
        html_cutoff: Optional[int] = ...,
        html_cutoff_text: str = ...,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: Any = ...,
        initial: Union[_MT, Callable[[Any], _MT]] = ...,
        source: Union[Callable[..., Any], str] = ...,
        label: Optional[str] = ...,
        help_text: str = ...,
        allow_null: bool = ...,
        validators: Optional[Sequence[Callable[..., Any]]] = ...,
        error_messages: Optional[Dict[str, str]] = ...,
        style: Optional[Dict[str, str]] = ...,
        slug_field: Optional[str] = ...,
    ): ...
    def to_internal_value(self, data: Any) -> Any: ...
    def to_representation(self, value: Any) -> str: ...

class ManyRelatedField(Field[Sequence[Any], Sequence[Any], List[Any], Any]):
    default_empty_html: List[object] = ...
    html_cutoff: Optional[int] = ...
    html_cutoff_text: Optional[str] = ...
    child_relation: RelatedField = ...
    allow_empty: bool = ...
    def __init__(
        self,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: Sequence[Any] = ...,
        initial: Union[Sequence[Any], Callable[[Any], Sequence[Any]]] = ...,
        source: Union[Callable[..., Any], str] = ...,
        label: Optional[str] = ...,
        help_text: Optional[str] = ...,
        style: Optional[Dict[str, str]] = ...,
        error_messages: Optional[Dict[str, str]] = ...,
        validators: Optional[Sequence[Callable[..., Any]]] = ...,
        allow_null: bool = ...,
        child_relation: RelatedField = ...,
    ): ...
    def get_value(self, dictionary: Mapping[Any, Any]) -> List[Any]: ...
    def get_choices(self, cutoff: Optional[int] = ...) -> OrderedDict[Any, Any]: ...
    @property
    def choices(self) -> OrderedDict[Any, Any]: ...
    @property
    def grouped_choices(self) -> OrderedDict[Any, Any]: ...
    def iter_options(self) -> Iterable[Option]: ...
