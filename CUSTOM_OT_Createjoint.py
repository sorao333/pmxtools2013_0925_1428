import bpy
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
            #エンプティオブジェクトプロパティ
            bpy.ops.object.add(location = bone.head)
            obj = bpy.context.active_object
            
            obj.empty_draw_size = 0.02
            obj.empty_draw_type = "SPHERE"
            bpy.ops.object.group_link(group="joint")
            
            print(bone.name)#動作確認用
            
            #初期カスタムプロパティ
            obj["*joint名"] = bone.name
            obj["00剛体名A"] = ""
            obj["01剛体名B"] = ""
            
            obj["02移動下限_x"] = 0.0
            obj["03移動下限_y"] = 0.0
            obj["04移動下限_z"] = 0.0
            
            obj["05移動上限_x"] = 0.0
            obj["06移動上限_y"] = 0.0
            obj["07移動上限_z"] = 0.0
            
            obj["08回転下限_x"] = 0.0
            obj["09回転下限_y"] = 0.0
            obj["10回転下限_z"] = 0.0
            
            obj["11回転上限_x"] = 0.0
            obj["12回転上限_y"] = 0.0
            obj["13回転上限_z"] = 0.0
            
            obj["14バネ定数-移動_x"] = 0.0
            obj["15バネ定数-移動_y"] = 0.0
            obj["16バネ定数-移動_z"] = 0.0
            
            obj["17バネ定数-回転_x"] = 0.0
            obj["18バネ定数-回転_y"] = 0.0
            obj["19バネ定数-回転_z"] = 0.0
            
            
        return {'FINISHED'}
                     
#-------------------------------------------------------
if __name__ == "__main__":
    bpy.utils.register_class(CUSTOM_OT_Createjoint)     