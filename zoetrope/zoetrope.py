import moderngl
import moderngl_window as mglw
import numpy as np
import shader

window_str = 'moderngl_window.context.pyglet.Window'
window_cls = mglw.get_window_cls(window_str)
window = window_cls(title='Zoetrope', gl_version=(3, 3), size=(1920, 1080))
mglw.activate_context(ctx=window.ctx)
ctx = moderngl.create_context()

vert = shader.read_shader('../shaders/vertex.vert');
frag = shader.read_shader('../shaders/fragment.frag');

prog = ctx.program(vertex_shader=vert, fragment_shader=frag)

vertices = np.asarray([
    -0.5, -0.5, 1, 0, 0,
    0.5, -0.5, 0, 1, 0,
    0, 0.75, 0, 0, 1
], dtype='f4')
vbo = ctx.buffer(vertices.tobytes())
vao = ctx.vertex_array(prog, vbo, 'in_vert', 'in_color')

while not window.is_closing:
    window.clear(0.2, 0.3, 0.2)
    # Render stuff here
    vao.render()
    window.swap_buffers()
