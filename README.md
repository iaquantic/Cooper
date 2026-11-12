# Cooper

Cooper es el pulpo, la mascota de Quantic. Sale en publicaciones y animaciones, y también puede aparecer dentro de otros proyectos.

Este repositorio es la fuente única de Cooper: quién es, cómo se ve y los archivos del modelo 3D. Si un proyecto necesita a Cooper, lo saca de aquí.

## Estado

| Parte | Estado | Origen |
|---|---|---|
| Personalidad y características | Definidas el 2026-11-06 (`personaje/FICHA.md`) | Aspecto: Modelador 3D · Personalidad: Quantic |
| Modelo 3D | Entregado el 2026-11-12, versión v018 (v017 + logo oficial en las pantallas del portátil y del móvil, sin rayitas en el isotipo de la tapa); notas en `modelo/NOTAS.md` | Modelador 3D |

## Pendientes

- **Brazos sobre los cordones:** en la expresión «5 serio» y en el modo Trabajo (`Tecleo`) los brazos pasan por
  encima de los cordones, como ya pasaba con la tela de la sudadera. En los renders no se nota; arreglarlo del
  todo exige tocar las animaciones.
- **Texturas de `build_v018.py`:** el script lee las texturas de la carpeta `texturas/` de la versión, en el PC del
  Modelador, y allí no existen las de la v017 ni las de la v018. Antes de volver a ejecutarlo hay que crearla
  (detalle en `modelo/NOTAS.md`, punto 5).

## Estructura

```
personaje/
  FICHA.md          Personalidad, rasgos físicos, colores, voz, qué hace y qué no
modelo/
  blend/            Archivo de trabajo de Blender (.blend)
  web/              Único .glb: web, tiempo real y animación (con esqueleto)
  animacion/        Versión FBX con esqueleto para animar
  renders/          Imágenes con fondo transparente: modos/, expresiones/ y comparacion/ (.png)
  NOTAS.md          Notas de la versión entregada (v018): nombres de accesorios y visibilidad por modo
SOLICITUD-MODELADOR-3D.md   Pedido al Modelador 3D
```

## Reglas de uso

- Los archivos de `modelo/` se copian tal cual. Cooper no se redibuja ni se regenera con IA en cada proyecto: siempre se parte de este modelo.
- Si un proyecto necesita una pose, expresión o formato que no existe, se pide al Modelador 3D y se añade aquí como versión nueva.

## Archivos grandes (Git LFS)

Desde la v013, los `.glb`, `.fbx`, `.blend` y `.png` se guardan con Git LFS (ver `.gitattributes`). El
repositorio solo guarda una referencia y el archivo real se descarga aparte. Así, cada versión nueva no
engorda el historial.

- Para clonar o actualizar el repositorio hace falta tener Git LFS instalado. Git para Windows ya lo trae.
  Si al abrir un `.glb` o un `.png` sale un archivo de texto pequeño en lugar del modelo o la imagen,
  ejecuta `git lfs install` y luego `git lfs pull`.
- Las versiones hasta la v012 siguen en el historial normal de Git.
