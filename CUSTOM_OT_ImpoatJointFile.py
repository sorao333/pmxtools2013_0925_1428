import bpy
from bpy_extras.io_utils import ExportHelper,ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator
from pmxtools.CsvTools import *

"""-----------------------------------------
jointファイル読み込み
1.先にgroup[joint]を作っておく
2.実行

--------------------------------------------"""
class CUSTOM_OT_ImpoatJointFile(Operator,ImportHelper):
    bl_idname = "mesh.impoat_joint_file"#bpy登録id半角限定
    bl_label = "jointファイル読み込み" #button label
    bl_description = "ImpoatJointFile" #tooltip
    #デフォルト拡張子
    filename_ext = ".csv"
    #ファイルフィルタ
    filter_glob = StringProperty(
            default="*.csv",
            options={'HIDDEN'},
            )
    

    def execute(self, context):
        readfile = CsvTools.Reader(self.filepath)
        for joint in range(1,len(readfile)):
            #エンプティオブジェクトプロパティ
            bpy.ops.object.add(location = (float(readfile[joint][5])/5
                                        ,float(readfile[joint][7])/5
                                        ,float(readfile[joint][6])/5))
            obj = bpy.context.active_object                            
            obj.name = "joint"
            obj.rotation_euler = (float(readfile[joint][8])
                                                    ,float(readfile[joint][10])
                                                    ,float(readfile[joint][9]))
            obj.empty_draw_size = 0.02
            obj.empty_draw_type = "SPHERE"
            bpy.ops.object.group_link(group="joint")
            
            print(readfile[joint][1])#動作確認用
            
            #初期カスタムプロパティ
            obj["*joint名"] = readfile[joint][1]
            obj["00剛体名A"] = readfile[joint][3]
            obj["01剛体名B"] = readfile[joint][4]
            
            obj["02移動下限_x"] = float(readfile[joint][11])
            obj["03移動下限_y"] = float(readfile[joint][12])
            obj["04移動下限_z"] = float(readfile[joint][13])
            
            obj["05移動上限_x"] = float(readfile[joint][14])
            obj["06移動上限_y"] = float(readfile[joint][15])
            obj["07移動上限_z"] = float(readfile[joint][16])
            
            obj["08回転下限_x"] = float(readfile[joint][17])
            obj["09回転下限_y"] = float(readfile[joint][18])
            obj["10回転下限_z"] = float(readfile[joint][19])
            
            obj["11回転上限_x"] = float(readfile[joint][20])
            obj["12回転上限_y"] = float(readfile[joint][21])
            obj["13回転上限_z"] = float(readfile[joint][22])
            
            obj["14バネ定数-移動_x"] = float(readfile[joint][23])
            obj["15バネ定数-移動_y"] = float(readfile[joint][24])
            obj["16バネ定数-移動_z"] = float(readfile[joint][25])
            
            obj["17バネ定数-回転_x"] = float(readfile[joint][26])
            obj["18バネ定数-回転_y"] = float(readfile[joint][27])
            obj["19バネ定数-回転_z"] = float(readfile[joint][28])
        
        print("ImpoatJointFile")
        print(readfile)
        return {'FINISHED'}
    
#----------------------------------------------------    
if __name__ == "__main__":
    bpy.utils.register_class(CUSTOM_OT_ImpoatJointFile)
    print("CUSTOM_OT_ImpoatJointFile")