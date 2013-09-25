import bpy
from bpy_extras.io_utils import ExportHelper,ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator
from pmxtools.CsvTools import *
import math

"""-----------------------------------------
剛体ファイル読み込み
1.先にgroup[rigid]を作っておく
2.実行

--------------------------------------------"""
class ImportRigidBody(Operator,ImportHelper):
    bl_idname = "mesh.impoat_rigid_file"#bpy登録id半角限定
    bl_label = "剛体ファイル読み込み" #button label
    bl_description = "先にgroup[rigid]を作っておく" #tooltip
    #デフォルト拡張子
    filename_ext = ".csv"
    #ファイルフィルタ
    filter_glob = StringProperty(
            default="*.csv",
            options={'HIDDEN'},
            )
    
        
    def execute(self, context):
        readfile = CsvTools.Reader(self.filepath)
        for rigid in range(1,len(readfile)):
            #オブジェクトプロパティ
            #loc(位置)
            loc = (float(readfile[rigid][11])/5,float(readfile[rigid][13])/5,float(readfile[rigid][12])/5)
            #形状追加
            if readfile[rigid][7] == "0":#球
                bpy.ops.mesh.primitive_uv_sphere_add(location = loc)
                obj = bpy.context.active_object
                obj.dimensions = (float(readfile[rigid][8])/2.5
                                                    ,float(readfile[rigid][8])/2.5
                                                    ,float(readfile[rigid][8])/2.5)
            elif readfile[rigid][7] == "1":#箱
                bpy.ops.mesh.primitive_cube_add(location = loc)
                obj = bpy.context.active_object
                obj.dimensions = (float(readfile[rigid][8])/2
                                                    ,float(readfile[rigid][10])/2
                                                    ,float(readfile[rigid][9])/2)
            elif readfile[rigid][7] == "2":#カプセル
                bpy.ops.mesh.primitive_cylinder_add(location = loc)
                obj = bpy.context.active_object
                obj.dimensions = (float(readfile[rigid][8])/3
                                                    ,float(readfile[rigid][8])/3
                                                    ,float(readfile[rigid][9])/4)
                
            obj.name = "rigid"                          
            obj["*剛体名"] = readfile[rigid][1]
            obj.rotation_mode = 'XYZ'
            #Number = r * 180 / Math.PI math.pi
            rotation_x = -float(readfile[rigid][14]) * math.pi / 180 
            rotation_y = -float(readfile[rigid][16]) * math.pi / 180
            rotation_z = -float(readfile[rigid][15]) * math.pi / 180
            obj.rotation_euler = (rotation_x,rotation_y,rotation_z)
            
                                                                                        
            bpy.ops.object.group_link(group="rigid")
                                                    
            obj["00剛体名(英)"] = readfile[rigid][2]
            obj["01関連ボーン名"] = readfile[rigid][3]
            obj["02剛体タイプ"] = int(readfile[rigid][4])
            obj["03グループ(0~15)"] = int(readfile[rigid][5])
            obj["04非衝突グループ"] = readfile[rigid][6]
            obj["05形状"] = int(readfile[rigid][7])
            obj["06質量"] = float(readfile[rigid][17])
            obj["07移動減衰"] = float(readfile[rigid][18])
            obj["08回転減衰"] = float(readfile[rigid][19])
            obj["09反発力"] = float(readfile[rigid][20])
            obj["10摩擦力"] = float(readfile[rigid][21])           
        print("importrigid")
        return {'FINISHED'}

#----------------------------------------------------    
if __name__ == "__main__":
    bpy.utils.register_class(ImportRigidBody)
    print("ImportRigidBody")   