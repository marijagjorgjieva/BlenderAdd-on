from apply_changes_operator import ApplyChangesOperator
from csv_importer_panel import CSVImporterPanel
from import_csv_operator import ImportCSVOperator

bl_info = {
    "name": "CSV Scatter Plot",
    "blender": (3, 0, 0),
    "category": "Object",
}

import bpy

def register_properties():
    bpy.types.Scene.csv_shape = bpy.props.EnumProperty(
        name="Shape",
        items=[
            ('SPHERE', "Sphere", ""),
            ('CUBE', "Cube", ""),
            ('CONE', "Cone", ""),
            ('CYLINDER', "Cylinder", ""),
        ],
        default='SPHERE'
    )

    bpy.types.Scene.csv_size = bpy.props.FloatProperty(name="Size", default=0.1)
    bpy.types.Scene.csv_color = bpy.props.FloatVectorProperty(name="Color", subtype='COLOR', default=(1.0, 0.0, 0.0),
                                                              min=0.0, max=1.0)


def unregister_properties():
    del bpy.types.Scene.csv_shape
    del bpy.types.Scene.csv_size
    del bpy.types.Scene.csv_color


def menu_func_import(self, context):
    self.layout.operator(ImportCSVOperator.bl_idname, text="CSV Scatter Plot")


def register():
    register_properties()
    bpy.utils.register_class(ImportCSVOperator)
    bpy.utils.register_class(CSVImporterPanel)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)
    bpy.utils.register_class(ApplyChangesOperator)


def unregister():
    unregister_properties()
    bpy.utils.unregister_class(ImportCSVOperator)
    bpy.utils.unregister_class(CSVImporterPanel)
    bpy.utils.unregister_class(ApplyChangesOperator)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()
