import bpy
import csv
import codecs

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

        row = layout.row()
        row.label(text="Add Objects:")

        split = layout.split()
        col = split.column(align=True)
        #ボタン登録
        col.operator("mesh.jointool")
        col.operator("mesh.joint_file_w")
        col.operator("mesh.impoat_joint_file")
#---------------------------------------------------------        
"""
ＣＳＶファイルツール
書き込んだり読み込んだり
"""
class CsvTools(csv.excel):
    """
    読み込みパラメータとか
    quoting
    csv.QUOTE_MINIMAL csv.QUOTE_ALL csv.QUOTE_NONNUMERIC
    """
#   quoting   = csv.QUOTE_ALL
#   delimiter = "\t"
    """
    書き込み
    rows 書き込む内容二次配列[(ver,ver),(ver,ver)]
    file 書き込むファイル名:string
    """
    @classmethod
    def writer(cls,rows,file):
        with open(file ,"w", newline='') as csvfile:
            writer = csv.writer(csvfile,CsvTools())
            writer.writerows(rows)
    #-----------------------------------------------
    """
    CSVを読み込んでCSVオブジェクトで返す
    file 読み込むファイル名:string
    return 読み込まれたデータのリスト
    """
    @classmethod
    def Reader(cls,file):
        with open(file,newline='') as csvfile:
            RtRows = list(csv.reader(csvfile,CsvTools()))[:]
        return RtRows
#-------------------------------------------------------
"""-----------------------------------
 骨に沿ってジョイント配置
1.先にgroup[joint]を作っておく
2.エディットモードでボーンを選択する
3.実行
-----------------------------------"""
class CUSTOM_OT_Createjoint(bpy.types.Operator):
    bl_idname = "mesh.jointool"#bpy登録id半角限定
    bl_label = "骨に沿ってjoint設置  " #button label
    bl_description = "Createjoint" #tooltip
        
    def execute(self, context):
        bones = bpy.context.selected_editable_bones
        bpy.ops.object.mode_set()
        for bone in bones:
            bpy.ops.object.add(location = bone.head)
            bpy.context.active_object.name = "joint_" + bone.name
            #scn = bpy.context.scene 
            #scn.objects.active = scn.objects["joint_" + bone.name]
            bpy.ops.object.group_link(group="joint")
            
            print(bone.name)#動作確認用
            bpy.context.active_object.empty_draw_size = 0.02
            bpy.context.active_object.empty_draw_type = "SPHERE"
            #初期プロパティ
            bpy.context.active_object["00剛体名A"] = ""
            bpy.context.active_object["01剛体名B"] = ""
            
            bpy.context.active_object["02移動下限_x"] = 0.0
            bpy.context.active_object["03移動下限_y"] = 0.0
            bpy.context.active_object["04移動下限_z"] = 0.0
            
            bpy.context.active_object["05移動上限_x"] = 0.0
            bpy.context.active_object["06移動上限_y"] = 0.0
            bpy.context.active_object["07移動上限_z"] = 0.0
            
            bpy.context.active_object["08回転下限_x"] = 0.0
            bpy.context.active_object["09回転下限_y"] = 0.0
            bpy.context.active_object["10回転下限_z"] = 0.0
            
            bpy.context.active_object["11回転上限_x"] = 0.0
            bpy.context.active_object["12回転上限_y"] = 0.0
            bpy.context.active_object["13回転上限_z"] = 0.0
            
            bpy.context.active_object["14バネ定数-移動_x"] = 0.0
            bpy.context.active_object["15バネ定数-移動_y"] = 0.0
            bpy.context.active_object["16バネ定数-移動_z"] = 0.0
            
            bpy.context.active_object["17バネ定数-回転_x"] = 0.0
            bpy.context.active_object["18バネ定数-回転_y"] = 0.0
            bpy.context.active_object["19バネ定数-回転_z"] = 0.0
            
            
        return {'FINISHED'}
                     
#-------------------------------------------------------        
"""
ジョイントデータ書き出し
*書き出したファイルはBlenderフォルダに作られる。(xxx.cvs)
*ジョイントは必ず同一グループに登録すること
*ジョイントを必ず一つ選択する事
*カスタムプロパティが足りないとエラー
"""
class JointFileW(bpy.types.Operator):
    bl_idname = "mesh.joint_file_w"#bpy登録id半角限定
    bl_label = "jointデータ書き出し" #button label
    
    def execute(self, context):
        bpy.ops.object.select_grouped(type = "GROUP")
        """
        selected_objectsが尻から処理されるため
        行ごとに先頭に追加していく
        """
        ystr = []#ｙ軸文字列（全体）
        for x in bpy.context.selected_objects:
            ystr.insert(0,["Joint",
                        x.name,
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
        CsvTools.writer(ystr,"joint.csv")    
        
        print("\nwrite")
        return {'FINISHED'}    
#---------------------------------
"""-----------------------------------------
jointファイル読み込み



--------------------------------------------"""
class CUSTOM_OT_ImpoatJointFile(bpy.types.Operator):
    bl_idname = "mesh.impoat_joint_file"#bpy登録id半角限定
    bl_label = "jointファイル読み込み" #button label
    bl_description = "ImpoatJointFile" #tooltip
    
    def execute(self, context):
        readfile = CsvTools.Reader("joint.csv")
        print("ImpoatJointFile")
        print(readfile)
        return {'FINISHED'}
    
#----------------------------------------------------    
def register():
    bpy.utils.register_class(CUSTOM_OT_ImpoatJointFile)
    bpy.utils.register_class(CUSTOM_OT_Createjoint)
    bpy.utils.register_class(JointFileW)
    bpy.utils.register_class(CustomPanel)

def unregister():
    bpy.utils.unregister_class(CustomPanel)

if __name__ == "__main__":
    register()