# Pedido al Modelador 3D: Cooper v012

Copia el mensaje en la sesión del Modelador 3D (C:\Trabajo\Modelador 3D). Los pedidos anteriores se
entregaron como v009, v010 y v011.

---

Revisamos la v011 de Cooper: los brazos por las mangas, el encuadre, los tentáculos relajados y el `.glb`
único están aprobados. Necesito una v012, partiendo de v011, con dos arreglos de alcance de los brazos:

**1. La taza tiene que llegar a la boca en `Relax`.** Ahora el sorbo se queda a la altura del pecho, por
debajo de la boca, porque el brazo es más corto que el tentáculo de v010. En el momento del sorbo, el
borde de la taza tiene que tocar la boca, inclinada hacia ella. Puedes acercar el hombro, doblar más el
brazo o inclinar un poco la cabeza hacia la taza, lo que quede más natural. Compruébalo también en el
`.glb` exportado, no solo en el render de Blender.

**2. La mano tiene que tocar la barbilla en la expresión `3 pensativo`.** Ahora queda separada de la
cara, delante del pecho. Como en la hoja de personaje: la punta del brazo izquierdo apoyada bajo la
barbilla.

Regenera los renders afectados (`cooper_relax_*`, `cooper_expresion_3_pensativo.png` y las comparaciones)
y las exportaciones (`.blend`, `.glb` y `.fbx`). No cambies nada más: colores, proporciones, rasgos,
reparto de accesorios, nombres `Acc_*` y visibilidad por modo siguen como en v011.

Antes de subir, haz `git pull` de la rama claude/admiring-planck-jnf3aj: anoté estos dos puntos en
`modelo/NOTAS.md`. Súbelo a esa rama, sustituyendo los archivos v011 por los v012, con su `modelo/NOTAS.md`.
La personalidad de la ficha no se toca.
