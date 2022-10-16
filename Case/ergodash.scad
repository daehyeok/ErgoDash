include <BOSL2/std.scad>
include <BOSL2/fnliterals.scad>

include <key_position.scad>
$fn=100;

plate_thick=1.5;
_middle_bottom_thick=5;
_middle_top_thick=5;
middle_thick= 9;
bottom_floor_thick=3;
bottom_pcb_depth=10.5;
bottom_plate_depth=3;
bottom_thick=bottom_floor_thick+bottom_pcb_depth+bottom_plate_depth;
top_plate_depth=plate_thick+0.1;
top_wall_thick=3;
top_thick=3;

outline_size = [152.393,130.852];
//https://katofastening.com/inserts/specs.html
m2dot_margin=1.2*2;
m2dot5_outer=3.70 + m2dot_margin;
m2_drill=2;
m2_heil_coil_drill=2.1;

//mount holes for top, 
module topMounts(r=1.5){
    positions =[
        [19.05/2+10,19.05*4.5+4],
        [19.05 * 5.5 + 8,19.05*4.5],
        [35, -8],
        [70, -8],
        [130, 13],
    
    ];
    color([1,0,0])
   for(pos = positions)
        translate(pos)
         circle(r);
}

//mount holes for top, 
module plateMounts(r=0.5){
    positions =[
        [19.05/2+10,19.05*4.5+4],
        [19.05 * 5.5 + 8,19.05*4.5],
        [35, -8],
        [70, -8],
        [130, 13],
    
    ];
    color([1,0,0])
   for(pos = positions)
        translate(pos)
         circle(r);
}

module rectmagnet(){
    //20x4x1
        positions =[
        [19.05 * 2.5,19.05*4.5+8],
        [19.05 * 2.5,-8.5],
    ];
   for(pos = positions)
        translate(pos)
        square([20,4]);
}

//mount holes for bottom, 
module magnetMounts(r=1){
    positions =[
        [19.05,-9.5],
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

module plate(thick=plate_thick, 
            stack_height=0){
    up(stack_height)
    color("LightGray")
    linear_extrude(height = thick)
    difference(){
        plateOutline(include_hole=true);
        plateHoles();
        pcbHoles(r=1.05);
        plateMounts(r=2); //mark
    }
}


module top(thick=top_thick, 
            stack_height=0){
    up(bottom_thick)
  union(){
      color("red")
    linear_extrude(height = top_plate_depth )
    difference()
    {
    
        caseOutline();
        plateOutline();
    
    }
    
   up(top_plate_depth)
   linear_extrude(height = top_thick - top_plate_depth )
   difference()
    {
        caseOutline();
        keyOutline();
    }
    
    
}
}

module bottom(thick=bottom_thick, 
            stack_height=0){
     up(stack_height-bottom_pcb_depth-bottom_floor_thick)
   
    union()
    {
        color("Burlywood")
        linear_extrude(height = bottom_floor_thick)
        caseOutline();
        
       color("Wheat")
        up(bottom_floor_thick)
        linear_extrude(height = bottom_pcb_depth)
        difference(){
            caseOutline();
            pcbOutline();
        }
        /*
        color("Burlywood")
        up(bottom_floor_thick+bottom_pcb_depth)
        linear_extrude(height = bottom_plate_depth)
        difference(){
            caseOutline();
            plateOutline();
        }*/
    }
}

bottom();