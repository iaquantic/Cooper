# Cooper v012 — notas de la versión

**Fecha:** 2026-11-06 · **Parte de:** v011 (aprobada: brazos por las mangas, encuadre, tentáculos relajados y
`.glb` único) · **Pedido:** Quantic, dos arreglos de alcance de los brazos (`SOLICITUD-MODELADOR-3D.md`).

Archivos de esta versión en el repositorio `iaquantic/Cooper`:

| Archivo | Qué es |
|---|---|
| `modelo/blend/cooper_v012.blend` | Archivo de trabajo de Blender 5.2 con las texturas empaquetadas (autónomo). |
| `modelo/blend/build_v012.py` | Script que reconstruye Cooper desde cero; `bake_reuse(dir)` carga las texturas ya horneadas (las de v011, sin cambios). |
| `modelo/web/cooper_v012.glb` | **Único `.glb`**: para web, tiempo real y animación. Escala 1, Y arriba, texturas, esqueleto de 55 huesos, shape keys y las 7 animaciones. |
| `modelo/animacion/cooper_v012_rig.fbx` | Versión FBX con esqueleto, shape keys, texturas incrustadas y las 7 animaciones. |
| `modelo/renders/modos/` | PNG 1600 × 2000 con fondo transparente, un accesorio por modo (de frente y de tres cuartos), sin accesorios y saludando. |
| `modelo/renders/expresiones/` | Las siete expresiones, sin accesorios, con el mismo encuadre. |
| `modelo/renders/comparacion/` | Comparaciones con la hoja de personaje (frente, modos y expresiones). |

Colores, proporciones, rasgos, mangas y brazos, reparto de accesorios, nombres `Acc_*`, visibilidad por modo y
texturas: **iguales que en v011** (ver la nota de v011 para el reparto y lo que hace cada brazo en cada clip;
se reproduce abajo). Solo cambian dos poses.

## Qué cambió respecto a v011

### 1. La taza llega a la boca en `Relax`
En v011 el sorbo se quedaba a la altura del pecho: el objetivo del brazo era un punto fijo delante de los labios
calculado para el tentáculo de v010, y la taza, que cuelga de la mano, quedaba además tumbada hacia un lado.
Ahora el script **resuelve el objetivo midiendo la taza ya colocada** (`solve_sip()`): gira el hueso `Acc_Taza`
para que la taza quede casi vertical e inclinada hacia la boca, y mueve el control IK de la mano derecha hasta
que el centro del borde de la taza queda 3,6 cm delante de los labios, de modo que el borde trasero los toca.
La cabeza se inclina 5° hacia la taza (`HEAD_SIP`). El brazo se dobla más; el hombro no se ha movido.

Medido en el sorbo (fotograma 30, coordenadas de Blender, Z arriba): labios en (0,00, −0,155, 0,471) m, centro del
borde de la taza en (−0,004, −0,192, 0,461) m: 3,7 cm por delante y 1 cm por debajo de los labios, con el borde
de la taza (radio 3,5 cm) tocándolos. **Comprobado también en el `.glb` exportado**: importado en un Blender
limpio, con la pista `Relax` en el fotograma 30, el borde queda a 3,8 cm de los labios, igual que en el archivo
de trabajo (la tira importada empieza en el fotograma 1, así que el fotograma glTF 30 es el 31 de Blender).

### 2. La mano toca la barbilla en `3 pensativo`
En v011 la punta del brazo izquierdo quedaba a (−0,06, −0,235, 0,46) m, separada de la cara. Ahora el punto se
calcula **sobre la superficie de la cabeza** (`chin_point()`): intersección de la dirección "abajo y adelante" con
el elipsoide de la cabeza ya girada 8°, más 1,4 cm de radio de la mano, de modo que la punta se apoya bajo la
barbilla como en la hoja. El brazo se dobla hacia dentro; la sudadera y la manga se arrugan en el codo.

Renders regenerados: `cooper_relax_frente.png`, `cooper_relax_tres_cuartos.png`,
`cooper_expresion_3_pensativo.png` y las tres comparaciones (el resto de renders se volvieron a generar con el
mismo resultado). Exportaciones regeneradas: `.blend`, `.glb` y `.fbx`.

## Reparto de accesorios y brazos (sin cambios desde v011)

| Accesorio | Nodo / hueso | Quién lo sostiene | Sube en |
|---|---|---|---|
| Bombilla | `Acc_Bombilla` | T1, tentáculo de abajo trasero izquierdo | `Idea` |
| Portátil | `Acc_Laptop` | T2, brazo izquierdo (delante del pecho, a su izquierda) | `Tecleo` |
| Móvil | `Acc_Movil` | T3, tentáculo de abajo delantero izquierdo | ningún clip (se muestra solo por código) |
| Taza | `Acc_Taza` | T7, brazo derecho | `Relax` |
| Checklist | `Acc_Checklist` | T6, tentáculo de abajo delantero derecho | `Organizar` |
| Panel de datos | `Acc_Panel` | flota junto a la cabeza (hueso `Panel`) | `Organizar` |

| Clip | Brazo izquierdo (T2) | Brazo derecho (T7) |
|---|---|---|
| `Expresiones` | cuelga; en **3 pensativo** la punta se apoya bajo la barbilla | cuelga; en **5 serio** los dos brazos se cruzan sobre el pecho |
| `Idle` | cuelga con balanceo suave | cuelga con balanceo suave |
| `Saludo` | cuelga | se levanta y saluda |
| `Idea` | se abre un poco con la sorpresa y vuelve | igual; la bombilla la sube T1 |
| `Tecleo` | sube el portátil delante del pecho y lo baja al final | teclea en la mitad derecha del teclado |
| `Relax` | cuelga | **sube la taza hasta que el borde toca los labios**, sorbo, la baja |
| `Organizar` | cuelga | marca la tarea en la checklist que sube T6 |

Mientras un accesorio no se usa, su tentáculo descansa (los de abajo en el suelo; los brazos cuelgan a los
lados con la mano asomando por el puño) y solo sube en su clip de modo.

## Visibilidad por modo (sin cambios)
`Idea` → `Acc_Bombilla` · `Tecleo` → `Acc_Laptop` · `Relax` → `Acc_Taza` · `Organizar` → `Acc_Checklist` y
`Acc_Panel` · `Saludo` → ninguno. `Expresiones` e `Idle` no tocan la visibilidad. `Acc_Movil` solo por código.

## Pendiente
- Revisión de Quantic: en `3 pensativo` la mano sigue sin tocar la cara. Queda a la altura del cuello de la
  sudadera, por debajo y por delante de la boca, tanto en el render como en el `.glb`. En la hoja la punta
  del tentáculo se apoya en la cara, justo debajo de la boca.
- Revisión de Quantic: en el `.glb`, la animación `Expresiones` no lleva las bocas. El canal `Boca.weights`
  tiene dos claves en 0 (de 0 a 3 s), así que sorprendido, pensativo y serio salen con la boca por defecto
  (sonrisa abierta), a diferencia de los renders. Además, ese canal hace que el clip dure 3 s en vez de 0,25 s.
- Confirmar los hex oficiales con la guía de marca de Quantic y, si difieren, rehornear las texturas.
- El estado de la bombilla (`Luz` / `LuzOff`) solo lo cambia `Idea`; en reposo está encendida.
- Las mangas nacen dentro del cuerpo de la sudadera; si un brazo se lleva muy atrás por código, la manga
  puede asomar por la espalda. Los clips entregados no lo hacen.

## Qué se infirió
- Igual que en versiones anteriores: toda la geometría sale de una hoja de personaje raster sin escala
  real; la altura de 1,000 m es decisión nuestra y el grosor de cada pieza se dedujo de las vistas.
- Mangas, brazos, reparto de accesorios y lo que hacen los brazos en cada clip: propuesta del Modelador 3D
  sobre el pedido de Quantic (v011).
- Cuánto se inclina la taza (unos 25°) y la cabeza (5°) en el sorbo, y por dónde se apoya la mano en la
  barbilla, son decisiones de pose del Modelador 3D; el pedido solo fija que el borde toque la boca y que la
  mano toque la barbilla.

## Medidas (sin cambios)
Alto 1,000 m, ancho 0,80 m, fondo 0,65 m en reposo con todos los accesorios en alto; topología 28 446 quads,
1 604 triángulos y 63 n-gonos; 55 huesos.
