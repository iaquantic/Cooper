# Cooper v016 — notas de la versión

**Fecha:** 2026-11-12 · **Parte de:** v015 · **Pedido:** Quantic, «alarga los cordones separándolos hacia los lados del logo».

Archivos de esta versión en el repositorio `iaquantic/Cooper`:

| Archivo | Qué es |
|---|---|
| `modelo/blend/cooper_v016.blend` | Archivo de trabajo de Blender 5.2 con las texturas empaquetadas (autónomo). |
| `modelo/blend/build_v016.py` | Script que reconstruye Cooper desde cero; `bake_reuse(dir)` con las texturas de v014 (ni la piel ni la sudadera cambian). La variable de entorno `COOPER_BASE` permite indicar la carpeta de la versión fuera del PC de trabajo. |
| `modelo/web/cooper_v016.glb` | **Único `.glb`**: para web, tiempo real y animación. Escala 1, Y arriba, texturas (logos de marca incluidos), esqueleto de 55 huesos, shape keys y las 7 animaciones con las bocas. |
| `modelo/animacion/cooper_v016_rig.fbx` | Versión FBX con esqueleto, shape keys animadas, texturas incrustadas y las 7 tomas. |
| `modelo/renders/modos/` | PNG 1600 × 2000 con fondo transparente, un accesorio por modo (de frente y de tres cuartos), sin accesorios y saludando. |
| `modelo/renders/expresiones/` | Las siete expresiones, sin accesorios, con el mismo encuadre. |
| `modelo/renders/comparacion/` | Comparaciones con la hoja de personaje y `bocas_glb_fbx_vs_renders.png` (renders frente a `.glb` y `.fbx` importados), las cuatro de v016. |

Colores, logos, logo del pecho y bolsillo (sitio y tamaño de v015), resto de la geometría, brazos, animaciones, reparto de
accesorios, nombres `Acc_*` y visibilidad por modo: **iguales que en v015**. Cambian solo los cordones.

## Qué cambió respecto a v015

Medidas en metros, en coordenadas de Blender (Z arriba, suelo en 0), con Cooper en reposo. En el `.glb` la Z de
Blender es la Y.

### 1. Cordones más largos que caen por los lados del logo
En v015 cada cordón era un cilindro recto y corto, inclinado, que flotaba 2,5 cm por delante del cuello. Ahora es un
tubo que **sale de debajo del ribete del cuello**, se apoya en la tela (con 1,2 mm de holgura) y baja abriéndose hacia
fuera hasta caer por el lado del logo, casi en vertical al final; la punta sigue la dirección de la cuerda. Los dos son
simétricos. Mismo grosor (cuerda Ø 1,1 cm, punta Ø 1,3 cm y 1,6 cm de largo) y mismo material que antes.

| Cordones (`Cordon_I/D`, `Cordon_Punta_I/D`) | v015 | v016 |
|---|---|---|
| Forma | cilindro recto, flotando delante del cuello | tubo que sale del ribete del cuello y sigue la tela |
| Largo de la cuerda | 0,032 | **0,084** (0,064 a la vista bajo el ribete; v014: 0,067) |
| Arranque en el cuello (x) | ±0,0405 | **±0,050** (bajo el ribete, z 0,449) |
| Cuerda (x / z) | ±0,035…±0,046 / 0,414–0,447 | **±0,045…±0,099 / 0,393–0,454** (por encima de z 0,436 va bajo el ribete) |
| Punta (x / z) | ±0,034…±0,047 / 0,400–0,418 | **±0,087…±0,104 / 0,380–0,399** |
| Inclinación de la punta | 8,6° hacia delante | 12° hacia fuera y 12° hacia delante, siguiendo la cuerda |

Las puntas acaban por encima de z 0,380 a propósito: en `Tecleo` el portátil sube pegado al pecho izquierdo y su borde
trasero barre la tela hasta z 0,376. Con la punta más abajo, el portátil la atravesaba al subir y al bajar (fotogramas
8–10 y 42). Por eso el cordón no es más largo.

### 2. Márgenes

| Margen (vista frontal) | v015 | v016 |
|---|---|---|
| Cuerda al logo | 2,6 cm (por encima) | **2,0 cm** (izquierda) · 2,7 cm (derecha) |
| Punta al logo | 1,2 cm (por encima) | **2,1 cm** en horizontal (izquierda) · 2,8 cm (derecha) |
| Punta al bolsillo (distancia mínima) | 5,3 cm | **4,6 cm** |
| Punta a la costura del bolsillo | 5,9 cm | **5,9 cm** |

El logo no es simétrico respecto al centro del cuerpo (x −0,0693 a +0,0622) y los cordones sí, por eso el margen
izquierdo es el menor. Logo y bolsillo no se mueven respecto a v015.

### 3. Contacto con la tela, los brazos y los accesorios
- **Sudadera:** por debajo del ribete, cuerda y punta quedan a 1,2 mm de la tela (y a 1,0 mm del ribete) en todo el
  recorrido; por encima de z 0,436 la cuerda entra bajo el ribete, que es por donde sale. (En v015 las puntas se
  hundían 1,2 mm en la tela.)
- **Animaciones** (comprobado fotograma a fotograma en el `.blend` y en el `.glb` y el `.fbx` importados): distancia
  mínima de los cordones a brazos y mangas en `Idle` 5,0 cm, `Saludo` 3,1 cm, `Idea` 5,1 cm, `Relax` 0,7 cm y
  `Organizar` 1,8 cm, sin contacto. En **`5 serio`** (brazos cruzados) y en **`Tecleo`** (la mano derecha teclea
  delante del pecho) brazos y mangas pasan por encima de los cordones: en esas poses los propios brazos ya se hunden en
  la sudadera, así que lo que esté sobre la tela queda bajo ellos. En los renders se ve el brazo por delante y el cordón
  desaparece debajo, sin asomar a través. Pasaba igual con los cordones de v015.
- **Portátil en `Tecleo`:** a 0,9 cm de la punta izquierda como mínimo (ver el punto 1).

### 4. Comprobación
De frente, de tres cuartos y de perfil, en los bustos de las siete expresiones, en todos los modos, en el `.glb`
importado en un Blender limpio y cargado en three.js, y en el `.fbx` importado. Comparados píxel a píxel con los de
v015, los renders solo cambian en la zona de los cordones: en `cooper_expresion_5_serio.png`,
`cooper_trabajo_frente.png` y `cooper_relax_tres_cuartos.png` los cordones quedan detrás de los brazos, el portátil o la taza
y la imagen es prácticamente la misma.

### 5. Comparación de bocas
`modelo/renders/comparacion/bocas_glb_fbx_vs_renders.png` se regenera con la v016. Las bocas siguen coincidiendo en las
tres filas: feliz Risa 0,35 · sorprendido O 1,0 · pensativo Puchero 1,0 · guiñando ninguna · serio Plano 1,0 · risa
Risa 1,0 (neutro, ninguna). Como antes, en las filas del `.glb` y del `.fbx` los accesorios se ven, porque
`Expresiones` no fija la visibilidad.

### 6. Entrega
Todos los renders regenerados (modos, expresiones y comparaciones) con la misma receta que v014 y v015 (Eevee,
32 muestras, vista Standard, 1600 × 2000, mismas cámaras, luces y fotogramas) y las tres exportaciones con los mismos
ajustes (el `.glb` conserva la interpolación STEP de la boca en `Expresiones`, de 0 a 0,25 s). En `build_v016.py` el
recorrido está en `CORD_PATH` (37 puntos, unidades del script) y la punta en `CORD_TIP`. Archivos binarios por Git LFS.

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
- En `5 serio` y en `Tecleo` los brazos se hunden en la sudadera (también en v015). Si se corrigiera la pose para que
  apoyen encima de la tela, habría que comprobar de nuevo los cordones.
- Si un proyecto muestra el portátil durante `Expresiones` (ese clip no fija la visibilidad), en `3 pensativo` el
  portátil, que sigue a la mano apoyada en la cara, roza el cordón izquierdo. Los renders de expresiones van sin
  accesorios.

## Qué se infirió
- Igual que en versiones anteriores: toda la geometría sale de una hoja de personaje raster sin escala
  real; la altura de 1,000 m es decisión nuestra y el grosor de cada pieza se dedujo de las vistas.
- El recorrido de los cordones (arranque bajo el ribete en x ±0,05, apertura hacia fuera y caída casi vertical) es
  decisión del Modelador 3D. Quantic pidió que caigan por los lados del logo, con al menos 1 cm de margen y sin
  atravesar la tela. El largo lo limita la altura a la que sube el portátil en `Tecleo`.

## Medidas
Alto 1,000 m, ancho 0,80 m, fondo 0,65 m en reposo con todos los accesorios en alto (sin cambios); topología
27 870 quads, 420 triángulos y 59 n-gonos (v015: 27 198 / 388 / 63, por los tubos de los cordones); 55 huesos.
