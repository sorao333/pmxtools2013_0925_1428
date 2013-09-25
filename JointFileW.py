import bpy
from bpy_extras.io_utils import ExportHelper,ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator
from pmxtools.CsvTools import *
"""
ジョイントデータ書き出し
*ジョイントは必ず同一グループに登録すること
*ジョイントを必ず一つ選択する事
*カスタムプロパティが足りないとエラー
"""
class JointFileW(Operator, ExportHelper):
    bl_idname = "mesh.joint_file_w"#bpy登録id半角限定
    bl_label = "jointデータ書き出し" #button label
    #デフォルト拡張子
    filename_ext = ".csv"
    #ファイルフィルタ
    filter_glob = StringProperty(
            default="*.csv",
            options={'HIDDEN'},
            )
    
        
    def execute(self, context):
        bpy.ops.object.select_grouped(type = "GROUP")
        """
        selected_objectsが尻から処理されるため
        行ごとに先頭に追加していく
        """
        ystr = []#ｙ軸文字列（全体）
        for x in bpy.context.selected_objects:
            ystr.insert(0,["Joint",
                        x["*joint名"],
                        "",
                        x["00剛体名A"],
                        x["01剛体名B"],
                        str(x.location[0]*5),
                        str(x.location[2]*5),
                        str(x.location[1]*5),
                        str(x.rotation_euler[0]),
                        str(x.rotation_euler[2]),
                        str(x.rotation_euler[1]),
                        str(x["02移動下限_x"]),
                        str(x["03移動下限_y"]),
                        str(x["04移動下限_z"]),
                        str(x["05移動上限_x"]),
                        str(x["06移動上限_y"]),
                        str(x["07移動上限_z"]),
                        str(x["08回転下限_x"]),
                        str(x["09回転下限_y"]),
                        str(x["10回転下限_z"]),
                        str(x["11回転上限_x"]),
                        str(x["12回転上限_y"]),
                        str(x["13回転上限_z"]),
                        str(x["14バネ定数-移動_x"]),
                        str(x["15バネ定数-移動_y"]),
                        str(x["16バネ定数-移動_z"]),
                        str(x["17バネ定数-回転_x"]),
                        str(x["18バネ定数-回転_y"]),
                        str(x["19バネ定数-回転_z"])
                        ]) 
        head = [";Joint","Joint名","Joint名(英)","剛体名A","剛体名B","位置_x","位置_y","位置_z","回転_x[deg]","回転_y[deg]","回転_z[deg]","移動下限_x","移動下限_y","移動下限_z","移動上限_x","移動上限_y","移動上限_z","回転下限_x[deg]","回転下限_y[deg]","回転下限_z[deg]","回転上限_x[deg]","回転上限_y[deg]","回転上限_z[deg]","バネ定数-移動_x","バネ定数-移動_y","バネ定数-移動_z","バネ定数-回転_x","バネ定数-回転_y","バネ定数-回転_z\n"]
        ystr.insert(0 ,head) 
        CsvTools.writer(ystr,self.filepath)        
        print("\nwrite")
        return {'FINISHED'}    
#---------------------------------
if __name__ == "__main__":
    bpy.utils.register_class(JointFileW)
    print("JointFileW.py")