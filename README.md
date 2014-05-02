## NOGrasshopperUtil

*Incoming library's name change to **GettingArchitectureDoneKit.gh***

Just-add-water functions in Grasshopper for Rhino to perform frequent design and architecture tasks. This library is part of the [Getting Architecture Done](http://www.gettingarchitecturedone.com/?utm_source=github&utm_medium=GHUtil) project.

## Usage

Just download *NOGrasshopperUtil.gh* and drag it onto Grasshopper. There are various clusters to simplify frequent tasks.

Currently, the documentation is incomplete, and the Grasshopper library contains more functions than is written below. An update with a cleanup of documentation and library will arrive soon.

Also, the Inbox folder now contains sepparated nodes that will be incorporated to the library in the near future.

## Nodes

### LIST: Remove List Extremes

Remove elements from the beginning and the end of a list with integers.

### CRV: Line With Center, Direction, Length

Create a line with its middle point as a parameter.

### CRV: Thicken With Offset Thickness

Create an outline from a line with a given thickness.

### SRF: Solid With Outline, Base Z, Height

Create a solid with the plan drawing outline, as a extrusion from a *Z* distance with a given *Height.*

### PEOPLE: Populate Surface With Amount, Angle

Add human scale to a surface with a certain number of people and a rotation angle. It returns the outlines as planar curves which can be used to create a planar surface via *Boundary Surfaces,* and it gets a *seed* value to re-randomize the locations.

## License

NOGrasshopperUtil is licensed under the MIT license. (http://opensource.org/licenses/MIT)

## Me

I tweet at [@nonoesp](http://www.twitter.com/nonoesp) and blog at [nono.ma/says](http://nono.ma/says). I would love to hear about it if you use this library. Thanks!
