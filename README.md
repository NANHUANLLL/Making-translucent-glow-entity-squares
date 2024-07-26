文件一    
resource_pack\materials\entity.materialss
{
  "materials": {
    "version": "1.0.0",
    "tms_alpha_light:entity_static": {
      "+defines": [
        "USE_UV_ANIM",
        "ALPHA_TEST",
        "USE_EMISSIVE"
      ],
      "+states":["Blending","DisableCulling"]
    }
  }
}
文件二
resource\entity\xcuxn_block.json
"materials": {
    "default": "tms_alpha_light"
},
"render_controllers": [
    "controller.render.default"
],
![2ec656f617fd4adf87ca19bd7b10e3db](https://github.com/user-attachments/assets/729d3e98-270d-4595-9069-d927832762e1)
