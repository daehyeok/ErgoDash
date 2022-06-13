include <BOSL2/std.scad>
include <BOSL2/shapes2d.scad>;
$fn=100;
module switches(w=19.05,h=19.05){
    positions =[
        [0.0, 76.2, 0.0],
        [38.1, 61.9125, 0.0],
        [38.1, 42.8625, 0.0],
        [38.1, 23.8125, 0.0],
        [57.15, 83.34375, 0.0],
        [57.15, 64.29375, 0.0],
        [57.15, 45.24375, 0.0],
        [57.15, 26.19375, 0.0],
        [76.2, 80.9625, 0.0],
        [76.2, 61.9125, 0.0],
        [76.2, 42.8625, 0.0],
        [0.0, 57.15, 0.0],
        [76.2, 23.8125, 0.0],
        [95.25, 78.58125, 0.0],
        [95.25, 59.53125, 0.0],
        [95.25, 40.48125, 0.0],
        [95.25, 21.43125, 0.0],
        [114.3, 69.05625, 0.0],
        [114.3, 50.00625, 0.0],
        [114.3, 30.95625, 0.0],
        [113.32, 6.9732, -30.0],
        [0.0, 38.1, 0.0],
        [0.0, -0.0, 0.0],
        [19.05, -0.0, 0.0],
        [38.1, 4.7625, 0.0],
        [87.297, 0.00025, -30.0],
        [103.795, -9.5248, -30.0],
        [60.96, 4.7625, 0.0], //1.25u
        [0.0, 19.05, 0.0],
        [125.0555, -10.8008, -120.0], //2u
        [19.05, 76.2, 0.0],
        [19.05, 57.15, 0.0],
        [19.05, 38.1, 0.0],
        [19.05, 19.05, 0.0],
        [38.1, 80.9625, 0.0],];

    for(pos = positions)
        translate([pos[0], pos[1]])
        square([w,h], spin=pos[2], center=true);
}

module pcbHoles(r=2.5){
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

module pcbOutline(){
    color([0,1,0])
    difference(){
        import (file = "ergodash-Edge_Cuts.dxf");
        pcbHoles();
    }
}


module plateHoles(){
   pcbHoles(r=2.5);
}


module plate(height=1.6){
    difference(){
        import (file = "outline.dxf");
        pcbHoles();
        switches(14,14);
    }
}


module caseBaseOutline(){
    import (file = "outline.svg");
}


module caseBase(){
    import (file = "outline.dxf");
}


module bottom(){
    import (file = "outline.dxf");
}

module top(){
    caseOutlineBase();
}

plate();
