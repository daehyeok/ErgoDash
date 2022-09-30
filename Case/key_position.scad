include <BOSL2/std.scad>
key_positions =[
    //x,y,degree, size
     [0.0, -0.0, 0.0, 1],
     [0.0, 19.05, 0.0, 1],
     [0.0, 38.1, 0.0, 1],
     [0.0, 57.15, 0.0, 1],
     [0.0, 76.2, 0.0, 1],
     [19.05, -0.0, 0.0, 1],
     [19.05, 19.05, 0.0, 1],
     [19.05, 38.1, 0.0, 1],
     [19.05, 57.15, 0.0, 1],
     [19.05, 76.2, 0.0, 1],
     [38.1, 4.7625, 0.0, 1],
     [38.1, 23.8125, 0.0, 1],
     [38.1, 42.8625, 0.0, 1],
     [38.1, 61.9125, 0.0, 1],
     [38.1, 80.9625, 0.0, 1],
     [57.15, 26.19375, 0.0, 1],
     [57.15, 45.24375, 0.0, 1],
     [57.15, 64.29375, 0.0, 1],
     [57.15, 83.34375, 0.0, 1],
     [60.96, 4.7625, 0.0, 1],
     [76.2, 23.8125, 0.0, 1],
     [76.2, 42.8625, 0.0, 1],
     [76.2, 61.9125, 0.0, 1],
     [76.2, 80.9625, 0.0, 1],
     [87.297, 0.00025, -30.0, 1],
     [95.25, 21.43125, 0.0, 1],
     [95.25, 40.48125, 0.0, 1],
     [95.25, 59.53125, 0.0, 1],
     [95.25, 78.58125, 0.0, 1],
     [103.795, -9.5248, -30.0, 1],
     [113.32, 6.9732, -30.0, 1],
     [114.3, 30.95625, 0.0, 1],
     [114.3, 50.00625, 0.0, 1],
     [114.3, 69.05625, 0.0, 1],
     [125.0555, -10.8008, -120.0, 2],];
     
module plateCutout(u=1){
    paths = [[0, 14],
 [7, 14],
 [7, 9.300],
 [8.525, 9.300],
 [8.525, 12.530],
 [15.275, 12.530],
 [15.275, 9.300],
 [16.100, 9.300],
 [16.100, 6.515],
 [15.275, 6.515],
 [15.275, 0.230],
 [13.550, 0.230],
 [13.550, -0.970],
 [10.250, -0.970],
 [10.250, 0.230],
 [8.525, 0.230],
 [8.525, 4.700],
 [7, 4.700],
 [7, 0],
 [0, 0],
 [0, 14]];
 
 if(u==2){
     union(){
     fwd(7)
     polygon(paths);
     fwd(7)
     xflip()
      polygon(paths);
     }
 }else{
     rect(14);
 }
}

module plateHoles(){
    for(key = key_positions){
       back(key[1])
       right(key[0])
       zrot(key[2])
       plateCutout(key[3]);
    }
}

module pcbHoles(r=2.5, height = 10){
 positions = [[47.705, 54.4155],
                [86.565, 69.4055],
                [98.806, 9.4615],
                [9.525, 66.6115],
                [9.525, 9.2075],
                [48.133, 16.8275]];
                for (pos = positions) 
                        translate(pos)
                            circle(r);
}


module switches(w=19.05,h=19.05, scaling=false, height = 10){
    for(key = key_positions){
        size = [w,h, height];
        if (scaling == true){
            size = [w,h, height] * [key[3],1,1];
        }
        translate([key[0], key[1]])
        square([w*key[3],h, height], spin=key[2], center=true);
    }
}


module pcb(thick=1.6, stack_height=0){
    up(stack_height)
    color("green")
    difference(){
        linear_extrude(height = thick)
        pcbOutline();
        pcbHoles();
    }
}


module pcbOutline(){
     import (file = "outlines/pcb.dxf");
}
module caseOutline(){
     import (file = "outlines/case.dxf");
}


module plateOutline(include_hole=false){
 import (file = "outline.dxf");
}

module keyOutline(){
 import (file = "outlines/key.dxf");
}

