# Cooper v018 — notas de la versión

**Fecha:** 2026-11-12 · **Parte de:** v017 · **Pedido:** Quantic aprueba los dos pendientes de la v017: el logo oficial en
las pantallas del portátil y del móvil, y quitar las rayitas junto a la Q de la tapa del portátil.

Archivos de esta versión en el repositorio `iaquantic/Cooper`:

| Archivo | Qué es |
|---|---|
| `modelo/blend/cooper_v018.blend` | Archivo de trabajo de Blender 5.2 con las texturas empaquetadas (autónomo). |
| `modelo/blend/build_v018.py` | Script que reconstruye Cooper desde cero; `bake_reuse(dir)` con las texturas de v014 (ni la piel ni la sudadera cambian). Toma de `TEX` el logo, el isotipo, la taza y las dos pantallas; `taza_png()`, `pantalla_laptop_png()` y `pantalla_movil_png()` generan las texturas derivadas del logo. La variable de entorno `COOPER_BASE` permite indicar la carpeta de la versión fuera del PC de trabajo. |
| `modelo/web/cooper_v018.glb` | **Único `.glb`**: para web, tiempo real y animación. Escala 1, Y arriba, texturas (logos de marca incluidos), esqueleto de 55 huesos, shape keys y las 7 animaciones con las bocas. |
| `modelo/animacion/cooper_v018_rig.fbx` | Versión FBX con esqueleto, shape keys animadas, texturas incrustadas y las 7 tomas. |
| `modelo/renders/modos/` | PNG 1600 × 2000 con fondo transparente. De v018: `cooper_trabajo_frente.png` y `cooper_trabajo_tres_cuartos.png` (los únicos donde se ve el portátil); el resto, de v017 (ver punto 4). |
| `modelo/renders/expresiones/` | Las siete expresiones, de v017 (sin accesorios: no cambian). |
| `modelo/renders/comparacion/` | Las cuatro comparaciones y `bocas_glb_fbx_vs_renders.png`, de v018. |

Geometría, colores, logo del pecho, taza, cordones, brazos, animaciones, reparto de accesorios, nombres `Acc_*` y
visibilidad por modo: **iguales que en v017**. Cambian la cabecera de las dos pantallas y la extensión de tres texturas.

## Qué cambió respecto a v017

### 1. Logo oficial en las pantallas del portátil y del móvil
La cabecera de las dos pantallas era un aro cian con «Quantic» en tipografía normal (de cuando se hicieron las
pantallas, antes de tener el logo oficial). Ahora lleva el **logo oficial de la web**, `personaje/marca/quantic-logo-blanco.png`
tal cual (aro y letras blancos, barra `#8070E7`; solo se reescala, con Lanczos y alfa premultiplicado para que no salgan
halos), sobre el mismo fondo azul marino `#182036` de la cabecera: blanco sobre azul oscuro, buen contraste. El logo
completo se lee bien en los dos sitios, así que no hizo falta el isotipo. El resto de cada pantalla (gráfico, cifras,
tarjetas, puntos cian, «Panel de control») no cambia.

| Pantalla | v017 | v018 |
|---|---|---|
| Portátil (`pantalla_laptop.png`, 768 × 480) | aro cian + «Quantic» en x 22–170, y 14–42 de la barra superior | **logo oficial 131 × 28 px en (22, 14)** |
| Móvil (`pantalla_movil.png`, 384 × 768) | aro cian (x 44–104) + «Quantic» (x 122–247) en la tarjeta de cabecera, «Asistente» debajo del texto en (122, 144) | **logo oficial 200 × 43 px en (44, 90)**; «Asistente» se mueve debajo del logo, alineado con él, a (44, 142) |

Las recetas quedan en `build_v018.py` (`pantalla_laptop_png()` y `pantalla_movil_png()`, como `taza_png()`): parten de las
pantallas de v014–v017 y del logo oficial, y dan exactamente las texturas empaquetadas.

Se revisaron las demás piezas: ninguna otra lleva el «Quantic» antiguo ni el aro cian como marca. Los puntos cian de
las tarjetas del móvil y los marcos y barras cian del panel de datos son elementos de interfaz, no la marca, y se quedan.
La checklist y las teclas no llevan logo.

### 2. Sin rayitas junto a la Q de la tapa (y en las pantallas)
El isotipo de la tapa toca los bordes de su imagen y la textura se repetía (REPEAT): de cerca se veían una raya sobre la
Q y una línea a su derecha. Ahora `Q_LogoLaptop` se muestrea con extensión **EXTEND** (en el `.glb`, `CLAMP_TO_EDGE`),
como el logo del pecho desde v015. Por el mismo motivo pasan a EXTEND las dos pantallas (`Q_PantallaLaptop` y
`Q_PantallaMovil`), que no se repiten: así sus bordes tampoco arrastran el lado contrario de la imagen. La taza se queda en
REPEAT a propósito: su textura da la vuelta al cilindro y el logo queda lejos de los bordes. Estado final de las texturas
con logo o isotipo: pecho, tapa del portátil y pantallas en EXTEND; taza en REPEAT.

### 3. Comprobación
- **De cerca** (cámaras ortográficas frente a cada pieza, mismas para v017 y v018): pantalla del portátil en reposo y en
  `Tecleo`, pantalla del móvil e isotipo de la tapa. El logo se lee «Qucntic», y en la tapa ya no hay rayas.
- **`.blend`, `.glb` y `.fbx`:** las dos pantallas embebidas son idénticas píxel a píxel a las nuevas, y en el `.glb` el
  isotipo y las pantallas llevan `CLAMP_TO_EDGE`. El logo, el isotipo y la taza siguen siendo los de v017. Las rutas de
  las dos pantallas en el `.blend` apuntan a la carpeta `texturas` de v018.
- **three.js:** el `.glb` cargado muestra el logo oficial en las dos pantallas (reposo y `Tecleo`).
- **Bocas:** siguen coincidiendo en las tres filas de `bocas_glb_fbx_vs_renders.png`. El `.fbx` importado tiene la misma
  estructura que el de v017.

### 4. Renders
Se regeneraron todos con la misma receta (Eevee, 32 muestras, Standard, 1600 × 2000). Solo cambian los de `Trabajo`
(el portátil) y el reposo con todos los accesorios de `comparacion_frente.png` (portátil y móvil). Los otros 16 de
`modos/` y `expresiones/` salen idénticos píxel a píxel a los de v017 (diferencia máxima 0/255), así que se dejan los de
v017. Las cuatro comparaciones se rehacen con el rótulo de v018.

### 5. Texturas en la carpeta de la versión
El `.blend` es autónomo, pero `build_v018.py` lee las texturas de `BASE/texturas`. En el PC del Modelador esa carpeta
(`proyectos/mascota-quantic/v018/texturas`, y la de v017) no existe todavía, porque esta sesión no escribe en el repositorio del
Modelador. Para ejecutar el build allí hay que crearla: las de v014 más `quantic-logo-blanco.png` (de `personaje/marca/`),
`taza.png`, `pantalla_laptop.png` y `pantalla_movil.png`. Las tres últimas se generan con `taza_png()`,
`pantalla_laptop_png()` y `pantalla_movil_png()` o se extraen del `.blend`.

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
- En `5 serio` y en `Tecleo` los brazos se hunden en la sudadera (también en v015–v017) y pasan por encima de los
  cordones. Si se corrigiera la pose, habría que comprobar de nuevo los cordones.
- Si un proyecto muestra el portátil durante `Expresiones` (ese clip no fija la visibilidad), en `3 pensativo` el
  portátil roza el cordón izquierdo.
- Carpeta `texturas` de v018 en el PC del Modelador: ver el punto 5.

## Qué se infirió
- Igual que en versiones anteriores: toda la geometría sale de una hoja de personaje raster sin escala
  real; la altura de 1,000 m es decisión nuestra y el grosor de cada pieza se dedujo de las vistas.
- El tamaño y la posición del logo en cada pantalla, y mover «Asistente» bajo el logo en el móvil, son decisión del
  Modelador 3D: el logo ocupa el sitio de la cabecera antigua, con la misma altura que el aro en el portátil.

## Medidas (sin cambios)
Alto 1,000 m, ancho 0,80 m, fondo 0,65 m en reposo con todos los accesorios en alto; topología 27 870 quads,
420 triángulos y 59 n-gonos; 55 huesos.
