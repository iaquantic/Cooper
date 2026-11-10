# Pedido al Modelador 3D: Cooper v014 (colores oficiales)

Copia el mensaje en la sesión del Modelador 3D (C:\Trabajo\Modelador 3D). Los pedidos anteriores se
entregaron como v009 a v013. La v013 está aprobada.

---

Ya tenemos los colores oficiales de Quantic. Salen del manual de marca de la web. En el repositorio
iaquantic/Cooper, la carpeta `personaje/marca/` tiene los logos oficiales en versión blanca y un `README.md`
con los hex. Necesito una v014, partiendo de v013, con estos cambios:

**1. Cuerpo en el violeta de marca.** Es decisión de Quantic: el cuerpo, la cabeza y los tentáculos pasan
de `#5B2BE0` a **`#8070E7`**. Ajusta los tonos que dependen de él para que conserven el contraste de antes.
Como punto de partida, el mismo salto de tono aplicado al violeta nuevo da esto:
- Manchas de la cabeza: `#3A1A9E` → `#564CA3`.
- Iris: `#3B1E9C` → `#564EA1`.

Si con la luz no se distinguen bien, ajústalos y deja en `modelo/NOTAS.md` los hex finales y el motivo.
Hay que rehornear las texturas de cabeza y cuerpo.

**2. Logo oficial en la sudadera, el portátil y la taza.** El logo actual (aro cian con «Quantic») no es el
oficial. El de la marca es la **Q con su barra diagonal**: aro y letras en blanco `#FFFFFF` (versión para
fondos oscuros) y la barra diagonal en violeta `#8070E7`. Usa los archivos de `personaje/marca/`, sin
redibujarlos:
- Sudadera, en el pecho: logo completo, `quantic-logo-blanco.png`.
- Tapa del portátil: isotipo, `quantic-isotipo-blanco.png`.
- Taza: logo completo, `quantic-logo-blanco.png`.

Mantén el tamaño y la posición actuales de cada logo, y que el logo de la sudadera siga legible en los
renders.

**3. Lo que no cambia.** Las pantallas del portátil, del móvil y del panel de datos se quedan con su azul
y cian actuales, por decisión de Quantic. Tampoco cambian las ventosas, los ojos, las gafas, la sudadera,
la bombilla, la boca, la geometría, los brazos, las animaciones, los nombres `Acc_*` ni la visibilidad por
modo.

**4. Entrega.** Regenera todos los renders (modos, expresiones y comparaciones) y las exportaciones
(`.blend`, `.glb` y `.fbx`). En `personaje/FICHA.md`, actualiza la tabla de colores con los hex nuevos y
quita el pendiente de confirmar los hex. La personalidad no se toca.

Antes de subir, haz `git pull` de la rama claude/admiring-planck-jnf3aj (añadí `personaje/marca/`). Súbelo
a esa rama, sustituyendo los archivos v013 por los v014, con su `modelo/NOTAS.md`. Antes del commit,
comprueba con `git lfs status` que los `.glb`, `.fbx`, `.blend` y `.png` nuevos van por LFS.
