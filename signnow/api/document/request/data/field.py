"""
This file is a part of signNow SDK API client.

(c) Copyright © 2011-present airSlate Inc. (https://www.signnow.com)

For more details on copyright, see LICENSE.md file
that was distributed with this source code.
"""

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Field:
    """
    Represents a Field in the signNow API.
    """

    x: int
    """The x-coordinate of the field."""

    y: int
    """The y-coordinate of the field."""

    width: int
    """The width of the field."""

    height: int
    """The height of the field."""

    type: str
    """The type of the field."""

    page_number: int
    """The page number where the field is located."""

    required: bool
    """Whether the field is required or not."""

    role: str
    """The role of the field."""

    name: str
    """The name of the field."""

    label: Optional[str] = None
    """The label of the field."""

    custom_defined_option: bool = False
    """Whether the field has a custom defined option or not."""

    tooltip: Optional[str] = None
    """The tooltip of the field."""

    formula: Optional[str] = None
    """The formula of the field."""

    conditional: bool = False
    """Whether the field is conditional or not."""

    stretch_to_grid: bool = False
    """Whether the field is stretched to grid or not."""

    active: bool = True
    """Whether the field is active or not."""

    bold: bool = False
    """Whether the field is bold or not."""

    italic: bool = False
    """Whether the field is italic or not."""

    underline: bool = False
    """Whether the field is underlined or not."""

    subtype: Optional[str] = None
    """The subtype of the field."""

    align: Optional[str] = None
    """The alignment of the field."""

    calculation_precision: Optional[str] = None
    """The calculation precision of the field."""

    color: Optional[str] = None
    """The color of the field."""

    validator_id: Optional[str] = None
    """The validator id of the field."""

    def to_dict(self) -> Dict:
        """
        Converts the field to a dictionary.

        Returns:
            A dictionary representing the field.
        """
        result: Dict = {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "type": self.type,
            "page_number": self.page_number,
            "required": self.required,
            "role": self.role,
            "name": self.name,
            "custom_defined_option": self.custom_defined_option,
            "conditional": self.conditional,
            "stretch_to_grid": self.stretch_to_grid,
            "active": self.active,
            "bold": self.bold,
            "italic": self.italic,
            "underline": self.underline,
        }
        if self.label is not None:
            result["label"] = self.label
        if self.tooltip is not None:
            result["tooltip"] = self.tooltip
        if self.formula is not None:
            result["formula"] = self.formula
        if self.subtype is not None:
            result["subtype"] = self.subtype
        if self.align is not None:
            result["align"] = self.align
        if self.calculation_precision is not None:
            result["calculation_precision"] = self.calculation_precision
        if self.color is not None:
            result["color"] = self.color
        if self.validator_id is not None:
            result["validator_id"] = self.validator_id
        return result
