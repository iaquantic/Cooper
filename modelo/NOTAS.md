# Cooper v011 — notas de la versión

**Fecha:** 2026-11-06 · **Parte de:** v010 (aprobada) · **Pedido:** Quantic, cuatro cambios tras revisar la v010
(`SOLICITUD-MODELADOR-3D.md`): encuadre de las expresiones, **dos tentáculos como brazos por las mangas**,
tentáculos relajados cuando no usan su accesorio y un solo `.glb`.

Archivos de esta versión en el repositorio `iaquantic/Cooper`:

| Archivo | Qué es |
|---|---|
| `modelo/blend/cooper_v011.blend` | Archivo de trabajo de Blender 5.2 con las texturas empaquetadas (autónomo). |
| `modelo/blend/build_v011.py` | Script que reconstruye Cooper desde cero; `reuse_head(dir)` carga la textura de la cabeza de v008 y `bake_body()` + `bake_hoodie()` + `bake_finish()` hornean cuerpo y sudadera. |
| `modelo/web/cooper_v011.glb` | **Único `.glb`**: para web, tiempo real y animación. Escala 1, Y arriba, texturas, esqueleto de 55 huesos, shape keys y las 7 animaciones. |
| `modelo/animacion/cooper_v011_rig.fbx` | Versión FBX con esqueleto, shape keys, texturas incrustadas y las 7 animaciones. |
| `modelo/renders/modos/` | PNG 1600 × 2000 con fondo transparente, un accesorio por modo (de frente y de tres cuartos), sin accesorios y saludando. |
| `modelo/renders/expresiones/` | Las siete expresiones, sin accesorios, con el mismo encuadre. |
| `modelo/renders/comparacion/` | Comparaciones con la hoja de personaje (frente, modos y expresiones). |

Colores, proporciones, rasgos, nombres de accesorio (`Acc_*`) y visibilidad por modo: **iguales que en v010**.
Lo único nuevo en el aspecto son las mangas y los dos brazos, por decisión de Quantic.

## Qué cambió respecto a v010

### 1. Encuadre de las expresiones
La cámara de busto (`Cam_Busto`) sube su centro 3,5 cm y amplía el encuadre de 0,62 a 0,70 m de alto, de
modo que las rayitas de énfasis de `cooper_expresion_2_sorprendido.png` y `cooper_expresion_6_risa.png`
entran enteras con margen. **Las siete expresiones usan este mismo encuadre.**

### 2. Dos tentáculos como brazos, saliendo por las mangas
Cooper sigue teniendo **ocho tentáculos**: dos salen por las mangas de la sudadera como brazos (T2, brazo
izquierdo, y T7, brazo derecho) y los otros seis quedan abajo (T1, T3, T4, T5, T6 y T8).

**Mangas.** Cada manga es un tubo de la sudadera de 23 cm que nace en el hombro, dentro del cuerpo de la
sudadera, y llega hasta el codo del brazo: Ø 14 cm en el hombro y Ø 10 cm en el puño. Llevan el mismo
material que la sudadera (normales horneadas de nuevo, con las arrugas) y dos costuras del mismo material
que las demás: una en el hombro, donde la manga sale del cuerpo, y otra en el puño. Las mangas van pesadas
a la misma cadena de huesos que su brazo, así que se doblan con él (codo). Los puños están cerrados por
dentro para que no se vea el hueco.

**Brazos.** Son tentáculos algo más finos que los de abajo (Ø 11 cm en la raíz frente a 13, 36 cm de largo
siguiendo la curva frente a 46) y asoman 11-13 cm por el puño; las ventosas (5 por brazo) van solo en la
mano que asoma, para que no atraviesen la manga. La raíz de la cadena está en el hombro, a (±0,11, −0,01,
0,41) m. Los huesos se llaman `T2_BrazoIzq.001-003` / `T7_BrazoDer.001-003` con control `T2_BrazoIzq_IK`
/ `T7_BrazoDer_IK`; el tentáculo del móvil pasa a llamarse `T3_Movil.001-003`. **Los nombres `Acc_*` no
cambian.** El esqueleto sigue teniendo 55 huesos.

**Reparto de accesorios** (junto a la tabla de visibilidad, más abajo):

| Accesorio | Nodo / hueso | Quién lo sostiene | Sube en |
|---|---|---|---|
| Bombilla | `Acc_Bombilla` | T1, tentáculo de abajo trasero izquierdo | `Idea` |
| Portátil | `Acc_Laptop` | **T2, brazo izquierdo** (lo sujeta delante del pecho, a su izquierda) | `Tecleo` |
| Móvil | `Acc_Movil` | T3, tentáculo de abajo delantero izquierdo | ningún clip (se muestra solo por código) |
| Taza | `Acc_Taza` | **T7, brazo derecho** | `Relax` |
| Checklist | `Acc_Checklist` | T6, tentáculo de abajo delantero derecho | `Organizar` |
| Panel de datos | `Acc_Panel` | flota junto a la cabeza (hueso `Panel`) | `Organizar` |

El portátil pasa del lado izquierdo (v010) a delante del pecho: es la única forma de que la mano derecha
llegue al teclado. De frente se ve la tapa con la Q; en el render de tres cuartos se ve la mano tecleando.

**Qué hacen los brazos en cada clip:**

| Clip | Brazo izquierdo (T2) | Brazo derecho (T7) |
|---|---|---|
| `Expresiones` | cuelga; en **3 pensativo** la mano va a la barbilla | cuelga; en **5 serio** los dos brazos se cruzan sobre el pecho |
| `Idle` | cuelga con balanceo suave | cuelga con balanceo suave |
| `Saludo` | cuelga | **se levanta y saluda** (antes lo hacía el pie derecho T5) |
| `Idea` | se abre un poco con la sorpresa y vuelve | igual; la bombilla la sube T1 |
| `Tecleo` | **sube el portátil** delante del pecho y lo baja al final | **teclea** en la mitad derecha del teclado (antes T4) |
| `Relax` | cuelga | **sube la taza** a la boca, sorbo, la baja (antes T3) |
| `Organizar` | cuelga | **marca la tarea** en la checklist que sube T6, un poco hacia el centro (antes T5) |

Los pies T4 y T5 quedan siempre apoyados; T8 queda atrás.

### 3. Tentáculos y brazos relajados cuando su accesorio no se usa
Cualquier tentáculo o brazo que sostiene un accesorio descansa mientras no se usa, y **sube solo en su clip**:

| Tentáculo | Accesorio | Posición relajada | Sube en |
|---|---|---|---|
| T1 (abajo) | bombilla | suelo, atrás-izquierda, entre T4 y T8 | `Idea` |
| T2 (brazo izquierdo) | portátil | colgando junto a la sudadera, mano bajo el dobladillo | `Tecleo` |
| T3 (abajo) | móvil | suelo, delante-izquierda | ningún clip |
| T6 (abajo) | checklist | suelo, delante-derecha | `Organizar` |
| T7 (brazo derecho) | taza | colgando junto a la sudadera, mano bajo el dobladillo | `Relax`, y saluda en `Saludo` |

Revisados `Saludo`, `Idea`, `Idle` y `Expresiones` con todo relajado: los brazos cuelgan a los lados con la
mano asomando por el puño y nada sale del encuadre. Renders regenerados todos: modos, sin accesorios, saludo,
las siete expresiones y las comparaciones.

Consecuencia para quien muestre un accesorio por código durante `Idle` o `Expresiones`: aparece donde
descansa su tentáculo (portátil y taza colgando de la mano, bombilla, móvil y checklist en el suelo), no en
alto. Para verlo en alto hay que reproducir su clip de modo.

### 4. Un solo `.glb`
`modelo/web/cooper_v011.glb` sustituye a `cooper_v010.glb` y a `cooper_v010_rig.glb`, que eran el mismo
archivo. En `modelo/animacion/` queda solo `cooper_v011_rig.fbx`. Las rutas del apartado de uso de
`personaje/FICHA.md` están actualizadas.

## Visibilidad por modo (sin cambios)
`Idea` → `Acc_Bombilla` · `Tecleo` → `Acc_Laptop` · `Relax` → `Acc_Taza` · `Organizar` → `Acc_Checklist` y
`Acc_Panel` · `Saludo` → ninguno. `Expresiones` e `Idle` no tocan la visibilidad. `Acc_Movil` solo por código.

## Texturas
Cabeza: reutilizada de v008 (no cambia). Cuerpo y tentáculos (brazos incluidos): atlas horneado de nuevo
(color y normales 2048²). Sudadera con mangas: normales horneadas de nuevo (1024²). Pantallas, taza, checklist
y teclas: iguales.

## Pendiente
- Confirmar los hex oficiales con la guía de marca de Quantic y, si difieren, rehornear las texturas.
- En `Relax` la taza no llega a la boca: el sorbo se queda a la altura del pecho, por debajo de la boca.
  En v010, con el tentáculo de abajo, sí llegaba. Revisión de Quantic.
- En la expresión `3 pensativo` la mano queda separada de la cara, delante del pecho; en la hoja toca
  la barbilla. Revisión de Quantic.
- El estado de la bombilla (`Luz` / `LuzOff`) solo lo cambia `Idea`; en reposo está encendida.
- Las mangas nacen dentro del cuerpo de la sudadera; si un brazo se lleva muy atrás por código, la manga
  puede asomar por la espalda. Los clips entregados no lo hacen.

## Qué se infirió
- Igual que en versiones anteriores: toda la geometría sale de una hoja de personaje raster sin escala
  real; la altura de 1,000 m es decisión nuestra y el grosor de cada pieza se dedujo de las vistas.
- Las mangas y los brazos no están en la hoja: largo, grosor, dónde nacen y qué tentáculo hace de brazo son
  propuesta del Modelador 3D sobre el pedido de Quantic. También el reparto de accesorios y lo que hacen los
  brazos en cada clip.
- Las posiciones relajadas y el ritmo con que suben y bajan son propuesta del Modelador 3D; la hoja solo
  muestra la pose con todo en alto.
- El encuadre del busto es una decisión de composición (margen de unos 5 cm sobre las rayitas).

## Medidas
Alto 1,000 m, ancho 0,80 m, fondo 0,65 m en reposo con todos los accesorios en alto (en v010 el ancho era
0,92 m porque el portátil sobresalía por la izquierda); topología 28 446 quads, 1 604 triángulos y
63 n-gonos; 55 huesos.
