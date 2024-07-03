import bpy


class ApplyChangesOperator(bpy.types.Operator):
    bl_idname = "object.apply_color"
    bl_label = "Apply Color"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        selected_objects = bpy.context.selected_objects
        color = context.scene.csv_color
        size = context.scene.csv_size
        for obj in selected_objects:
            if obj.type == 'MESH':
                obj.scale = (size, size, size)
                mat = bpy.data.materials.new(name="Material")
                mat.diffuse_color = (*color, 1)

                if obj.data.materials:
                    obj.data.materials[0] = mat
                else:
                    obj.data.materials.append(mat)

        return {'FINISHED'}