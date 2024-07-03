import bpy


class CSVImporterPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_csv_importer"
    bl_label = "CSV Importer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'

    def draw(self, context):
        layout = self.layout
        layout.operator("object.import_csv")
        layout.prop(context.scene, "csv_shape")
        layout.prop(context.scene, "csv_size")
        layout.prop(context.scene, "csv_color")
        layout.operator("object.apply_color", text="Apply Color")
