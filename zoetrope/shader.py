# import sys
# from os.path import dirname, abspath, join
import moderngl

def read_shader(filepath: str) -> str:
    shader = ""
    with open(filepath) as file:
        shader = file.read()
    return shader

def create_shader(ctx: moderngl.Context, filepath: str) -> moderngl.Program:
    vert = read_shader(filepath);
    frag = read_shader(filepath);
    
    prog = ctx.program(vertex_shader=vert, fragment_shader=frag)
    return prog
