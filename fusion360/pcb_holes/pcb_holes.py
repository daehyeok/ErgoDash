#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

positions = [[47.705, 54.4155],
                [86.565, 69.4055],
                [98.806, 9.4615],
                [9.525, 66.6115],
                [9.525, 9.2075],
                [48.133, 16.8275]];

def run(context):
    ui = None
    try: 
        app = adsk.core.Application.get()
        ui = app.userInterface

        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = app.activeProduct

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create a new sketch on the xy plane.
        sketches = rootComp.sketches;
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)


        # Draw two connected lines.
        # Draw some circles.
        circles = sketch.sketchCurves.sketchCircles
        for x,y in positions:
            circles.addByCenterRadius(adsk.core.Point3D.create(x, y, 0), 0.49/2)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
