# Cooper v019 — notas de la versión

**Fecha:** 2026-11-19 · **Parte de:** v018 · **Pedido:** Quantic pide que **todas las animaciones funcionen limpias con
todas las expresiones**: revisar cada clip con cada expresión, corregir cada choque en su causa (sin cambiar colores, logo,
proporciones ni personalidad) y volver a comprobar hasta que no quede ninguno.

Archivos de esta versión en el repositorio `iaquantic/Cooper`:

| Archivo | Qué es |
|---|---|
| `modelo/blend/cooper_v019.blend` | Archivo de trabajo de Blender 5.2 con las texturas empaquetadas (autónomo). |
| `modelo/blend/build_v019.py` | Script que reconstruye Cooper desde cero (mismas texturas y recetas que v018, ver punto 6). La variable de entorno `COOPER_BASE` permite indicar la carpeta de la versión fuera del PC de trabajo. |
| `modelo/web/cooper_v019.glb` | **Único `.glb`**: para web, tiempo real y animación. Escala 1, Y arriba, texturas (logos de marca incluidos), esqueleto de 55 huesos, shape keys y las 7 animaciones con las bocas. |
| `modelo/animacion/cooper_v019_rig.fbx` | Versión FBX con esqueleto, shape keys animadas, texturas incrustadas y las 7 tomas. |
| `modelo/renders/modos/` | PNG 1600 × 2000 con fondo transparente, todos de v019. |
| `modelo/renders/expresiones/` | Las siete expresiones, de v019 (sin accesorios). |
| `modelo/renders/comparacion/` | Las cuatro comparaciones y `bocas_glb_fbx_vs_renders.png`, de v019. |

Colores, texturas, logo del pecho y de la taza, pantallas, proporciones, esqueleto (55 huesos), nombres de los clips y de
los `Acc_*`, duraciones y visibilidad por modo: **iguales que en v018**. Cambian las poses de las animaciones, el reposo de
cuatro tentáculos y, por dentro de las mangas, el grosor del brazo y los pesos de la manga.

## Cómo se comprobó: matriz de colisiones

Se cruzaron los **7 clips** (`Expresiones`, `Idle`, `Saludo`, `Idea`, `Tecleo`, `Relax`, `Organizar`) con las **7
expresiones**: cada pose de cuerpo se probó con la cara propia del clip y con la cara (boca, párpados, cejas, ojos felices,
dientes y marcas) de cada una de las siete expresiones encima. En v019 se miró **cada fotograma** de cada clip (en v018, uno
de cada cinco y los extremos), sobre las **mallas deformadas** de verdad, no sobre cajas. Se mide el cruce real (caras que se
cortan y profundidad de lo que queda dentro de una malla cerrada) en estos grupos: brazos y mangas contra cordones, contra la
sudadera y contra la cabeza; tentáculos entre sí y contra la sudadera; accesorios contra cuerpo, brazos y cordones; piezas de
la cara contra lo que se les acerque (la taza, el brazo) y entre sí (párpados, cejas y dientes contra las gafas). Se descuenta
solo lo que está dentro por diseño en reposo (la raíz de los tentáculos en el cuerpo, el hombro en la sisa). Tolerancia: 0,5 mm.

| Clip | v018: peor cruce (cualquier cara) | v019 |
|---|---|---|
| `Expresiones` | **118 mm**: en 3 pensativo el portátil se mete en la sudadera; en 5 serio los brazos entran 49 mm en la sudadera, uno en otro 20 mm, y pisan el cordón 50 mm; en 0 neutro el portátil atraviesa el tentáculo del móvil 16 mm | sin cruces |
| `Idle` | **33 mm**: el tentáculo de la checklist (T6) atraviesa el pie derecho (T5); el portátil, el tentáculo del móvil 19 mm | sin cruces |
| `Saludo` | **6,8 mm**: la manga derecha entra en el bajo de la sudadera al bajar el brazo | sin cruces |
| `Idea` | **50 mm**: el tentáculo de la bombilla atraviesa la manga izquierda y 31 mm el costado | sin cruces |
| `Tecleo` | **53 mm**: el brazo derecho pisa el cordón derecho, entra 37 mm en la sudadera y 13 mm en la barbilla; con la boca de risa, la manga entra 36 mm en la boca | sin cruces |
| `Relax` | **18 mm**: el borde de la taza entra en la boca (15 mm con la cara del clip, 18 mm con la de risa) | sin cruces |
| `Organizar` | **22 mm**: T6 atraviesa el pie T5; la manga derecha, el bajo 15 mm; la mano está 3,6 mm dentro de la tabla todo el gesto | sin cruces |

**Contactos de diseño** (tienen que tocar sin atravesar), medidos en v019: la mano que teclea toca las teclas a 0,5 mm en
cada golpe (`Tecleo` f24) y se levanta 3 cm entre golpes; la mano que marca queda a 1,2 mm de la hoja en el golpe
(`Organizar` f20) y a 2 cm el resto del gesto; el borde de la taza, a 2 mm del labio en el sorbo (`Relax` f30); en
3 pensativo la punta del brazo se apoya en la cara a 0,2 mm; en 5 serio los antebrazos descansan sobre la sudadera (0 a 0,2 mm)
con 15 mm entre uno y otro.

**La piel asomando por la manga** (encontrado al revisar las mangas de cerca; ya pasaba desde v011): cerca del puño la piel del
brazo rozaba la tela por dentro y, al doblar el brazo, asomaba en manchas moradas sobre la manga (pensativo, serio, Saludo,
Tecleo, Relax, Organizar; con el brazo izquierdo, incluso en reposo). Se mide mirando cada manga desde siete direcciones con
rayos cada 2 mm: en v018 daban positivo **todos los fotogramas de todos los clips** (de 200 a 1150 rayos por clip); en v019,
**ninguno**.

## Qué cambió respecto a v018 y por qué

### 1. Los giros iniciales de los brazos ya se guardan en la animación
Las poses usan un giro inicial en los huesos de cada cadena para que el IK doble el tentáculo por donde conviene. Desde v013
ese giro se aplicaba al construir, pero **no se clavaba**: en el `.glb`, el `.fbx` y la línea de tiempo el IK partía de cero
y los brazos se doblaban por otro lado (de ahí buena parte de los cruces de `Tecleo` y de 5 serio). Ahora se clava la rotación
de los 24 huesos de las ocho cadenas en todas las claves, y lo que se comprueba es lo que se entrega.

### 2. Una clave por fotograma
Los clips de modo y `Saludo` llevaban una clave cada 4 fotogramas; entre claves la interpolación hacía pasar mallas a través
de otras (`Idea` f9, `Tecleo` f47, el antebrazo contra la tabla en `Organizar`). Ahora hay una clave en cada fotograma: la
animación es exactamente la pose comprobada. Duraciones y nombres, iguales.

### 3. Reposo de los tentáculos que sostienen accesorios
En v018, el del móvil (T3) y el de la checklist (T6) descansaban delante, cruzando por encima de los pies delanteros
(T4 y T5). Ahora descansan a los lados, entre el pie delantero y el trasero; T1 (bombilla) se aparta un poco hacia afuera y
los brazos cuelgan algo más abiertos y adelantados, sin rozar el bajo de la sudadera. Es lo que se ve en `Idle` y en el
arranque y final de cada clip.

### 4. Expresiones
- **3 pensativo:** la punta del brazo izquierdo se apoya un poco más a la izquierda y separada de la boca, de modo que
  ninguna boca (tampoco la risa) la toca.
- **5 serio:** brazos cruzados delante del pecho, el derecho encima, apoyados en la sudadera, sin hundirse en ella ni pisar
  los cordones.
- **Accesorios en 3 y 5:** si el proyecto muestra el portátil o la taza durante `Expresiones` (ese clip no fija la
  visibilidad), en esas dos expresiones quedan **apoyados en el suelo**, a los lados, porque el brazo que los sostiene está en
  la cara o cruzado. Se hace solo con la posición y el giro de `Acc_Laptop` y `Acc_Taza`, nunca con la escala (que es la
  visibilidad). En las otras cinco expresiones siguen en la mano.

### 5. Clips de modo
- **`Idea`:** la bombilla sube por detrás del brazo izquierdo (cima 7 cm más atrás y 8 cm más baja) y los brazos se abren algo
  menos y más adelante.
- **`Tecleo`:** el portátil queda delante del pecho, casi centrado (11,5 cm más al centro, 6 cm más adelante y 6 cm más
  bajo), y el brazo derecho teclea por delante, sin cruzar el pecho ni los cordones. La mano deja de teclear en el fotograma
  40,75 (antes 42), cuando el portátil empieza a bajar.
- **`Relax`:** el centro del borde de la taza queda a 6,7 cm del centro de la boca (antes 3,6 cm, y el borde entraba 2 cm):
  toca los labios sin entrar en la boca. En el sorbo los labios se fruncen menos (forma `O` al 10 %, antes al 50 %), para que
  la boca no se cierre sobre la taza.
- **`Organizar`:** T6 sube la checklist girando por encima del pie derecho; la hoja queda 6 cm más a la derecha, 3 cm más
  baja y 2 cm más adelante que en v018; la tabla se reorienta (hueso `Acc_Checklist`, solo giro) para que la hoja **mire a cámara igual que en v018**; el
  brazo derecho llega por delante de la tabla, la punta toca la hoja en el golpe y se aparta 2 cm el resto del tiempo.
- **`Saludo`:** mismo gesto; el bajo ya no se cruza gracias al nuevo reposo de los brazos.

### 6. Mangas: la piel ya no asoma
La manga es un tubo cerrado sobre el brazo, pesado a la misma cadena. Junto al puño la piel quedaba a ras de la tela (de 0 a
1,7 mm por fuera en algunos puntos) y, como cada malla calculaba sus pesos por su cuenta, al doblar el brazo la cara interior
de la manga se hundía más que la piel. Dos cambios en `build_v019.py`:
- `thin_under_sleeve()`: la parte del brazo **tapada por la manga** queda al menos 12 mm por dentro de la tela. El
  adelgazamiento se funde a cero en el último centímetro antes del puño, así que la mano y el tramo que se ve no cambian.
- `weights_from_surface()`: la manga toma los pesos de la piel que tiene debajo, así las dos se doblan igual y la holgura
  se conserva.

Nada de esto se ve en reposo: la manga, el puño y la mano tienen la misma forma que en v018.

### 7. Texturas en la carpeta de la versión
Igual que en v018: el `.blend` es autónomo, pero `build_v019.py` lee las texturas de `BASE/texturas`, que en el PC del
Modelador (`proyectos/mascota-quantic/v019/texturas`) no existe todavía. Son las mismas que las de v018: las de v014 más
`quantic-logo-blanco.png` (de `personaje/marca/`), `taza.png`, `pantalla_laptop.png` y `pantalla_movil.png` (las tres
últimas se generan con `taza_png()`, `pantalla_laptop_png()` y `pantalla_movil_png()` o se extraen del `.blend`).

## Comprobación de las exportaciones
- **`.blend`:** se hizo sobre el de v018 cambiando solo las animaciones, la posición de los vértices del brazo bajo la manga
  y los pesos de brazos y mangas. Sus mallas deformadas coinciden con las de una construcción limpia de `build_v019.py`
  (diferencia máxima 0,01 mm) y la matriz da lo mismo sobre los dos.
- **`.glb`:** 156 nodos con los mismos nombres que v018, una piel con 55 articulaciones, las 7 animaciones con los mismos
  nombres y duraciones (166 canales cada una), los 6 nodos `Acc_*`, mismos materiales, imágenes y shape keys. Extensión de
  las texturas sin cambios: pecho, isotipo de la tapa y pantallas en `CLAMP_TO_EDGE`; taza en `REPEAT`.
- **`.fbx`:** misma estructura que el de v018 (objetos, huesos, tomas con sus duraciones y shape keys).
- **Bocas:** coinciden en las tres filas de `bocas_glb_fbx_vs_renders.png` (Blender, `.glb` importado, `.fbx` importado).

## Renders
Todos regenerados con la receta de siempre (Eevee, 32 muestras, Standard, 1600 × 2000): cambian las poses de los modos, el
reposo de los brazos y de los tentáculos con accesorio, y las expresiones 3 pensativo y 5 serio. Las cuatro comparaciones
llevan el rótulo de v019.

## Reparto de accesorios y brazos

| Accesorio | Nodo / hueso | Quién lo sostiene | Sube en |
|---|---|---|---|
| Bombilla | `Acc_Bombilla` | T1, tentáculo de abajo trasero izquierdo | `Idea` |
| Portátil | `Acc_Laptop` | T2, brazo izquierdo (delante del pecho, casi centrado) | `Tecleo` |
| Móvil | `Acc_Movil` | T3, tentáculo de abajo izquierdo | ningún clip (se muestra solo por código) |
| Taza | `Acc_Taza` | T7, brazo derecho | `Relax` |
| Checklist | `Acc_Checklist` | T6, tentáculo de abajo derecho | `Organizar` |
| Panel de datos | `Acc_Panel` | flota junto a la cabeza (hueso `Panel`) | `Organizar` |

| Clip | Brazo izquierdo (T2) | Brazo derecho (T7) |
|---|---|---|
| `Expresiones` | cuelga; en **3 pensativo** sube curvado y la punta se apoya en la cara, bajo la boca y a la izquierda | cuelga; en **5 serio** los dos brazos se cruzan delante del pecho, el derecho encima |
| `Idle` | cuelga con balanceo suave | cuelga con balanceo suave |
| `Saludo` | cuelga | se levanta y saluda |
| `Idea` | se abre un poco con la sorpresa y vuelve | igual; la bombilla la sube T1 por detrás del brazo izquierdo |
| `Tecleo` | sube el portátil delante del pecho y lo baja al final | teclea en la mitad derecha del teclado |
| `Relax` | cuelga | sube la taza hasta que el borde toca los labios, sorbo, la baja |
| `Organizar` | cuelga | marca la tarea en la checklist que sube T6 |

En 3 pensativo y 5 serio, el portátil y la taza (si el proyecto los muestra) quedan en el suelo; ver el punto 4.

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
- La matriz cubre los siete clips entregados con las siete caras. Una pose nueva hecha por código (o mezclar clips) no está
  comprobada: si un proyecto la necesita, conviene pedirla como versión nueva.
- Carpeta `texturas` de v019 en el PC del Modelador: ver el punto 7.

## Qué se infirió
- Igual que en versiones anteriores: toda la geometría sale de una hoja de personaje raster sin escala
  real; la altura de 1,000 m es decisión nuestra y el grosor de cada pieza se dedujo de las vistas.
- Las poses corregidas (dónde descansan los tentáculos, dónde se apoya la mano en pensativo, cómo se cruzan los brazos en
  serio, dónde quedan el portátil, la taza y la checklist, y dejar el portátil y la taza en el suelo en 3 y 5) son decisión
  del Modelador 3D, buscando el mismo gesto que en v018 sin choques.

## Medidas (sin cambios)
Alto 1,000 m, ancho 0,80 m, fondo 0,65 m en reposo con todos los accesorios en alto; topología 27 870 quads,
420 triángulos y 59 n-gonos; 55 huesos.
