# Ficha de Cooper

Cooper es el pulpo, la mascota de Quantic. Esta ficha reúne lo que el Modelador 3D tiene de él a
2026-11-06, tras once versiones del modelo (`modelo/NOTAS.md` es la nota de la versión entregada, v011).

**Qué es dato y qué decidió Quantic.** El aspecto, los colores y las expresiones salen de la hoja de
personaje raster (cuatro vistas de cuerpo entero y seis expresiones) y de la tabla de identidad. La
personalidad, el tono y las reglas de uso los definió Quantic el 2026-11-06 a partir de la propuesta del
Modelador 3D.

## Identidad
- **Nombre:** Cooper
- **Especie:** pulpo (8 tentáculos: dos salen por las mangas de la sudadera como brazos y seis quedan abajo)
- **Rol:** mascota de Quantic. Sale en publicaciones, animaciones y dentro de otros proyectos.
- **Resumen en una frase:** un pulpo del equipo de Quantic, curioso y divertido, que en cada momento usa
  el tentáculo que toca: la bombilla para las ideas, el portátil para trabajar, el café para relajarse y
  la checklist para organizar.

## Personalidad

### Rasgos
Cooper es **curioso y entusiasta**, **organizado y multitarea**, **cercano y amable** e **ingenioso y
relajado**. No muestra los cuatro a la vez: **cada situación saca uno**, con su accesorio.

### Modos según la situación
Cooper aparece con **un solo accesorio protagonista**, el del modo que toca. El resto de accesorios se
ocultan. Cada accesorio tiene un nombre fijo en el modelo (`Acc_*`) y la animación de cada modo ya deja
visible solo el suyo.

| Modo | Cuándo | Rasgo | Accesorio | Animación |
|---|---|---|---|---|
| **Idea** | Lluvias de ideas, lanzamientos, propuestas nuevas | Curioso y entusiasta | Bombilla que se enciende | `Idea` |
| **Trabajo** | Desarrollo, automatizaciones, «estamos en ello» | Organizado y multitarea | Portátil | `Tecleo` |
| **Relax** | Pausas, viernes, mensajes informales, celebraciones tranquilas | Ingenioso y relajado | Taza de café | `Relax` |
| **Organizar y datos** | Resultados, planificación, reportes, avances | Organizado y multitarea | Checklist y panel de datos (o móvil) | `Organizar` |

En todos los modos es **cercano y amable**. Para saludar o presentarse usa la animación `Saludo`.

### Cómo habla
- **Tono:** cercano, claro y divertido. Tutea, explica lo técnico sin jerga y celebra los avances.
- **Humor:** por encima de la media. Bromea a menudo, pero el mensaje se entiende igual sin la broma.
- **Persona:** habla en **primera persona, como parte del equipo**: «en Quantic hemos…», «te ayudo a…».
- **Saludo:** sin frase fija. Saluda distinto cada vez, según el contexto.
- **Emojis:** no usa. La expresividad la ponen el modelo y las animaciones.
- **Voz:** sin voz definida; el modelo no incluye audio.

### Lo que Cooper nunca hace
- **Cambiar su aspecto:** nunca cambia de colores ni pierde las gafas, la sudadera con el logo o las
  ventosas rosas. Siempre tiene ocho tentáculos: dos salen por las mangas de la sudadera como brazos
  y seis quedan abajo (decisión de Quantic del 2026-11-06, a partir de v011).
- **Ser agresivo o burlón:** su humor nunca va contra nadie. Nada de sarcasmo, burla ni enfado; sus
  expresiones van de serio a risa.
- **Regenerarse con IA:** nunca se redibuja ni se regenera en cada proyecto; siempre se parte del modelo
  de este repositorio.

## Aspecto

### Colores (hex)
Los hex se leyeron de la imagen de referencia y son los usados en el modelo. **Quantic debe confirmar los
oficiales de la guía de marca**; si difieren, se cambian en el script y se rehornean las texturas.

| Elemento | Color | Hex |
|---|---|---|
| Cuerpo y cabeza | Morado intenso | `#5B2BE0` |
| Manchas de la cabeza | Morado oscuro | `#3A1A9E` |
| Ventosas | Rosa suave | `#E8A8C8` (centro `#C98AB0`) |
| Ojos | Blanco | `#FFFFFF` |
| Iris | Morado oscuro | `#3B1E9C` |
| Pupila | Negro | `#0A0A14` |
| Gafas y cejas | Negro | `#101014` |
| Sudadera | Azul marino casi negro | `#0E1424` (interior capucha `#070A14`, costuras `#2A3450`) |
| Logo Quantic | Blanco y cian | `#FFFFFF` y `#22D3EE` |
| Interior de la boca / lengua | Negro / rosa | `#0A0A14` / `#E8486C` |
| Bombilla encendida | Amarillo cálido | vidrio `#FFD060`, filamento `#FFC43A`, emisión `#FFB020` |
| Pantallas (laptop, móvil, panel) | Azul y cian emisivos | `#1A6FFF`, `#22D3EE` |

### Proporciones y medidas reales
El modelo mide **1,000 m de alto** en reposo (bombilla incluida), con la base en el suelo. Es la única
dimensión decidida por nosotros (la hoja no tiene escala); el resto son proporciones de la hoja aplicadas
a esa altura. Medidas tomadas del modelo v011:

| Pieza | Medida (m) |
|---|---|
| Alto total (con bombilla) | 1,000 |
| Ancho total (tentáculos y accesorios en alto) | 0,797 |
| Fondo total | 0,649 |
| Cabeza | Ø 0,36 (ligeramente achatada, 0,34 de fondo); centro a 0,56 m del suelo |
| Cuerpo con sudadera | 0,345 de ancho × 0,30 de fondo |
| Manga (cada una) | 0,23 de largo desde el hombro, Ø 0,14 en el hombro → Ø 0,10 en el puño; costura en hombro y puño |
| Brazo (tentáculo por la manga) | 0,36 de largo, Ø 0,11 en la raíz → 0,03 en la punta; asoma 0,11-0,13 por el puño, 5 ventosas en la mano; raíz en el hombro a 0,41 m del suelo |
| Ojo | Ø 0,144, centro a 0,58 m, separación entre centros 0,16 |
| Montura de gafas (cada aro) | 0,163 × 0,148, banda de 13 mm |
| Tentáculo de abajo (apoyado) | 0,46 de largo siguiendo la curva (~0,35 de alcance), Ø 0,13 en la raíz → 0,03 en la punta, 8 ventosas |
| Bombilla | 0,094 × 0,108 |
| Laptop / móvil / taza / checklist / panel | 0,18 × 0,14 · 0,064 × 0,11 · Ø 0,079 · 0,10 × 0,12 · 0,105 × 0,09 |

Proporciones clave: la cabeza es un 36 % de la altura total y casi tan ancha como el cuerpo; los ojos
ocupan un 40 % del diámetro de la cabeza y quedan casi pegados bajo el puente de las gafas.

### Rasgos que lo hacen reconocible
- Cabeza esférica morada con **poros** y **manchas** más oscuras, concentradas en la cabeza.
- **Ojos grandes y juntos**, blancos con iris morado y pupila negra, tras unas **gafas de montura gruesa
  tipo wayfarer** con puente corto.
- **Sudadera** azul marino con capucha, cordones, bolsillo canguro, **mangas con puño**, costuras y el
  logo **Q Quantic** en el pecho.
- **Ocho tentáculos** con ventosas rosas en anillo: **dos son brazos** que salen por las mangas (el
  izquierdo sostiene el portátil, el derecho la taza; decisión de Quantic, a partir de v011) y **seis
  quedan abajo**; uno de los de abajo sube la **bombilla** en el modo Idea.

### Accesorios
Laptop con logo Q en la tapa y pantalla con panel de control, móvil con asistente en pantalla, taza negra
"Q Quantic" con café, checklist "Tareas de hoy", panel de datos flotante con gráfico y la bombilla
(apagada o encendida). Cada accesorio sigue al tentáculo que lo sostiene (portátil: brazo izquierdo; taza:
brazo derecho; bombilla, móvil y checklist: tentáculos de abajo; el panel flota junto a la cabeza); se
pueden ocultar por objeto. El reparto completo está en `modelo/NOTAS.md`.

## Expresiones y poses disponibles
En el `.glb` y el `.fbx` van como animaciones; en el `.blend` como pistas NLA. Versión v011.

| Animación | Contenido | Accesorio visible |
|---|---|---|
| `Expresiones` (fotogramas 0-6) | 0 neutro · 1 feliz · 2 sorprendido · 3 pensativo (mano izquierda en la barbilla) · 4 guiñando · 5 serio (brazos cruzados) · 6 risa; los brazos cuelgan en las demás | no cambia (lo decide el proyecto) |
| `Idle` (72 f, 3 s, bucle) | respiración, balanceo de cabeza, tentáculos ondulando, brazos colgando con balanceo, mirada que vaga, parpadeo | no cambia (lo decide el proyecto) |
| `Saludo` (48 f, 2 s) | levanta el brazo derecho y saluda, ojos felices | ninguno |
| `Idea` (48 f, 2 s) | un tentáculo de abajo sube la bombilla, se enciende con un bote, sorpresa y sonrisa; los brazos se abren un poco | `Acc_Bombilla` |
| `Tecleo` (48 f, 2 s) | el brazo izquierdo sube el portátil delante del pecho, mira la pantalla y teclea con la mano derecha | `Acc_Laptop` |
| `Relax` (72 f, 3 s, bucle) | la mano derecha sube la taza, da un sorbo con los ojos cerrados y felices, la baja y sonríe | `Acc_Taza` |
| `Organizar` (48 f, 2 s) | un tentáculo de abajo sube la checklist, mira la hoja, marca una tarea con la mano derecha y sonríe | `Acc_Checklist` y `Acc_Panel` |

Accesorios con nombre fijo para mostrar u ocultar desde código: `Acc_Bombilla`, `Acc_Laptop`,
`Acc_Movil`, `Acc_Taza`, `Acc_Checklist`, `Acc_Panel` (nodo con ese nombre en el `.glb`/`.fbx`;
colección y hueso con ese nombre en el `.blend`). Qué va visible en cada modo: `modelo/NOTAS.md`.

Mientras un accesorio no se usa, su tentáculo descansa (los de abajo en el suelo; los brazos cuelgan a los
lados con la mano asomando por el puño) y solo sube en su clip de modo. Renders con fondo transparente (1600 × 2000) en `modelo/renders/`: `modos/` (un accesorio
por modo, de frente y de tres cuartos; sin accesorios; saludando) y `expresiones/` (las siete, sin
accesorios y con el mismo encuadre).

## Uso
- **Publicaciones:** elegir primero el modo según la situación y usar el render de ese modo en
  `modelo/renders/modos/`: `cooper_idea_*`, `cooper_trabajo_*`, `cooper_relax_*`, `cooper_organizar_*`
  (de frente y de tres cuartos), `cooper_sin_accesorios_frente.png` y `cooper_saludo_*`. Las expresiones
  están en `modelo/renders/expresiones/`. Para una pose o expresión nueva se renderiza desde el `.blend`.
- **Animaciones:** `modelo/animacion/cooper_v011_rig.fbx` (FBX) o el mismo `modelo/web/cooper_v011.glb`,
  que ya lleva el esqueleto. Esqueleto de 55 huesos: raíz, cuerpo, cabeza, mirada (los ojos la siguen), párpados, cejas, ojos felices, dientes,
  marcas, bombilla encendida/apagada, seis huesos de accesorio `Acc_*` y ocho cadenas de tres huesos con
  control IK en la punta: dos brazos (`T2_BrazoIzq`, `T7_BrazoDer`, con raíz en los hombros; las mangas van
  pesadas a la misma cadena) y seis tentáculos de abajo (`T1_Bombilla`, `T3_Movil`, `T4_PieIzq`,
  `T5_PieDer`, `T6_Checklist`, `T8_Trasero`); boca con shape keys (O, plano, risa, puchero). Los siete clips vienen incluidos;
  los de modo fijan solos qué accesorio se ve.
- **Dentro de proyectos:** `modelo/web/cooper_v011.glb` (escala 1, Y arriba, 15 MB con texturas, esqueleto
  y las siete animaciones; es el único `.glb`). Al cargarlo los seis accesorios están visibles: ocultar por nombre los que no
  toquen (`Acc_*`) o reproducir el clip del modo, que ya lo hace. Para pantallas con otro contenido,
  sustituir los PNG de pantalla y reexportar.

## Pendiente
- Confirmar los hex oficiales con la guía de marca de Quantic y, si difieren, rehornear.
