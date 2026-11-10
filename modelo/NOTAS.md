# Cooper v013 — notas de la versión

**Fecha:** 2026-11-10 · **Parte de:** v012 (taza de Relax aprobada) · **Pedido:** Quantic, dos arreglos
(`SOLICITUD-MODELADOR-3D.md`): la mano en la cara en `3 pensativo` y las bocas de `Expresiones` en el `.glb` y el `.fbx`.

Archivos de esta versión en el repositorio `iaquantic/Cooper`:

| Archivo | Qué es |
|---|---|
| `modelo/blend/cooper_v013.blend` | Archivo de trabajo de Blender 5.2 con las texturas empaquetadas (autónomo). |
| `modelo/blend/build_v013.py` | Script que reconstruye Cooper desde cero; `bake_reuse(dir)` carga las texturas ya horneadas (las de v011, sin cambios). |
| `modelo/web/cooper_v013.glb` | **Único `.glb`**: para web, tiempo real y animación. Escala 1, Y arriba, texturas, esqueleto de 55 huesos, shape keys y las 7 animaciones **con las bocas**. |
| `modelo/animacion/cooper_v013_rig.fbx` | Versión FBX con esqueleto, shape keys animadas, texturas incrustadas y las 7 tomas. |
| `modelo/renders/modos/` | PNG 1600 × 2000 con fondo transparente, un accesorio por modo (de frente y de tres cuartos), sin accesorios y saludando. |
| `modelo/renders/expresiones/` | Las siete expresiones, sin accesorios, con el mismo encuadre. |
| `modelo/renders/comparacion/` | Comparaciones con la hoja de personaje y `bocas_glb_fbx_vs_renders.png` (renders frente a `.glb` y `.fbx` importados). |

Colores, proporciones, rasgos, mangas y brazos, reparto de accesorios, nombres `Acc_*`, visibilidad por modo y
texturas: **iguales que en v012**. Cambian una pose y la forma de exportar las bocas.

## Qué cambió respecto a v012

### 1. La mano toca la cara en `3 pensativo`
El punto "bajo la barbilla" de v012 caía dentro del cuello de la sudadera. Ahora la punta del brazo izquierdo se
apoya en la **parte delantera de la cara, justo debajo de la boca y a la izquierda** (`FACE_DIR` sobre el elipsoide
de la cabeza, más 1,2 cm de radio de la mano), y el tentáculo sube **curvado hacia arriba** desde la manga: antes de
resolver el IK se da una pose inicial a los dos primeros huesos del brazo (`ARM_BIAS_1/2`) que lleva el codo abajo,
y el solucionador parte de ahí. Medido: punta en (−0,057, −0,149, 0,457) m con la boca en (−0,004, −0,151, 0,484)
m: 5,3 cm a la izquierda y 2,7 cm por debajo de la boca, sobre la piel. Comprobado de frente, de tres cuartos y de
perfil; la boca (puchero) queda libre.

### 2. Las bocas de `Expresiones` en el `.glb` y el `.fbx`
Dos causas, las dos en el script:
- La acción `Expresiones_Boca` arrastraba las claves de boca de `Idle` (todas en 0, hasta el fotograma 72): por
  eso el clip duraba 3 s. Ahora `Idle` tiene su propia `Idle_Boca` y `Expresiones_Boca` va de 0 a 6.
- Al exportar, las pistas NLA de las shape keys estaban silenciadas (el estado en que las deja `solo()` para
  renderizar), y el exportador glTF las hornea con sus ceros. Ahora el estado de entrega es **todas las pistas
  activas** (`unmute_all()`), y para que no se pisen **cada clip ocupa su propio rango de fotogramas** de la escena
  (`CLIP_START`: Expresiones 0, Idle 100, Saludo 200, Idea 300, Tecleo 400, Relax 500, Organizar 600; tiras con
  extrapolación "nada"). Así también el exportador FBX, que hornea la escena tira a tira, saca la boca correcta
  de cada toma. En el `.glb` cada animación empieza en 0 s (`export_anim_slide_to_zero`).
- El canal de pesos de `Expresiones` en el `.glb` se escribe con interpolación **STEP** (el exportador siempre
  pone LINEAR en shape keys; se corrige en el posproceso del archivo), 7 claves de 0 a 0,25 s, como los huesos.

Comprobación, importando los archivos exportados en un Blender limpio (`glbcheck/check_bocas.py`):

| Fotograma de `Expresiones` | Shape keys esperadas | `.glb` | `.fbx` |
|---|---|---|---|
| 0 neutro | ninguna | ninguna | ninguna |
| 1 feliz | Risa 0,35 | Risa 0,35 | Risa 0,35 |
| 2 sorprendido | O 1,0 | O 1,0 | O 1,0 |
| 3 pensativo | Puchero 1,0 | Puchero 1,0 | Puchero 1,0 |
| 4 guiñando | ninguna | ninguna | ninguna |
| 5 serio | Plano 1,0 | Plano 1,0 | Plano 1,0 |
| 6 risa | Risa 1,0 | Risa 1,0 | Risa 1,0 |

Duración de `Expresiones` en el `.glb`: 0,000–0,250 s (ningún canal más largo). El resto de clips también lleva su
boca: `Saludo` f24 Risa 0,30 · `Idea` f36 Risa 0,35 · `Tecleo` f24 ninguna · `Relax` f30 O 0,5 · `Organizar` f32
Risa 0,35 · `Idle` ninguna, iguales en `.glb` y `.fbx` que en Blender. La hoja
`modelo/renders/comparacion/bocas_glb_fbx_vs_renders.png` pone las siete expresiones renderizadas desde Blender,
desde el `.glb` importado y desde el `.fbx` importado, una fila cada uno.

**Para quien use el `.blend`:** las tiras van en serie en la línea de tiempo (ver `CLIP_START`). Para posar o
renderizar un clip, `solo(nombre)` + `sc.frame_set(clip_frame(nombre, f))`, o `goto(nombre, f)` con todas las
pistas activas. Con todas activas, fuera del rango de los clips de modo los huesos `Acc_*` vuelven a su valor por
defecto (visibles): es lo esperado en `Expresiones` e `Idle`, que no fijan la visibilidad.

Renders regenerados: `cooper_expresion_3_pensativo.png`, la comparación de expresiones (y las otras dos
comparaciones, por el rótulo de versión). El resto de renders no cambia. Exportaciones regeneradas: `.blend`,
`.glb` y `.fbx`.

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
| `Expresiones` | cuelga; en **3 pensativo** sube curvado y la punta se apoya en la cara, bajo la boca y a la izquierda | cuelga; en **5 serio** los dos brazos se cruzan sobre el pecho |
| `Idle` | cuelga con balanceo suave | cuelga con balanceo suave |
| `Saludo` | cuelga | se levanta y saluda |
| `Idea` | se abre un poco con la sorpresa y vuelve | igual; la bombilla la sube T1 |
| `Tecleo` | sube el portátil delante del pecho y lo baja al final | teclea en la mitad derecha del teclado |
| `Relax` | cuelga | sube la taza hasta que el borde toca los labios, sorbo, la baja |
| `Organizar` | cuelga | marca la tarea en la checklist que sube T6 |

## Visibilidad por modo (sin cambios)
`Idea` → `Acc_Bombilla` · `Tecleo` → `Acc_Laptop` · `Relax` → `Acc_Taza` · `Organizar` → `Acc_Checklist` y
`Acc_Panel` · `Saludo` → ninguno. `Expresiones` e `Idle` no tocan la visibilidad. `Acc_Movil` solo por código.

## Pendiente
- Confirmar los hex oficiales con la guía de marca de Quantic y, si difieren, rehornear las texturas.
- El estado de la bombilla (`Luz` / `LuzOff`) solo lo cambia `Idea`; en reposo está encendida.
- Las mangas nacen dentro del cuerpo de la sudadera; si un brazo se lleva muy atrás por código, la manga
  puede asomar por la espalda. Los clips entregados no lo hacen.

## Qué se infirió
- Igual que en versiones anteriores: toda la geometría sale de una hoja de personaje raster sin escala
  real; la altura de 1,000 m es decisión nuestra y el grosor de cada pieza se dedujo de las vistas.
- El punto exacto de apoyo de la mano en la cara (5 cm a la izquierda y 3 cm bajo la boca) y la curva del brazo
  son decisiones de pose del Modelador 3D; el pedido fija que toque la cara bajo la boca, a la izquierda, con el
  tentáculo curvado hacia arriba y sin tapar la boca.
- Los rangos de fotogramas por clip (de 100 en 100) son una convención del archivo de trabajo; los exportados
  empiezan todos en 0.

## Medidas (sin cambios)
Alto 1,000 m, ancho 0,80 m, fondo 0,65 m en reposo con todos los accesorios en alto; topología 28 446 quads,
1 604 triángulos y 63 n-gonos; 55 huesos.
