# Pedido al Modelador 3D: Cooper v015 (pendiente de enviar)

**Estado:** preparado el 2026-11-10 y todavía sin enviar. Quantic lo enviará al Modelador al día siguiente.

Copia el mensaje en la sesión del Modelador 3D (C:\Trabajo\Modelador 3D). Los pedidos anteriores se
entregaron como v009 a v014.

---

Revisamos la v014 de Cooper: los colores de marca y los logos del portátil y de la taza están aprobados.
Necesito una v015, partiendo de v014, con dos arreglos:

**1. Que el bolsillo y los cordones no tapen el logo del pecho.** El borde del bolsillo canguro, el aro de
la sudadera, pasa por encima de la parte baja del logo: tapa la barra violeta de la Q y el pie de las
letras, en los renders y en el `.glb`. Además, los extremos de los cordones pisan la parte alta del logo.
El logo tiene que verse entero y limpio, con algo de margen respecto al bolsillo y a los cordones. Elige
lo que quede más natural: subir el logo, reducirlo un poco, bajar el borde del bolsillo o acortar los
cordones. Comprueba que se ve entero de frente, de tres cuartos y en los bustos de las expresiones, y
también en el `.glb` exportado. Deja en `modelo/NOTAS.md` qué cambiaste y las medidas nuevas.

**2. Comparación de bocas al día.** `modelo/renders/comparacion/bocas_glb_fbx_vs_renders.png` sigue siendo
la de v013, con los colores y el logo antiguos. Regenérala con la v015.

Regenera todos los renders en los que se ve el pecho y las exportaciones (`.blend`, `.glb` y `.fbx`). No
cambies nada más: colores, logos del portátil y de la taza, geometría, brazos, animaciones, nombres `Acc_*`
y visibilidad por modo siguen como en v014.

Antes de subir, haz `git pull` de la rama claude/admiring-planck-jnf3aj (anoté estos puntos en
`modelo/NOTAS.md`). Súbelo a esa rama, sustituyendo los archivos v014 por los v015, con su `modelo/NOTAS.md`.
Antes del commit, comprueba con `git lfs status` que los archivos binarios nuevos van por LFS. La
personalidad de la ficha no se toca.
