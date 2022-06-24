include <BOSL2/std.scad>

$fn=100;

plate_thick=3;
_middle_bottom_thick=5;
_middle_top_thick=5;
middle_thick= 9;
bottom_thick=3;
top_wall_thick=3;
top_thick=3;

outline_size = [152.393,130.852];
//https://katofastening.com/inserts/specs.html
m2dot_margin=1.2*2;
m2dot5_outer=3.70 + m2dot_margin;
m2_drill=2;
m2_heil_coil_drill=2.1;

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
     [60.96, 4.7625, 0.0, 1.5],
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

module pcbOutline(){
     import (file = "ergodash-Edge_Cuts.dxf");
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

//mount holes for bottom, 
module plateMounts(r=3){
    /* positions =[
        [-12,-9],
        [34.0, -8.5],
        [74.5, -8.5],
        [-8, 88],
        [43, 94],
        [80.5, 94.5],
        [123, 82],
    ];
    */
    positions =[
        [-11.5,-9.5],
        [-11.5, 48.25-9.5],
        [-11.5, 87],
        [34.0, -8.5],
        [74.5, -8.5],
        
        [30, 95],
        [85, 97],
        [120, 84],
        [128.5, 14],
        [143.8, -3],
        [128.2, -30],
    ];
    color([1,0,0])
   for(pos = positions)
        translate(pos)
         circle(r);
}

module baseOutline(scale=1){
    delta= [-outline_size[0]/2 + 9.756,
    outline_size[1]/2 -197.903/2 ];
    translate(-delta) 
    scale(scale)
    translate(delta) //move to center
    import (file = "outline.dxf");
    //152.393,130.852
}

module caseOutline(){
    baseOutline(1.065);
}

module plateOutline(include_hole=false){
   difference(){
   caseOutline();
       
   if(include_hole ==true){
    union(){
       //pcbHoles(r=1.1);
       switches(14,14);
       plateMounts(m2_drill/2);
      }
   }
   };
}

module plate(thick=plate_thick, 
            stack_height=0){
    up(stack_height)
    linear_extrude(height = thick)
    plateOutline(include_hole=true);
}

module bottom(thick=bottom_thick){
    color("purple")
    linear_extrude(height = thick)
    caseOutline();
}


module trrsCutter(thick=middle_thick, stack_height=0){
    up(stack_height)
    linear_extrude(height = thick)
    trrsCutterOutline();
}

module trrsCutterOutline(){
    back(87)
    right(105)
    square([25,14], true);
}

module middleOutline(){
       difference(){
        caseOutline();
           scale(1.01)
        pcbOutline();  //TODO: add margin for pcb
        plateMounts(m2_heil_coil_drill/2);
        trrsCutterOutline();
    };
};

module middle(thick=middle_thick, stack_height=0){
    up(stack_height)
    color("red")
    linear_extrude(height = thick)
    middleOutline();
}

module topWall(thick=top_wall_thick, stack_height=0){
    up(stack_height)
     color("green")
    linear_extrude(height = thick)
    difference(){
        caseOutline();
        plateOutline();  //TODO: add margin for plate
    };
}

module topCase(thick=top_thick, stack_height=0){

    module switch_cutter(){
        addiction_pos = [
        [57.15, 20.3125],
        [76.2, 4.7625],
        [114.3, 20.3],
        [95.25,4.7625],
        ];
        union(){
        switches(19.1, 19.1);
        for (pos = addiction_pos)
         translate(pos)
          square([19.1, 19.1], center=true);
        };
    }
    
    up(stack_height)
    color("white")
    linear_extrude(height = thick)
    difference(){
     caseOutline();
      pcbHoles(r=1.1);
        switch_cutter();
   }
}


module Rendering(){
    //topCase(stack_height=bottom_thick + middle_thick + top_wall_thick);
    //topWall(stack_height=bottom_thick +middle_thick);
  // plate(stack_height=bottom_thick+middle_thick);

    pcb(stack_height=bottom_thick+middle_thick-5);
    trrsCutter(stack_height=bottom_thick);
    middle(stack_height=bottom_thick);
    bottom(bottom_thick);
}

//plateOutline(true);
//plateMounts(true);
Rendering();
