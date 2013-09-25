import bpy
def drawtype(type):
    for x in bpy.context.selected_objects:
        x.draw_type = type
"""
関連ボーンに位置合わせ
位置を合わせるオブジェクト＞アマチュアの順に選択して実行
"""
def bonecenter():
  #  bpy.data.objects[target]
    context = bpy.context
    armname = context.active_object.name
    for obj in bpy.context.selected_objects:
        if obj.name != armname:     
            bonename = obj["01関連ボーン名"]
            bone = bpy.data.objects[armname].data.bones[bonename]
            print(bone.tail)
            #location
            riglocation_x = bone.tail_local[0] + ((bone.head_local[0] - bone.tail_local[0]) / 2)
            riglocation_y = bone.tail_local[1] + ((bone.head_local[1] - bone.tail_local[1]) / 2)
            riglocation_z = bone.tail_local[2] + ((bone.head_local[2] - bone.tail_local[2]) / 2)
            riglocation = (riglocation_x , riglocation_y, riglocation_z)#ボーンの真ん中
            obj.location = riglocation
            
"""
オブジェクトトランスフォームのミラーコピー
（location位置，rotation回転，dimension寸法）
コピー元>コピー先の順に選択して実行

"""    
def DataMirrorCopy(location = True , rotation = True , dimension = True):
    act = bpy.context.active_object
    print(act)
    for obj in bpy.context.selected_objects:
        if obj.name != act.name:
            if location:
                obj.location = (-act.location[0],act.location[1],act.location[2])
            if rotation:
                obj.rotation_euler = (act.rotation_euler[0],-act.rotation_euler[1],-act.rotation_euler[2])
            if dimension:
                obj.dimensions = act.dimensions        
#--------------------------------------------------------
bonecenter()     
#DataMirrorCopy()    