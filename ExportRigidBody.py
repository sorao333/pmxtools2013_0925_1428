import bpy
from bpy_extras.io_utils import ExportHelper,ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator
from pmxtools.CsvTools import *
import math
"""
剛体データ書き出し
*剛体は必ず同一グループに登録すること
*剛体を必ず一つ選択する事
*カスタムプロパティが足りないとエラー
"""
class ExportRigidBody(Operator, ExportHelper):
    bl_idname = "mesh.export_rigid"#bpy登録id半角限定
    bl_label = "剛体データ書き出し" #button label
    #デフォルト拡張子
    filename_ext = ".csv"
    #ファイルフィルタ
    filter_glob = StringProperty(
            default="*.csv",
            options={'HIDDEN'},
            )
    
            
    def execute(self, context):
        bpy.ops.object.select_grouped(type = "GROUP")
        ystr = []#ｙ軸文字列（全体）
        for x in bpy.context.selected_objects:
            if x["05形状"] == 0 :#球
                 dimensions_x = str(x.dimensions[0]*2.5)
                 dimensions_y = str(x.dimensions[2]*2.5)
                 dimensions_z = str(x.dimensions[1]*2.5)
            elif x["05形状"] == 1:#箱
                 dimensions_x = str(x.dimensions[0]*2)
                 dimensions_y = str(x.dimensions[2]*2)
                 dimensions_z = str(x.dimensions[1]*2)
            elif x["05形状"] == 2:#カプセル
                 dimensions_x = str(x.dimensions[0]*3)
                 dimensions_y = str(x.dimensions[2]*3)
                 dimensions_z = str(x.dimensions[1]*4)   
            
            rotation_x = str(-x.rotation_euler[0] * 180 / math.pi)
            rotation_y = str(-x.rotation_euler[2] * 180 / math.pi)
            rotation_z = str(-x.rotation_euler[1] * 180 / math.pi)     
            ystr.insert(0,["Body",
                        x["*剛体名"],
                        x["00剛体名(英)"],
                        x["01関連ボーン名"],
                        x["02剛体タイプ"],
                        x["03グループ(0~15)"],
                        x["04非衝突グループ"],
                        x["05形状"],
                        dimensions_x,
                        dimensions_y,
                        dimensions_z,
                        str(x.location[0]*5),
                        str(x.location[2]*5),
                        str(x.location[1]*5),
                        rotation_x,
                        rotation_y,
                        rotation_z,
                        str(x["06質量"]),
                        str(x["07移動減衰"]),
                        str(x["08回転減衰"]),
                        str(x["09反発力"]),
                        str(x["10摩擦力"])                        
                        ]) 
        head = [";Body","剛体名","剛体名(英)","関連ボーン名","剛体タイプ(0:Bone/1:物理演算/2:物理演算+ボーン追従)","グループ(0~15)","非衝突グループ文字列(ex:1 2 3 4)","形状(0:球/1:箱/2:カプセル)","サイズ_x","サイズ_y","サイズ_z","位置_x","位置_y","位置_z","回転_x[deg]","回転_y[deg]","回転_z[deg]","質量","移動減衰","回転減衰","反発力","摩擦力\n"]
        ystr.insert(0 ,head) 
        CsvTools.writer(ystr,self.filepath)
        print("export_rigid")
        return {'FINISHED'}

#---------------------------------
if __name__ == "__main__":
    bpy.utils.register_class(ExportRigidBody)
    print("ExportRigidBody.py")    