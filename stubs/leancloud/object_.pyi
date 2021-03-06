from typing import Any, Dict, Union, SupportsFloat
import leancloud
from leancloud.query import Query
from leancloud.acl import ACL
from leancloud.relation import Relation


class Object(object):
    id = ... # type: str
    _class_name = ... # type: str
    _attributes = ... # type: Dict

    def __init__(self, **attrs) -> None: ...

    # the real implementation of query property is on metaclass
    @property
    def query(cls) -> Query:...
    
    @classmethod
    def extend(cls, name: str) -> type:...

    @classmethod
    def create(cls, class_name: str, **attributes) -> Object:...

    @classmethod
    def create_without_data(cls, id_: str) -> Object:...
    
    @classmethod
    def save_all(cls, objs: List[Object]) -> None:...

    @classmethod
    def destroy_all(cls, objs: List[Object]) -> None:...

    @property
    def attributes(self) -> Dict:...

    def dump(self) -> Object:...

    def is_dirty(self, attr: str=None) -> bool:...

    def destroy(self) -> None:...

    def save(self, where: Query=None) -> None:...

    def get(self, attr: str, deafult: Any=None) -> Any:...

    def relation(self, attr: str) -> Relation:...

    def has(self, attr: str) -> bool: ...

    def set(self, key_or_attrs: Union[str,Dict[Any,Any]], value: Any=None, unset: bool=False) -> Object:...

    def unset(self, attr: str) -> Object:...

    def increment(self, attr: str, amount: SupportsFloat=1) -> Object:...

    def add(self, attr: str, item: Any) -> Object:...

    def add_unique(self, attr: str, item: Any) -> Object:...

    def remove(self, attr: str, item: Any) -> Object:...

    def clear(self) -> Object:...

    def fetch(self) -> None:...

    def is_new(self) -> bool:...

    def is_exitsted(self) -> bool:...

    def get_acl(self) -> ACL:...

    def set_acl(self, ACL) -> Object:...
