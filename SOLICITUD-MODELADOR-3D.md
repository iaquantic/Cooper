# Pedido al Modelador 3D: Cooper v011

Copia el mensaje en la sesión del Modelador 3D (C:\Trabajo\Modelador 3D). Los pedidos anteriores se
entregaron como v009 y v010.

---

Revisamos la v010 de Cooper y está aprobada. Necesito una v011, partiendo de v010, con cuatro cambios:

**1. Encuadre de dos expresiones.** En `cooper_expresion_2_sorprendido.png` y
`cooper_expresion_6_risa.png`, las rayitas de énfasis tocan el borde superior y se cortan. Baja el
encuadre para que entren enteras con algo de margen. Para que la serie sea coherente, usa el mismo
encuadre en las siete expresiones.

**2. Dos tentáculos como brazos, saliendo por las mangas.** Es una decisión de Quantic y se aparta de
la hoja de personaje: dos de los ocho tentáculos salen por las mangas de la sudadera, como brazos, y los
otros seis quedan abajo. Cooper sigue teniendo ocho tentáculos en total.
- Añade mangas a la sudadera, con el mismo material y costuras, y que cada tentáculo-brazo asome por el
  puño.
- Tú decides qué tentáculo sostiene cada accesorio (brazos o tentáculos de abajo) y qué hacen los brazos
  en cada clip (`Saludo`, `Expresiones`, `Idle`, `Idea`, `Tecleo`, `Relax`, `Organizar`). Deja el reparto
  en `modelo/NOTAS.md`, junto a la tabla de accesorios.
- Mantén los nombres `Acc_*` y la visibilidad por modo.
- Actualiza en `personaje/FICHA.md` los apartados de aspecto, medidas y esqueleto.

**3. Tentáculos relajados cuando su accesorio no se usa.** Igual que hiciste con T1 y T7: cualquier
tentáculo, brazo o de abajo, que sostiene un accesorio baja a una pose natural en las animaciones que no
usan ese accesorio, y solo sube con él en su clip. Revisa que `Saludo`, `Idea`, `Idle` y `Expresiones`
se vean naturales, y regenera todos los renders.

**4. Un solo `.glb`.** `modelo/web/cooper_v010.glb` y `modelo/animacion/cooper_v010_rig.glb` son el mismo
archivo. Deja solo `modelo/web/cooper_v011.glb` y, en `modelo/animacion/`, solo el `.fbx`. Actualiza las
rutas en el apartado de uso de `personaje/FICHA.md`.

Fuera de las mangas y los brazos, no cambies colores, proporciones, rasgos, nombres de accesorios ni la
visibilidad por modo.

Súbelo a la rama claude/admiring-planck-jnf3aj, sustituyendo los archivos v010 por los v011, con su
`modelo/NOTAS.md`. La personalidad de la ficha no se toca.
