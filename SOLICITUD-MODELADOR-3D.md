# Pedido al Modelador 3D: Cooper v010

Copia el mensaje en la sesión del Modelador 3D (C:\Trabajo\Modelador 3D). El pedido anterior se entregó
como v009.

---

Quantic ya definió la personalidad de Cooper: está en `personaje/FICHA.md` del repositorio iaquantic/Cooper,
rama claude/admiring-planck-jnf3aj. Léela antes de empezar. La regla nueva que afecta al modelo es esta:
**Cooper actúa según la situación y lleva un solo accesorio cada vez**. Hay cuatro modos:

| Modo | Accesorio visible | Animación |
|---|---|---|
| Idea | Bombilla | `Idea` (ya existe) |
| Trabajo | Portátil | `Tecleo` (ya existe) |
| Relax | Taza de café | **nueva**: `Relax` |
| Organizar y datos | Checklist (y panel de datos o móvil si encajan) | **nueva**: `Organizar` |

Necesito una versión v010, partiendo de v009, con esto:

**1. Animaciones nuevas.**
- `Relax`: bucle tranquilo en el que da un sorbo a la taza, con gesto relajado.
- `Organizar`: marca una tarea en la checklist con un tentáculo y sonríe.
- Revisa que `Idea`, `Tecleo` y `Saludo` se vean bien con un solo accesorio visible.

**2. Accesorios que se puedan mostrar u ocultar por modo.** Que cada accesorio sea un objeto con un
nombre fijo, para poder ocultarlo desde código en web y en otros proyectos. En `modelo/NOTAS.md`, pon la
lista de nombres y qué accesorios van visibles en cada modo.

**3. Renders por modo** (PNG 1600 × 2000, fondo transparente), solo con el accesorio del modo:
- De frente y de tres cuartos para Idea, Trabajo, Relax y Organizar y datos.
- Una versión de Cooper sin accesorios, de frente y saludando.
- Las siete expresiones de nuevo, sin accesorios a la vista. En las de v009 asoman la bombilla y el
  panel por los bordes.

**4. Exportaciones** iguales que en v009: `.blend` con las texturas empaquetadas, `.glb` para web y
`.fbx` y `.glb` con rig, todos con las animaciones nuevas.

**5. Notas.** El `modelo/NOTAS.md` de v010 con lo que cambió, lo pendiente y lo que se infirió. Usa las
rutas y nombres de archivo del repositorio, no los de tu carpeta local. Sube también las imágenes de
comparación con la referencia a `modelo/renders/comparacion/`.

No cambies colores, proporciones ni rasgos: siguen como en v009 hasta que Quantic confirme los hex de
la guía de marca.

Súbelo a la misma rama, sustituyendo los archivos v009 por los v010 (Git guarda las versiones anteriores).
Actualiza la ficha solo en el apartado de expresiones, animaciones y uso; la personalidad no se toca.
