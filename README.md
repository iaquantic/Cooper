# Cooper

Cooper es el pulpo, la mascota de Quantic. Sale en publicaciones y animaciones, y también puede aparecer dentro de otros proyectos.

Este repositorio es la fuente única de Cooper: quién es, cómo se ve y los archivos del modelo 3D. Si un proyecto necesita a Cooper, lo saca de aquí.

## Estado

| Parte | Estado | Origen |
|---|---|---|
| Personalidad y características | Pendiente | Modelador 3D |
| Modelo 3D | Pendiente | Modelador 3D |

## Estructura

```
personaje/
  FICHA.md          Personalidad, rasgos físicos, colores, voz, qué hace y qué no
modelo/
  blend/            Archivo de trabajo de Blender (.blend)
  web/              Modelo para web y proyectos en tiempo real (.glb)
  animacion/        Versión con esqueleto para animar (.fbx / .glb con rig)
  renders/          Imágenes de Cooper con fondo transparente (.png)
SOLICITUD-MODELADOR-3D.md   Pedido al Modelador 3D
```

## Reglas de uso

- Los archivos de `modelo/` se copian tal cual. Cooper no se redibuja ni se regenera con IA en cada proyecto: siempre se parte de este modelo.
- Si un proyecto necesita una pose, expresión o formato que no existe, se pide al Modelador 3D y se añade aquí como versión nueva.
