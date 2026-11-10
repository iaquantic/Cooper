# Aviso al Modelador 3D: Git LFS

Copia el mensaje en la sesión del Modelador 3D (C:\Trabajo\Modelador 3D). Los pedidos anteriores se
entregaron como v009 a v013. La v013 está aprobada.

---

La v013 de Cooper está aprobada: la mano en la cara de `3 pensativo` y las bocas de `Expresiones` en el
`.glb` funcionan. Gracias. No hace falta ninguna versión nueva por ahora.

Un cambio en el repositorio iaquantic/Cooper: desde la v013, los `.glb`, `.fbx`, `.blend` y `.png` se guardan
con **Git LFS** (reglas en `.gitattributes`). Antes de la próxima entrega, haz esto una vez en tu copia del
repositorio:

1. `git lfs install`, para activar Git LFS en tu equipo (Git para Windows ya lo trae).
2. `git pull` de la rama claude/admiring-planck-jnf3aj, para recibir el `.gitattributes`.
3. `git lfs pull`, para descargar los archivos reales de la v013.
4. Comprueba que `git lfs ls-files` lista los 25 archivos de la v013 y que el `.glb` se abre como modelo y
   no como un texto pequeño.

En las próximas entregas, antes de hacer commit, comprueba con `git lfs status` que los archivos nuevos
aparecen como LFS. Si alguno aparece como Git normal, no lo subas: avísame. No reescribas el historial ni
hagas push forzado.
