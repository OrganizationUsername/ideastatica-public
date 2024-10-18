# coding: utf-8

# flake8: noqa
"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from ideastatica_connection_api.models.anchor_grid import AnchorGrid
from ideastatica_connection_api.models.anchor_type import AnchorType
from ideastatica_connection_api.models.base_template_conversion import BaseTemplateConversion
from ideastatica_connection_api.models.beam_data import BeamData
from ideastatica_connection_api.models.bend_data import BendData
from ideastatica_connection_api.models.bolt_grid import BoltGrid
from ideastatica_connection_api.models.bolt_shear_type import BoltShearType
from ideastatica_connection_api.models.buckling_res import BucklingRes
from ideastatica_connection_api.models.check_res_anchor import CheckResAnchor
from ideastatica_connection_api.models.check_res_bolt import CheckResBolt
from ideastatica_connection_api.models.check_res_concrete_block import CheckResConcreteBlock
from ideastatica_connection_api.models.check_res_plate import CheckResPlate
from ideastatica_connection_api.models.check_res_summary import CheckResSummary
from ideastatica_connection_api.models.check_res_weld import CheckResWeld
from ideastatica_connection_api.models.con_analysis_type_enum import ConAnalysisTypeEnum
from ideastatica_connection_api.models.con_calculation_parameter import ConCalculationParameter
from ideastatica_connection_api.models.con_connection import ConConnection
from ideastatica_connection_api.models.con_load_effect import ConLoadEffect
from ideastatica_connection_api.models.con_load_effect_member_load import ConLoadEffectMemberLoad
from ideastatica_connection_api.models.con_load_effect_position_enum import ConLoadEffectPositionEnum
from ideastatica_connection_api.models.con_load_effect_section_load import ConLoadEffectSectionLoad
from ideastatica_connection_api.models.con_load_settings import ConLoadSettings
from ideastatica_connection_api.models.con_member import ConMember
from ideastatica_connection_api.models.con_mprl_cross_section import ConMprlCrossSection
from ideastatica_connection_api.models.con_mprl_element import ConMprlElement
from ideastatica_connection_api.models.con_operation import ConOperation
from ideastatica_connection_api.models.con_production_cost import ConProductionCost
from ideastatica_connection_api.models.con_project import ConProject
from ideastatica_connection_api.models.con_project_data import ConProjectData
from ideastatica_connection_api.models.con_result_summary import ConResultSummary
from ideastatica_connection_api.models.con_template_apply_param import ConTemplateApplyParam
from ideastatica_connection_api.models.con_template_mapping_get_param import ConTemplateMappingGetParam
from ideastatica_connection_api.models.concrete_block import ConcreteBlock
from ideastatica_connection_api.models.concrete_block_data import ConcreteBlockData
from ideastatica_connection_api.models.concrete_setup import ConcreteSetup
from ideastatica_connection_api.models.cone_breakout_check_type import ConeBreakoutCheckType
from ideastatica_connection_api.models.connection_check_res import ConnectionCheckRes
from ideastatica_connection_api.models.connection_data import ConnectionData
from ideastatica_connection_api.models.connection_setup import ConnectionSetup
from ideastatica_connection_api.models.crt_comp_check_is import CrtCompCheckIS
from ideastatica_connection_api.models.cut_beam_by_beam_data import CutBeamByBeamData
from ideastatica_connection_api.models.cut_data import CutData
from ideastatica_connection_api.models.cut_method import CutMethod
from ideastatica_connection_api.models.cut_orientation import CutOrientation
from ideastatica_connection_api.models.cut_part import CutPart
from ideastatica_connection_api.models.distance_comparison import DistanceComparison
from ideastatica_connection_api.models.draw_data import DrawData
from ideastatica_connection_api.models.e_purpose import EPurpose
from ideastatica_connection_api.models.folded_plate_data import FoldedPlateData
from ideastatica_connection_api.models.i_group import IGroup
from ideastatica_connection_api.models.idea_parameter import IdeaParameter
from ideastatica_connection_api.models.idea_parameter_update import IdeaParameterUpdate
from ideastatica_connection_api.models.line import Line
from ideastatica_connection_api.models.load_effect_data import LoadEffectData
from ideastatica_connection_api.models.message_number import MessageNumber
from ideastatica_connection_api.models.open_element_id import OpenElementId
from ideastatica_connection_api.models.open_message import OpenMessage
from ideastatica_connection_api.models.open_messages import OpenMessages
from ideastatica_connection_api.models.param_value_type import ParamValueType
from ideastatica_connection_api.models.parameter_data import ParameterData
from ideastatica_connection_api.models.pin_grid import PinGrid
from ideastatica_connection_api.models.plate_data import PlateData
from ideastatica_connection_api.models.point2_d import Point2D
from ideastatica_connection_api.models.point3_d import Point3D
from ideastatica_connection_api.models.poly_line2_d import PolyLine2D
from ideastatica_connection_api.models.reference_element import ReferenceElement
from ideastatica_connection_api.models.region2_d import Region2D
from ideastatica_connection_api.models.segment2_d import Segment2D
from ideastatica_connection_api.models.selected import Selected
from ideastatica_connection_api.models.selected_type import SelectedType
from ideastatica_connection_api.models.template_conversions import TemplateConversions
from ideastatica_connection_api.models.text import Text
from ideastatica_connection_api.models.text_position import TextPosition
from ideastatica_connection_api.models.validation_type import ValidationType
from ideastatica_connection_api.models.vector3_d import Vector3D
from ideastatica_connection_api.models.weld_data import WeldData
from ideastatica_connection_api.models.weld_evaluation import WeldEvaluation
from ideastatica_connection_api.models.weld_type import WeldType