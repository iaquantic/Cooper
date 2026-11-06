# Cooper v011 — notas de la versión

**Fecha:** 2026-11-06 · **Parte de:** v010 (aprobada) · **Pedido:** Quantic, tres ajustes tras revisar la v010.

Archivos de esta versión en el repositorio `iaquantic/Cooper`:

| Archivo | Qué es |
|---|---|
| `modelo/blend/cooper_v011.blend` | Archivo de trabajo de Blender 5.2 con las texturas empaquetadas (autónomo). |
| `modelo/blend/build_v011.py` | Script que reconstruye Cooper desde cero; `bake_reuse(dir)` carga las texturas ya horneadas. |
| `modelo/web/cooper_v011.glb` | **Único `.glb`**: para web, tiempo real y animación. Escala 1, Y arriba, texturas, esqueleto de 55 huesos, shape keys y las 7 animaciones. |
| `modelo/animacion/cooper_v011_rig.fbx` | Versión FBX con esqueleto, shape keys, texturas incrustadas y las 7 animaciones. |
| `modelo/renders/modos/` | PNG 1600 × 2000 con fondo transparente, un accesorio por modo. |
| `modelo/renders/expresiones/` | Las siete expresiones, sin accesorios, con el mismo encuadre. |
| `modelo/renders/comparacion/` | Comparaciones con la hoja de personaje. |

Colores, proporciones, rasgos, nombres de accesorio (`Acc_*`) y visibilidad por modo: **iguales que en v010**.

## Qué cambió respecto a v010

### 1. Encuadre de las expresiones
La cámara de busto (`Cam_Busto`) sube su centro 3,5 cm y amplía el encuadre de 0,62 a 0,70 m de alto, de
modo que las rayitas de énfasis de `cooper_expresion_2_sorprendido.png` y `cooper_expresion_6_risa.png`
entran enteras con margen. **Las siete expresiones usan este mismo encuadre**, así que la serie es
coherente (todas se han vuelto a renderizar).

### 2. Tentáculos relajados cuando su accesorio no se usa
Igual que ya hacían T1 (bombilla) y T7 (móvil) en v010, ahora **T2 (portátil), T3 (taza) y T6
(checklist) descansan en el suelo** mientras no se usa su accesorio, y **cada uno sube solo en su clip**:

| Tentáculo | Accesorio | Posición relajada | Sube en |
|---|---|---|---|
| T1 | bombilla | junto a la sudadera, lado izquierdo | `Idea` |
| T2 | portátil | suelo, a la izquierda, por fuera del pie T4 | `Tecleo` (sube el portátil al empezar, lo baja al final) |
| T3 | taza | suelo, delante-izquierda | `Relax` (sube la taza hasta la boca y la baja) |
| T6 | checklist | suelo, delante-derecha | `Organizar` (sube la checklist al empezar, la baja al final) |
| T7 | móvil | junto a la sudadera, lado derecho | ningún clip (el móvil se muestra solo por código) |

Revisados `Saludo`, `Idea`, `Idle` y `Expresiones` con los tentáculos bajados: se ven naturales (ocho
tentáculos repartidos alrededor, ninguno "sosteniendo nada"). Renders regenerados: los de modo, los de sin
accesorios y saludo, las siete expresiones y las comparaciones.

Consecuencia para quien muestre un accesorio por código durante `Idle` o `Expresiones`: el accesorio
aparece en la posición relajada de su tentáculo (en el suelo o junto a la sudadera), no en alto. Para verlo
en alto hay que reproducir su clip de modo.

### 3. Un solo `.glb`
`modelo/web/cooper_v011.glb` sustituye a `cooper_v010.glb` y a `cooper_v010_rig.glb`, que eran el mismo
archivo. En `modelo/animacion/` queda solo `cooper_v011_rig.fbx`. Las rutas del apartado de uso de
`personaje/FICHA.md` están actualizadas.

## Pendiente
- Confirmar los hex oficiales con la guía de marca de Quantic y, si difieren, rehornear las texturas.
- En `personaje/FICHA.md`, la tabla de modos dentro de "Personalidad" sigue asignando `Idle` a Relax y
  ninguna animación a Organizar; corresponden `Relax` y `Organizar`. No se toca por ser apartado de Quantic.
- El estado de la bombilla (`Luz` / `LuzOff`) solo lo cambia `Idea`; en reposo está encendida.

## Qué se infirió
- Igual que en versiones anteriores: toda la geometría sale de una hoja de personaje raster sin escala
  real; la altura de 1,000 m es decisión nuestra y el grosor de cada pieza se dedujo de las vistas.
- Las posiciones relajadas de los cinco tentáculos con accesorio y el ritmo con que suben y bajan son una
  propuesta del Modelador 3D; la hoja solo muestra la pose con todo en alto.
- El encuadre del busto es una decisión de composición (margen de unos 5 cm sobre las rayitas).

## Medidas (sin cambios)
Alto 1,000 m, ancho 0,92 m, fondo 0,64 m en reposo con todos los accesorios; topología 27 702 quads,
1 532 triángulos y 63 n-gonos; 55 huesos.
