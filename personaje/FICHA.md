# Ficha de Cooper

Cooper es el pulpo, la mascota de Quantic. Esta ficha reúne lo que el Modelador 3D tiene de él a
2026-11-06, tras nueve versiones del modelo (`modelo/NOTAS.md` es la nota de la versión entregada, v009).

**Qué es dato y qué es propuesta.** La fuente de Cooper es una hoja de personaje raster (cuatro vistas de
cuerpo entero y seis expresiones) más una tabla de identidad con colores y accesorios. De ahí salen el
aspecto, los colores y las expresiones. **Quantic no ha entregado todavía personalidad, tono, voz ni guía
de marca**; lo que aparece en esos apartados es una **propuesta deducida de la hoja** (postura, accesorios y
gestos) y está marcado como tal. Hay que validarla antes de usarla como canon.

## Identidad
- **Nombre:** Cooper
- **Especie:** pulpo (8 tentáculos)
- **Rol:** mascota de Quantic. Sale en publicaciones, animaciones y dentro de otros proyectos.
- **Resumen en una frase (propuesta):** un pulpo curioso y multitarea que, con sus ocho tentáculos, lleva a
  la vez el portátil, el móvil, el café y la lista de tareas mientras se le enciende la bombilla.

## Personalidad (propuesta, pendiente de validar por Quantic)
- **Rasgos principales:** entusiasta y curioso (bombilla encendida, ojos muy abiertos), organizado y
  multitarea (checklist, panel de datos, laptop), cercano y amable (sonrisa abierta, guiño), con un punto
  de ingenio relajado (sudadera con capucha y taza de café).
- **Cómo habla (tono y voz):** cercano, claro y optimista; explica cosas técnicas sin jerga y celebra los
  avances. Sin voz definida: el modelo no incluye audio.
- **Frases o gestos típicos:** levantar un tentáculo con la bombilla cuando tiene una idea; saludar con un
  tentáculo; teclear en el laptop mirando la pantalla; sostener la taza; marcar tareas en la checklist.
  (Los cuatro primeros existen como clips de animación; ver "Expresiones y poses".)
- **Lo que Cooper nunca hace (reglas de uso, propuesta):**
  - Nunca cambia de colores ni pierde las gafas, la sudadera con el logo o las ventosas rosas: son lo que
    lo hace reconocible.
  - Nunca aparece con menos de ocho tentáculos ni con tentáculos amenazantes; se usan para sostener,
    señalar y saludar.
  - Nunca es agresivo, sarcástico ni burlón; sus expresiones van de serio a risa, sin enfado.
  - Nunca se redibuja ni se regenera con IA en cada proyecto: siempre se parte de este modelo
    (regla del repositorio).
  - No lleva textos ni logos que no sean el de Quantic.

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
a esa altura. Medidas tomadas del modelo v009:

| Pieza | Medida (m) |
|---|---|
| Alto total (con bombilla) | 1,000 |
| Ancho total (tentáculos y accesorios) | 0,922 |
| Fondo total | 0,641 |
| Cabeza | Ø 0,36 (ligeramente achatada, 0,34 de fondo); centro a 0,56 m del suelo |
| Cuerpo con sudadera | 0,345 de ancho × 0,30 de fondo |
| Ojo | Ø 0,144, centro a 0,58 m, separación entre centros 0,16 |
| Montura de gafas (cada aro) | 0,163 × 0,148, banda de 13 mm |
| Tentáculo (apoyado) | ~0,35 de largo, Ø 0,115 en la raíz → 0,025 en la punta, 8 ventosas |
| Bombilla | 0,094 × 0,108 |
| Laptop / móvil / taza / checklist / panel | 0,18 × 0,14 · 0,064 × 0,11 · Ø 0,079 · 0,10 × 0,12 · 0,105 × 0,09 |

Proporciones clave: la cabeza es un 36 % de la altura total y casi tan ancha como el cuerpo; los ojos
ocupan un 40 % del diámetro de la cabeza y quedan casi pegados bajo el puente de las gafas.

### Rasgos que lo hacen reconocible
- Cabeza esférica morada con **poros** y **manchas** más oscuras, concentradas en la cabeza.
- **Ojos grandes y juntos**, blancos con iris morado y pupila negra, tras unas **gafas de montura gruesa
  tipo wayfarer** con puente corto.
- **Sudadera** azul marino con capucha, cordones, bolsillo canguro, costuras y el logo **Q Quantic** en
  el pecho.
- **Ocho tentáculos** con ventosas rosas en anillo, uno siempre en alto con la **bombilla**.

### Accesorios
Laptop con logo Q en la tapa y pantalla con panel de control, móvil con asistente en pantalla, taza negra
"Q Quantic" con café, checklist "Tareas de hoy", panel de datos flotante con gráfico y la bombilla
(apagada o encendida). Cada accesorio sigue al tentáculo que lo sostiene; se pueden ocultar por objeto.

## Expresiones y poses disponibles
En el `.glb` y el `.fbx` van como animaciones; en el `.blend` como pistas NLA.

| Animación | Contenido |
|---|---|
| `Expresiones` (fotogramas 0-6) | 0 neutro · 1 feliz · 2 sorprendido · 3 pensativo (tentáculo en la barbilla) · 4 guiñando · 5 serio (tentáculos cruzados) · 6 risa |
| `Idle` (72 f, 3 s, bucle) | respiración, balanceo de cabeza, tentáculos ondulando, mirada que vaga, parpadeo |
| `Saludo` (48 f, 2 s) | levanta el tentáculo delantero derecho y saluda, ojos felices |
| `Idea` (48 f, 2 s) | la bombilla se enciende con un bote del tentáculo, sorpresa y sonrisa |
| `Tecleo` (48 f, 2 s) | mira al laptop y teclea con el tentáculo delantero izquierdo |

Renders con fondo transparente en `modelo/renders/`: frontal, tres cuartos y las siete expresiones.

## Uso
- **Publicaciones:** usar los PNG de `modelo/renders/` (1600 × 2000, fondo transparente). Para una pose o
  expresión nueva se renderiza desde el `.blend`.
- **Animaciones:** `modelo/animacion/cooper_v009_rig.fbx` o el `.glb` con rig. Esqueleto de 49 huesos:
  raíz, cuerpo, cabeza, mirada (los ojos la siguen), párpados, cejas, ojos felices, dientes, marcas,
  bombilla encendida/apagada y ocho cadenas de tentáculo con control IK en la punta; boca con shape keys
  (O, plano, risa, puchero). Los cinco clips anteriores vienen incluidos.
- **Dentro de proyectos:** `modelo/web/cooper_v009.glb` (escala 1, Y arriba, 14,9 MB con texturas y las
  cinco animaciones). Para pantallas con otro contenido, sustituir los PNG de pantalla y reexportar.

## Pendiente
- Confirmar los hex oficiales con la guía de marca de Quantic y, si difieren, rehornear.
- Validar personalidad, tono y reglas de uso propuestas.
