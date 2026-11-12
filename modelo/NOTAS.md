# Cooper v015 — notas de la versión

**Fecha:** 2026-11-12 · **Parte de:** v014 · **Pedido:** Quantic, revisión de la v014: el logo del pecho tapado por el bolsillo y
los cordones, y la comparación de bocas antigua (`SOLICITUD-MODELADOR-3D.md`).

Archivos de esta versión en el repositorio `iaquantic/Cooper`:

| Archivo | Qué es |
|---|---|
| `modelo/blend/cooper_v015.blend` | Archivo de trabajo de Blender 5.2 con las texturas empaquetadas (autónomo). |
| `modelo/blend/build_v015.py` | Script que reconstruye Cooper desde cero; `bake_reuse(dir)` con las texturas de v014 (ni la piel ni la sudadera cambian). La variable de entorno `COOPER_BASE` permite indicar la carpeta de la versión fuera del PC de trabajo. |
| `modelo/web/cooper_v015.glb` | **Único `.glb`**: para web, tiempo real y animación. Escala 1, Y arriba, texturas (logos de marca incluidos), esqueleto de 55 huesos, shape keys y las 7 animaciones con las bocas. |
| `modelo/animacion/cooper_v015_rig.fbx` | Versión FBX con esqueleto, shape keys animadas, texturas incrustadas y las 7 tomas. |
| `modelo/renders/modos/` | PNG 1600 × 2000 con fondo transparente, un accesorio por modo (de frente y de tres cuartos), sin accesorios y saludando. |
| `modelo/renders/expresiones/` | Las siete expresiones, sin accesorios, con el mismo encuadre. |
| `modelo/renders/comparacion/` | Comparaciones con la hoja de personaje y `bocas_glb_fbx_vs_renders.png` (renders frente a `.glb` y `.fbx` importados), las cuatro de v015. |

Colores, logos del portátil y de la taza, geometría, brazos, animaciones, reparto de accesorios, nombres `Acc_*` y
visibilidad por modo: **iguales que en v014**. Cambian solo el sitio del logo del pecho, la costura del bolsillo y el
largo de los cordones.

## Qué cambió respecto a v014

Medidas en metros, en coordenadas de Blender (Z arriba, suelo en 0), con Cooper en reposo. En el `.glb` la Z de
Blender es la Y.

### 1. El aro sobre el logo era la costura del bolsillo, mal escalada
El «aro» que tapaba la barra violeta de la Q y el pie de las letras es la costura del bolsillo canguro
(`Costura_Bolsillo`). Tenía que seguir el borde del bolsillo al 82 % de su tamaño, pero el script la escalaba en el
eje equivocado (el 0,6 caía en la profundidad y no en la altura), así que era una elipse tan alta como ancha que
asomaba 2 cm por encima del bolsillo, flotando delante del logo, y 2 cm por debajo. Ahora sigue el bolsillo en ancho
y en alto (`scale (1.4, 0.6, 0.6)` en el script) y queda medio hundida en su cara delantera, como el resto de costuras.

| `Costura_Bolsillo` | v014 | v015 |
|---|---|---|
| Ancho | 0,184 | 0,184 (igual) |
| Alto | 0,131 (z 0,239–0,371) | **0,079** (z 0,265–0,344) |
| Borde superior frente al del bolsillo (z 0,351) | 2,0 cm por encima | 0,7 cm por debajo |

### 2. El logo sube 1,5 cm
Mismo tamaño (13,2 × 2,9 cm sobre la tela) y mismo archivo; solo cambia la altura, para dejar margen sobre el bolsillo.

| `Logo_Sudadera` | v014 | v015 |
|---|---|---|
| Altura (z) | 0,3445–0,3731 | **0,3594–0,3879** |
| Centro del plano en el script, antes de envolverlo a la tela | 0,395 | 0,4117 (`LOGO_Z`) |

Además, la textura del logo se muestrea con extensión **EXTEND** (en el `.glb`, `CLAMP_TO_EDGE`; el `.fbx` también la
conserva). El logo toca los cuatro bordes de `quantic-logo-blanco.png` y con la repetición por defecto el filtrado
traía el pie de las letras al borde superior: salían unas rayitas sobre «Quantic» (también en v014). El archivo de
marca no se toca.

### 3. Cordones más cortos
Cada cordón pierde 3,5 cm por abajo; el arranque en el cuello no se mueve y la punta sube con él.

| Cordones (`Cordon_I/D`, `Cordon_Punta_I/D`) | v014 | v015 |
|---|---|---|
| Largo de la cuerda | 0,067 (z 0,379–0,447) | **0,032** (z 0,414–0,447) |
| Punta (z) | 0,365–0,383 | **0,400–0,418** |
| En el script | `CORD_SHORTEN` no existía | `CORD_SHORTEN = 0,0394` (unidades del script, antes de escalar a 1 m) |

### 4. Márgenes del logo

| Margen | v014 | v015 |
|---|---|---|
| Logo sobre el borde del bolsillo (z 0,351) | −0,6 cm (el bolsillo llegaba más arriba que el pie del logo) | **0,9 cm** |
| Logo sobre la costura del bolsillo | −2,6 cm (la costura cruzaba el logo) | **1,5 cm** |
| Puntas de los cordones sobre el logo | −0,8 cm (las puntas pisaban el logo) | **1,2 cm** |

Comprobado de frente, de tres cuartos y en los bustos de las expresiones (renders de Blender), en el `.glb`
importado en un Blender limpio y cargado en three.js, y en el `.fbx` importado. El logo se ve entero en todas las
vistas salvo donde lo tapa la pose, igual que en v014: en **5 serio** los brazos cruzados van delante del pecho (como
en la hoja de personaje) y en **Trabajo** el portátil está delante del pecho.

### 5. Comparación de bocas al día
`modelo/renders/comparacion/bocas_glb_fbx_vs_renders.png` se regenera con la v015: las siete expresiones
renderizadas desde Blender, desde el `.glb` importado y desde el `.fbx` importado, una fila cada uno. Las bocas
coinciden en las tres filas:

| Fotograma de `Expresiones` | Shape keys | `.glb` | `.fbx` |
|---|---|---|---|
| 0 neutro | ninguna | ninguna | ninguna |
| 1 feliz | Risa 0,35 | Risa 0,35 | Risa 0,35 |
| 2 sorprendido | O 1,0 | O 1,0 | O 1,0 |
| 3 pensativo | Puchero 1,0 | Puchero 1,0 | Puchero 1,0 |
| 4 guiñando | ninguna | ninguna | ninguna |
| 5 serio | Plano 1,0 | Plano 1,0 | Plano 1,0 |
| 6 risa | Risa 1,0 | Risa 1,0 | Risa 1,0 |

Como en v013, en las filas del `.glb` y del `.fbx` los accesorios se ven, porque `Expresiones` no fija la visibilidad.

### 6. Entrega
Todos los renders regenerados (modos, expresiones y comparaciones) con la misma receta que v014 (Eevee, 32 muestras,
vista Standard, 1600 × 2000, mismas cámaras, luces y fotogramas): comparados píxel a píxel con los de v014, solo cambia
la zona del pecho. Las tres exportaciones, con los mismos ajustes que v014 (el `.glb` conserva la interpolación STEP
de la boca en `Expresiones`, de 0 a 0,25 s). Archivos binarios por Git LFS.

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
- Los cordones quedan más cortos (3,2 cm de cuerda más la punta). Si se prefieren más largos, habría que separarlos
  hacia los lados del logo o bajar el bolsillo; no se ha hecho para no cambiar nada más.

## Qué se infirió
- Igual que en versiones anteriores: toda la geometría sale de una hoja de personaje raster sin escala
  real; la altura de 1,000 m es decisión nuestra y el grosor de cada pieza se dedujo de las vistas.
- Cómo liberar el logo (corregir la costura del bolsillo, subir el logo 1,5 cm y acortar los cordones 3,5 cm) y los
  márgenes (0,9 cm sobre el bolsillo y 1,2 cm bajo los cordones) son decisión del Modelador 3D, entre las opciones
  que dio Quantic. En la hoja de personaje los cordones también acaban por encima del logo.

## Medidas (sin cambios)
Alto 1,000 m, ancho 0,80 m, fondo 0,65 m en reposo con todos los accesorios en alto; topología 27 198 quads,
388 triángulos y 63 n-gonos; 55 huesos.
