import bpy
"""-----------------------------------
 骨に沿っ剛体を配置
1.先にgroup[rigid]を作っておく
2.エディットモードでボーンを選択する
3.実行
-----------------------------------"""
"""
CUBE
"""
class RigidCubeByBone(bpy.types.Operator):
    bl_idname = "mesh.rigid_cube_bone_add"#bpy登録id半角限定
    bl_label = "骨に沿ってCube剛体を配置" #button label
    bl_description = "1.先にgroup[rigid]を作っておく\n2.エディットモードでボーンを選択する\n3.実行" #tooltip
    
    def execute(self, context):
        bones = bpy.context.selected_editable_bones
        bpy.ops.object.mode_set()
        target = bpy.context.active_object.name#コンストレイントターゲット
        for bone in bones:
            #オブジェクトプロパティ
            #location
            riglocation_x = bone.tail[0] + ((bone.head[0] - bone.tail[0]) / 2)
            riglocation_y = bone.tail[1] + ((bone.head[1] - bone.tail[1]) / 2)
            riglocation_z = bone.tail[2] + ((bone.head[2] - bone.tail[2]) / 2)
            riglocation = (riglocation_x , riglocation_y, riglocation_z)#ボーンの真ん中
            bpy.ops.mesh.primitive_cube_add(radius = 0.25 , location = riglocation)
            #name and group
            bpy.ops.object.group_link(group="rigid")
            obj = bpy.context.active_object
            #rotation
            bpy.ops.object.constraint_add(type = "COPY_ROTATION")
            obj.constraints["回転コピー"].target = bpy.data.objects[target]
            obj.constraints["回転コピー"].subtarget = bone.name
            bpy.ops.object.visual_transform_apply()
            bpy.ops.transform.rotate(value = 1.5708 , constraint_axis = (True,False,False),constraint_orientation = "NORMAL")
            obj.constraints.remove(obj.constraints["回転コピー"])
            
            
            #初期カスタムプロパティ
            obj["*剛体名"] = bone.name
            obj["00剛体名(英)"] = "e"
            obj["01関連ボーン名"] = bone.name
            obj["02剛体タイプ"] = 0 #剛体タイプ(0:Bone/1:物理演算/2:物理演算+ボーン追従)
            obj["03グループ(0~15)"] = 0
            obj["04非衝突グループ"] = "0"#非衝突グループ文字列(ex:1 2 3 4)
            obj["05形状"] = 1#形状(0:球/1:箱/2:カプセル)
            obj["06質量"] = 1.0
            obj["07移動減衰"] = 0.5
            obj["08回転減衰"] = 0.5
            obj["09反発力"] = 0.0
            obj["10摩擦力"] = 0.5
            
            
            print(bone.name)#動作確認用
        print("CreateRBody")
        return {'FINISHED'}
#-------------------------------------------------------
"""
球
"""

class RigidSphereByBone(bpy.types.Operator):
    bl_idname = "mesh.rigid_sphere_bone_add"#bpy登録id半角限定
    bl_label = "骨に沿ってSphere剛体を配置" #button label
    bl_description = "1.先にgroup[rigid]を作っておく\n2.エディットモードでボーンを選択する\n3.実行" #tooltip
    
    def execute(self, context):
        bones = bpy.context.selected_editable_bones
        bpy.ops.object.mode_set()
        target = bpy.context.active_object.name#コンストレイントターゲット
        for bone in bones:
            #オブジェクトプロパティ
            #location
            riglocation_x = bone.tail[0] + ((bone.head[0] - bone.tail[0]) / 2)
            riglocation_y = bone.tail[1] + ((bone.head[1] - bone.tail[1]) / 2)
            riglocation_z = bone.tail[2] + ((bone.head[2] - bone.tail[2]) / 2)
            riglocation = (riglocation_x , riglocation_y, riglocation_z)#ボーンの真ん中
            bpy.ops.mesh.primitive_uv_sphere_add(size = 0.25 ,location = riglocation)
            #name and group
            bpy.ops.object.group_link(group="rigid")
            obj = bpy.context.active_object
            #初期カスタムプロパティ
            obj["*剛体名"] = bone.name
            obj["00剛体名(英)"] = "e"
            obj["01関連ボーン名"] = bone.name
            obj["02剛体タイプ"] = 0 #剛体タイプ(0:Bone/1:物理演算/2:物理演算+ボーン追従)
            obj["03グループ(0~15)"] = 0
            obj["04非衝突グループ"] = "0"#非衝突グループ文字列(ex:1 2 3 4)
            obj["05形状"] = 0#形状(0:球/1:箱/2:カプセル)
            obj["06質量"] = 1.0
            obj["07移動減衰"] = 0.5
            obj["08回転減衰"] = 0.5
            obj["09反発力"] = 0.0
            obj["10摩擦力"] = 0.5
            
            
            print(bone.name)#動作確認用
        print("CreateRBody")
        return {'FINISHED'}
#-------------------------------------------------------
"""
カプセル（シリンダー）
"""

class RigidCylinderByBone(bpy.types.Operator):
    bl_idname = "mesh.rigid_cylinder_bone_add"#bpy登録id半角限定
    bl_label = "骨に沿ってcylinder剛体を配置" #button label
    bl_description = "1.先にgroup[rigid]を作っておく\n2.エディットモードでボーンを選択する\n3.実行" #tooltip
    
    def execute(self, context):
        bones = bpy.context.selected_editable_bones
        bpy.ops.object.mode_set()
        target = bpy.context.active_object.name#コンストレイントターゲット
        for bone in bones:
            #オブジェクトプロパティ
            #location
            riglocation_x = bone.tail[0] + ((bone.head[0] - bone.tail[0]) / 2)
            riglocation_y = bone.tail[1] + ((bone.head[1] - bone.tail[1]) / 2)
            riglocation_z = bone.tail[2] + ((bone.head[2] - bone.tail[2]) / 2)
            riglocation = (riglocation_x , riglocation_y, riglocation_z)#ボーンの真ん中
            bpy.ops.mesh.primitive_cylinder_add(radius = 0.25 ,location = riglocation)
            #name and group
            bpy.ops.object.group_link(group="rigid")
            obj = bpy.context.active_object
            #rotation
            bpy.ops.object.constraint_add(type = "COPY_ROTATION")
            obj.constraints["回転コピー"].target = bpy.data.objects[target]
            obj.constraints["回転コピー"].subtarget = bone.name
            bpy.ops.object.visual_transform_apply()
            bpy.ops.transform.rotate(value = 1.5708 , constraint_axis = (True,False,False),constraint_orientation = "NORMAL")
            obj.constraints.remove(obj.constraints["回転コピー"])
                        
            #初期カスタムプロパティ
            obj["*剛体名"] = bone.name
            obj["00剛体名(英)"] = "e"
            obj["01関連ボーン名"] = bone.name
            obj["02剛体タイプ"] = 0 #剛体タイプ(0:Bone/1:物理演算/2:物理演算+ボーン追従)
            obj["03グループ(0~15)"] = 0
            obj["04非衝突グループ"] = "0"#非衝突グループ文字列(ex:1 2 3 4)
            obj["05形状"] = 2#形状(0:球/1:箱/2:カプセル)
            obj["06質量"] = 1.0
            obj["07移動減衰"] = 0.5
            obj["08回転減衰"] = 0.5
            obj["09反発力"] = 0.0
            obj["10摩擦力"] = 0.5
            
            
            print(bone.name)#動作確認用
        print("CreateRBody")
        return {'FINISHED'}
#-------------------------------------------------------


if __name__ == "__main__":
    bpy.utils.register_class(RigidCubeByBone)
    bpy.utils.register_class(RigidSphereByBone)
    bpy.utils.register_class(RigidCylinderByBone)
      
        