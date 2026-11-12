# Cooper v017 — notas de la versión

**Fecha:** 2026-11-12 · **Parte de:** v016 · **Pedido:** Quantic confirma que el logo oficial es el de la web publicada
(https://quantic.bequantic.org/); `personaje/marca/quantic-logo-blanco.png` pasa a ser ese archivo (ver `personaje/marca/README.md`).

Archivos de esta versión en el repositorio `iaquantic/Cooper`:

| Archivo | Qué es |
|---|---|
| `modelo/blend/cooper_v017.blend` | Archivo de trabajo de Blender 5.2 con las texturas empaquetadas (autónomo). |
| `modelo/blend/build_v017.py` | Script que reconstruye Cooper desde cero; `bake_reuse(dir)` con las texturas de v014 (ni la piel ni la sudadera cambian). Toma el logo y la taza de `TEX` (`quantic-logo-blanco.png` y `taza.png`); `taza_png()` genera la taza a partir del logo. La variable de entorno `COOPER_BASE` permite indicar la carpeta de la versión fuera del PC de trabajo. |
| `modelo/web/cooper_v017.glb` | **Único `.glb`**: para web, tiempo real y animación. Escala 1, Y arriba, texturas (logos de marca incluidos), esqueleto de 55 huesos, shape keys y las 7 animaciones con las bocas. |
| `modelo/animacion/cooper_v017_rig.fbx` | Versión FBX con esqueleto, shape keys animadas, texturas incrustadas y las 7 tomas. |
| `modelo/renders/modos/` | PNG 1600 × 2000 con fondo transparente, un accesorio por modo (de frente y de tres cuartos), sin accesorios y saludando. |
| `modelo/renders/expresiones/` | Las siete expresiones, sin accesorios, con el mismo encuadre. |
| `modelo/renders/comparacion/` | Comparaciones con la hoja de personaje y `bocas_glb_fbx_vs_renders.png` (renders frente a `.glb` y `.fbx` importados), las cuatro de v017. |

Geometría (cordones de v016 incluidos), colores, isotipo del portátil, pantallas, brazos, animaciones, reparto de
accesorios, nombres `Acc_*` y visibilidad por modo: **iguales que en v016**. Cambian solo las dos texturas que llevan el
logo completo.

## Qué cambió respecto a v016

### 1. Logo oficial de la web en el pecho
El archivo anterior (`assets/quantic-blanco.png` de la web) tenía la última «c» invertida y el modelo leía «Qucntiɔ».
El nuevo (`quantic_blanco_1`, el que usa la web publicada) es igual en tamaño (3546 × 758) y diseño salvo esa «c»,
que abre a la derecha: ahora se lee «Qucntic», como en la web.

| `Logo_Sudadera` | v016 | v017 |
|---|---|---|
| Imagen (material `Q_LogoSudadera`) | logo antiguo, «c» invertida | **logo de la web** (`personaje/marca/quantic-logo-blanco.png`, byte a byte) |
| Tamaño, sitio y extensión de la textura | 13,2 × 2,9 cm, z 0,3594–0,3879, EXTEND | igual |

### 2. Taza regenerada desde el logo nuevo
`taza.png` (1024 × 512, fondo `#15151C`) era una textura **derivada** del logo antiguo: el logo reescalado a 425 × 91 px
(Lanczos) en (365, 210). Esa receta reproduce exactamente la taza de v014–v016 a partir del logo antiguo; con el logo
nuevo da la taza de v017, que solo cambia en la última «c» (x 730–789, y 239–300 de la imagen). Queda en el script como
`taza_png()`. Mismo tamaño, sitio y colores en la taza.

### 3. Lo que se revisó y no cambia
- **Portátil:** lleva el **isotipo** (`quantic-isotipo-blanco.png`), idéntico byte a byte al de `personaje/marca/` y al
  de la web. Sin cambios.
- **Pantallas del portátil y del móvil, checklist, teclas y panel:** ninguna usa el archivo del logo ni deriva de él.
  Las pantallas del portátil y del móvil tienen una cabecera propia (aro cian y «Quantic» escrito en tipografía normal,
  que se lee bien) de cuando se hicieron las pantallas; el panel solo tiene marcos y barras. No se tocan: el pedido es
  sustituir el archivo del logo y el resto sigue como en v016. Ver Pendiente.
- Ninguna referencia al archivo antiguo: en el `.blend`, las dos imágenes empaquetadas son los archivos nuevos (y su
  ruta apunta a la carpeta `texturas` de v017); en el `.glb` y el `.fbx`, las imágenes embebidas del logo y la taza son
  idénticas píxel a píxel a las nuevas y no queda ninguna copia de las antiguas.

### 4. Comprobación
Renders comparados píxel a píxel con los de v016: solo cambia la última «c» del logo del pecho (y la de la taza en
`cooper_relax_frente.png`); en `cooper_expresion_5_serio.png` y en los dos de `cooper_trabajo_*` el logo queda detrás de
los brazos o del portátil y la imagen es la misma. Comprobado de frente, de tres cuartos, en los bustos, en el `.glb`
importado en un Blender limpio y cargado en three.js (pecho «Qucntic», taza y portátil) y en el `.fbx` importado.
Las bocas siguen coincidiendo en las tres filas de `bocas_glb_fbx_vs_renders.png` (feliz Risa 0,35 · sorprendido O 1,0 ·
pensativo Puchero 1,0 · guiñando ninguna · serio Plano 1,0 · risa Risa 1,0).

### 5. Entrega
Todos los renders regenerados (modos, expresiones y comparaciones) con la misma receta que v014–v016 (Eevee, 32 muestras,
vista Standard, 1600 × 2000, mismas cámaras, luces y fotogramas) y las tres exportaciones con los mismos ajustes (el
`.glb` conserva la interpolación STEP de la boca en `Expresiones`). Cordones, márgenes del logo y contactos en las
animaciones: los de v016 (ver el historial de este archivo). Archivos binarios por Git LFS.

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
- En `5 serio` y en `Tecleo` los brazos se hunden en la sudadera (también en v015 y v016) y pasan por encima de los
  cordones. Si se corrigiera la pose, habría que comprobar de nuevo los cordones.
- Si un proyecto muestra el portátil durante `Expresiones` (ese clip no fija la visibilidad), en `3 pensativo` el
  portátil roza el cordón izquierdo.
- Pantallas del portátil y del móvil: su cabecera es un aro cian con «Quantic» escrito, no el logo oficial. Si Quantic
  quiere el logo de la web también ahí, se cambian esas dos texturas.
- Isotipo de la tapa del portátil: la imagen toca sus bordes y la textura se repite (REPEAT), así que de cerca se ven
  rayitas finas junto a la Q (igual que pasaba en el pecho hasta v015). Se arregla poniendo la extensión EXTEND en
  `Q_LogoLaptop`, como en el pecho; no se ha hecho porque el pedido era no cambiar nada más.

## Qué se infirió
- Igual que en versiones anteriores: toda la geometría sale de una hoja de personaje raster sin escala
  real; la altura de 1,000 m es decisión nuestra y el grosor de cada pieza se dedujo de las vistas.
- La receta de la taza (425 × 91 px en (365, 210), Lanczos) se dedujo de la taza de v016: reproducirla con el logo
  antiguo da la misma imagen, píxel a píxel.

## Medidas (sin cambios)
Alto 1,000 m, ancho 0,80 m, fondo 0,65 m en reposo con todos los accesorios en alto; topología 27 870 quads,
420 triángulos y 59 n-gonos; 55 huesos.
