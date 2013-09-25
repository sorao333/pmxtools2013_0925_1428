import bpy
"""
剛体ＡとＢをジョイントで結合
"""
class JointAtoB(bpy.types.Operator):
    bl_idname = "mesh.joint_a_to_b"#bpy登録id半角限定
    bl_label = "剛体ＡとＢをジョイントで結合" #button label
#    bl_description = "" #tooltip

    def execute(self, context):
        aobj = bpy.context.active_object#剛体Ａ
        print(aobj)
        for obj in bpy.context.selected_objects:
            if obj.name != aobj.name:
                bobj = obj#剛体B
        loc_x = aobj.location[0] + ((bobj.location[0] - aobj.location[0]) / 2)            
        loc_y = aobj.location[1] + ((bobj.location[1] - aobj.location[1]) / 2)
        loc_z = aobj.location[2] + ((bobj.location[2] - aobj.location[2]) / 2)
        loc = (loc_x, loc_y, loc_z)
        #エンプティオブジェクトプロパティ
        bpy.ops.object.add(location = loc)
        obj = bpy.context.active_object
        
        obj.empty_draw_size = 0.02
        obj.empty_draw_type = "SPHERE"
        bpy.ops.object.group_link(group="joint")
            #初期カスタムプロパティ
             
        obj["*joint名"] = bobj["*剛体名"] +"to"+ aobj["*剛体名"] 
        obj["00剛体名A"] = bobj["*剛体名"]
        obj["01剛体名B"] = aobj["*剛体名"]
        
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
    
        
        print(JointAtoB)
        return {'FINISHED'}
#---------------------------------------------------
if __name__ == "__main__":
    bpy.utils.register_class(JointAtoB)