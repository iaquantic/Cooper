# Cooper v010 — notas de la versión

**Fecha:** 2026-11-06 · **Parte de:** v009 · **Pedido:** Quantic, "modos con un solo accesorio"
(`SOLICITUD-MODELADOR-3D.md` del repositorio).

Archivos de esta versión en el repositorio `iaquantic/Cooper`:

| Archivo | Qué es |
|---|---|
| `modelo/blend/cooper_v010.blend` | Archivo de trabajo de Blender 5.2 con las texturas empaquetadas (autónomo). |
| `modelo/blend/build_v010.py` | Script que reconstruye Cooper desde cero; `bake_reuse(dir)` carga las texturas ya horneadas. |
| `modelo/web/cooper_v010.glb` | Para web y tiempo real: escala 1, Y arriba, texturas y las 7 animaciones. |
| `modelo/animacion/cooper_v010_rig.fbx` y `cooper_v010_rig.glb` | Con esqueleto (55 huesos), shape keys de la boca y las 7 animaciones. |
| `modelo/renders/modos/` | PNG 1600 × 2000 con fondo transparente, un accesorio por modo. |
| `modelo/renders/expresiones/` | Las siete expresiones, sin accesorios a la vista. |
| `modelo/renders/comparacion/` | Comparaciones con la hoja de personaje. |

Colores, proporciones y rasgos: **iguales que en v009**; siguen pendientes los hex de la guía de marca.

## Qué cambió respecto a v009

### 1. Accesorios con nombre fijo, visibles u ocultos por modo
Cada accesorio cuelga de un **hueso de visibilidad con nombre fijo**. En el `.glb` y el `.fbx` ese hueso
es un nodo con ese nombre y todas las mallas del accesorio están debajo de él, así que basta con
ocultar el nodo (`scene.getObjectByName('Acc_Taza').visible = false` en three.js, o el equivalente del
motor que se use). En Blender, además, cada accesorio tiene su **colección** con el mismo nombre dentro
de `Accesorios`, y el hueso se puede ocultar escalándolo a 0,001.

| Nombre fijo (nodo / hueso / colección) | Accesorio | Cuelga de |
|---|---|---|
| `Acc_Bombilla` | Bombilla con casquillo, rosca y dos estados: `Luz` (encendida, con rayos) y `LuzOff` (apagada), que son hijos suyos | punta del tentáculo T1 |
| `Acc_Laptop` | Portátil: base, tapa con logo Q, pantalla con imagen, bisagra, teclado con letras, trackpad | punta del tentáculo T2 |
| `Acc_Movil` | Móvil con pantalla, cámara y barra | punta del tentáculo T7 |
| `Acc_Taza` | Taza "Q Quantic" con café y asa | punta del tentáculo T3 |
| `Acc_Checklist` | Checklist: tabla, hoja "Tareas de hoy" y clip | punta del tentáculo T6 |
| `Acc_Panel` | Panel de datos flotante con marco, barras y flecha | hueso `Panel` (junto al cuerpo) |

**Qué va visible en cada modo**

| Modo | Visible | Oculto | Animación |
|---|---|---|---|
| Idea | `Acc_Bombilla` | el resto | `Idea` |
| Trabajo | `Acc_Laptop` | el resto | `Tecleo` |
| Relax | `Acc_Taza` | el resto | `Relax` (nueva) |
| Organizar y datos | `Acc_Checklist` y `Acc_Panel` (el móvil, `Acc_Movil`, queda disponible por nombre si encaja mejor) | el resto | `Organizar` (nueva) |
| Sin accesorios (saludo, presentación) | ninguno | todos | `Saludo` |

Comportamiento en las animaciones: **los clips de modo (`Idea`, `Tecleo`, `Relax`, `Organizar`) y
`Saludo` fijan la visibilidad** de los seis accesorios. **`Expresiones` e `Idle` no la tocan**, para que
el proyecto decida qué accesorio muestra mientras Cooper está en reposo o hace una expresión. En el
estado de reposo exportado los seis están visibles (escala 1) y es el código el que oculta.

### 2. Animaciones nuevas
- **`Relax`** (72 fotogramas, 3 s, bucle): el tentáculo T3 sube la taza hasta la boca, Cooper da un
  sorbo con los ojos cerrados y felices, baja la taza y sonríe relajado. Respiración suave de fondo.
- **`Organizar`** (48 fotogramas, 2 s): mira la checklist que sostiene T6, el tentáculo delantero
  derecho (T5) se acerca y toca la hoja para marcar una tarea, y Cooper sonríe con los ojos felices.
  Checklist y panel visibles.

### 3. Revisión de los clips existentes con un solo accesorio
- `Idea`, `Tecleo` y `Saludo` ahora fijan la visibilidad (bombilla, portátil y ninguno).
- El tentáculo T1, que en v009 estaba siempre en alto sosteniendo la bombilla, **se relaja junto a la
  sudadera** siempre que la bombilla no se usa (reposo, `Expresiones`, `Idle`, `Saludo`, `Tecleo`,
  `Relax`, `Organizar`). En `Idea` sube la bombilla desde esa posición y se enciende con un bote.
  Así no queda un tentáculo levantado "sosteniendo nada" y ya no asoma por el borde de los bustos.

### 4. Renders (fondo transparente, 1600 × 2000)
`modelo/renders/modos/`: `cooper_idea_frente.png` y `cooper_idea_tres_cuartos.png` (fotograma 36 de
`Idea`, bombilla encendida), `cooper_trabajo_*` (fotograma 24 de `Tecleo`), `cooper_relax_*`
(fotograma 30 de `Relax`, en pleno sorbo), `cooper_organizar_*` (fotograma 32 de `Organizar`),
`cooper_sin_accesorios_frente.png` (reposo sin accesorios) y `cooper_saludo_frente.png` /
`cooper_saludo_tres_cuartos.png` (fotograma 24 de `Saludo`).
`modelo/renders/expresiones/`: `cooper_expresion_0_neutro.png` … `cooper_expresion_6_risa.png`, sin
ningún accesorio ni tentáculo asomando por los bordes.
`modelo/renders/comparacion/`: `comparacion_frente.png` (hoja frente a v010 en reposo con todos los
accesorios), `comparacion_expresiones.png` (fila de expresiones de la hoja frente a las de v010) y
`comparacion_modos.png` (hoja frente a los cuatro modos).

## Pendiente
- Confirmar los hex oficiales con la guía de marca de Quantic y, si difieren, rehornear las texturas.
- En `personaje/FICHA.md`, la tabla de modos dentro de "Personalidad" asigna `Idle` a Relax y ninguna
  animación a Organizar; con v010 corresponden `Relax` y `Organizar`. No se ha tocado porque ese
  apartado es de Quantic.
- Los tentáculos que sostienen un accesorio oculto conservan la pose de sostenerlo (salvo T1). Si en
  algún modo molesta, se puede relajar igual que T1.
- El estado de la bombilla (`Luz` / `LuzOff`) solo lo cambia la animación `Idea`; en reposo está
  encendida.

## Qué se infirió
- Igual que en versiones anteriores: toda la geometría sale de una hoja de personaje raster, sin escala
  real; la altura de 1,000 m es decisión nuestra y el grosor de cada pieza se dedujo de las vistas.
- Las poses de `Relax` y `Organizar` (altura de la taza, punto donde se marca la tarea, ritmo) son una
  propuesta del Modelador 3D; la hoja no las muestra.
- La posición relajada de T1 junto a la sudadera es también una propuesta.
- Los contenidos de pantallas, taza y checklist son textos de ejemplo.

## Medidas (sin cambios)
Alto 1,000 m, ancho 0,92 m, fondo 0,64 m en reposo con todos los accesorios; topología 27 702 quads,
1 532 triángulos y 63 n-gonos; 55 huesos (49 de v009 más los 6 `Acc_*`).
