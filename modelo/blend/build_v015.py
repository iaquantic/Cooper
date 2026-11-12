# Cooper (mascota Quantic) — construcción v015 (Blender 5.2, ejecutar dentro de Blender)
# v015 (revisión de Quantic de la v014): el logo del pecho se ve entero y limpio. (1) La costura del bolsillo canguro
# (Costura_Bolsillo) se escalaba en el eje equivocado (0,6 en la profundidad en vez de en la altura) y era un aro 2 cm más
# alto que el bolsillo que cruzaba el pie del logo: ahora sigue el borde del bolsillo al 82 % en ancho y en alto
# (scale (1.4, 0.6, 0.6)). (2) El logo sube 1,5 cm (LOGO_Z). (3) Los cordones se acortan 3,9 cm del script (3,5 cm en el
# mundo) desde abajo, con el arranque en el cuello fijo, y la punta sube con ellos (CORD_SHORTEN). (4) La textura del logo
# del pecho se muestrea con extensión EXTEND (CLAMP_TO_EDGE en glTF): el logo toca los cuatro bordes de la imagen y con
# REPEAT el filtrado traía el pie de las letras al borde superior. Nada más cambia respecto a v014.
# v014 (colores oficiales de Quantic, personaje/marca/README.md del repo): cuerpo, cabeza y tentáculos en el violeta de marca
# #8070E7 (antes #5B2BE0); manchas #564CA3 e iris #564EA1 (mismo salto de tono). Logo oficial (Q con barra violeta, versión
# blanca) como textura con alfa: en el pecho (quantic-logo-blanco.png envuelto a la sudadera), en la tapa del portátil
# (quantic-isotipo-blanco.png) y en la taza (taza.png regenerada con el logo). Pantallas, ventosas, ojos, gafas, sudadera,
# bombilla, boca, geometría, brazos, animaciones, Acc_* y visibilidad: sin cambios. Cabeza y cuerpo rehorneados; normales de
# la sudadera reutilizadas (reuse_hoodie).
# v013 (revisión de Quantic de la v012): (1) en 3 pensativo la punta del brazo izquierdo se apoya en la cara, bajo la
# boca y a la izquierda, con el tentáculo curvado hacia arriba (face_point sobre el elipsoide de la cabeza, con pose
# inicial del brazo que lleva el codo abajo); (2) las bocas de Expresiones en el .glb/.fbx: la acción Expresiones_Boca
# ya no arrastra las claves de Idle (Idle tiene su propia Idle_Boca) y cada clip ocupa un rango de fotogramas distinto
# (CLIP_START) para que FBX hornee la boca correcta por clip; al exportar se desilencian las pistas de boca.
# v012 (dos arreglos de alcance de los brazos, revisión de Quantic de la v011): en Relax el borde de la taza toca
# la boca, con la taza inclinada hacia ella (objetivo resuelto midiendo la taza evaluada, cabeza 5° hacia la taza);
# en la expresión 3 pensativo la punta del brazo izquierdo se apoya bajo la barbilla (punto calculado sobre la
# superficie de la cabeza). Nada más cambia respecto a v011; texturas reutilizadas con bake_reuse(v011/texturas).
# v011 (ajustes tras aprobar v010): encuadre del busto más bajo y común a las siete expresiones (las rayitas
# de énfasis entran enteras), y T2 (portátil), T3 (taza) y T6 (checklist) relajados junto a la sudadera
# siempre que su accesorio no se usa; cada uno sube solo en su clip (Tecleo, Relax, Organizar).
# Además (pedido ampliado de Quantic): dos tentáculos son BRAZOS que salen por las mangas de la sudadera:
# T2 (brazo izquierdo, portátil) y T7 (brazo derecho, taza). El móvil pasa al tentáculo inferior T3. Las
# mangas son tubos de la sudadera con puño de costura, pesados a la cadena del brazo.
# Colores, proporciones, nombres Acc_* y visibilidad por modo: sin cambios.
# Parte de build_v009.py. Pedido de Quantic/Leo del 2026-11-06: Cooper lleva un solo accesorio según el
# modo. Cada accesorio cuelga de un hueso de visibilidad con nombre fijo (Acc_Bombilla, Acc_Laptop,
# Acc_Movil, Acc_Taza, Acc_Checklist, Acc_Panel) y vive en una colección del mismo nombre; en el glTF ese
# hueso es el nodo que hay que ocultar. Los clips de modo (Idea, Tecleo, Relax, Organizar) y Saludo
# animan esa visibilidad; Expresiones e Idle no la tocan. Clips nuevos: Relax (sorbo a la taza, bucle)
# y Organizar (marca una tarea en la checklist y sonríe). Piel, colores y proporciones: iguales que v009
# (bake_reuse con v008/texturas).
import bpy, math, bmesh, random, os
from mathutils import Vector, Matrix
from mathutils.geometry import interpolate_bezier

BASE = os.environ.get("COOPER_BASE", r"C:\Trabajo\Modelador 3D\proyectos\mascota-quantic\v015")   # v015: COOPER_BASE permite ejecutarlo fuera del PC de trabajo
TEX = os.path.join(BASE, "texturas")
sc = bpy.context.scene; vl = bpy.context.view_layer
if bpy.context.mode != 'OBJECT':
    bpy.ops.object.mode_set(mode='OBJECT')
sc.frame_set(0)

# ---------------------------------------------------------------- limpieza
for o in list(bpy.data.objects):
    bpy.data.objects.remove(o, do_unlink=True)
for a in list(bpy.data.actions):          # las acciones llevan fake user: quitarlas siempre
    bpy.data.actions.remove(a)
for coll_name in ("meshes", "curves", "materials", "armatures", "cameras", "lights", "shape_keys"):
    for d in list(getattr(bpy.data, coll_name)):
        if d.users == 0:
            getattr(bpy.data, coll_name).remove(d)
sc.unit_settings.system = 'METRIC'; sc.unit_settings.scale_length = 1.0
random.seed(11)

def coll(name):
    c = bpy.data.collections.get(name)
    if not c:
        c = bpy.data.collections.new(name); sc.collection.children.link(c)
    return c
C_CHAR = coll("Mascota"); C_ACC = coll("Accesorios"); C_RIG = coll("Rig"); C_SRC = coll("Fuente_Curvas"); C_SET = coll("Escena")

def link(o, c):
    for cc in o.users_collection:
        cc.objects.unlink(o)
    c.objects.link(o)

# ---------------------------------------------------------------- materiales
def s2l(c): return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
def hex2lin(h):
    h = h.lstrip('#'); return tuple(s2l(int(h[i:i + 2], 16) / 255) for i in (0, 2, 4)) + (1.0,)
def mat(name, hexcol, rough=0.5, emit=0.0, metal=0.0, emit_hex=None, bump=0.0, pores=6.0, fade_to=None, spots_hex=None, wrinkles=0.0):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True; nt = m.node_tree
    bsdf = next(n for n in nt.nodes if n.type == 'BSDF_PRINCIPLED')
    col = hex2lin(hexcol)
    bsdf.inputs['Base Color'].default_value = col
    bsdf.inputs['Roughness'].default_value = rough
    bsdf.inputs['Metallic'].default_value = metal
    bsdf.inputs['Emission Color'].default_value = hex2lin(emit_hex) if emit_hex else col
    bsdf.inputs['Emission Strength'].default_value = emit
    if bump:
        noise = nt.nodes.new('ShaderNodeTexNoise'); noise.inputs['Scale'].default_value = 28.0
        noise.inputs['Detail'].default_value = 6.0; noise.inputs['Roughness'].default_value = 0.6
        # poros: celdas Voronoi pequeñas (distancia al borde) restadas al relieve
        vor = nt.nodes.new('ShaderNodeTexVoronoi'); vor.feature = 'DISTANCE_TO_EDGE'; vor.inputs['Scale'].default_value = 90.0
        ramp = nt.nodes.new('ShaderNodeMath'); ramp.operation = 'SMOOTH_MIN'; ramp.inputs[1].default_value = 0.06; ramp.inputs[2].default_value = 0.02
        nt.links.new(vor.outputs['Distance'], ramp.inputs[0])
        mix = nt.nodes.new('ShaderNodeMath'); mix.operation = 'MULTIPLY_ADD'
        nt.links.new(ramp.outputs[0], mix.inputs[0]); mix.inputs[1].default_value = pores; nt.links.new(noise.outputs['Fac'], mix.inputs[2])
        bm_ = nt.nodes.new('ShaderNodeBump'); bm_.inputs['Strength'].default_value = bump; bm_.inputs['Distance'].default_value = 0.004
        nt.links.new(mix.outputs[0], bm_.inputs['Height']); nt.links.new(bm_.outputs['Normal'], bsdf.inputs['Normal'])
    if fade_to:
        # borde difuso: el color de la mancha se funde con el del cuerpo hacia el borde (coordenadas Generated, 0..1 en la caja)
        tc = nt.nodes.new('ShaderNodeTexCoord')
        sub = nt.nodes.new('ShaderNodeVectorMath'); sub.operation = 'SUBTRACT'; sub.inputs[1].default_value = (0.5, 0.5, 0.5)
        mul = nt.nodes.new('ShaderNodeVectorMath'); mul.operation = 'MULTIPLY'; mul.inputs[1].default_value = (2.0, 2.0, 0.0)
        ln_ = nt.nodes.new('ShaderNodeVectorMath'); ln_.operation = 'LENGTH'
        mr = nt.nodes.new('ShaderNodeMapRange'); mr.interpolation_type = 'SMOOTHSTEP'
        mr.inputs['From Min'].default_value = 0.55; mr.inputs['From Max'].default_value = 1.0
        mixc = nt.nodes.new('ShaderNodeMix'); mixc.data_type = 'RGBA'
        mixc.inputs[6].default_value = col; mixc.inputs[7].default_value = hex2lin(fade_to)
        nt.links.new(tc.outputs['Generated'], sub.inputs[0]); nt.links.new(sub.outputs[0], mul.inputs[0])
        nt.links.new(mul.outputs[0], ln_.inputs[0]); nt.links.new(ln_.outputs['Value'], mr.inputs['Value'])
        nt.links.new(mr.outputs['Result'], mixc.inputs[0]); nt.links.new(mixc.outputs[2], bsdf.inputs['Base Color'])
    if spots_hex:
        # manchas orgánicas: ruido de baja frecuencia con umbral suave, mezclado al color base
        sn = nt.nodes.new('ShaderNodeTexNoise'); sn.inputs['Scale'].default_value = 3.4; sn.inputs['Detail'].default_value = 2.0; sn.inputs['Roughness'].default_value = 0.55
        smr = nt.nodes.new('ShaderNodeMapRange'); smr.interpolation_type = 'SMOOTHSTEP'; smr.inputs['From Min'].default_value = 0.55; smr.inputs['From Max'].default_value = 0.63
        smix = nt.nodes.new('ShaderNodeMix'); smix.data_type = 'RGBA'; smix.inputs[6].default_value = col; smix.inputs[7].default_value = hex2lin(spots_hex)
        nt.links.new(sn.outputs['Fac'], smr.inputs['Value']); nt.links.new(smr.outputs['Result'], smix.inputs[0]); nt.links.new(smix.outputs[2], bsdf.inputs['Base Color'])
    if wrinkles:
        # arrugas de tela (ruido grande) más trama fina del tejido
        wn = nt.nodes.new('ShaderNodeTexNoise'); wn.inputs['Scale'].default_value = 7.0; wn.inputs['Detail'].default_value = 3.0; wn.inputs['Roughness'].default_value = 0.5
        tw = nt.nodes.new('ShaderNodeTexNoise'); tw.inputs['Scale'].default_value = 420.0; tw.inputs['Detail'].default_value = 1.0
        wm = nt.nodes.new('ShaderNodeMath'); wm.operation = 'MULTIPLY_ADD'; wm.inputs[1].default_value = 0.12
        nt.links.new(tw.outputs['Fac'], wm.inputs[0]); nt.links.new(wn.outputs['Fac'], wm.inputs[2])
        wb = nt.nodes.new('ShaderNodeBump'); wb.inputs['Strength'].default_value = wrinkles; wb.inputs['Distance'].default_value = 0.012
        nt.links.new(wm.outputs[0], wb.inputs['Height']); nt.links.new(wb.outputs['Normal'], bsdf.inputs['Normal'])
    m.diffuse_color = col
    return m
M = {
    'cuerpo':   mat('Q_Cuerpo',    '#8070E7', 0.5, bump=0.3, pores=1.2),   # v014: violeta de marca           # cuerpo y tentáculos: poros suaves
    'cabeza':   mat('Q_Cabeza',    '#8070E7', 0.5, bump=0.4, pores=7.0, spots_hex='#564CA3'),   # cabeza: poros marcados y manchas procedurales
    'manchas':  mat('Q_Manchas',   '#564CA3', 0.55, bump=0.3, pores=3.0, fade_to='#8070E7'),
    'vidrio_off': mat('Q_VidrioOff', '#B8AA7E', 0.35),
    'filamento_off': mat('Q_FilamentoOff', '#5A4A2E', 0.5),
    'ventosas': mat('Q_Ventosas',  '#E8A8C8', 0.55),
    'ventosa_in': mat('Q_VentosaCentro', '#C98AB0', 0.6),
    'ojo':      mat('Q_OjoBlanco', '#FFFFFF', 0.2),
    'pupila':   mat('Q_Pupila',    '#0A0A14', 0.15),
    'iris':     mat('Q_Iris',      '#564EA1', 0.25),
    'pestana':  mat('Q_Pestana',   '#1A0A4E', 0.4),
    'dientes':  mat('Q_Dientes',   '#F4F4F8', 0.3),
    'gafas':    mat('Q_Gafas',     '#101014', 0.3),
    'sudadera': mat('Q_Sudadera',  '#0E1424', 0.9, wrinkles=0.5),
    'costura':  mat('Q_Costura',   '#2A3450', 0.8),
    'sudadera_in': mat('Q_SudaderaInterior', '#070A14', 0.95),
    'blanco':   mat('Q_Blanco',    '#FFFFFF', 0.4),
    'cian':     mat('Q_Cian',      '#22D3EE', 0.3, emit=1.5),
    'boca':     mat('Q_Boca',      '#0A0A14', 0.6),   # interior de la boca negro (v009)
    'lengua':   mat('Q_Lengua',    '#E8486C', 0.45),
    'cuerda':   mat('Q_Cuerda',    '#C8C8D0', 0.6),
    'gris':     mat('Q_Gris',      '#3C3C46', 0.4, metal=0.6),
    'negro':    mat('Q_Negro',     '#15151C', 0.35),
    'pantalla': mat('Q_Pantalla',  '#1A6FFF', 0.2, emit=2.0),
    'bombilla': mat('Q_Bombilla',  '#FFC43A', 0.1, emit=12.0, emit_hex='#FFB020'),
    'vidrio':   mat('Q_Vidrio',    '#FFD060', 0.05, emit=5.0, emit_hex='#FFB83A'),
    'rayo':     mat('Q_Rayo',      '#FFE08A', 0.2, emit=8.0, emit_hex='#FFD24A'),
}

# ---------------------------------------------------------------- primitivas (quads)
def qsphere(name, loc, r, scale=(1, 1, 1), m=None, levels=3, c=C_CHAR):
    """Esfera de quads: cubo subdividido (Catmull-Clark) y proyectado al radio r. Sin polos de valencia alta."""
    bpy.ops.mesh.primitive_cube_add(size=2.0, location=loc)
    o = bpy.context.active_object; o.name = name
    sub = o.modifiers.new("sub", 'SUBSURF'); sub.levels = levels; sub.render_levels = levels
    bpy.ops.object.modifier_apply(modifier="sub")
    for v in o.data.vertices:
        v.co = v.co.normalized() * r
    o.scale = scale
    if m: o.data.materials.append(m)
    bpy.ops.object.shade_smooth(); link(o, c); return o
def cube(name, loc, dims, m=None, rot=(0, 0, 0), c=C_CHAR):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.active_object; o.name = name; o.scale = dims; o.rotation_euler = rot
    if m: o.data.materials.append(m)
    link(o, c); return o
def cyl(name, loc, r, depth, m=None, rot=(0, 0, 0), verts=24, c=C_CHAR):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=depth, vertices=verts, location=loc, rotation=rot)
    o = bpy.context.active_object; o.name = name
    if m: o.data.materials.append(m)
    bpy.ops.object.shade_smooth(); link(o, c); return o
def torus(name, loc, R, r, m=None, rot=(0, 0, 0), c=C_CHAR, maj=32, mino=12):
    bpy.ops.mesh.primitive_torus_add(major_radius=R, minor_radius=r, major_segments=maj, minor_segments=mino, location=loc, rotation=rot)
    o = bpy.context.active_object; o.name = name
    if m: o.data.materials.append(m)
    bpy.ops.object.shade_smooth(); link(o, c); return o
def parent_keep(child, parent):
    vl.update(); child.parent = parent; child.matrix_parent_inverse = parent.matrix_world.inverted()
def bisect_keep(o, plane_co, plane_no, keep_positive=True, fill=False):
    bm = bmesh.new(); bm.from_mesh(o.data)
    geom = bm.verts[:] + bm.edges[:] + bm.faces[:]
    bmesh.ops.bisect_plane(bm, geom=geom, plane_co=plane_co, plane_no=plane_no, clear_inner=keep_positive, clear_outer=not keep_positive)
    if fill:
        bmesh.ops.holes_fill(bm, edges=bm.edges[:])
    bm.to_mesh(o.data); bm.free(); o.data.update()

# ---------------------------------------------------------------- cabeza
HZ = 0.62; HR = 0.20
head = qsphere("Cabeza", (0, 0, HZ), HR, scale=(1.0, 0.95, 1.0), m=M['cabeza'], levels=4)
spots = [(-0.6, 0.5, 0.55, 0.045), (0.5, 0.6, 0.6, 0.038), (-0.2, 0.95, 0.25, 0.05), (0.75, 0.3, 0.35, 0.03),
         (-0.85, 0.2, 0.1, 0.032), (0.2, 0.55, 0.82, 0.042), (0.9, -0.2, 0.3, 0.028), (-0.5, 0.7, -0.3, 0.03),
         (0.0, 0.3, 0.95, 0.036), (0.55, 0.75, -0.2, 0.034), (-0.35, 0.85, 0.6, 0.026), (0.3, 0.9, -0.45, 0.024)]
# v007: las manchas son procedurales en Q_Cabeza (se hornean a textura); las mallas Mancha_* desaparecen

# ojos grandes y casi pegados (EX ampliado en el ajuste de gafas para dejar sitio al puente)
ER = 0.068; EX = 0.095; EY = -0.150; EZ = HZ + 0.025
eyes = {}; EF = EY - ER   # frente del globo ocular
for side, sx in (("I", -1), ("D", 1)):
    e = qsphere(f"Ojo_{side}", (sx * EX, EY, EZ), ER, m=M['ojo'], levels=3)
    # iris, pupila y brillo como discos pegados a la superficie del ojo (quedan bajo el párpado cerrado)
    ir = qsphere(f"Iris_{side}", (sx * EX * 1.03, EF + 0.012, EZ - 0.003), 0.040, scale=(1, 0.4, 1), m=M['iris'], levels=2)
    p = qsphere(f"Pupila_{side}", (sx * EX * 1.03, EF + 0.004, EZ - 0.003), 0.027, scale=(1, 0.4, 1), m=M['pupila'], levels=2)
    h = qsphere(f"Brillo_{side}", (sx * EX * 1.03 - 0.011 * sx, EF - 0.004, EZ + 0.013), 0.008, scale=(1, 0.4, 1), m=M['ojo'], levels=1)
    parent_keep(e, head); parent_keep(ir, e); parent_keep(p, e); parent_keep(h, e); eyes[side] = e
    # párpado: casquete trasero (local +Y) que un hueso gira hacia delante
    lid = qsphere(f"Parpado_{side}", (sx * EX, EY, EZ), ER * 1.13, m=M['cabeza'], levels=3)
    bisect_keep(lid, (0, 0.0, 0), (0, 1, 0), keep_positive=True)
    # ojo feliz "^": arco oscuro sobre el párpado cerrado, oculto (escala ~0) salvo en feliz y risa
    arc = torus(f"OjoFeliz_{side}", (sx * EX, EF - 0.013, EZ - 0.006), ER * 0.62, 0.0085, m=M['pestana'], rot=(math.pi / 2, 0, 0), maj=40, mino=10)
    # el toro se crea en su plano XY local y luego se gira 90° en X: el "arriba" del mundo es +Y local
    bisect_keep(arc, (0, 0.004, 0), (0, 1, 0), keep_positive=True)
    arc.scale = (1.0, 0.8, 1.0)

# gafas: montura gruesa tipo wayfarer (aros rectangulares redondeados, banda plana, puente corto, patillas rectas)
GY = -0.236          # plano central de la montura, delante del párpado cerrado (frente en EY-1.13*ER)
GA, GB = 0.084, 0.076   # semiejes del aro (línea media de la banda): ancho 0,168 / alto 0,152
GBAND, GDEPTH = 0.013, 0.013   # ancho de banda (en el plano) y profundidad (en Y)
def superellipse(a, b, n_top, n_bot, N=72):
    pts = []
    for i in range(N):
        t = 2 * math.pi * i / N; c, s_ = math.cos(t), math.sin(t)
        n = n_top if s_ >= 0 else n_bot
        pts.append((a * math.copysign(abs(c) ** (2 / n), c), b * math.copysign(abs(s_) ** (2 / n), s_)))
    return pts
def smooth_by_angle(angle=40):
    try: bpy.ops.object.shade_smooth_by_angle(angle=math.radians(angle))
    except Exception: bpy.ops.object.shade_smooth()
def frame_ring(name, center, a, b, band, depth, m, n_top=3.4, n_bot=2.4, N=72):
    """aro de gafas: anillo plano entre dos superelipses, extruido en Y. Todo quads."""
    outer = superellipse(a + band / 2, b + band / 2, n_top, n_bot, N)
    inner = superellipse(a - band / 2, b - band / 2, n_top, n_bot, N)
    verts = [(x, -depth / 2, z) for x, z in outer] + [(x, -depth / 2, z) for x, z in inner] + \
            [(x, depth / 2, z) for x, z in outer] + [(x, depth / 2, z) for x, z in inner]
    OF, IF, OB, IB = 0, N, 2 * N, 3 * N; faces = []
    for i in range(N):
        j = (i + 1) % N
        faces += [(OF + i, OF + j, IF + j, IF + i), (OB + j, OB + i, IB + i, IB + j),
                  (OF + j, OF + i, OB + i, OB + j), (IF + i, IF + j, IB + j, IB + i)]
    me = bpy.data.meshes.new(name); me.from_pydata(verts, [], faces); me.update()
    o = bpy.data.objects.new(name, me); C_CHAR.objects.link(o); o.location = center; o.data.materials.append(m)
    bm = bmesh.new(); bm.from_mesh(me); bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:]); bm.to_mesh(me); bm.free()
    bv = o.modifiers.new("bisel", 'BEVEL'); bv.width = 0.0025; bv.segments = 2; bv.limit_method = 'ANGLE'
    bpy.ops.object.select_all(action='DESELECT'); o.select_set(True); vl.objects.active = o
    smooth_by_angle()
    return o
def bar(name, loc, dims, m, rot=(0, 0, 0), bevel=0.003):
    o = cube(name, loc, dims, m, rot=rot)
    bv = o.modifiers.new("bisel", 'BEVEL'); bv.width = bevel; bv.segments = 2; bv.limit_method = 'ANGLE'
    bpy.ops.object.select_all(action='DESELECT'); o.select_set(True); vl.objects.active = o
    smooth_by_angle(); return o
for side, sx in (("I", -1), ("D", 1)):
    ring_ = frame_ring(f"Gafa_{side}", (sx * EX, GY, EZ), GA, GB, GBAND, GDEPTH, M['gafas'])
    parent_keep(ring_, head)
    # bisagra y patilla recta hacia atrás, pegada a la cabeza
    hx = sx * (EX + GA + GBAND / 2 + 0.003)
    hinge = bar(f"Gafa_Bisagra_{side}", (hx, GY + 0.010, EZ + 0.030), (0.012, 0.020, 0.016), M['gafas'], bevel=0.002)
    temple = bar(f"Patilla_{side}", (hx, GY + 0.165, EZ + 0.032), (0.009, 0.31, 0.013), M['gafas'], rot=(0.03, 0, 0), bevel=0.002)
    parent_keep(hinge, head); parent_keep(temple, head)
# puente: barra corta y gruesa entre los aros, en el tercio superior
gap = 2 * (EX - GA - GBAND / 2)
bridge = bar("Gafa_Puente", (0, GY, EZ + 0.028), (gap + 2 * GBAND + 0.004, GDEPTH, 0.015), M['gafas'], bevel=0.003)
parent_keep(bridge, head)
brows = {}
for side, sx in (("I", -1), ("D", 1)):
    brows[side] = cyl(f"Ceja_{side}", (sx * EX, -0.165, EZ + 0.125), 0.010, 0.075, m=M['gafas'], rot=(0, math.pi / 2, -sx * 0.22))   # cejas negras (v009)

# boca con lengua unida (shape keys después del escalado)
mouth = qsphere("Boca", (0, -0.168, HZ - 0.085), 0.045, scale=(1.35, 0.6, 0.9), m=M['boca'], levels=3)
bisect_keep(mouth, (0, 0, 0), (0, 0, 1), keep_positive=False, fill=True)
mouth.rotation_euler = (-0.25, 0, 0)
tongue = qsphere("Lengua", (0, -0.185, HZ - 0.108), 0.022, scale=(1.2, 0.8, 0.5), m=M['lengua'], levels=2)
N_MOUTH = len(mouth.data.vertices)
bpy.ops.object.select_all(action='DESELECT'); tongue.select_set(True); mouth.select_set(True); vl.objects.active = mouth
bpy.ops.object.join(); parent_keep(mouth, head)
# dientes (fila superior) y marcas de sorpresa/risa: ocultos salvo en sus expresiones (escala del hueso)
teeth = cube("Dientes", (0, -0.203, HZ - 0.080), (0.044, 0.012, 0.011), M['dientes'], rot=(-0.25, 0, 0))
bv = teeth.modifiers.new("bisel", 'BEVEL'); bv.width = 0.002; bv.segments = 2
marks = []
for i, ang in enumerate((-35, 0, 35)):
    a = math.radians(ang); mx = 0.19 + math.sin(a) * 0.045; mz = HZ + 0.19 + math.cos(a) * 0.045
    marks.append(cube(f"Marca_{i + 1}", (mx, -0.10, mz), (0.006, 0.006, 0.03), M['blanco'], rot=(0, -a, 0)))
marks_e = bpy.data.objects.new("Marcas", None); C_CHAR.objects.link(marks_e); marks_e.location = (0.19, -0.10, HZ + 0.19); vl.update()
for mk in marks:
    mk.parent = marks_e; mk.matrix_parent_inverse = marks_e.matrix_world.inverted()

# ---------------------------------------------------------------- cuerpo y sudadera
body = qsphere("Cuerpo", (0, 0, 0.40), 0.175, scale=(1.0, 0.85, 0.95), m=M['cuerpo'], levels=3)
hood = qsphere("Sudadera", (0, 0, 0.40), 0.192, scale=(1.0, 0.86, 0.86), m=M['sudadera'], levels=3)
collar = torus("Sudadera_Cuello", (0, 0.02, 0.495), 0.145, 0.034, m=M['sudadera'], rot=(0.25, 0, 0))
# capucha: casquete trasero con solidify (quads)
hoodback = qsphere("Sudadera_Capucha", (0, 0.14, 0.545), 0.165, scale=(1.1, 0.85, 0.9), m=M['sudadera'], levels=3)
hoodback.data.materials.append(M['sudadera_in'])
bisect_keep(hoodback, (0, (0.02 - 0.14) / 0.85, 0), (0, 1, 0), keep_positive=True)
bisect_keep(hoodback, (0, 0, -0.02 / 0.9), (0, 0, 1), keep_positive=True)
so = hoodback.modifiers.new("grosor", 'SOLIDIFY'); so.thickness = 0.022; so.offset = -1; so.material_offset = 1; so.material_offset_rim = 1
bpy.ops.object.select_all(action='DESELECT'); hoodback.select_set(True); vl.objects.active = hoodback
bpy.ops.object.modifier_apply(modifier="grosor")
hem = torus("Sudadera_Bajo", (0, 0, 0.285), 0.155, 0.024, m=M['sudadera'])
CORD_SHORTEN = 0.0394   # v015: los cordones pierden 3,9 cm (3,5 cm en el mundo tras escalar a 1 m) por abajo; el arranque en el cuello no se mueve
CORD_AX = Vector((0, -math.sin(0.15), math.cos(0.15)))   # eje del cordón (girado 0,15 rad en X), hacia arriba
for side, sx in (("I", -1), ("D", 1)):
    cyl(f"Cordon_{side}", Vector((sx * 0.045, -0.160, 0.455)) + CORD_AX * (CORD_SHORTEN / 2), 0.006, 0.075 - CORD_SHORTEN, m=M['cuerda'], rot=(0.15, 0, 0))
    cyl(f"Cordon_Punta_{side}", Vector((sx * 0.045, -0.155, 0.412)) + CORD_AX * CORD_SHORTEN, 0.0075, 0.018, m=M['cuerda'], rot=(0.15, 0, 0))
pocket = qsphere("Sudadera_Bolsillo", (0, -0.155, 0.335), 0.085, scale=(1.4, 0.35, 0.6), m=M['sudadera'], levels=2)
# costuras: hilo visible en el borde del bolsillo, el bajo, el cuello y los hombros
# (toros finos medio hundidos en la tela: solo asoma la mitad exterior del hilo)
seams = [torus("Costura_Bolsillo", (0, -0.172, 0.335), 0.070, 0.003, m=M['costura'], rot=(math.pi / 2, 0, 0), maj=48, mino=6)]
seams[-1].scale = (1.4, 0.6, 0.6)   # v015: sigue el elipsoide del bolsillo al 82 % del radio (local Y = altura tras el giro en X; en v014 era 1.0 y el aro asomaba 2 cm sobre el bolsillo)
seams.append(torus("Costura_Bajo", (0, 0, 0.300), 0.173, 0.003, m=M['costura'], maj=64, mino=6)); seams[-1].scale = (1.0, 0.86, 1.0)
seams.append(torus("Costura_Cuello", (0, 0.02, 0.527), 0.138, 0.003, m=M['costura'], rot=(0.25, 0, 0), maj=64, mino=6))
seams.append(torus("Costura_Capucha", (0, 0.145, 0.60), 0.085, 0.003, m=M['costura'], rot=(0, math.pi / 2, 0), maj=48, mino=6))   # costura central de la capucha
seams[-1].scale = (1.0, 1.0, 0.75)
# v014: el logo del pecho ya no es geometría (aro cian + texto): es el logo oficial como textura, ver Logo_Sudadera más abajo
for n in ("Sudadera", "Sudadera_Cuello", "Sudadera_Capucha", "Sudadera_Bajo", "Cordon_I", "Cordon_D", "Cordon_Punta_I",
          "Cordon_Punta_D", "Sudadera_Bolsillo") + tuple(sm.name for sm in seams):
    parent_keep(bpy.data.objects[n], body)

# ---------------------------------------------------------------- tentáculos
R_ROOT = 0.064
RADII = [1.0, 0.84, 0.62, 0.40, 0.22]
TENT = {
    "T1_Bombilla":  [(-0.09, 0.02, 0.28), (-0.26, 0.00, 0.34), (-0.34, -0.02, 0.56), (-0.31, -0.05, 0.78), (-0.25, -0.06, 0.88)],
    "T2_BrazoIzq":  [(-0.12, -0.01, 0.45), (-0.25, -0.08, 0.39), (-0.32, -0.15, 0.38), (-0.31, -0.21, 0.40), (-0.25, -0.24, 0.41)],   # brazo izquierdo (hombro → mano, sostiene el portátil delante)
    "T3_Movil":      [(-0.08, -0.05, 0.26), (-0.21, -0.14, 0.17), (-0.31, -0.19, 0.15), (-0.35, -0.22, 0.23), (-0.31, -0.24, 0.29)],
    "T4_PieIzq":    [(-0.05, -0.07, 0.25), (-0.13, -0.19, 0.11), (-0.22, -0.27, 0.045), (-0.33, -0.25, 0.045), (-0.37, -0.20, 0.10)],
    "T5_PieDer":    [(0.05, -0.07, 0.25), (0.13, -0.19, 0.11), (0.22, -0.27, 0.045), (0.33, -0.25, 0.045), (0.37, -0.20, 0.10)],
    "T6_Checklist": [(0.08, -0.05, 0.26), (0.23, -0.12, 0.18), (0.33, -0.16, 0.14), (0.39, -0.19, 0.22), (0.36, -0.21, 0.29)],
    "T7_BrazoDer":  [(0.12, -0.01, 0.45), (0.25, -0.07, 0.41), (0.33, -0.12, 0.46), (0.31, -0.15, 0.55), (0.26, -0.17, 0.57)],      # brazo derecho (hombro → mano, sostiene la taza)
    "T8_Trasero":   [(0.00, 0.09, 0.26), (0.07, 0.23, 0.12), (0.15, 0.33, 0.045), (0.26, 0.37, 0.045), (0.31, 0.33, 0.10)],
}
ARMS = ("T2_BrazoIzq", "T7_BrazoDer")
RADII_ARM = [1.0, 0.92, 0.78, 0.50, 0.26]    # los brazos son algo más finos; la manga los cubre hasta el codo y la mano asoma por el puño
def make_curve(name, pts, depth=None, radii=None, mat_=None):
    cd = bpy.data.curves.new(name, 'CURVE'); cd.dimensions = '3D'
    cd.resolution_u = 12; cd.bevel_depth = depth or R_ROOT; cd.bevel_resolution = 7
    cd.fill_mode = 'FULL'; cd.use_fill_caps = False
    sp = cd.splines.new('BEZIER'); sp.bezier_points.add(len(pts) - 1)
    for i, (p, r) in enumerate(zip(pts, radii or RADII)):
        bp = sp.bezier_points[i]; bp.co = p; bp.handle_left_type = bp.handle_right_type = 'AUTO'; bp.radius = r
    o = bpy.data.objects.new(name, cd); C_SRC.objects.link(o); o.data.materials.append(mat_ or M['cuerpo'])
    return o
def eval_curve(obj, n=24):
    bps = obj.data.splines[0].bezier_points; res = []
    for i in range(len(bps) - 1):
        a, b = bps[i], bps[i + 1]
        seg = interpolate_bezier(a.co, a.handle_right, b.handle_left, b.co, n)
        for k, p in enumerate(seg):
            tt = k / (n - 1); r = (a.radius * (1 - tt) + b.radius * tt) * obj.data.bevel_depth
            if not res or (p - res[-1][0]).length > 1e-6:
                res.append((obj.matrix_world @ p, r))
    return res
def close_tube(o):
    """cierra los dos extremos abiertos del tubo: n-gono + poke (abanico de triángulos)"""
    bm = bmesh.new(); bm.from_mesh(o.data)
    before = set(f.index for f in bm.faces)
    res = bmesh.ops.holes_fill(bm, edges=bm.edges[:])
    new_faces = res.get('faces', [])
    if new_faces:
        bmesh.ops.poke(bm, faces=new_faces, offset=0.0)
    bm.to_mesh(o.data); bm.free(); o.data.update()
tent_meshes = {}
for name, pts in TENT.items():
    c = make_curve(name + "_Curva", pts, depth=(R_ROOT * 0.875 if name in ARMS else None), radii=(RADII_ARM if name in ARMS else None)); vl.update()
    m = c.copy(); m.data = c.data.copy(); m.name = name; C_CHAR.objects.link(m)
    bpy.ops.object.select_all(action='DESELECT'); m.select_set(True); vl.objects.active = m
    bpy.ops.object.convert(target='MESH'); close_tube(m); bpy.ops.object.shade_smooth()
    c.hide_viewport = True; c.hide_render = True
    pts_ev = eval_curve(c); L = len(pts_ev); parts = []
    n_v, v0, v1 = (5, 0.66, 0.96) if name in ARMS else (8, 0.10, 0.96)   # brazos: ventosas solo en la mano que asoma por el puño
    for j in range(n_v):
        idx = int((v0 + (v1 - v0) * j / (n_v - 1)) * (L - 1)); p, r = pts_ev[idx]
        p2 = pts_ev[min(idx + 1, L - 1)][0]; tang = (p2 - p).normalized()
        down = Vector((0, -1, -0.7)).normalized()
        d = down - tang * down.dot(tang); d = d.normalized() if d.length > 1e-4 else Vector((0, -1, 0))
        loc = p + d * (r * 0.96); rot = d.to_track_quat('Z', 'Y').to_euler()
        tr = torus(f"_v{j}", loc, r * 0.46, r * 0.16, m=M['ventosas'], rot=rot, maj=16, mino=8)
        ce = qsphere(f"_vc{j}", loc - d * (r * 0.02), r * 0.36, scale=(1, 1, 0.3), m=M['ventosa_in'], levels=1)
        ce.rotation_euler = rot; parts += [tr, ce]
    bpy.ops.object.select_all(action='DESELECT')
    for s in parts: s.select_set(True)
    m.select_set(True); vl.objects.active = m; bpy.ops.object.join()
    tent_meshes[name] = m
# mangas: tubo de sudadera sobre la primera mitad de cada brazo, con puño de costura; se pesan a la cadena del brazo
sleeves = {}
for an, side in zip(ARMS, ("I", "D")):
    pts3 = TENT[an][:3]
    co = make_curve(f"Manga_{side}_Curva", pts3, depth=0.070, radii=[1.0, 0.90, 0.72], mat_=M['sudadera']); vl.update()
    m = co.copy(); m.data = co.data.copy(); m.name = f"Manga_{side}"; C_CHAR.objects.link(m)
    bpy.ops.object.select_all(action='DESELECT'); m.select_set(True); vl.objects.active = m
    bpy.ops.object.convert(target='MESH'); close_tube(m); bpy.ops.object.shade_smooth()
    co.hide_viewport = True; co.hide_render = True
    ev = eval_curve(co); p_end, r_end = ev[-1]; tang = (ev[-1][0] - ev[-2][0]).normalized()
    cuff = torus(f"Costura_Puno_{side}", p_end, r_end, 0.003, m=M['costura'], rot=tang.to_track_quat('Z', 'Y').to_euler(), maj=32, mino=6)
    p_sh, r_sh = ev[0]; tsh = (ev[1][0] - ev[0][0]).normalized()
    shoulder = torus(f"Costura_Hombro_{side}", p_sh + tsh * 0.075, r_sh * 1.02, 0.003, m=M['costura'], rot=tsh.to_track_quat('Z', 'Y').to_euler(), maj=32, mino=6)
    bpy.ops.object.select_all(action='DESELECT'); cuff.select_set(True); shoulder.select_set(True); m.select_set(True); vl.objects.active = m; bpy.ops.object.join()
    sleeves[an] = m

# ---------------------------------------------------------------- accesorios
def acc_coll(name):
    c = bpy.data.collections.get(name)
    if not c:
        c = bpy.data.collections.new(name); C_ACC.children.link(c)
    return c
def group(name, objs, coll_name):
    """empty Grp_* que agrupa las mallas de un accesorio; todo en la colección Acc_* del accesorio"""
    vl.update(); c = acc_coll(coll_name)
    e = bpy.data.objects.new(name, None); c.objects.link(e); e.empty_display_size = 0.03
    e.location = objs[0].matrix_world.translation.copy(); vl.update()
    for o in objs:
        o.parent = e; o.matrix_parent_inverse = e.matrix_world.inverted(); link(o, c)
    return e
A = C_ACC
bx, by, bz = -0.25, -0.06, 0.88
b_base = cyl("Bombilla_Casquillo", (bx, by, bz + 0.045), 0.024, 0.04, M['gris'], c=A)
b_ring = torus("Bombilla_Rosca", (bx, by, bz + 0.062), 0.024, 0.004, M['gris'], c=A)
b_glass = qsphere("Bombilla_Vidrio", (bx, by, bz + 0.12), 0.052, m=M['vidrio'], scale=(1, 1, 1.15), levels=3, c=A)
b_fil = qsphere("Bombilla_Filamento", (bx, by, bz + 0.115), 0.022, m=M['bombilla'], levels=1, c=A)
rays = []
for i, ang in enumerate((-55, -18, 18, 55)):
    a = math.radians(ang); rx = bx + math.sin(a) * 0.095; rz = bz + 0.12 + math.cos(a) * 0.095
    rays.append(cyl(f"Bombilla_Rayo_{i + 1}", (rx, by, rz), 0.0035, 0.035, M['rayo'], rot=(0, a, 0), verts=8, c=A))
b_glass_off = qsphere("Bombilla_Vidrio_Off", (bx, by, bz + 0.12), 0.052, m=M['vidrio_off'], scale=(1, 1, 1.15), levels=3, c=A)
b_fil_off = qsphere("Bombilla_Filamento_Off", (bx, by, bz + 0.115), 0.022, m=M['filamento_off'], levels=1, c=A)
group("Grp_Bombilla", [b_base, b_ring], "Acc_Bombilla")
def vis_group(name, objs, loc):
    c = acc_coll("Acc_Bombilla")
    e = bpy.data.objects.new(name, None); c.objects.link(e); e.location = loc; vl.update()
    for o in objs:
        o.parent = e; o.matrix_parent_inverse = e.matrix_world.inverted(); link(o, c)
    return e
luz_e = vis_group("Luz", [b_glass, b_fil] + rays, (bx, by, bz + 0.12))          # encendida: vidrio emisivo, filamento y rayos
luzoff_e = vis_group("LuzOff", [b_glass_off, b_fil_off], (bx, by, bz + 0.12))   # apagada: vidrio mate y filamento oscuro
lx, ly, lz = -0.16, -0.23, 0.41   # v011: delante del pecho, a la izquierda; lo sostiene la mano izquierda (T2)
l_base = cube("Laptop_Base", (lx, ly, lz), (0.18, 0.13, 0.008), M['gris'], rot=(0, 0, 0.15), c=A)
l_lid = cube("Laptop_Tapa", (lx - 0.01, ly - 0.062, lz + 0.06), (0.18, 0.008, 0.125), M['gris'], rot=(-0.25, 0, 0.15), c=A)
def screen_mat(name, png, emit=1.6, rough=0.25, alpha=False, extension='REPEAT'):
    """material con imagen: emisivo para pantallas (emit>0), mate para objetos, con transparencia si alpha"""
    m = bpy.data.materials.new(name); m.use_nodes = True; nt = m.node_tree
    bsdf = next(n for n in nt.nodes if n.type == 'BSDF_PRINCIPLED'); bsdf.inputs['Roughness'].default_value = rough
    img = bpy.data.images.load(os.path.join(TEX, png)); tex = nt.nodes.new('ShaderNodeTexImage'); tex.image = img; tex.extension = extension
    nt.links.new(tex.outputs['Color'], bsdf.inputs['Base Color'])
    if emit:
        nt.links.new(tex.outputs['Color'], bsdf.inputs['Emission Color']); bsdf.inputs['Emission Strength'].default_value = emit
    if alpha:
        nt.links.new(tex.outputs['Alpha'], bsdf.inputs['Alpha'])
        try: m.surface_render_method = 'BLENDED'
        except Exception: m.blend_method = 'BLEND'
    return m
def screen_plane(name, center, size, rot_matrix, m, c=C_ACC):
    bpy.ops.mesh.primitive_plane_add(size=1, location=center); o = bpy.context.active_object; o.name = name
    o.scale = (size[0], size[1], 1); o.rotation_euler = (rot_matrix @ Matrix.Rotation(math.pi / 2, 4, 'X')).to_euler()
    o.data.materials.append(m); link(o, c); return o
# v014: logo oficial de Quantic en el pecho (personaje/marca/quantic-logo-blanco.png): rejilla con la textura con alfa, envuelta
# a la sudadera con Shrinkwrap; mismo ancho que el logo anterior (aro + «Quantic», de x=-0,085 a +0,075)
# v015: 1,5 cm más alto que en v014 (en el mundo; 1,67 cm del script): 0,9 cm libres sobre el bolsillo y 1,2 cm bajo las puntas de los cordones
LOGO_W = 0.160; LOGO_H = LOGO_W * 758 / 3546; LOGO_Z = 0.395 + 0.0167
bpy.ops.mesh.primitive_grid_add(x_subdivisions=24, y_subdivisions=6, size=1, location=(-0.005, -0.181, LOGO_Z))
logo = bpy.context.active_object; logo.name = "Logo_Sudadera"; logo.scale = (LOGO_W, LOGO_H, 1); logo.rotation_euler = (math.pi / 2, 0, 0)
logo.data.materials.append(screen_mat('Q_LogoSudadera', 'quantic-logo-blanco.png', emit=0.0, rough=0.55, alpha=True, extension='EXTEND')); link(logo, C_CHAR)   # v015: EXTEND, sin rayitas en el borde
sw = logo.modifiers.new("Envolver", 'SHRINKWRAP'); sw.target = hood; sw.wrap_method = 'NEAREST_SURFACEPOINT'; sw.offset = 0.005
parent_keep(logo, body)
R_lid = Matrix.Rotation(0.15, 4, 'Z') @ Matrix.Rotation(-0.25, 4, 'X')
# la pantalla mira al teclado (+Y local de la tapa); la cara hacia el espectador es la trasera, con el logo Q
l_scr = screen_plane("Laptop_Pantalla", Vector((lx - 0.01, ly - 0.062, lz + 0.06)) + (R_lid @ Vector((0, 0.0045, 0))), (0.165, 0.108),
                     R_lid @ Matrix.Rotation(math.pi, 4, 'Z'), screen_mat('Q_PantallaLaptop', 'pantalla_laptop.png'))
ISO_W = 0.050; ISO_H = ISO_W * 1407 / 1490   # v014: isotipo oficial (personaje/marca/quantic-isotipo-blanco.png) en la cara trasera de la tapa
l_q = screen_plane("Laptop_LogoQ", Vector((lx - 0.01, ly - 0.062, lz + 0.06)) + (R_lid @ Vector((0, -0.0048, 0))), (ISO_W, ISO_H), R_lid,
                   screen_mat('Q_LogoLaptop', 'quantic-isotipo-blanco.png', emit=0.0, rough=0.55, alpha=True), c=A)
l_kb = cube("Laptop_Teclado", (lx, ly + 0.01, lz + 0.005), (0.15, 0.08, 0.003), M['negro'], rot=(0, 0, 0.15), c=A)
l_hinge = cyl("Laptop_Bisagra", (lx - 0.005, ly - 0.060, lz), 0.006, 0.17, M['negro'], rot=(0, math.pi / 2, 0.15), verts=12, c=A)
Rz = Matrix.Rotation(0.15, 4, 'Z')
k0 = Vector((lx, ly + 0.012, lz + 0.009)) + (Rz @ Vector((-0.066, -0.022, 0)))
l_key = cube("Laptop_Teclas", k0, (0.011, 0.011, 0.003), M['cuerda'], rot=(0, 0, 0.15), c=A)
ax = l_key.modifiers.new("filas", 'ARRAY'); ax.count = 11; ax.relative_offset_displace = (1.3, 0, 0)
ay = l_key.modifiers.new("columnas", 'ARRAY'); ay.count = 4; ay.relative_offset_displace = (0, 1.4, 0)
tp = Vector((lx, ly + 0.012, lz + 0.006)) + (Rz @ Vector((0, 0.048, 0)))
l_tp = cube("Laptop_Trackpad", tp, (0.05, 0.028, 0.002), M['cuerda'], rot=(0, 0, 0.15), c=A)
kc = k0 + (Rz @ Vector((10 * 0.011 * 1.3 / 2, 3 * 0.011 * 1.4 / 2, 0.0)))   # centro de la rejilla de 11×4 teclas (k0 es el centro de la primera)
bpy.ops.mesh.primitive_plane_add(size=1, location=(kc.x, kc.y, lz + 0.0112)); l_letters = bpy.context.active_object
l_letters.name = "Laptop_Letras"; l_letters.scale = (0.157, 0.062, 1); l_letters.rotation_euler = (0, 0, 0.15 + math.pi)   # legible desde el lado de la pantalla
l_letters.data.materials.append(screen_mat('Q_Teclas', 'teclas.png', emit=0.0, rough=0.6, alpha=True)); link(l_letters, A)
group("Grp_Laptop", [l_base, l_lid, l_scr, l_q, l_kb, l_hinge, l_key, l_tp, l_letters], "Acc_Laptop")
px, py, pz = -0.33, -0.27, 0.32   # v011: el móvil lo lleva el tentáculo inferior izquierdo T3
p_body = cube("Movil_Cuerpo", (px, py, pz), (0.058, 0.009, 0.115), M['negro'], rot=(0.1, -0.15, 0.25), c=A)
R_ph = Matrix.Rotation(0.25, 4, 'Z') @ Matrix.Rotation(-0.15, 4, 'Y') @ Matrix.Rotation(0.1, 4, 'X')
p_scr = screen_plane("Movil_Pantalla", Vector((px, py, pz)) + (R_ph @ Vector((0, -0.0047, 0))), (0.050, 0.100), R_ph,
                     screen_mat('Q_PantallaMovil', 'pantalla_movil.png'))
Rp = Matrix.Rotation(0.25, 4, 'Z') @ Matrix.Rotation(-0.15, 4, 'Y') @ Matrix.Rotation(0.1, 4, 'X')
p_cam = cyl("Movil_Camara", Vector((px, py, pz)) + (Rp @ Vector((0, -0.006, 0.046))), 0.004, 0.002, M['gris'], rot=(math.pi / 2 + 0.1, -0.15, 0.25), verts=12, c=A)
p_bar = cube("Movil_Barra", Vector((px, py, pz)) + (Rp @ Vector((0, -0.006, -0.047))), (0.022, 0.001, 0.003), M['blanco'], rot=(0.1, -0.15, 0.25), c=A)
group("Grp_Movil", [p_body, p_scr, p_cam, p_bar], "Acc_Movil")
tx, ty, tz = 0.28, -0.20, 0.58   # v011: la taza la lleva la mano derecha (brazo T7)
TAZA_GIRO = math.radians(-90)   # gira el cilindro para que el centro de la tira UV (logo) mire al frente (-Y)
def uv_cylinder(name, loc, r, h, m, N=48, front=-math.pi / 2, c=C_ACC):
    """cilindro con UV explícito: u da la vuelta (u=0,5 en el ángulo 'front', hacia -Y), v = altura; tapas en una esquina del mapa"""
    bm = bmesh.new()
    bot = [bm.verts.new((r * math.cos(2 * math.pi * i / N), r * math.sin(2 * math.pi * i / N), -h / 2)) for i in range(N)]
    top = [bm.verts.new((r * math.cos(2 * math.pi * i / N), r * math.sin(2 * math.pi * i / N), h / 2)) for i in range(N)]
    bm.verts.ensure_lookup_table(); uv = bm.loops.layers.uv.new("UVMap")
    def u_of(i):
        ang = 2 * math.pi * i / N; return ((ang - front) / (2 * math.pi) + 0.5) % 1.0
    for i in range(N):
        j = (i + 1) % N
        f = bm.faces.new((bot[i], bot[j], top[j], top[i]))
        ui, uj = u_of(i), u_of(j)
        if uj < ui: uj += 1.0          # costura: el último quad continúa más allá de u=1
        for lp, (uu, vv) in zip(f.loops, ((ui, 0), (uj, 0), (uj, 1), (ui, 1))): lp[uv].uv = (uu, vv)
    for ring, z in ((bot, -1), (top, 1)):
        f = bm.faces.new(ring if z < 0 else list(reversed(ring)))
        for lp in f.loops:   # tapas: círculo pequeño en una zona negra de la textura (UV no degenerada)
            a = math.atan2(lp.vert.co.y, lp.vert.co.x); lp[uv].uv = (0.12 + 0.06 * math.cos(a), 0.86 + 0.06 * math.sin(a))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces[:])
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free(); me.update()
    o = bpy.data.objects.new(name, me); c.objects.link(o); o.location = loc; o.data.materials.append(m)
    bpy.ops.object.select_all(action='DESELECT'); o.select_set(True); vl.objects.active = o; smooth_by_angle(40)
    return o
t_body = uv_cylinder("Taza_Cuerpo", (tx, ty, tz), 0.044, 0.088, screen_mat('Q_Taza', 'taza.png', emit=0.0, rough=0.35), c=A)
t_in = cyl("Taza_Cafe", (tx, ty, tz + 0.0405), 0.039, 0.01, mat('Q_Cafe', '#3A2414', 0.15), c=A)   # café al ras del borde (v009)
# asa en medio óvalo (forma de D): toro alargado en vertical, con la mitad interior recortada; sobresale por el lateral -X
t_h = torus("Taza_Asa", (tx + 0.044 - 0.004, ty, tz), 0.030, 0.0075, M['negro'], rot=(math.pi / 2, 0, 0), c=A)   # asa hacia fuera (+X)
t_h.scale = (0.75, 1.15, 1.0)                       # más alto que ancho (local Y = mundo Z tras el giro de 90° en X)
bisect_keep(t_h, (0.0, 0, 0), (1, 0, 0), keep_positive=True)    # conserva solo la mitad exterior (x local >= 0)
group("Grp_Taza", [t_body, t_in, t_h], "Acc_Taza")
cx, cy, cz = 0.41, -0.24, 0.34; rotc = (0.1, -0.1, -0.2)
c_board = cube("Checklist_Tabla", (cx, cy, cz), (0.095, 0.008, 0.125), M['negro'], rot=rotc, c=A)
R_cl = Matrix.Rotation(-0.2, 4, 'Z') @ Matrix.Rotation(-0.1, 4, 'Y') @ Matrix.Rotation(0.1, 4, 'X')
c_paper = screen_plane("Checklist_Hoja", Vector((cx, cy, cz - 0.005)) + (R_cl @ Vector((0, -0.0045, 0))), (0.082, 0.105), R_cl,
                       screen_mat('Q_Checklist', 'checklist.png', emit=0.0, rough=0.7))
c_clip = cube("Checklist_Clip", (cx, cy, cz + 0.062), (0.035, 0.014, 0.018), M['cuerda'], rot=rotc, c=A)
group("Grp_Checklist", [c_board, c_paper, c_clip], "Acc_Checklist")
dx, dy, dz = 0.44, -0.10, 0.74; rotd = (0, 0, -0.35)
Rd = Matrix.Rotation(-0.35, 4, 'Z'); dc = Vector((dx, dy, dz))
d_frames = [cube(f"Panel_Marco_{n}", dc + (Rd @ Vector(off)), dims, M['cian'], rot=rotd, c=A) for n, off, dims in (
    ("Sup", (0, 0, 0.054), (0.13, 0.008, 0.006)), ("Inf", (0, 0, -0.054), (0.13, 0.008, 0.006)),
    ("Izq", (-0.063, 0, 0), (0.006, 0.008, 0.112)), ("Der", (0.063, 0, 0), (0.006, 0.008, 0.112)))]
d_body = cube("Panel_Fondo", (dx, dy, dz), (0.122, 0.006, 0.102), M['negro'], rot=rotd, c=A)
bars = [cube(f"Panel_Barra_{i + 1}", (dx - 0.03 + i * 0.03, dy - 0.004, dz - 0.04 + h / 2), (0.02, 0.003, h), M['cian'], rot=rotd, c=A)
        for i, h in enumerate((0.025, 0.04, 0.058))]
d_arrow = cube("Panel_Flecha", (dx, dy - 0.004, dz + 0.03), (0.09, 0.002, 0.005), M['blanco'], rot=(0, -0.5, -0.35), c=A)
tip = Vector((dx, dy - 0.004, dz + 0.03)) + (Rd @ (Matrix.Rotation(-0.5, 4, 'Y') @ Vector((0.045, 0, 0))))
d_head = cube("Panel_Flecha_Punta", tip, (0.014, 0.002, 0.014), M['blanco'], rot=(0, -0.5 + math.pi / 4, -0.35), c=A)
group("Grp_Panel", d_frames + [d_body] + bars + [d_arrow, d_head], "Acc_Panel")

# ---------------------------------------------------------------- escala a 1 m y aplicar
def bbox():
    pts = [o.matrix_world @ Vector(c) for o in bpy.data.objects if o.type == 'MESH' and not o.hide_render for c in o.bound_box]
    return [(min(p[i] for p in pts), max(p[i] for p in pts)) for i in range(3)]
vl.update(); bb = bbox(); h = bb[2][1] - bb[2][0]; s = 1.0 / h
Ms = Matrix.Translation((0, 0, -bb[2][0] * s)) @ Matrix.Scale(s, 4)
for o in [o for o in bpy.data.objects if o.parent is None]:
    o.matrix_world = Ms @ o.matrix_world
vl.update()
bpy.ops.object.select_all(action='DESELECT')
for o in bpy.data.objects:
    if o.type == 'MESH' and o.data.users == 1: o.select_set(True)
vl.objects.active = head; bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
vl.update(); ESCALA = s

# ---------------------------------------------------------------- shape keys de la boca
mouth.shape_key_add(name="Basis", from_mix=False)
base_co = [v.co.copy() for v in mouth.data.vertices]
def add_key(name, fn_mouth, tongue_scale=1.0):
    k = mouth.shape_key_add(name=name, from_mix=False)
    for i, co in enumerate(base_co):
        if i < N_MOUTH: k.data[i].co = fn_mouth(co)
        else:
            tc = Vector((0, -0.02, -0.02)) * ESCALA
            k.data[i].co = tc + (co - tc) * tongue_scale
    return k
add_key("O",       lambda c: Vector((c.x * 0.5, c.y * 1.0, c.z * 1.6 + 0.012 * ESCALA)), tongue_scale=0.05)
add_key("Plano",   lambda c: Vector((c.x * 1.05, c.y * 0.6, c.z * 0.12)), tongue_scale=0.05)
add_key("Risa",    lambda c: Vector((c.x * 1.3, c.y * 1.0, c.z * 1.7)), tongue_scale=1.15)
add_key("Puchero", lambda c: Vector((c.x * 0.45, c.y * 0.8, c.z * 0.5)), tongue_scale=0.05)

# ---------------------------------------------------------------- rig
def chain_points(curve_obj, n=3):
    pts = [p for p, r in eval_curve(curve_obj, 20)]
    L = [0.0]
    for i in range(1, len(pts)): L.append(L[-1] + (pts[i] - pts[i - 1]).length)
    out = [pts[0]]
    for k in range(1, n):
        target = L[-1] * k / n
        for i in range(1, len(pts)):
            if L[i] >= target:
                f = (target - L[i - 1]) / max(L[i] - L[i - 1], 1e-9); out.append(pts[i - 1].lerp(pts[i], f)); break
    out.append(pts[-1]); return out
arm_data = bpy.data.armatures.new("Rig_Mascota"); arm = bpy.data.objects.new("Rig_Mascota", arm_data); C_RIG.objects.link(arm)
bpy.ops.object.select_all(action='DESELECT'); arm.select_set(True); vl.objects.active = arm
bpy.ops.object.mode_set(mode='EDIT'); eb = arm_data.edit_bones
CTRL = set()
def bone(name, hd, tl, parent=None, connect=False, ctrl=False, deform=True):
    b = eb.new(name); b.head = Vector(hd); b.tail = Vector(tl); b.use_deform = deform
    if parent: b.parent = eb[parent]; b.use_connect = connect
    if ctrl: CTRL.add(name)
    return b
head_c = head.matrix_world.translation.copy(); body_c = body.matrix_world.translation.copy()
bone("Root", (0, 0, 0), (0, 0, 0.12), ctrl=True)
bone("Cuerpo", (0, 0, body_c.z - 0.15), (0, 0, body_c.z + 0.09), "Root", ctrl=True)
bone("Cabeza", (0, 0, body_c.z + 0.09), (0, 0, head_c.z + 0.19), "Cuerpo", True, ctrl=True)
for side in ("I", "D"):
    e = eyes[side].matrix_world.translation
    bone(f"Ojo_{side}", (e.x, e.y + 0.02, e.z), (e.x, e.y - 0.06, e.z), "Cabeza")
    bone(f"Parpado_{side}", (e.x, e.y, e.z), (e.x, e.y, e.z + 0.06), "Cabeza", ctrl=True)
    bc = brows[side].matrix_world.translation
    bone(f"Ceja_{side}", (0, 0, head_c.z), (bc.x, bc.y, bc.z), "Cabeza", ctrl=True)   # gira sobre el centro: la ceja recorre la superficie
    bone(f"OjoFeliz_{side}", (e.x, e.y, e.z), (e.x, e.y - 0.04, e.z), "Cabeza", ctrl=True, deform=False)
ez = eyes["I"].matrix_world.translation.z
bone("Mirada", (0, -0.55, ez), (0, -0.55, ez + 0.06), "Cabeza", ctrl=True, deform=False)
tc = teeth.matrix_world.translation; bone("Dientes", (tc.x, tc.y, tc.z), (tc.x, tc.y - 0.04, tc.z), "Cabeza", ctrl=True, deform=False)
mc = marks_e.matrix_world.translation; bone("Marcas", (mc.x, mc.y, mc.z), (mc.x, mc.y - 0.04, mc.z), "Cabeza", ctrl=True, deform=False)
pc = bpy.data.objects["Panel_Fondo"].matrix_world.translation
bone("Panel", (pc.x - 0.15, pc.y, pc.z - 0.12), pc, "Cuerpo", ctrl=True)
chains = {}; ik_targets = {}
for tn in TENT:
    pts = chain_points(bpy.data.objects[tn + "_Curva"], 3); names = []
    for i in range(3):
        nm = f"{tn}.{i + 1:03d}"; bone(nm, pts[i], pts[i + 1], "Cuerpo" if i == 0 else names[-1], i > 0); names.append(nm)
    chains[tn] = names
    tip = pts[-1]; d = (pts[-1] - pts[-2]).normalized() * 0.05
    bone(f"{tn}_IK", tip, tip + d, "Root", ctrl=True, deform=False); ik_targets[tn] = f"{tn}_IK"
ACC_PARENT = {"Acc_Bombilla": ("Grp_Bombilla", "T1_Bombilla.003"), "Acc_Laptop": ("Grp_Laptop", "T2_BrazoIzq.003"), "Acc_Taza": ("Grp_Taza", "T7_BrazoDer.003"),
              "Acc_Checklist": ("Grp_Checklist", "T6_Checklist.003"), "Acc_Movil": ("Grp_Movil", "T3_Movil.003"), "Acc_Panel": ("Grp_Panel", "Panel")}
ACC = set(ACC_PARENT)
for an, (gn, parent_bone) in ACC_PARENT.items():   # un hueso de visibilidad por accesorio, con nombre fijo
    gc = bpy.data.objects[gn].matrix_world.translation
    bone(an, (gc.x, gc.y, gc.z), (gc.x, gc.y - 0.05, gc.z), parent_bone, ctrl=True, deform=False)
rc = luz_e.matrix_world.translation
bone("Luz", (rc.x, rc.y, rc.z), (rc.x, rc.y - 0.04, rc.z), "Acc_Bombilla", ctrl=True, deform=False)
bone("LuzOff", (rc.x, rc.y + 0.01, rc.z), (rc.x, rc.y - 0.03, rc.z), "Acc_Bombilla", ctrl=True, deform=False)
bpy.ops.object.mode_set(mode='OBJECT'); arm.show_in_front = True; vl.update()
# colecciones de huesos
bc_def = arm_data.collections.new("Deformacion"); bc_ctl = arm_data.collections.new("Controles")
for b in arm_data.bones:
    (bc_ctl if b.name in CTRL else bc_def).assign(b)
# restricciones: IK en cada cadena, mirada en los ojos
for tn, names in chains.items():
    pb = arm.pose.bones[names[-1]]
    ik = pb.constraints.new('IK'); ik.target = arm; ik.subtarget = ik_targets[tn]; ik.chain_count = 3; ik.use_tail = True
for side in ("I", "D"):
    pb = arm.pose.bones[f"Ojo_{side}"]
    dt = pb.constraints.new('DAMPED_TRACK'); dt.target = arm; dt.subtarget = "Mirada"; dt.track_axis = 'TRACK_Y'
for pb in arm.pose.bones:
    pb.rotation_mode = 'XYZ'
def bone_parent(obj, bname):
    pb = arm.pose.bones[bname]
    pm = arm.matrix_world @ pb.matrix @ Matrix.Translation((0, pb.bone.length, 0))
    obj.parent = arm; obj.parent_type = 'BONE'; obj.parent_bone = bname; obj.matrix_parent_inverse = pm.inverted()
bone_parent(head, "Cabeza"); bone_parent(body, "Cuerpo")
for side in ("I", "D"):
    bone_parent(eyes[side], f"Ojo_{side}")
    bone_parent(bpy.data.objects[f"Parpado_{side}"], f"Parpado_{side}")
    bone_parent(brows[side], f"Ceja_{side}")
    bone_parent(bpy.data.objects[f"OjoFeliz_{side}"], f"OjoFeliz_{side}")
bone_parent(teeth, "Dientes"); bone_parent(marks_e, "Marcas"); bone_parent(luz_e, "Luz"); bone_parent(luzoff_e, "LuzOff")
for an, (gn, _) in ACC_PARENT.items():
    bone_parent(bpy.data.objects[gn], an)
def seg_param(p, a, b):
    ab = b - a; t = (p - a).dot(ab) / max(ab.length_squared, 1e-12); t = max(0.0, min(1.0, t))
    return t, ((a + ab * t) - p).length
def skin_to_chain(o, names):
    bones = [arm.data.bones[n] for n in names]
    pts = [arm.matrix_world @ b.head_local for b in bones] + [arm.matrix_world @ bones[-1].tail_local]
    for vg in list(o.vertex_groups): o.vertex_groups.remove(vg)
    vgs = [o.vertex_groups.new(name=n) for n in names]; mw = o.matrix_world
    for v in o.data.vertices:
        p = mw @ v.co; best = None
        for i in range(3):
            tt, d = seg_param(p, pts[i], pts[i + 1])
            if best is None or d < best[1]: best = (i + tt, d)
        u = best[0]
        for j, vg in enumerate(vgs):
            c = j + 0.5; w = 1.0 if ((j == 0 and u <= c) or (j == 2 and u >= c)) else max(0.0, 1.0 - abs(u - c))
            if w > 0: vg.add([v.index], w, 'REPLACE')
    mod = o.modifiers.new("Armature", 'ARMATURE'); mod.object = arm
    o.parent = arm; o.matrix_parent_inverse = arm.matrix_world.inverted()
for tn, names in chains.items():
    skin_to_chain(tent_meshes[tn], names)
    if tn in sleeves: skin_to_chain(sleeves[tn], names)
vl.update()

ARM_BIAS_1 = (0.0, 0.0, -1.1); ARM_BIAS_2 = (-1.1, 0.0, 0.0)   # v013: giro inicial de los dos primeros huesos del brazo izquierdo en pensativo (codo abajo)
# ---------------------------------------------------------------- expresiones (acción "Expresiones", fotogramas 0-6)
PB = arm.pose.bones
KEYS = mouth.data.shape_keys.key_blocks
def set_world_loc(pbone, world):
    """coloca la cabeza del hueso de control en una posición mundial (armature en identidad)"""
    par = pbone.parent
    if par:
        # matriz de reposo del hueso en espacio del padre posado
        rest_in_parent = par.bone.matrix_local.inverted() @ pbone.bone.matrix_local
        world_rest = par.matrix @ rest_in_parent
    else:
        world_rest = pbone.bone.matrix_local
    pbone.location = world_rest.inverted() @ Vector(world)
VIS = {"OjoFeliz_I", "OjoFeliz_D", "Dientes", "Marcas", "LuzOff"}   # huesos de visibilidad: escala 0,001 = oculto, 1 = visible (Luz va al revés: visible por defecto)
def reset():
    for pb in PB:
        pb.location = (0, 0, 0); pb.rotation_euler = (0, 0, 0); pb.scale = (0.001, 0.001, 0.001) if pb.name in VIS else (1, 1, 1)
    for k in KEYS: k.value = 0.0
    vl.update()
    for tn, pos in TENT_DOWN.items(): tent_to(tn, pos)   # v011: todo tentáculo con accesorio se relaja hasta que su clip lo usa
    vl.update()
def show(*names):
    for n in names: PB[n].scale = (1, 1, 1)
def hide(*names):
    for n in names: PB[n].scale = (0.001, 0.001, 0.001)
def key_all(frame, acc=False):
    """clava todos los controles; los huesos Acc_* solo si acc=True (clips de modo), para que Expresiones e Idle no fuercen la visibilidad"""
    for pb in PB:
        if pb.name in CTRL and (acc or pb.name not in ACC):
            pb.keyframe_insert("location", frame=frame); pb.keyframe_insert("rotation_euler", frame=frame); pb.keyframe_insert("scale", frame=frame)
    for k in KEYS:
        if k.name != "Basis": k.keyframe_insert("value", frame=frame)
def mode(*visible):
    """deja visibles solo los accesorios indicados (huesos Acc_*)"""
    for a in ACC: (show if a in visible else hide)(a)
D = math.radians
tip_rest = {tn: (arm.matrix_world @ arm.data.bones[ik_targets[tn]].head_local).copy() for tn in TENT}
T1_DOWN = Vector((-0.30, 0.16, 0.07))                      # T1 relajado en el suelo, atrás-izquierda (entre T4 y T8), cuando no sostiene la bombilla
# v011: posiciones relajadas de los tentáculos que sostienen accesorios; los brazos cuelgan a los lados
TENT_DOWN = {"T1_Bombilla": T1_DOWN,
             "T2_BrazoIzq": Vector((-0.28, -0.11, 0.18)),    # brazo izquierdo colgando junto a la sudadera, mano bajo el dobladillo
             "T7_BrazoDer": Vector((0.28, -0.11, 0.18)),     # brazo derecho colgando junto a la sudadera
             "T3_Movil": Vector((-0.21, -0.35, 0.06)),       # móvil: al suelo, delante-izquierda
             "T6_Checklist": Vector((0.21, -0.35, 0.06))}   # checklist: al suelo, delante-derecha
idle_rest = dict(tip_rest); idle_rest.update(TENT_DOWN)
def tent_to(tn, world): set_world_loc(PB[ik_targets[tn]], world)
def world_of(name):
    """posición mundial de un objeto con el rig evaluado (huesos IK y parentesco a hueso incluidos)"""
    vl.update(); dg = bpy.context.evaluated_depsgraph_get()
    return bpy.data.objects[name].evaluated_get(dg).matrix_world.translation.copy()
def reach_object(tn, obj_name, goal, start, iters=6):
    """mueve el control IK de tn hasta que el objeto obj_name (colgado de la mano) queda en goal; devuelve el objetivo del control"""
    target = Vector(start)
    for _ in range(iters):
        tent_to(tn, target); err = goal - world_of(obj_name)
        if err.length < 0.0015: break
        target = target + err
    return target
def aim_bone_axis(pb, obj_bottom, obj_top, up_world, iters=3):
    """gira el hueso pb (rotación XYZ local) para que el eje obj_bottom→obj_top apunte a up_world (mundo)"""
    for _ in range(iters):
        vl.update(); axis = (world_of(obj_top) - world_of(obj_bottom)).normalized()
        q = axis.rotation_difference(Vector(up_world).normalized())
        if q.angle < 0.01: break
        M = (arm.matrix_world @ pb.matrix).to_3x3()
        R_local = M.inverted() @ q.to_matrix() @ M
        pb.rotation_euler = (pb.rotation_euler.to_matrix() @ R_local).to_euler('XYZ')   # giro añadido en el espacio local del hueso
    return pb.rotation_euler.copy()
BROW_R = arm.data.bones["Ceja_I"].length
def brow(side, dz=0.0, tilt=0.0):
    """ceja: subir/bajar dz (m, aprox.) girando el hueso sobre el centro de la cabeza, e inclinar tilt (grados)"""
    pb = PB[f"Ceja_{side}"]; pb.rotation_euler.x = -dz / BROW_R; pb.rotation_euler.y = D(tilt)
def lids(i, d): PB["Parpado_I"].rotation_euler.x = D(i); PB["Parpado_D"].rotation_euler.x = D(d)
# 0 neutro
reset(); key_all(0)
# 1 feliz: ojos cerrados, cejas arriba, sonrisa amplia
reset(); lids(180, 180); show("OjoFeliz_I", "OjoFeliz_D", "Dientes"); brow("I", 0.010); brow("D", 0.010); KEYS["Risa"].value = 0.35; key_all(1)
# 2 sorprendido: ojos abiertos, cejas muy arriba, boca en O
reset(); show("Marcas"); brow("I", 0.018); brow("D", 0.018); KEYS["O"].value = 1.0; PB["Cabeza"].rotation_euler.x = D(-4); key_all(2)
# 3 pensativo: mirada arriba-izquierda, ceja I arriba, ceja D abajo, puchero, tentáculo D en la barbilla
reset(); lids(40, 40); set_world_loc(PB["Mirada"], (-0.25, -0.55, ez + 0.22))
brow("I", 0.012, 12); brow("D", -0.005, -6); KEYS["Puchero"].value = 1.0; PB["Cabeza"].rotation_euler.z = D(8)
def chin_point(d_local=(-0.12, -0.70, -0.70), out=0.014):
    """punto sobre la cabeza: intersección de la dirección d_local (local de la cabeza) con su elipsoide (evaluado), más el radio de la mano.
    v013: para pensativo se usa la parte delantera de la cara, bajo la boca y a la izquierda (FACE_DIR), no la barbilla (quedaba en el cuello)"""
    vl.update(); dg = bpy.context.evaluated_depsgraph_get(); M = head.evaluated_get(dg).matrix_world
    bb = head.bound_box; rx, ry, rz = [(bb[6][i] - bb[0][i]) / 2 for i in range(3)]
    d = Vector(d_local).normalized(); t = 1.0 / math.sqrt((d.x / rx) ** 2 + (d.y / ry) ** 2 + (d.z / rz) ** 2)
    p = M @ (d * t); n = (M.to_3x3() @ d).normalized()
    return p + n * out
FACE_DIR = (-0.30, -0.80, -0.52)   # v013: delante de la cara, justo debajo de la boca y a la izquierda (la boca queda libre)
def arm_bias(tn, rot1, rot2):
    """pose inicial de la cadena antes de resolver el IK: el solucionador parte de aquí, así que decide hacia dónde va el codo"""
    PB[f"{tn}.001"].rotation_euler = rot1; PB[f"{tn}.002"].rotation_euler = rot2; vl.update()
arm_bias("T2_BrazoIzq", ARM_BIAS_1, ARM_BIAS_2)
tent_to("T2_BrazoIzq", chin_point(FACE_DIR, out=0.012)); key_all(3)   # v013: la punta del brazo izquierdo apoyada en la cara bajo la boca, tentáculo curvado hacia arriba
# 4 guiñando: ojo I cerrado, ceja I bajada, sonrisa
reset(); lids(180, 0); show("OjoFeliz_I"); brow("I", -0.008, -10); brow("D", 0.010); PB["Cabeza"].rotation_euler.z = D(-6); key_all(4)
# 5 serio: párpados a medio cerrar, cejas bajas e inclinadas, boca plana, tentáculos cruzados
reset(); lids(100, 100); brow("I", -0.012, -18); brow("D", -0.012, 18); KEYS["Plano"].value = 1.0
tent_to("T2_BrazoIzq", (0.10, -0.21, 0.36)); tent_to("T7_BrazoDer", (-0.10, -0.215, 0.40)); key_all(5)   # v011: brazos cruzados
# 6 risa: ojos cerrados, cabeza hacia atrás, boca abierta a carcajada
reset(); lids(180, 180); show("OjoFeliz_I", "OjoFeliz_D", "Dientes", "Marcas"); brow("I", 0.014); brow("D", 0.014); KEYS["Risa"].value = 1.0
PB["Cabeza"].rotation_euler.x = D(-14); key_all(6)
reset(); sc.frame_start = 0; sc.frame_end = 6; sc.frame_set(0)
if arm.animation_data and arm.animation_data.action: arm.animation_data.action.name = "Expresiones"
if mouth.data.shape_keys.animation_data and mouth.data.shape_keys.animation_data.action:
    mouth.data.shape_keys.animation_data.action.name = "Expresiones_Boca"
# interpolación constante: cada fotograma es una pose, no una transición
def all_fcurves(action):
    """Blender 5: acciones por capas/strips/channelbags; fallback a action.fcurves en versiones previas"""
    if hasattr(action, "layers") and len(action.layers):
        for layer in action.layers:
            for strip in layer.strips:
                for cb in strip.channelbags:
                    yield from cb.fcurves
    elif hasattr(action, "fcurves"):
        yield from action.fcurves
for ad in (arm.animation_data, mouth.data.shape_keys.animation_data):
    if ad and ad.action:
        for fc in all_fcurves(ad.action):
            for kp in fc.keyframe_points: kp.interpolation = 'CONSTANT'

# ---------------------------------------------------------------- animación idle (bucle de 72 fotogramas a 24 fps)
act_expr = arm.animation_data.action; act_expr.use_fake_user = True
act_boca = mouth.data.shape_keys.animation_data.action; act_boca.use_fake_user = True
mouth.data.shape_keys.animation_data.action = None   # v013: las claves de boca de Idle ya no caen en Expresiones_Boca (que llegaba a 3 s en el .glb)
arm.animation_data.action = None
IDLE_LEN = 72; sc.render.fps = 24
def idle_key(frame): key_all(frame, acc=False)
phase = {tn: i * 2 * math.pi / 8 for i, tn in enumerate(TENT)}
for f in range(0, IDLE_LEN + 1, 6):
    t = 2 * math.pi * f / IDLE_LEN
    reset()
    PB["Root"].location.z = 0.006 * math.sin(t)                       # respiración (sube y baja)
    PB["Cabeza"].rotation_euler.z = D(3.0) * math.sin(t)                # balanceo lateral de la cabeza
    PB["Cabeza"].rotation_euler.x = D(1.5) * math.sin(2 * t)
    for tn in TENT:
        tent_to(tn, idle_rest[tn] + Vector((0.008 * math.sin(t + phase[tn]), 0.0, 0.014 * math.sin(t + phase[tn] + 1.0))))
    set_world_loc(PB["Mirada"], (0.06 * math.sin(t), -0.55, ez + 0.03 * math.sin(t + 0.7)))
    idle_key(f)
# parpadeo rápido en los fotogramas 40-46
for f, ang in ((40, 0), (42, 180), (44, 180), (46, 0)):
    sc.frame_set(f); lids(ang, ang); PB["Parpado_I"].keyframe_insert("rotation_euler", frame=f); PB["Parpado_D"].keyframe_insert("rotation_euler", frame=f)
act_idle = arm.animation_data.action; act_idle.name = "Idle"; act_idle.use_fake_user = True
for fc in all_fcurves(act_idle):
    for kp in fc.keyframe_points: kp.interpolation = 'BEZIER'
act_idle_boca = mouth.data.shape_keys.animation_data.action; act_idle_boca.name = "Idle_Boca"; act_idle_boca.use_fake_user = True   # v013: la boca de Idle en su propia acción
mouth.data.shape_keys.animation_data.action = None
arm.animation_data.action = None; reset(); sc.frame_set(0)
# pistas NLA: una por acción (el exportador glTF las saca como animaciones separadas)
# v013: cada clip ocupa su propio rango de fotogramas de la escena, para que las pistas de boca (shape keys) puedan estar
# todas activas a la vez sin pisarse: así el exportador FBX (que hornea la escena por tira) saca la boca correcta de cada clip.
CLIP_START = {"Expresiones": 0, "Idle": 100, "Saludo": 200, "Idea": 300, "Tecleo": 400, "Relax": 500, "Organizar": 600}
def clip_frame(name, f): return CLIP_START[name] + f
def nla_push(id_data, name, action, start=None):
    if start is None: start = CLIP_START[name]
    ad = id_data.animation_data or id_data.animation_data_create()
    tr = ad.nla_tracks.new(); tr.name = name
    st = tr.strips.new(name, start, action); st.extrapolation = 'NOTHING'   # v013: fuera de su rango la tira no suena (los clips van en serie)
    try:
        if hasattr(st, "action_slot") and action.slots: st.action_slot = action.slots[0]
    except Exception as ex: print("slot:", ex)
    tr.mute = False; return tr
mouth.data.shape_keys.animation_data.action = None
NLA_EXPR_ARM = nla_push(arm, "Expresiones", act_expr); NLA_EXPR_BOCA = nla_push(mouth.data.shape_keys, "Expresiones", act_boca)
NLA_IDLE = nla_push(arm, "Idle", act_idle); NLA_IDLE_BOCA = nla_push(mouth.data.shape_keys, "Idle", act_idle_boca)
sc.frame_start = 0; sc.frame_end = CLIP_START["Organizar"] + 48
NT_LUZ = []   # v006: la bombilla apagada/encendida son dos mallas; no se anima ningún material
def anim_ids():
    return [idd for idd in [arm, mouth.data.shape_keys] + NT_LUZ if idd.animation_data]
def solo(name):
    """deja sonando solo la pista NLA indicada (Expresiones, Idle, Saludo, Idea, Tecleo, Relax, Organizar); con name=None, ninguna.
    v013: los clips viven en rangos distintos (CLIP_START), así que para posar basta goto(); solo() se mantiene por comodidad."""
    for idd in anim_ids():
        for tr in idd.animation_data.nla_tracks:
            tr.is_solo = (tr.name == name)
            tr.mute = (tr.name != name)
    sc.frame_set(sc.frame_current)
def unmute_all():
    """todas las pistas activas (estado de entrega: así exportan bien glTF y FBX, cada clip en su rango)"""
    for idd in anim_ids():
        for tr in idd.animation_data.nla_tracks: tr.is_solo = False; tr.mute = False
def goto(name, f):
    """pone la escena en el fotograma f del clip name (con todas las pistas activas)"""
    unmute_all(); sc.frame_set(clip_frame(name, f))

# ---------------------------------------------------------------- clips: Saludo, Idea, Tecleo (48 fotogramas, 24 fps)
def emis(nt):
    return next(n for n in nt.nodes if n.type == 'BSDF_PRINCIPLED').inputs['Emission Strength']
EMIS_REST = {nt.name: emis(nt).default_value for nt in NT_LUZ}
def key_emis(frame, factor):
    for nt in NT_LUZ:
        emis(nt).default_value = EMIS_REST[nt.name] * factor; emis(nt).keyframe_insert("default_value", frame=frame)
def make_clip(name, length, keyer, step=4, with_light=False, acc=True):
    for idd in [arm, mouth.data.shape_keys] + NT_LUZ:
        if idd.animation_data: idd.animation_data.action = None
    for f in range(0, length + 1, step):
        reset(); keyer(f, f / length); key_all(f, acc=acc)
    acts = []
    for idd in [arm, mouth.data.shape_keys] + (NT_LUZ if with_light else []):
        ad = idd.animation_data
        if ad and ad.action:
            a = ad.action; a.name = name if idd is arm else f"{name}_{'Boca' if idd is mouth.data.shape_keys else idd.name}"
            a.use_fake_user = True
            for fc in all_fcurves(a):
                for kp in fc.keyframe_points: kp.interpolation = 'BEZIER'
            ad.action = None; nla_push(idd, name, a); acts.append(a.name)
    for nt in NT_LUZ: emis(nt).default_value = EMIS_REST[nt.name]
    reset(); return acts
LAPTOP = bpy.data.objects["Laptop_Teclado"].matrix_world.translation.copy()
def k_saludo(f, u):
    """el brazo derecho (T7) se levanta y saluda; cara contenta; sin accesorios"""
    mode()
    up = smooth(f / 8.0); back = smooth((f - 40) / 8.0)
    lift = up * (1 - back)
    wave = math.sin((f - 8) / 32.0 * 2 * math.pi * 2) if 8 <= f <= 40 else 0.0
    target = TENT_DOWN["T7_BrazoDer"].lerp(Vector((0.28 + 0.06 * wave, -0.20, 0.60)), lift)
    tent_to("T7_BrazoDer", target)
    PB["Cabeza"].rotation_euler.z = D(5) * lift; brow("I", 0.006 * lift); brow("D", 0.006 * lift)
    KEYS["Risa"].value = 0.3 * lift
    if 10 <= f <= 38: show("OjoFeliz_I", "OjoFeliz_D"); lids(180, 180)
def k_idea(f, u):
    """la bombilla está apagada, el tentáculo la alza, se enciende con rayos y marcas; cara de sorpresa y luego sonrisa"""
    mode("Acc_Bombilla")
    on = 0.0 if f < 18 else min(1.0, (f - 18) / 4.0)
    if on < 1.0: hide("Luz"); show("LuzOff")
    bounce = math.sin(min(1.0, max(0.0, (f - 14) / 16.0)) * math.pi) * 0.07
    up = min(1.0, f / 14.0); up = up * up * (3 - 2 * up)       # sube la bombilla desde la posición relajada
    tent_to("T1_Bombilla", T1_DOWN.lerp(tip_rest["T1_Bombilla"], up) + Vector((0, 0, bounce)))
    tilt = min(1.0, max(0.0, (f - 8) / 10.0)) * (1 - max(0.0, (f - 36) / 12.0))
    PB["Cabeza"].rotation_euler.x = D(-6) * tilt; brow("I", 0.016 * tilt); brow("D", 0.016 * tilt)
    for an, sx in (("T2_BrazoIzq", -1), ("T7_BrazoDer", 1)):   # los brazos se abren un poco con la sorpresa
        tent_to(an, TENT_DOWN[an].lerp(Vector((sx * 0.33, -0.14, 0.33)), tilt))
    if 20 <= f <= 34: show("Marcas"); KEYS["O"].value = 1.0
    elif f > 34: KEYS["Risa"].value = 0.35; show("Dientes")
def k_tecleo(f, u):
    """el brazo izquierdo sube el portátil, mira la pantalla y teclea con la mano derecha; parpadeo a mitad; solo el portátil"""
    mode("Acc_Laptop")
    tap = abs(math.sin(f / 48.0 * 2 * math.pi * 4))
    lift = smooth(f / 10.0) * smooth(1 - (f - 40) / 8.0)
    tent_to("T2_BrazoIzq", TENT_DOWN["T2_BrazoIzq"].lerp(tip_rest["T2_BrazoIzq"], lift))   # v011: T2 sube el portátil solo aquí
    reach = smooth((f - 6) / 8.0) * (1 - max(0.0, (f - 42) / 6.0))
    vl.update(); kb = bpy.data.objects["Laptop_Teclado"].matrix_world.translation.copy()   # teclado donde está ahora el portátil
    key_pos = kb + Vector((0.045 + 0.015 * math.sin(f / 48.0 * 2 * math.pi * 2), -0.02, 0.02 + 0.03 * tap))
    tent_to("T7_BrazoDer", TENT_DOWN["T7_BrazoDer"].lerp(key_pos, reach))   # v011: teclea la mano derecha
    PB["Cabeza"].rotation_euler.z = D(-18) * reach; PB["Cabeza"].rotation_euler.x = D(6) * reach
    set_world_loc(PB["Mirada"], Vector((0, -0.55, ez)).lerp(kb + Vector((0, -0.05, 0.08)), reach))
    lids(25 * reach, 25 * reach)
    if 22 <= f <= 26: lids(180, 180)
MOUTH = bpy.data.objects["Boca"].matrix_world.translation.copy()
CHECK = bpy.data.objects["Checklist_Hoja"].matrix_world.translation.copy()
def smooth(x): x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)
HEAD_SIP = D(5)                                   # v012: la cabeza se inclina un poco hacia la taza (+x = mirar abajo, como en Tecleo)
MUG_UP = Vector((0.08, 0.42, 0.90))               # eje de la taza en el sorbo: inclinada hacia la boca (+Y), casi vertical
def solve_sip():
    """v012: calcula el objetivo del control IK de T7 y el giro de Acc_Taza para que el borde de la taza toque los labios"""
    reset(); mode("Acc_Taza"); PB["Cabeza"].rotation_euler.x = HEAD_SIP; vl.update()
    lips = world_of("Boca"); goal = lips + Vector((-0.004, -0.036, -0.010))   # centro del borde: 3,6 cm delante de los labios → el borde trasero los toca
    target = MOUTH + Vector((-0.02, -0.05, -0.055)); rot = None
    for _ in range(3):
        rot = aim_bone_axis(PB["Acc_Taza"], "Taza_Cuerpo", "Taza_Cafe", MUG_UP)
        target = reach_object("T7_BrazoDer", "Taza_Cafe", goal, target)
    rim = world_of("Taza_Cafe"); print("sorbo: labios", [round(v, 3) for v in lips], "borde taza", [round(v, 3) for v in rim], "error %.3f" % (goal - rim).length)
    reset(); return target, rot
SIP_TARGET, SIP_ROT = solve_sip()
def k_relax(f, u):
    """bucle tranquilo: la mano derecha (T7) sube la taza hasta la boca (el borde toca los labios), sorbo con ojos cerrados, baja y sonríe; solo la taza"""
    mode("Acc_Taza")
    if f <= 18: s = smooth(f / 18.0)
    elif f <= 42: s = 1.0
    elif f <= 60: s = smooth(1 - (f - 42) / 18.0)
    else: s = 0.0
    tent_to("T7_BrazoDer", TENT_DOWN["T7_BrazoDer"].lerp(SIP_TARGET, s))   # v012: objetivo resuelto con la taza evaluada
    PB["Acc_Taza"].rotation_euler = tuple(a * s for a in SIP_ROT)          # la taza se inclina hacia la boca al llegar
    PB["Cabeza"].rotation_euler.x = HEAD_SIP * s; PB["Root"].location.z = 0.004 * math.sin(2 * math.pi * f / 72.0)
    brow("I", 0.004 * s); brow("D", 0.004 * s)
    if 22 <= f <= 40: lids(180, 180); show("OjoFeliz_I", "OjoFeliz_D"); KEYS["O"].value = 0.5
    else: lids(18 * s, 18 * s)
    if f >= 48 or f <= 6: KEYS["Risa"].value = 0.25 * (1 - s)   # sonrisa relajada al bajar la taza
def k_organizar(f, u):
    """T6 sube la checklist y la mano derecha (T7) marca una tarea; mira la hoja y sonríe; checklist y panel"""
    mode("Acc_Checklist", "Acc_Panel")
    reach = smooth(f / 10.0) * smooth(1 - (f - 38) / 10.0)
    CK_UP = tip_rest["T6_Checklist"] + Vector((-0.06, -0.02, 0.0))   # un poco hacia el centro: la mano derecha llega a la hoja
    tent_to("T6_Checklist", TENT_DOWN["T6_Checklist"].lerp(CK_UP, reach))   # v011: T6 sube la checklist solo aquí
    tap = math.sin(math.pi * (f - 16) / 8.0) if 16 <= f <= 24 else 0.0
    vl.update(); ck = bpy.data.objects["Checklist_Hoja"].matrix_world.translation.copy()   # hoja donde está ahora la checklist
    pos = ck + Vector((-0.015, -0.045 + 0.02 * tap, 0.01))     # delante de la hoja (mira a -Y); el toque acerca la punta
    tent_to("T7_BrazoDer", TENT_DOWN["T7_BrazoDer"].lerp(pos, reach))   # v011: marca con la mano derecha
    PB["Cabeza"].rotation_euler.z = D(14) * reach; PB["Cabeza"].rotation_euler.x = D(4) * reach
    set_world_loc(PB["Mirada"], Vector((0, -0.55, ez)).lerp(ck + Vector((0, -0.35, 0.02)), reach))
    lids(15 * reach, 15 * reach)
    if f >= 26: g = smooth((f - 26) / 6.0); KEYS["Risa"].value = 0.35 * g; brow("I", 0.008 * g); brow("D", 0.008 * g); show("Dientes")
    if 30 <= f <= 42: lids(180, 180); show("OjoFeliz_I", "OjoFeliz_D")
CLIPS = {"Saludo": make_clip("Saludo", 48, k_saludo), "Idea": make_clip("Idea", 48, k_idea), "Tecleo": make_clip("Tecleo", 48, k_tecleo),
         "Relax": make_clip("Relax", 72, k_relax), "Organizar": make_clip("Organizar", 48, k_organizar)}
print("clips:", CLIPS)
unmute_all(); sc.frame_set(clip_frame("Idle", 0))

# ---------------------------------------------------------------- cámaras, luces, render
def cam(name, loc, rot, ortho=True, scale=1.3):
    cd = bpy.data.cameras.new(name); c = bpy.data.objects.new(name, cd); C_SET.objects.link(c)
    c.location = loc; c.rotation_euler = rot; cd.type = 'ORTHO' if ortho else 'PERSP'; cd.ortho_scale = scale; cd.lens = 50
    return c
cam("Cam_Frente", (0, -3, 0.5), (math.pi / 2, 0, 0))
cam("Cam_Perfil_Der", (-3, 0, 0.5), (math.pi / 2, 0, -math.pi / 2))
cam("Cam_Perfil_Izq", (3, 0, 0.5), (math.pi / 2, 0, math.pi / 2))
cam("Cam_Espalda", (0, 3, 0.5), (math.pi / 2, 0, math.pi))
cam("Cam_3-4", (1.55, -1.55, 0.95), (math.radians(72), 0, math.radians(45)), ortho=False)
cam("Cam_Busto", (0, -3, head_c.z - 0.045), (math.pi / 2, 0, 0), scale=0.70)   # v011: encuadre más amplio y centrado más alto; las rayitas de énfasis entran con margen
def light(name, kind, energy, loc, rot, size=None):
    ld = bpy.data.lights.new(name, kind); ld.energy = energy
    if size and kind == 'AREA': ld.size = size
    if kind == 'SUN': ld.angle = math.radians(10)
    l = bpy.data.objects.new(name, ld); C_SET.objects.link(l); l.location = loc; l.rotation_euler = rot; return l
light("Sol", 'SUN', 3.0, (0, 0, 3), (math.radians(50), math.radians(-20), math.radians(30)))
light("Relleno", 'AREA', 150, (-2, -2.5, 1.2), (math.radians(70), 0, math.radians(-40)), size=3)
light("Contra", 'AREA', 220, (1.5, 2.8, 1.6), (math.radians(60), 0, math.radians(155)), size=3)
light("Relleno_Espalda", 'AREA', 120, (-1.5, 2.5, 0.8), (math.radians(75), 0, math.radians(-150)), size=3)
w = sc.world or bpy.data.worlds.new("World"); sc.world = w; w.use_nodes = True
bg = w.node_tree.nodes.get("Background"); bg.inputs[0].default_value = (0.09, 0.09, 0.11, 1); bg.inputs[1].default_value = 1.0
sc.render.engine = 'BLENDER_EEVEE'; sc.eevee.taa_render_samples = 32
sc.view_settings.view_transform = 'Standard'; sc.view_settings.look = 'None'
sc.render.resolution_x = 800; sc.render.resolution_y = 1000; sc.render.resolution_percentage = 100
# ---------------------------------------------------------------- horneado de texturas (llamar a bake_all() tras el script)
HEAD = [head, bpy.data.objects["Parpado_I"], bpy.data.objects["Parpado_D"]]
BODY = [body] + list(tent_meshes.values())
SKIN = HEAD + BODY
HOODIE = [bpy.data.objects[n] for n in ("Sudadera", "Sudadera_Cuello", "Sudadera_Capucha", "Sudadera_Bajo", "Sudadera_Bolsillo")] + list(sleeves.values())
def _unwrap(objs, margin=0.004):
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs: o.select_set(True)
    vl.objects.active = objs[0]; bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.uv.smart_project(angle_limit=math.radians(66), island_margin=margin, correct_aspect=True, scale_to_bounds=False)
    bpy.ops.object.mode_set(mode='OBJECT')
def _image(name, size, color_data=True):
    img = bpy.data.images.new(name, size, size, alpha=False, float_buffer=False)
    img.colorspace_settings.name = 'sRGB' if color_data else 'Non-Color'; return img
def _bake(objs, img, btype, **kw):
    mats = {sl.material for o in objs for sl in o.material_slots if sl.material}
    nodes = []
    for m in mats:
        n = m.node_tree.nodes.new('ShaderNodeTexImage'); n.image = img; m.node_tree.nodes.active = n; nodes.append((m, n))
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs: o.select_set(True)
    vl.objects.active = objs[0]
    bpy.ops.object.bake(type=btype, use_clear=True, margin=8, **kw)
    for m, n in nodes: m.node_tree.nodes.remove(n)
def _save(img, fn):
    img.filepath_raw = os.path.join(TEX, fn); img.file_format = 'PNG'; img.save()
def _baked_material(name, hexcol, color_img, normal_img, rough):
    m = bpy.data.materials.new(name); m.use_nodes = True; nt = m.node_tree
    bsdf = next(n for n in nt.nodes if n.type == 'BSDF_PRINCIPLED'); bsdf.inputs['Roughness'].default_value = rough
    if color_img:
        tc = nt.nodes.new('ShaderNodeTexImage'); tc.image = color_img; nt.links.new(tc.outputs['Color'], bsdf.inputs['Base Color'])
    else:
        bsdf.inputs['Base Color'].default_value = hex2lin(hexcol)
    tn = nt.nodes.new('ShaderNodeTexImage'); tn.image = normal_img; tn.image.colorspace_settings.name = 'Non-Color'
    nm = nt.nodes.new('ShaderNodeNormalMap'); nm.inputs['Strength'].default_value = 1.0
    nt.links.new(tn.outputs['Color'], nm.inputs['Color']); nt.links.new(nm.outputs['Normal'], bsdf.inputs['Normal'])
    m.diffuse_color = hex2lin(hexcol); return m
BAKED = {}
def _prep(samples):
    sc.render.engine = 'CYCLES'; sc.cycles.samples = samples; sc.cycles.device = 'CPU'; sc.render.bake.use_selected_to_active = False
def bake_head(size=2048, samples=8):
    """atlas propio de cabeza y párpados: color + normales"""
    _prep(samples); _unwrap(HEAD, margin=0.006)
    c = _image("Cabeza_Color", size, True); n = _image("Cabeza_Normal", size, False)
    _bake(HEAD, c, 'DIFFUSE', pass_filter={'COLOR'}); _save(c, "cabeza_color.png")
    _bake(HEAD, n, 'NORMAL', normal_space='TANGENT'); _save(n, "cabeza_normal.png")
    BAKED["cabeza"] = (c, n); sc.render.engine = 'BLENDER_EEVEE'; print("bake cabeza ok")
def bake_body(size=2048, samples=8):
    """atlas de cuerpo y tentáculos (con ventosas): color + normales"""
    _prep(samples); _unwrap(BODY, margin=0.004)
    c = _image("Cuerpo_Color", size, True); n = _image("Cuerpo_Normal", size, False)
    _bake(BODY, c, 'DIFFUSE', pass_filter={'COLOR'}); _save(c, "cuerpo_color.png")
    _bake(BODY, n, 'NORMAL', normal_space='TANGENT'); _save(n, "cuerpo_normal.png")
    BAKED["cuerpo"] = (c, n); sc.render.engine = 'BLENDER_EEVEE'; print("bake cuerpo ok")
def bake_hoodie(size=1024, samples=8):
    _prep(samples); _unwrap(HOODIE, margin=0.006)
    n = _image("Sudadera_Normal", size, False)
    _bake(HOODIE, n, 'NORMAL', normal_space='TANGENT'); _save(n, "sudadera_normal.png")
    BAKED["sudadera"] = (None, n); sc.render.engine = 'BLENDER_EEVEE'; print("bake sudadera ok")
def bake_finish():
    """asigna los materiales de imagen a partir de lo horneado (o de las imágenes ya cargadas)"""
    def img(name): return BAKED.get(name.split('_')[0].lower(), (None, None))
    c, n = BAKED["cabeza"]; m_cab = _baked_material("Q_Cabeza_Horneada", '#8070E7', c, n, 0.5)
    c, n = BAKED["cuerpo"]; m_cue = _baked_material("Q_Cuerpo_Horneada", '#8070E7', c, n, 0.5)
    _, n = BAKED["sudadera"]; m_sud = _baked_material("Q_Sudadera_Horneada", '#0E1424', None, n, 0.9)
    for o in HEAD:
        for sl in o.material_slots: sl.material = m_cab
    for o in BODY:
        for sl in o.material_slots: sl.material = m_cue
    for o in HOODIE:
        for sl in o.material_slots:
            if sl.material and sl.material.name != 'Q_SudaderaInterior': sl.material = m_sud
    sc.render.engine = 'BLENDER_EEVEE'; print("materiales horneados asignados")
def bake_all():
    bake_head(); bake_body(); bake_hoodie(); bake_finish()
def reuse_head(src_dir):
    """v011: la cabeza no cambia; se desenvuelve igual y se cargan sus texturas. Cuerpo (brazos nuevos) y sudadera (mangas) se hornean de nuevo."""
    _unwrap(HEAD, margin=0.006)
    def load(fn, color):
        img = bpy.data.images.load(os.path.join(src_dir, fn)); img.name = fn.replace(".png", "")
        img.colorspace_settings.name = 'sRGB' if color else 'Non-Color'; return img
    BAKED["cabeza"] = (load("cabeza_color.png", True), load("cabeza_normal.png", False)); print("cabeza reutilizada de", src_dir)
def reuse_hoodie(src_dir):
    """v014: la sudadera no cambia; se desenvuelve igual y se carga su normal. Cabeza y cuerpo (color nuevo) se hornean de nuevo."""
    _unwrap(HOODIE, margin=0.006)
    img = bpy.data.images.load(os.path.join(src_dir, "sudadera_normal.png")); img.name = "sudadera_normal"; img.colorspace_settings.name = 'Non-Color'
    BAKED["sudadera"] = (None, img); print("sudadera reutilizada de", src_dir)
def bake_reuse(src_dir):
    """mismo desenvuelto que el horneado (determinista para la misma geometría) y texturas ya horneadas de otra versión"""
    _unwrap(HEAD, margin=0.006); _unwrap(BODY, margin=0.004); _unwrap(HOODIE, margin=0.006)
    def load(fn, color):
        img = bpy.data.images.load(os.path.join(src_dir, fn)); img.name = fn.replace(".png", "")
        img.colorspace_settings.name = 'sRGB' if color else 'Non-Color'; return img
    BAKED["cabeza"] = (load("cabeza_color.png", True), load("cabeza_normal.png", False))
    BAKED["cuerpo"] = (load("cuerpo_color.png", True), load("cuerpo_normal.png", False))
    BAKED["sudadera"] = (None, load("sudadera_normal.png", False))
    bake_finish(); print("texturas reutilizadas de", src_dir)
# recuento de topología
quads = tris = ngons = 0
for o in bpy.data.objects:
    if o.type == 'MESH' and not o.hide_render:
        for p in o.data.polygons:
            n = len(p.vertices); quads += n == 4; tris += n == 3; ngons += n > 4
print("BUILD v015 OK · escala %.4f · objetos %d · huesos %d · caras quad/tri/ngon %d/%d/%d" % (ESCALA, len(bpy.data.objects), len(arm_data.bones), quads, tris, ngons))
