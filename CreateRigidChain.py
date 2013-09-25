import bpy
class CreateRigidChain(bpy.types.Operator):
    bl_idname = "mesh.create_rchain"#bpy登録id半角限定
    bl_label = "骨に沿って剛体チェーンを接合" #button label
#    bl_description = ""
    def execute(self, context):
        #剛体とジョイントを振り分け
        JointAry = []
        RigidAry = []
        for select in bpy.context.selected_objects:
            if select.type == "EMPTY":
                JointAry.insert(0,select)    
            else:
                RigidAry.insert(0,select)
        #ジョイントに接合情報入力
        for num in range(len(JointAry)):
            if not num:
                JointAry[num]["01剛体名B"] = RigidAry[num]["*剛体名"]
            else:
                JointAry[num]["00剛体名A"] = RigidAry[num-1]["*剛体名"]
                JointAry[num]["01剛体名B"] = RigidAry[num]["*剛体名"]    
        
        print("Createchain")
        return {'FINISHED'}
#-------------------------------------------------------
if __name__ == "__main__":
    bpy.utils.register_class(CreateRigidChain)    