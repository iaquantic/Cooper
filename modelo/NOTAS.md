# Cooper v014 — notas de la versión

**Fecha:** 2026-11-10 · **Parte de:** v013 (aprobada) · **Pedido:** Quantic, colores oficiales de marca y logo oficial
(`SOLICITUD-MODELADOR-3D.md`; colores y logos en `personaje/marca/`).

Archivos de esta versión en el repositorio `iaquantic/Cooper`:

| Archivo | Qué es |
|---|---|
| `modelo/blend/cooper_v014.blend` | Archivo de trabajo de Blender 5.2 con las texturas empaquetadas (autónomo). |
| `modelo/blend/build_v014.py` | Script que reconstruye Cooper desde cero; `reuse_hoodie(dir)` + `bake_head()` + `bake_body()` + `bake_finish()` hornean la piel con los colores nuevos. |
| `modelo/web/cooper_v014.glb` | **Único `.glb`**: para web, tiempo real y animación. Escala 1, Y arriba, texturas (logos de marca incluidos), esqueleto de 55 huesos, shape keys y las 7 animaciones con las bocas. |
| `modelo/animacion/cooper_v014_rig.fbx` | Versión FBX con esqueleto, shape keys animadas, texturas incrustadas y las 7 tomas. |
| `modelo/renders/modos/` | PNG 1600 × 2000 con fondo transparente, un accesorio por modo (de frente y de tres cuartos), sin accesorios y saludando. |
| `modelo/renders/expresiones/` | Las siete expresiones, sin accesorios, con el mismo encuadre. |
| `modelo/renders/comparacion/` | Comparaciones con la hoja de personaje y `bocas_glb_fbx_vs_renders.png` (de v013, sin cambios en las bocas). |

Geometría, brazos, animaciones, reparto de accesorios, nombres `Acc_*`, visibilidad por modo, pantallas, ventosas, ojos,
gafas, sudadera, bombilla y boca: **iguales que en v013**. Cambian los colores de la piel y los tres logos.

## Qué cambió respecto a v013

### 1. Violeta de marca en cuerpo, cabeza y tentáculos
Decisión de Quantic, con los hex del manual de marca (`personaje/marca/README.md`):

| Elemento | v013 | v014 | Motivo |
|---|---|---|---|
| Cuerpo, cabeza y tentáculos | `#5B2BE0` | **`#8070E7`** | violeta oficial de Quantic |
| Manchas de la cabeza | `#3A1A9E` | **`#564CA3`** | el mismo salto de tono aplicado al violeta nuevo, tal como propuso Quantic |
| Iris | `#3B1E9C` | **`#564EA1`** | ídem |

Se dejaron los hex propuestos sin retocar: con la iluminación de los renders las manchas siguen distinguiéndose
(más suaves que antes, porque el violeta nuevo es más claro y el contraste relativo es el mismo) y el iris se lee
bien dentro del blanco del ojo. Las texturas de **cabeza y cuerpo se hornearon de nuevo** (color y normales
2048²); las normales de la sudadera se reutilizan (`reuse_hoodie`). Ventosas, boca, bombilla, pantallas: sin cambio.

### 2. Logo oficial en la sudadera, el portátil y la taza
Los archivos de `personaje/marca/` se usan tal cual, como texturas con transparencia (aro y letras blancos
`#FFFFFF`, barra diagonal `#8070E7`):

| Dónde | Archivo | Cómo | Tamaño y sitio |
|---|---|---|---|
| Pecho de la sudadera | `quantic-logo-blanco.png` | objeto `Logo_Sudadera`: rejilla con la textura, envuelta a la sudadera con Shrinkwrap (5 mm por delante de la tela), material mate | mismo ancho que el logo anterior (16 cm); **1 cm más alto** (centro a 0,395 m en vez de 0,385), porque el logo anterior era geometría que flotaba delante del bolsillo y una textura pegada a la tela quedaba tapada por el bolsillo y su costura |
| Tapa del portátil | `quantic-isotipo-blanco.png` | objeto `Laptop_LogoQ`: plano con la textura en la cara trasera de la tapa | mismo sitio y diámetro (5 cm) que el aro anterior |
| Taza | `quantic-logo-blanco.png` | textura `taza.png` regenerada (1024 × 512, fondo `#15151C`): el logo ocupa la misma franja que el «Q Quantic» anterior (425 px de ancho, centrado al frente) | igual que antes |

El logo anterior (aro cian con «Quantic», objetos `Logo_Anillo`, `Logo_Q_Cola` y `Logo_Texto`, y el aro
`Laptop_LogoQ` cian) desaparece. El cian `#22D3EE` queda solo en las pantallas, por decisión de Quantic.
En los renders de frente y de busto el logo del pecho se lee entero («Quantic» con la Q de barra violeta).

### 3. Lo que no cambia
Pantallas del portátil, del móvil y del panel (azul `#1A6FFF` y cian `#22D3EE`), ventosas, ojos, gafas, sudadera,
bombilla, boca, geometría, brazos, animaciones, nombres `Acc_*` y visibilidad por modo.

### 4. Entrega
Todos los renders regenerados (modos, expresiones y comparaciones) y las tres exportaciones. `personaje/FICHA.md`
con la tabla de colores nueva y sin el pendiente de confirmar los hex. Archivos binarios por Git LFS.

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

**Para quien use el `.blend`:** las tiras van en serie en la línea de tiempo (`CLIP_START`: Expresiones 0, Idle 100,
Saludo 200, Idea 300, Tecleo 400, Relax 500, Organizar 600). Para posar o renderizar un clip, `solo(nombre)` +
`sc.frame_set(clip_frame(nombre, f))`, o `goto(nombre, f)` con todas las pistas activas.

## Pendiente
- El estado de la bombilla (`Luz` / `LuzOff`) solo lo cambia `Idea`; en reposo está encendida.
- Las mangas nacen dentro del cuerpo de la sudadera; si un brazo se lleva muy atrás por código, la manga
  puede asomar por la espalda. Los clips entregados no lo hacen.

## Qué se infirió
- Igual que en versiones anteriores: toda la geometría sale de una hoja de personaje raster sin escala
  real; la altura de 1,000 m es decisión nuestra y el grosor de cada pieza se dedujo de las vistas.
- Los hex de manchas e iris son los que propuso Quantic (mismo salto de tono); el Modelador 3D comprobó en
  los renders que se distinguen y no los retocó.
- Que el logo del pecho suba 1 cm es decisión del Modelador 3D para que la textura no quede tapada por el
  bolsillo; el ancho se mantiene.

## Medidas (sin cambios)
Alto 1,000 m, ancho 0,80 m, fondo 0,65 m en reposo con todos los accesorios en alto; topología 27 198 quads,
388 triángulos y 63 n-gonos (menos que en v013 porque el logo del pecho ya no es geometría); 55 huesos.
