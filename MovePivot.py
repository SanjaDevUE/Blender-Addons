bl_info = {
    "name": "Set Origin to Selected Vertex",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
import bmesh
from mathutils import Vector

class OBJECT_OT_set_origin_to_selected_vertex(bpy.types.Operator):
    bl_idname = "object.set_origin_to_selected_vertex"
    bl_label = "Set Origin to Selected Vertex"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.object.mode == 'EDIT'

    def execute(self, context):
        original_cursor_location = bpy.context.scene.cursor.location.copy()
        obj = context.object
        mesh = obj.data
        bm = bmesh.from_edit_mesh(mesh)
        selected_verts = [v for v in bm.verts if v.select]
        
        if len(selected_verts) != 1:
            self.report({'WARNING'}, "Please select exactly one vertex.")
            return {'CANCELLED'}
        
        vertex_location = obj.matrix_world @ selected_verts[0].co
        bpy.context.scene.cursor.location = vertex_location
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.context.scene.cursor.location = original_cursor_location

        self.report({'INFO'}, "Origin set to selected vertex location, cursor restored.")
        return {'FINISHED'}


class VIEW3D_PT_set_origin_panel(bpy.types.Panel):
    bl_label = "Set Origin to Vertex"
    bl_idname = "VIEW3D_PT_set_origin_to_vertex_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Set Origin'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Set Origin Operations", icon='OBJECT_ORIGIN')
        layout.operator("object.set_origin_to_selected_vertex", text="Set Origin to Selected Vertex")
        layout.label(text="Copyright by SanjaDev")


def register():
    bpy.utils.register_class(OBJECT_OT_set_origin_to_selected_vertex)
    bpy.utils.register_class(VIEW3D_PT_set_origin_panel)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_set_origin_to_selected_vertex)
    bpy.utils.unregister_class(VIEW3D_PT_set_origin_panel)


if __name__ == "__main__":
    register()
