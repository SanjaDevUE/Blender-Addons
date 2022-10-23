bl_info = {
    "name": "RemoveDoubles",
    "description": "A simple click button to remove everything that is duplicated.",
    "author": "SanjaDev",
    "version": (1, 0),
    "blender": (3, 1, 0),
    "location": "View3D > Add > Mesh",
    "warning": "",
    "support": "COMMUNITY",
    "category": "Add Mesh",
}

import bpy


class Remove3DDoubles(bpy.types.Panel):
    """Create a Panel"""
    bl_category = "SanjaDev Tools"
    bl_context = "objectmode"
    bl_space_type = "VIEW_3D"
    bl_name = "Removedoubleshelper"
    bl_label = "RemoveDoubles"
    bl_region_type = "UI"
        
    def draw(self, context):
        layout = self.layout
        view = context.space_data
        
        row = layout.row()
        row.operator("remove.alldouples", text="RemoveDoubles", icon="XRAY")
        
class RemoveDoubles3D(bpy.types.Operator):
    bl_idname = "remove.alldouples"
    bl_label = "Button"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        scene = context.scene
        
        if bpy.context.selected_objects != []:
            for obj in bpy.context.selected_objects:
                if obj.type == 'MESH':
                    print(obj.name)
                    bpy.ops.object.editmode_toggle()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.remove_doubles()
                    bpy.ops.object.editmode_toggle()
        
        return {'FINISHED'}


def register():
    bpy.utils.register_class(Remove3DDoubles)
    bpy.utils.register_class(RemoveDoubles3D)
    
    #import bpy.utils.previews
    #pcoll = bpy.utils.previews.new()
    
    #my_icon_dir = bpy.utils.user_resource('SCRIPTS', path='addons\Shader', create=False)
    #pcoll.load("my_rdicon", os.path.join(my_rdicon_dir, "rdicon.png"), 'IMAGE')
    
    #preview_collections["main"] = pcoll


def unregister():
    bpy.utils.unregister_class(Remove3DDoubles)
    bpy.utils.unregister_class(RemoveDoubles3D)


if __name__ == "__main__":
    register()