print("start")
bl_info = {
    "name": "PmxTools",
    "author": "sorao",
    "version": (1, 1),
    "blender": (2, 68, 0),
    "api": 38019,
    "location": "File > Import-Export",
    "description": "PMX tools",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Import-Export"}

import imp
if "bpy" in locals():
    print("in_bpy")
    imp.reload(CsvTools)
    imp.reload(CUSTOM_OT_Createjoint)
    imp.reload(JointFileW)
    imp.reload(CUSTOM_OT_ImpoatJointFile)
    imp.reload(RigidCubeByBone)
    imp.reload(ExportRigidBody)
    imp.reload(ImportRigidBody)
    imp.reload(RigidSphereByBone)
    imp.reload(RigidCylinderByBone)
    imp.reload(CreateRigidChain)
    imp.reload(JointAtoB)
else:    
    print("not_bpy")    
    
import bpy
from bpy_extras.io_utils import ExportHelper,ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator
from pmxtools.CsvTools import *
from pmxtools.CUSTOM_OT_Createjoint import *
from pmxtools.JointFileW import *
from pmxtools.CUSTOM_OT_ImpoatJointFile import *
from pmxtools.CreateRBdodyByBone import *
from pmxtools.ExportRigidBody import *
from pmxtools.ImportRigidBody import *
from pmxtools.CreateRigidChain import *
from pmxtools.JointAtoB import *
"""
pmxtool mainpanel
ボタン登録など
"""
class CustomPanel(bpy.types.Panel):
    """A Custom Panel in the Viewport Toolbar"""
    bl_label = "pmxtool"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    def draw(self, context):
        layout = self.layout
        
        row = layout.row(align=True)
        split = layout.split()
        col = split.column(align=True)
        col.label(text="JointTool:")
        col.operator("mesh.jointool")
        col.operator("mesh.joint_file_w")
        col.operator("mesh.impoat_joint_file")
        
        row = layout.row(align=True)
        split = layout.split()
        col = split.column(align=True)
        col.label(text="剛体Tool:")
        col.operator("mesh.rigid_cube_bone_add")
        col.operator("mesh.rigid_sphere_bone_add")
        col.operator("mesh.rigid_cylinder_bone_add")
        col.operator("mesh.impoat_rigid_file")
        col.operator("mesh.export_rigid")
        
        row = layout.row(align=True)
        split = layout.split()
        col = split.column(align=True)
        col.label(text="EtcTool:")
        col.operator("mesh.create_rchain")
        col.operator("mesh.joint_a_to_b")
        
        
        
#---------------------------------------------------------
def register():
    bpy.utils.register_class(CustomPanel)
    bpy.utils.register_class(JointFileW)
    bpy.utils.register_class(CUSTOM_OT_ImpoatJointFile)
    bpy.utils.register_class(CUSTOM_OT_Createjoint)
    bpy.utils.register_class(RigidCubeByBone)
    bpy.utils.register_class(ExportRigidBody)
    bpy.utils.register_class(ImportRigidBody)
    bpy.utils.register_class(RigidSphereByBone)
    bpy.utils.register_class(RigidCylinderByBone)
    bpy.utils.register_class(CreateRigidChain)
    bpy.utils.register_class(JointAtoB)
    print("register")

def unregister():
    bpy.utils.unregister_class(JointAtoB)
    bpy.utils.unregister_class(CreateRigidChain)
    bpy.utils.unregister_class(RigidCylinderByBone)
    bpy.utils.unregister_class(RigidSphereByBone)
    bpy.utils.unregister_class(ImportRigidBody)
    bpy.utils.unregister_class(ExportRigidBody)
    bpy.utils.unregister_class(RigidCubeByBone)
    bpy.utils.unregister_class(JointFileW)
    bpy.utils.unregister_class(CUSTOM_OT_ImpoatJointFile)
    bpy.utils.unregister_class(CUSTOM_OT_Createjoint)
    bpy.utils.unregister_class(CustomPanel)
    
   

if __name__ == "__main__":
    register()
    
    