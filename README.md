## GettingArchitectureDoneKit

Just-add-water utilities in Grasshopper for Rhino to perform frequent design and architecture tasks.

This library is part of the [Getting Architecture Done](http://www.gettingarchitecturedone.com/?utm_source=github&utm_medium=GADKit) project. Follow [@GettingArchDone](http://twitter.com/GettingArchDone) on Twitter or [Facebook](http://facebook.com/gettingarchitecturedone) to keep updated.

## Usage

* Download the Grasshopper utilities.
* Drag a definition onto Grasshopper.

## Structure

The new structure of **GADKit** contains separated files for each utility and workflow - rather than having a single Grasshopper file with all the clusters. This way, the library is more transparent on what's inside it, and can be browsed and maintained easily.

*All utilities and workflows in bold are already existing.*

### Utilities

A series of functions of frequent tasks as a shortcut or improvement of existing Grasshopper functionality.

* GADGeometryColorGradient
* **GADGeometryExtrudeFromCenter**
* GADGeometrySortByNeighbours
* **GADLineFromCenter**
* **GADCurveOffset**
* **GADCurveWiggle**
* GADCurveSubCurveWithPoints
* **GADPatternMaker**
* **GADPointOnPlane**
* **GADPeopleMaker**
* **GADRectangleFromCenter**

### Workflows

Ways to work. Already built in separate workflows.

* **GADWorkflowDictionary**
* **GADWorkflowBake**

## Old Library (still in transition)

### LIST: Remove List Extremes

Remove elements from beginning or end of a list with integers.

### CRV: Line With Center, Direction, Length

Create a line with its middle point as a parameter.

### CRV: Thicken With Offset Thickness

Create an outline from a line with a given thickness.

### SRF: Solid With Outline, Base Z, Height

Create a solid with the plan drawing outline, as a extrusion from a *Z* distance with a given *Height.*

### PEOPLE: Populate Surface With Amount, Angle

Add human scale to a surface with a certain number of people and a rotation angle. It returns the outlines as planar curves which can be used to create a planar surface via *Boundary Surfaces,* and it gets a *seed* value to re-randomize the locations.

### SRF: Ondulated Panel With Curve, DivisionLength, Thickness, Height

A constructive panel for facades and interior spaces which can be ondulated, created from a base Curve. Panels take a Thickness and a DivisionLength parameter to customize the ondulation of the panels. The Height is also variable.

## Inbox Folder

### Util_StairsFromPlanSteps

![Stairs From Plan Steps](Links/Util_StairsFromPlanSteps.jpg)

Create flat stairs with plan steps referenced from a 2D drawing and a height. Multiple stairs can be created at a time sharing a given height.

## License

GettingArchitectureDoneKit is licensed under the MIT license. (http://opensource.org/licenses/MIT)

## Me

I tweet at [@nonoesp](http://www.twitter.com/nonoesp) and blog at [nono.ma/says](http://nono.ma/says). If you use this library, I would love to hear about it. Thanks!
