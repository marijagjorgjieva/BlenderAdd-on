import csv
import os

import bpy


class ImportCSVOperator(bpy.types.Operator):
    bl_idname = "object.import_csv"
    bl_label = "Import CSV"
    bl_options = {'REGISTER', 'UNDO'}

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        if not self.filepath:
            self.report({'ERROR'}, "Filepath not set")
            return {'CANCELLED'}

        if not os.path.exists(self.filepath):
            self.report({'ERROR'}, f"File not found: {self.filepath}")
            return {'CANCELLED'}

        # Pass context to import_csv method
        self.import_csv(context, self.filepath)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def import_csv(self, context, filepath):
        # Clear existing objects
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)

        # Read CSV file
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                x = float(row['X'])
                y = float(row['Y'])
                z = float(row['Z'])
                label = row['Label']
                shape = context.scene.csv_shape
                size = context.scene.csv_size
                color = context.scene.csv_color

                if shape == 'SPHERE':
                    bpy.ops.mesh.primitive_uv_sphere_add(radius=size, location=(x, y, z))
                elif shape == 'CUBE':
                    bpy.ops.mesh.primitive_cube_add(size=size, location=(x, y, z))
                elif shape == 'CONE':
                    bpy.ops.mesh.primitive_cone_add(radius1=size, depth=size, location=(x, y, z))
                elif shape == 'CYLINDER':
                    bpy.ops.mesh.primitive_cylinder_add(radius=size, depth=size, location=(x, y, z))

                obj = bpy.context.object
                mat = bpy.data.materials.new(name="Material")
                mat.diffuse_color = (*color, 1)
                if obj.data.materials:
                    obj.data.materials[0] = mat
                else:
                    obj.data.materials.append(mat)
