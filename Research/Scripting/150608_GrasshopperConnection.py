import rhinoscriptsyntax as rs
import Rhino
import time
import Grasshopper as gh

gh2 = Rhino.RhinoApp.GetPlugInObject("Grasshopper")

ghObjects = gh.Component.OnPingDocument().Objects

for i in range (10,15):
    time.sleep(.05)
    rs.Redraw()
    gh2.SetSliderValue("eee4b8d8-231e-470d-92b2-d4dcd5f4a50d", i+1)
    gh.Instances.RedrawAll()
    gh.Instances.RedrawCanvas()
    gh.Kernel.GH_ActiveObject.ExpireSolution()