import bpy
class CreateRigidChain(bpy.types.Operator):
    bl_idname = "mesh.create_rchain"#bpy登録id半角限定
    bl_label = "骨に沿って剛体チェーンを接合" #button label
#    bl_description = ""
    def execute(self, context):
        for select in bpy.context.selected_objects:
            if select.type != "EMPTY":
                print(select.name)
            
        
        
        print("Createchain")
        return {'FINISHED'}
#-------------------------------------------------------
if __name__ == "__main__":
    bpy.utils.register_class(CreateRigidChain)    