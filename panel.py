import bpy
import os
from common_utilities import get_settings


            
class VIEW3D_PT_D3ToolAssitant(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type="TOOLS"
    bl_category = "Dental"
    bl_label = "D3Tool Assistant Panel"
    bl_context = ""

    def draw(self, context):
        sce = bpy.context.scene
        layout = self.layout
        
        #split = layout.split()
        row = layout.row()

        row.operator("wm.url_open", text = "Wiki", icon="INFO").url = "https://d3tool.com/knowledge-base/"
        row.operator("wm.url_open", text = "Tutorials", icon="ERROR").url = "https://d3tool.com/d3splint-membership-videos/"
        row.operator("wm.url_open", text = "Forum", icon="QUESTION").url = "https://www.facebook.com/groups/939777786197766"
        

        row = layout.row()
        row.label(text = "Save/Checkpoints")
        row = layout.row()
        col = row.column()
        col.operator("wm.save_as_mainfile", text = "Save").copy = False
        col.operator("wm.splint_saveincremental", text = "Save Checkpoint")      
          
class VIEW3D_PT_D3Models(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type="TOOLS"
    bl_category = "Dental"
    bl_label = "Model Operations"
    bl_context = ""
    
    def draw(self, context):
        prefs = get_settings()
        sce = bpy.context.scene
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Model Operators")
        row.operator("wm.url_open", text = "", icon="INFO").url = "https://d3tool.com/knowledge-base/"
          
        if context.object != None:
            row = layout.row()
            txt = context.object.name
            row.label(text = "Selected Model: " + txt)
        
        else:
            row = layout.row()
            row.label(text = "Please Select a Model")
            
        row = layout.row()
        row.label('Sculpt/Paint Mode Tools')
        row = layout.row()
        col = row.column()    
        col.operator("d3splint.enter_sculpt_paint_mask", text = "Paint Model")
        col.operator("paint.mask_flood_fill", text = "Clear Paint").mode = 'VALUE'
        col.operator("d3splint.delete_sculpt_mask", text = "Delete Painted") #defaults to .value = 0
        col.operator("d3splint.close_paint_hole", text = 'Close Paint Hole')
        col.operator("d3splint.delete_sculpt_mask_inverse", text = "Keep Only Painted")

        if context.mode == 'SCULPT':
            col.operator("object.mode_set", text = 'Finish Sculpt/Paint')
        
        row = layout.row()
        row.label('Fixing and Cleaning Operators')
        row = layout.row()
              
        #col.operator("d3splint.simple_offset_surface", text = "Simple Offset")
        
        row.prop(prefs, "d3_model_auto_fill_small")
        row.prop(prefs, "d3_model_max_hole_size")
        
        row = layout.row()
        col = row.column()
        col.operator("d3model.mesh_repair", text = "Fix Holes and Islands")
        col.operator("d3splint.delete_islands", text = "Delete Loose Parts")
        col.operator("d3splint.ragged_edges", text = "Remove Ragged Edges")
        
        row = layout.row()
        row.label('Open Model Cutting')
        row = layout.row()
        col = row.column()
        col.operator("d3splint.splint_plane_cut", text = "Plane Cut Open Model").cut_method = "SURFACE"
        
        row = layout.row()
        row.label('Close Model Cutting')
        row = layout.row()
        
        col = row.column()
        col.operator("d3splint.splint_plane_cut", text = "Plane Cut Closed Model").cut_method = "SOLID"
        
        col.operator("d3splint.splint_pause_plane_cuts", text = "De-Activate Cuts")
        col.operator("d3splint.splint_activate_plane_cuts", text = "Re-Activate Cuts")
        col.operator("d3splint.splint_finalize_plane_cuts", text = "Apply All Cuts")
        
        row = layout.row()
        row.label('Base and Thickness Operators')
        row = layout.row()
        col = row.column()
        col.operator("d3splint.simple_base", text = "Simple Base")            
        #col.operator("d3splint.model_wall_thicken", text = 'Hollow Model')
        col.operator("d3splint.model_wall_thicken2", text = 'Hollow Model')
        col.operator("d3tool.model_vertical_base", text = 'Vertical Base')
        
        row = layout.row()
        row.label('Batch Processing')
        row = layout.row()
        col = row.column()
        
        col.operator("d3splint.batch_process_plane_cuts", text = 'Batch Plane Cuts')
        
        
class VIEW3D_PT_D3SModelText(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type="TOOLS"
    bl_category = "Dental"
    bl_label = "Model Text Embossing"
    bl_context = ""
    
    def draw(self, context):
        sce = bpy.context.scene
        layout = self.layout
        prefs = get_settings()
         
        row = layout.row()
        row.label(text = "Model Labelling")
        #row.operator("wm.url_open", text = "", icon="INFO").url = "https://github.com/patmo141/odc_public/wiki"
          
        if context.object != None:
            row = layout.row()
            txt = context.object.name
            row.label(text = "Selected Model: " + txt)
        
        else:
            row = layout.row()
            row.label(text = "Please Select a Model")
            
            #row = layout.row()
            #row.label(text = 'SVG Image Workflow')
        
        row = layout.row()
        row.label(text = 'Add Text to Object')
        
        row = layout.row()
        col = row.column()
        col.prop(prefs, "d3_model_label", text = '')
        col.prop(prefs, "d3_model_label_depth", text = 'Text Depth')
        row = layout.row()
        row.operator("d3splint.stencil_text", text = 'Stencil Text Label')
        row = layout.row()
        row.operator("d3tool.remesh_and_emboss_text", text = 'Emboss All Labels onto Object')
        row = layout.row()
        row.operator("d3splint.splint_finalize_labels", text = 'Finalize Label Modifiers')
        
def register():
    bpy.utils.register_class(VIEW3D_PT_D3ToolAssitant)
    bpy.utils.register_class(VIEW3D_PT_D3Models)
    bpy.utils.register_class(VIEW3D_PT_D3SModelText)
    

    
def unregister():
    
    bpy.utils.unregister_class(VIEW3D_PT_D3ToolAssitant)
    bpy.utils.unregister_class(VIEW3D_PT_D3Models)
    bpy.utils.unregister_class(VIEW3D_PT_D3SModelText)
if __name__ == "__main__":
    register()