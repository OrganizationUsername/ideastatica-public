# coding: utf-8

"""
    RCS Rest API 1.0

    IDEA StatiCa RCS API, used for the automated design and calculation of reinforced concrete sections.

    The version of the OpenAPI document: 1.0
    Contact: info@ideastatica.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ideastatica_rcs_api.models.loading_type import LoadingType
from ideastatica_rcs_api.models.result_of_loading_item import ResultOfLoadingItem
from typing import Optional, Set
from typing_extensions import Self

class ResultOfLoading(BaseModel):
    """
    Result Of Loading
    """ # noqa: E501
    items: Optional[List[ResultOfLoadingItem]] = Field(default=None, description="Items od loading")
    loading_type: Optional[LoadingType] = Field(default=None, alias="loadingType")
    id: Optional[StrictInt] = Field(default=None, description="Id of loading")
    __properties: ClassVar[List[str]] = ["items", "loadingType", "id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ResultOfLoading from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['items'] = _items
        # set to None if items (nullable) is None
        # and model_fields_set contains the field
        if self.items is None and "items" in self.model_fields_set:
            _dict['items'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResultOfLoading from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "items": [ResultOfLoadingItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "loadingType": obj.get("loadingType"),
            "id": obj.get("id")
        })
        return _obj


