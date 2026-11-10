# Pedido al Modelador 3D: Cooper v013

Copia el mensaje en la sesión del Modelador 3D (C:\Trabajo\Modelador 3D). Los pedidos anteriores se
entregaron como v009, v010, v011 y v012.

---

Revisamos la v012 de Cooper: la taza de `Relax` está aprobada. Necesito una v013, partiendo de v012, con dos
arreglos:

**1. La mano tiene que tocar la cara en `3 pensativo`.** El punto «bajo la barbilla» de v012 queda dentro del
cuello de la sudadera, así que la mano acaba en el cuello, por debajo y por delante de la boca, sin tocar la
cara. Lo comprobé en el render y en el `.glb` desde varios ángulos. Lo que pide la hoja es otra cosa: la punta
del brazo izquierdo apoyada en la parte delantera de la cara, justo debajo de la boca y a la izquierda, con el
tentáculo curvado hacia arriba. Tiene que verse en contacto con la cara de frente, de tres cuartos y de
perfil. La boca no puede quedar tapada.

**2. Las bocas de `Expresiones` en el `.glb` (y revisa el `.fbx`).** En el `.glb`, la animación `Expresiones`
no lleva las bocas: el canal `Boca.weights` solo tiene dos claves, las dos en 0, de 0 a 3 s. Por eso
sorprendido sale sin la «O», pensativo sin la boca pequeña y serio sin la línea recta: todas salen con la
sonrisa abierta por defecto, a diferencia de los renders. Además, ese canal hace que el clip dure 3 s en vez
de 0,25 s. Necesito:
- Que cada fotograma de `Expresiones` (0 a 6) lleve los valores de las shape keys de la boca de esa
  expresión, igual que en los renders, con interpolación por pasos como el resto del clip.
- Que el clip dure lo mismo que sus fotogramas (0,25 s), sin canales más largos.
- Que revises que el resto de clips (`Idle`, `Saludo`, `Idea`, `Tecleo`, `Relax`, `Organizar`) exportan la
  boca igual que se ve en Blender.
- Que lo compruebes cargando el `.glb` exportado y comparando las bocas de las siete expresiones con los
  renders de `modelo/renders/expresiones/`. Comprueba lo mismo en el `.fbx`.

Regenera `cooper_expresion_3_pensativo.png`, la comparación de expresiones y las exportaciones (`.blend`,
`.glb` y `.fbx`). No cambies nada más: colores, proporciones, rasgos, reparto de accesorios, nombres `Acc_*`
y visibilidad por modo siguen como en v012.

Antes de subir, haz `git pull` de la rama claude/admiring-planck-jnf3aj: anoté estos dos puntos en
`modelo/NOTAS.md`. Súbelo a esa rama, sustituyendo los archivos v012 por los v013, con su `modelo/NOTAS.md`.
La personalidad de la ficha no se toca.
