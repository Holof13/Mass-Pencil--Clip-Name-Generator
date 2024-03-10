use <fontmetrics.scad>;

pencil_d = 3.88;
text = "EXAMPLE";
size = 10;
font = "Impact:style=Regular";
w = measureText(text, font=font, size=size);
h = ascender(font) - descender(font);

module text_gen() {
    linear_extrude(height=3) text(text, size=size, font=font, valign="center");
}

module base_gen() {
    translate([w/2,0,-3]) linear_extrude(height=3) square([w,5], center= true);
}

module base_ring_gen() {
    difference() {
        cylinder(h = 20, r = pencil_d +1);
        cylinder(h = 20, r = pencil_d);
    }
}

module cut_ring_gen() {
    translate([-5,0,0]) cylinder(20,8,8,$fn=3);
}

module f_ring_gen() {
    translate([10 + w/2, 0, -4 - (pencil_d + 1) / 2]) rotate([0,-90,0])
    difference(){
        base_ring_gen();
        cut_ring_gen();
    }
}

rotate([180,0,0]) {
    union() {
        union() {
            text_gen();
            f_ring_gen();
        }
        base_gen();
    }
}

            
