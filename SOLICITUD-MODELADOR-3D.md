# Pedido al Modelador 3D: Cooper v011

Copia el mensaje en la sesión del Modelador 3D (C:\Trabajo\Modelador 3D). Los pedidos anteriores se
entregaron como v009 y v010.

---

Revisamos la v010 de Cooper y está aprobada. Necesito una v011, partiendo de v010, con tres ajustes:

**1. Encuadre de dos expresiones.** En `cooper_expresion_2_sorprendido.png` y
`cooper_expresion_6_risa.png`, las rayitas de énfasis tocan el borde superior y se cortan. Baja el
encuadre para que entren enteras con algo de margen. Para que la serie sea coherente, usa el mismo
encuadre en las siete expresiones.

**2. Tentáculos relajados cuando su accesorio no se usa.** Igual que hiciste con T1 y T7: que T2
(portátil), T3 (taza) y T6 (checklist) bajen junto a la sudadera en las animaciones que no usan su
accesorio. Cada uno solo sube con su accesorio en su clip: T2 en `Tecleo`, T3 en `Relax` y T6 en
`Organizar`. Revisa que `Saludo`, `Idea`, `Idle` y `Expresiones` se vean naturales con los tentáculos
bajados, y regenera los renders que cambien.

**3. Un solo `.glb`.** `modelo/web/cooper_v010.glb` y `modelo/animacion/cooper_v010_rig.glb` son el mismo
archivo. Deja solo `modelo/web/cooper_v011.glb` y, en `modelo/animacion/`, solo el `.fbx`. Actualiza las
rutas en el apartado de uso de `personaje/FICHA.md`.

No cambies colores, proporciones, rasgos, nombres de accesorios ni la visibilidad por modo.

Súbelo a la rama claude/admiring-planck-jnf3aj, sustituyendo los archivos v010 por los v011, con su
`modelo/NOTAS.md`. La personalidad de la ficha no se toca.
